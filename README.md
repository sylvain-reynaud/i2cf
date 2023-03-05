# i2cf
> item-to-item collaborative filtering based on graph database

i2cf is an application that uses a graph database to provide personalized recommendations to users. It is designed to help users discover items that are relevant to their interests by analyzing their preferences and similarities with other users.

The application uses the item-to-item collaborative filtering technique to make recommendations. It works by analyzing the relationships between items and identifying items that are similar to each other.

The project is built on a **graph database**, which makes it easy to model complex relationships between items and users. The database stores information about the items, such as their attributes and ratings, as well as information about the users, such as their preferences and behaviors.
<!-- 
Overall, this project is ideal for anyone who wants to build a recommendation engine that is flexible, scalable, and easy to use. It is designed to be highly customizable, and can be easily integrated into existing applications or used as a standalone recommendation engine. -->

## Roadmap

### Epic 1: Data collection and preprocessing

- [ ] Define the data sources (e.g., user ratings, item features) to be used for building the recommendation engine. (1h - 2h)
- [ ] Collect and store the raw data in a suitable format (e.g., CSV, JSON). (1h - 4h)
- [ ] Clean and preprocess the data (e.g., remove duplicates, fill missing values). (1h - 6h)
- [ ] Split the data into training and testing sets. (.5h - 1h)

### Epic 2: Graph database setup

- [ ] Choose a suitable graph database (e.g., Neo4j, OrientDB) to store and manage the recommendation engine data. (.5h - 2h)
- [ ] Define the schema of the graph database (e.g., nodes for users and items, relationships between them). (.5h - 4h)
- [ ] Write code to create and populate the graph database with the preprocessed data. (2h - 8h)

### Epic 3: Similarity calculation

- [ ] Choose a suitable similarity measure (e.g., cosine similarity, Pearson correlation) to calculate the similarity between items. (.5h - 2h)
- [ ] Implement the similarity measure using the graph database (e.g., using Cypher queries for Neo4j). (2h - 8h)
- [ ] Store the similarity scores in the graph database for fast access during recommendation generation. (1h - 2h)

### Epic 4: Recommendation generation

- [ ] Implement the item-to-item collaborative filtering algorithm using the similarity scores and user ratings. (3h - 10h)
- [ ] Write code to generate personalized recommendations for users based on their ratings and preferences. (2h - 6h)
- [ ] Evaluate the performance of the recommendation engine using suitable metrics (e.g., precision, recall, F1-score). (3h - 4h)
- [ ] Iterate and improve the recommendation engine based on the evaluation results. (3h - 6h)

### Epic 5: API and user interface

- [ ] Develop a RESTful API for the recommendation engine that can be accessed by external applications. (3h - 8h)
- [ ] Design and implement a user interface for users to interact with the recommendation engine (e.g., https://hoppscotch.io/)

