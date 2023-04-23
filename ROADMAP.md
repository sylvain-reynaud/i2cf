## Roadmap

### Epic 1: Data collection and preprocessing

- [x] Define the data sources (e.g., user ratings, item features) to be used for building the recommendation engine. (1h - 2h)
    - Research available data sources (e.g., public datasets, data from partners).
    - Determine the required data fields (e.g., user ID, item ID, rating, item features).
    - Define the format of the data sources (e.g., CSV, JSON, SQL).
- [x] Collect and store the raw data in a suitable format (e.g., CSV, JSON). (1h - 4h)
    - Write code to collect data from the defined sources.
    - Save the raw data in a local file or database for further processing.
    - Validate the raw data for missing or invalid values.
- [x] Clean and preprocess the data (e.g., remove duplicates, fill missing values). (1h - 6h)
    - Remove duplicates from the data.
    - Fill missing values with appropriate estimates (e.g., mean, median).
    - Normalize the data if necessary (e.g., scale ratings to a specific range).
    - Convert the data to a suitable format for use in the graph database.
- [ ] Split the data into training and testing sets. (.5h - 1h)
    - Define the proportion of the data to be used for training and testing.
    - Randomly split the data into two sets (training and testing).
    - Save the two sets to separate files or databases.

### Epic 2: Graph database setup

- [x] Define the schema of the graph database. (.5h - 4h)
    - Define the nodes and relationships to be used in the graph database.
    - Map the preprocessed data fields to the nodes and relationships.
    - Define the properties of the nodes and relationships (e.g., data types, uniqueness constraints).
- [x] Write code to create and populate the graph database. (2h - 8h)
    - Write code to create the nodes and relationships in the graph database.
    - Load the preprocessed data into the graph database.
    - Verify the data has been correctly loaded into the graph database.

### Epic 3: Similarity calculation

- [x] Implement the similarity measure using the graph database (e.g., using Cypher queries for Neo4j). (2h - 8h)
    - Write code to calculate the similarity between items using the chosen similarity measure.
    - Use Cypher queries (or the appropriate query language for the chosen graph database) to efficiently compute the similarity scores.
    - Verify that the similarity measure has been correctly implemented and computed.
- [x] Store the similarity scores in the graph database for fast access during recommendation generation. (1h - 2h)
    - Define the appropriate data model for storing the similarity scores in the graph database.
    - Write code to store the similarity scores in the graph database.
    - Verify that the similarity scores have been correctly stored and can be efficiently accessed during recommendation generation.


### Epic 4: Recommendation generation

- [x] Implement the item-to-item collaborative filtering algorithm using the similarity scores and user ratings. (3h - 10h)
    - Define the item-to-item collaborative filtering algorithm to be used.
    - Write code to implement the algorithm using the similarity scores and user ratings.
    - Verify that the algorithm has been correctly implemented and can generate recommendations.
- [x] Write code to generate personalized recommendations for users based on their ratings and preferences. (2h - 6h)
    - Define the user preferences and ratings to be used in generating personalized recommendations.
    - Write code to generate personalized recommendations based on the user's ratings and preferences.
    - Verify that the personalized recommendations have been correctly generated.
- [ ] Add a fallback


### Epic 5: API and user interface

- [x] Develop a RESTful API for the recommendation engine that can be accessed by external applications. (3h - 8h)
    - Define the API endpoints and methods to be used.
    - Write code to implement the API using a suitable web framework (e.g., Flask, Django).
    - Verify that the API has been correctly implemented and can be accessed by external applications.

### Epic 6: Documentation

- [x] Write documentation for the recommendation engine.

### Epic 7: Deployment

- [x] Deploy the recommendation engine