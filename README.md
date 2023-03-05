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
    - Research available data sources (e.g., public datasets, data from partners).
    - Determine the required data fields (e.g., user ID, item ID, rating, item features).
    - Define the format of the data sources (e.g., CSV, JSON, SQL).
- [ ] Collect and store the raw data in a suitable format (e.g., CSV, JSON). (1h - 4h)
    - Write code to collect data from the defined sources.
    - Save the raw data in a local file or database for further processing.
    - Validate the raw data for missing or invalid values.
- [ ] Clean and preprocess the data (e.g., remove duplicates, fill missing values). (1h - 6h)
    - Remove duplicates from the data.
    - Fill missing values with appropriate estimates (e.g., mean, median).
    - Normalize the data if necessary (e.g., scale ratings to a specific range).
    - Convert the data to a suitable format for use in the graph database.
- [ ] Split the data into training and testing sets. (.5h - 1h)
    - Define the proportion of the data to be used for training and testing.
    - Randomly split the data into two sets (training and testing).
    - Save the two sets to separate files or databases.

### Epic 2: Graph database setup

- [ ] Choose a suitable graph database (e.g., Neo4j, OrientDB, ArangoDB). (.5h - 2h)
    - Research available graph databases.
    - Define the requirements for the graph database.
    - Choose a suitable graph database based on the requirements.
- [ ] Define the schema of the graph database. (.5h - 4h)
    - Define the nodes and relationships to be used in the graph database.
    - Map the preprocessed data fields to the nodes and relationships.
    - Define the properties of the nodes and relationships (e.g., data types, uniqueness constraints).
- [ ] Write code to create and populate the graph database. (2h - 8h)
    - Write code to create the nodes and relationships in the graph database.
    - Load the preprocessed data into the graph database.
    - Verify the data has been correctly loaded into the graph database.

### Epic 3: Similarity calculation

- [ ] Choose a suitable similarity measure (e.g., cosine similarity, Pearson correlation) to calculate the similarity between items. (.5h - 2h)
    - Research available similarity measures.
    - Define the requirements for the similarity measure.
    - Choose a suitable similarity measure based on the requirements.
- [ ] Implement the similarity measure using the graph database (e.g., using Cypher queries for Neo4j). (2h - 8h)
    - Write code to calculate the similarity between items using the chosen similarity measure.
    - Use Cypher queries (or the appropriate query language for the chosen graph database) to efficiently compute the similarity scores.
    - Verify that the similarity measure has been correctly implemented and computed.
- [ ] Store the similarity scores in the graph database for fast access during recommendation generation. (1h - 2h)
    - Define the appropriate data model for storing the similarity scores in the graph database.
    - Write code to store the similarity scores in the graph database.
    - Verify that the similarity scores have been correctly stored and can be efficiently accessed during recommendation generation.


### Epic 4: Recommendation generation

- [ ] Implement the item-to-item collaborative filtering algorithm using the similarity scores and user ratings. (3h - 10h)
    - Define the item-to-item collaborative filtering algorithm to be used.
    - Write code to implement the algorithm using the similarity scores and user ratings.
    - Verify that the algorithm has been correctly implemented and can generate recommendations.
- [ ] Write code to generate personalized recommendations for users based on their ratings and preferences. (2h - 6h)
    - Define the user preferences and ratings to be used in generating personalized recommendations.
    - Write code to generate personalized recommendations based on the user's ratings and preferences.
    - Verify that the personalized recommendations have been correctly generated.
- [ ] Evaluate the performance of the recommendation engine using suitable metrics (e.g., precision, recall, F1-score). (3h - 4h)
    - Choose suitable evaluation metrics.
    - Write code to compute the evaluation metrics using the testing set.
    - Analyze the performance of the recommendation engine and identify potential areas for improvement.
- [ ] Iterate and improve the recommendation engine based on the evaluation results. (3h - 6h)
    - Based on the evaluation results, define improvements to be made to the recommendation engine.
    - Write code to implement the improvements.
    - Verify that the improvements have been correctly implemented and improve the performance of the recommendation engine.


### Epic 5: API and user interface

- [ ] Develop a RESTful API for the recommendation engine that can be accessed by external applications. (3h - 8h)
    - Define the API endpoints and methods to be used.
    - Write code to implement the API using a suitable web framework (e.g., Flask, Django).
    - Verify that the API has been correctly implemented and can be accessed by external applications.
- [ ] Design and implement a user interface for users to interact with the recommendation engine (e.g., https://hoppscotch.io/). (4h - 10h)
    - Define the user interface requirements and design (e.g., web app, mobile app).
    - Write code to implement the user interface using suitable web development technologies (e.g., HTML, CSS, JavaScript).
    - Verify that the user interface has been correctly implemented and can interact with the recommendation engine.
