function g = sigmoid(z)
%%%% Applied Machine Learning - Project 1, Task 1: Logistic Regression
% Coded by Orestes Manzanilla (M.Sc.)
% orestes.manzanilla@polymtl.ca
% orestes.manzanilla@gerad.ca
%
%SIGMOID Computes sigmoid functoon
%   J = SIGMOID(z) calculates the sigmoid of z.


g = zeros(size(z));

%(z can be scalar, vector or matrix)

g=1./(1+exp(-z));


end
