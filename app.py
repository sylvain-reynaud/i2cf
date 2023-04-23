from flask import Flask, request, jsonify
from neo4j import GraphDatabase
import os

app = Flask(__name__)

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "neo4jneo4j")

db_driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))


def compute_similarity_scores():
    # The similarity score is calculated using cosine similarity.
    with db_driver.session() as session:
        # Remove existing SIMILAR_TO relationships
        remove_existing_relationships_query = """
        MATCH (v1:Video)-[r:SIMILAR_TO]->(v2:Video)
        DELETE r
        """
        session.run(remove_existing_relationships_query)

        # Compute similarity scores and store them as SIMILAR_TO relationships
        similarity_query = """
        MATCH (v1:Video)<-[r1:RATED]-(u:User)-[r2:RATED]->(v2:Video)
        WHERE v1 <> v2
        OPTIONAL MATCH (u)-[l1:LIKES]->(v1)
        OPTIONAL MATCH (u)-[w1:WATCHED]->(v1)
        OPTIONAL MATCH (u)-[l2:LIKES]->(v2)
        OPTIONAL MATCH (u)-[w2:WATCHED]->(v2)
        WITH v1, v2,
             [toFloat(r1.rating)/5, 
              COALESCE(toFloat(w1.watchtime)/v1.duration, 0),
              CASE WHEN l1 IS NOT NULL THEN 1 ELSE 0 END] AS vector1,
             [toFloat(r2.rating)/5,
              COALESCE(toFloat(w2.watchtime)/v2.duration, 0),
              CASE WHEN l2 IS NOT NULL THEN 1 ELSE 0 END] AS vector2
        WITH v1, v2, gds.similarity.cosine(vector1, vector2) AS similarity
        WHERE NOT isNaN(similarity)
        MERGE (v1)-[s:SIMILAR_TO]->(v2)
        SET s.similarity = similarity
        """
        session.run(similarity_query)



'''
This is a Cypher query, used with the Neo4j graph database.
The goal of the query is to find videos similar to a specified target video, based on user ratings, and return the top "$limit" results.
'''
def get_video_recommendations(user_id, limit):
    with db_driver.session() as session:
        query = """
        MATCH (targetUser:User {id: $user_id})-[r:RATED]->(v1:Video)-[s:SIMILAR_TO]->(v2:Video)
        RETURN v2.id AS id, v2.title AS title, s.similarity AS score
        ORDER BY score DESC
        LIMIT $limit
        """
        results = session.run(query, user_id=user_id, limit=limit)
        return [{"id": r["id"], "title": r["title"], "score": r["score"]} for r in results]


@app.route('/recommendations/<user_id>', methods=['GET'])
def recommendation(user_id):
    limit = int(request.args.get('limit', 5))
    recommendations = get_video_recommendations(user_id, limit)
    return jsonify(recommendations)

@app.route('/compute_similarity_scores', methods=['GET'])
def compute_similarity():
    compute_similarity_scores()
    return jsonify({"message": "Similarity scores computed and stored successfully"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
