# Code-smell-analysis

The application serves as a front-end interface, allowing users to submit code for processing and extraction. It also provides the option to specify additional details, such as the prompt that will help the SLM interpret the context or intended query, the selection of the SLM to be used during processing, and the definition of the extraction type, whether for classes or methods. Furthermore, the application informs the user when processing begins, ensuring clarity and ease of use throughout the execution of the task.


# Ml4smells-code-extractor.API

The application operates within an anti-corruption layer (ACL), acting as an event producer. Its main responsibility is to receive requests from the frontend service, process them, and extract relevant information, such as the classes or methods present in the submitted files. This functionality enables the identification of classes and methods, along with their respective properties. To achieve this, the application uses the Abstract Syntax Tree (AST) technique, which provides a structural representation of the input code. After extracting the information, the application sends an event to the router, allowing the ml4smells-llm-integrator service to consume it.


# Ml4smells-llm-integrator

The main objective of this application is to act as an event consumer, receiving messages from the router and processing them according to the attributes defined in the event payload. To perform this processing, the application interacts with SLMs, either through an instance of Ollama or via RESTful protocols. After the processing is completed and the operational data is obtained, the results are stored in a relational database, ensuring their availability for data analysis and future research.


# Contracts

This project adopts a distributed architecture, in which each service is responsible for a specific part of the system and, consequently, uses contracts to establish communication between the microservices. All contracts are organized in the folder: `docs/contracts`


# Machine Learning 

This application uses machine learning techniques to enhance the classification of code smells by analyzing multiple project-related metrics. The models were developed and executed using the PyCaret library, leveraging a set of 15 widely adopted ML algorithms commonly used in defect and code smell classification tasks.


## Machine Learning Algorithms Used

| #  | Algorithm Name                         | Abbreviation | Description                                                                 |
|----|---------------------------------------- |------------- |-----------------------------------------------------------------------------|
| 1  | k-Nearest Neighbor                     | kNN          | Instance-based learning algorithm that classifies data based on proximity.  |
| 2  | Linear Regression                      | LR           | Models the relationship between variables by fitting a linear equation.     |
| 3  | Support Vector Machine                  | SVM          | Finds the hyperplane that best separates classes in high-dimensional space. |
| 4  | Decision Tree                          | DT           | Tree-based model that splits data into branches based on feature values.    |
| 5  | Random Forest                          | RF           | Ensemble of decision trees to improve predictive accuracy and control overfitting. |
| 6  | Extreme Gradient Boosting package       | XGB          | Optimized gradient boosting framework with regularization to reduce overfitting. |
| 7  | Ridge Classifier                        | RC           | Linear classifier with L2 regularization to prevent overfitting.            |
| 8  | Light Gradient Boosting                 | LGB          | Fast, efficient gradient boosting framework optimized for speed and performance. |
| 9  | Gradient Boosting                       | GB           | Ensemble method that builds models sequentially to minimize prediction errors. |
| 10 | Ada Boost                               | ADA          | Boosting method that combines weak classifiers to form a strong classifier. |
| 11 | Extra Trees                             | ET           | Ensemble of randomized decision trees that improves diversity and performance. |
| 12 | Naive Bayes                             | NB           | Probabilistic classifier based on applying Bayes' theorem with independence assumptions. |
| 13 | Linear Discriminant Analysis            | LDA          | Linear classifier that projects data to maximize class separability.        |
| 14 | Quadratic Discriminant Analysis         | QDA          | Variant of LDA that allows quadratic decision boundaries.                   |
| 15 | Dummy Classifier                        | DC           | Baseline model that makes predictions using simple rules (e.g., stratified, most frequent). |



# Deep Learning

This application uses deep learning techniques to improve the classification of code smells by capturing complex, non-linear relationships between various project-related metrics. The models were developed and executed using state-of-the-art DL architectures, including MLP, LSTM, GRU, and AutoKeras, which automates neural network design and optimization for enhanced performance.


## Deep Learning Algorithms Used

| #  | Algorithm Name                         | Abbreviation | Description                                                                |
|----|---------------------------------------- |------------- |----------------------------------------------------------------------------|
| 1  | Multi-Layer Perceptron                  | MLP          | Neural network with multiple layers, effective in modeling complex patterns.|
| 2  | Long Short-Term Memory                  | LSTM         | RNN variant specialized in capturing long-term temporal dependencies.       |
| 3  | Gated Recurrent Unit                    | GRU          | Simplified RNN variant, often with performance comparable to LSTM.          |
| 4  | AutoKeras                               | -            | Automated framework for designing and tuning deep learning models.          |


# Article

[📄 Link to the Article]()
