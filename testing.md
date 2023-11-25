- In this document, we will establish the functions and tests required by the students. 
- All students will generate doc_strings for all classes and functions they create. These docstrings will 
  have a one line description of the functions, list the function arguments, and the return value. 
- I have not yet decided whether type hinting should be required. 
- Testing the code structure (if possible) would allow additional points to be accrued. 

# Part 1
## B. Load and prepare the mnist dataset, i.e., call the prepare_data and filter_out_7_9s functions, as a data matrix 𝑋 consisting of only the digits 7 and 9. Make sure that every element in the data matrix is a floating point number and scaled between 0 and 1. Also check that the labels are integers. Print out the length of the filtered 𝑋 and 𝑦, and the maximum value of 𝑋 for both training and test sets.

- Student code should include the class  MNIST_Part_1 along with the functions prepare_data and filter_out_7_9s (provided in the problem)
- test_prepare_data: check the size of the data readin (should work for all students since the datasets are provided)
test  that only 7 and 9's are included by calling prepare data and filter_out_7_9s. Test that all labels are integers by comparing the arrays read in before and after conversion
to ints. 

## C. Train your first classifier using 𝑘-fold cross validation (see train_simple_classifier_with_cv function). Use 5 splits and a Decision tree classifier. Print the mean and standard deviation for the accuracy scores in each validation set in cross validation. Also print the mean and std of the fit (or training) time.

Student should have a function part-1-C in the class. 
- check that the number of splits is 5. 

## D. Repeat Part C with a random permutation 𝑘-fold cross-validator.

## E. Repeat part D for 𝑘=2,5,8,16, but do not print the training time. Note that this may take a long time (2–5 mins) to run. Do you notice anything about the mean and/or standard deviation of the scores for each k?

## F. Repeat part D with another classifier of your choice (e.g., logistic regression, support vector machine). Make sure the train test splits are the same for both models when performing cross-validation. Which model has the highest accuracy on average? Which model has the lowest variance on average? Which model is faster to train?

## G. For the classifier you trained in part F, manually (or systematically i.e., using grid search (UNDERLINE)) modify hyperparameters, and see if you can get a higher mean accuracy. Finally train the classifier on all the training data (e.g., without cross-validation) and get an accuracy score on the test set. Print out the training and testing accuracy and comment on how it relates to the mean accuracy when performing cross validation. Is it higher, lower or about the same?

# Randomness: 
- emphasize to the students the importance of code reproducibility 
- random_tate should be set in all functions and set to 42. 

# Objects (validators, models=BaseEstimators)
Students will provide objects. That allows the testing to check whether the objects are set up correctly, for 
example checking array shapes, cross-validation folds, random_state. 

# Part 2
