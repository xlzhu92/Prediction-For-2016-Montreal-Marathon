function [J, grad] = logReg_costFunction(theta, X, y)
%%%% Applied Machine Learning - Project 1, Task 1: Logistic Regression
% Coded by Orestes Manzanilla (M.Sc.)
% orestes.manzanilla@polymtl.ca
% orestes.manzanilla@gerad.ca
%
%logReg_costFunction Computes cost (error function) and gradient
%for logistic regression.

%initialize:
m = length(y); % number of training examples
J = 0;
grad = zeros(size(theta));

%Compute J as the cost or error, and vector of gradient (one derivative for each
%parameter)
J=-(1/m)*( y' * log( sigmoid( X*theta ) ) + (1-y') * log( 1 - sigmoid( X*theta ) ) );

grad = (1/m) *  X'*( sigmoid( X*theta ) - y );


end
