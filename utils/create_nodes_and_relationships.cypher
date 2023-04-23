// Import Users
LOAD CSV WITH HEADERS FROM 'file:///users.csv' AS row
MERGE (u:User {id: row.id});

// Import Videos
LOAD CSV WITH HEADERS FROM 'file:///videos.csv' AS row
MERGE (v:Video {id: row.id, title: row.title})
WITH v, row
MATCH (a:User {id: row.author_id})
MERGE (a)-[:CREATED]->(v);

// Import Likes
LOAD CSV WITH HEADERS FROM 'file:///likes.csv' AS row
MATCH (u:User {id: row.user_id}), (v:Video {id: row.video_id})
MERGE (u)-[:LIKES]->(v);

// Import Ratings
LOAD CSV WITH HEADERS FROM 'file:///ratings.csv' AS row
MATCH (u:User {id: row.user_id}), (v:Video {id: row.video_id})
MERGE (u)-[:RATED {rating: toInteger(row.rating)}]->(v);

// Import Watchtime
LOAD CSV WITH HEADERS FROM 'file:///watchtime.csv' AS row
MATCH (u:User {id: row.user_id}), (v:Video {id: row.video_id})
MERGE (u)-[:WATCHED {watchtime: toInteger(row.watchtime)}]->(v);
