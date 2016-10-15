function p = predict(theta, X)
%%%% Applied Machine Learning - Project 1, Task 1: Logistic Regression
% Coded by Orestes Manzanilla (M.Sc.)
% orestes.manzanilla@polymtl.ca
% orestes.manzanilla@gerad.ca
%
%PREDICT Predicts the class of X. It uses a fitted logistic regression

m = size(X, 1); % Number of training examples
p = zeros(m, 1);

p=round(sigmoid(X*theta));



end
