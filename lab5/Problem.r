# Load the bnlearn package
library(bnlearn)

# Load your dataset containing grades earned by students in respective courses
data <- read.table("/content/drive/MyDrive/2020_bn_nb_data.txt", header = TRUE, sep = ",")

# Define the Bayesian network structure learning algorithm (Hill Climbing with K2 score)
hc_algorithm <- hc(data, score = "k2")

# Learn the structure of the Bayesian network using hill climbing
model <- bn.fit(hc_algorithm, data)

# Visualize the resulting Bayesian network
plot(model)

# Learn the Conditional Probability Tables (CPTs) for each course node
cpt <- bn.fit(model, data)

# Print the CPTs for each course node
print(cpt)

# Predict the grade in PH100 given specific grades in other courses
# Use cpdist function to get the distribution of grades in PH100
evidence <- list(EC100 = "DD", IT101 = "CC", MA101 = "CD")
distribution <- cpdist(model, nodes = "PH100", evidence = evidence)

# Visualize the distribution graph
plot(distribution)

# Print the distribution table
print(distribution)

# qeustion 2

# Learn the Conditional Probability Tables (CPTs) for each course node
cpt <- bn.fit(model, data)

# Print the CPTs for each course node
print(cpt)

# qeustion 3
# Predict the grade in PH100 given specific grades in other courses
evidence <- list(EC100 = "DD", IT101 = "CC", MA101 = "CD")
distribution <- cpdist(model, nodes = "PH100", evidence = evidence)

# Visualize the distribution graph
plot(distribution)

# Print the distribution table
print(distribution)
# qeustion 4

# Split the data into training and testing sets (70% training, 30% testing)
set.seed(123)  # Set seed for reproducibility
train_indices <- sample(1:nrow(data), 0.7 * nrow(data))
train_data <- data[train_indices, ]
test_data <- data[-train_indices, ]

# Build a naive Bayes classifier
model_nb <- naive.bayes(train_data[, -ncol(train_data)], train_data[, ncol(train_data)])

# Predict qualification status for test data
predictions <- predict(model_nb, test_data[, -ncol(test_data)])

# Calculate accuracy
accuracy <- sum(predictions == test_data[, ncol(test_data)]) / nrow(test_data)
print(paste("Accuracy:", accuracy))

# qeustion 5
# Learn the Bayesian network structure learning algorithm (Hill Climbing with K2 score)
hc_algorithm_dependent <- hc(data, score = "k2")

# Learn the structure of the Bayesian network using hill climbing
model_dependent <- bn.fit(hc_algorithm_dependent, data)

# Build a naive Bayes classifier
model_nb_dependent <- naive.bayes(train_data[, -ncol(train_data)], train_data[, ncol(train_data)], bayes_net = model_dependent)

# Predict qualification status for test data
predictions_dependent <- predict(model_nb_dependent, test_data[, -ncol(test_data)], bayes_net = model_dependent)

# Calculate accuracy
accuracy_dependent <- sum(predictions_dependent == test_data[, ncol(test_data)]) / nrow(test_data)
print(paste("Accuracy (dependent grades):", accuracy_dependent))

