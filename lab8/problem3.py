# # Taking Gini Index as criterion


# ## One tree


# %%
clf = DecisionTreeClassifier(criterion="gini")
clf.fit(X_train,y_train)
plot_tree(clf)[-1]


# %%
predictions = clf.predict(X_test)
accuracy = accuracy_score(y_test,predictions)
f1score = f1_score(y_test,predictions, average='weighted')
print("Accuracy: ", accuracy)
print("F1 score: ", f1score)


# %% [markdown]
# ## 20 trees


# %%
accuracies = []
f_scores = []


# Number of iterations
num_iterations = 20


for i in range(num_iterations):
    X_train_i = []
    y_train_i = []
    X_test_i = []
    y_test_i = []
    
    X_train_i,X_test_i,y_train_i,y_test_i=train_test_split(encoded_data,
target_encoded, test_size=0.4, random_state=i)


    # Initialize and train Decision Tree Classifier
    classifier = DecisionTreeClassifier(criterion='gini')
    classifier.fit(X_train_i, y_train_i)


    # Make predictions
    y_pred = classifier.predict(X_test_i)


    # Calculate F1-score
    f1 = f1_score(y_test, y_pred, average='weighted')


    # Calculate accuracy from confusion matrix
    accuracy = accuracy_score(y_test,y_pred)


    # Append accuracy and F1-score to lists
    accuracies.append(accuracy)
    f_scores.append(f1)


# Calculate average accuracy and F1-score
avg_accuracy = np.mean(accuracies)
avg_f1_score = np.mean(f_scores)


print("Average Accuracy:", avg_accuracy)
print("Average F1-Score:", avg_f1_score)
