# i2cf
> item-to-item collaborative filtering based on graph database

i2cf is an application that uses a graph database to provide personalized recommendations to users. It is designed to help users discover items that are relevant to their interests by analyzing their preferences and similarities with other users.

The application uses the item-to-item collaborative filtering technique to make recommendations. It works by analyzing the relationships between items and identifying items that are similar to each other.

The project is built on a **graph database**, which makes it easy to model complex relationships between items and users. The database stores information about the items, such as their attributes and ratings, as well as information about the users, such as their preferences and behaviors.
<!-- 
Overall, this project is ideal for anyone who wants to build a recommendation engine that is flexible, scalable, and easy to use. It is designed to be highly customizable, and can be easily integrated into existing applications or used as a standalone recommendation engine. -->

## Import data to Neo4j

1. Start Neo4j with docker-compose

```bash
docker-compose up -d
```

2. Import csv to Neo4j

csv files are in `volumes/neo4j/imported_csv` folder mounted to Neo4j container at `/imported_csv` folder:
- `likes.csv`
- `ratings.csv`
- `users.csv`
- `videos.csv`
- `watchtime.csv`

```bash
docker compose exec -it neo4j bash
cp /imported_csv/* /var/lib/neo4j/import/
chown -R neo4j:neo4j /var/lib/neo4j/import
```

Go to Neo4j browser at `http://localhost:7474/browser/` and the query in `utils/create_nodes_and_relationships.cypher` file.

## Run the application

```bash
docker-compose up -d
```

