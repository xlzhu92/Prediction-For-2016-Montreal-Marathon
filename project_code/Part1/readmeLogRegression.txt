In order to run the crossvalidation experiments for Logistic Regression with Gradient Descent, the script "crossValidation.m" has to be run in Matlab. 
The user will be inmediately prompted to indicate the number of folds / experiments.

The following changes can be of interest in the code in crossValidation.m:
1. Change line number 13 to use another dataset.
2. Eliminate the comment symbol "%" in line 18 in order to consider a sample of the dataset.
3. Change lines 31,32 and 33 in order to change the initial value of the vector of parameters.
4. Change norm to value = 0, in order to skip the Normalization part of the code.

The code to assign labels to data, and make the validation and training sets, is inspired by a code written by "im so cofused" in the forum
http://stackoverflow.com/questions/12630293/matlab-10-fold-cross-validation-without-using-existing-functions in September 2012.

References:
"im so confused" (2012, September 27). Stack Overflow: MATLAB: 10 fold cross Validation without using existing functions [Online forum comment]. Message posted to http://stackoverflow.com/questions/12630293/matlab-10-fold-cross-validation-without-using-existing-functions
