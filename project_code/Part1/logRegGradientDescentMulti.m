function [theta, cost_history, grad_history] = logRegGradientDescentMulti(X, y, theta, alpha, num_iters)
%%%% Applied Machine Learning - Project 1, Task 1: Logistic Regression
% Coded by Orestes Manzanilla (M.Sc.)
% orestes.manzanilla@polymtl.ca
% orestes.manzanilla@gerad.ca
%
%logRegGradientDescentMulti Performs gradient descent to learn theta

%Initialization
m = length(y); % size of training dataset
cost_history = zeros(num_iters, 1);
grad_history = zeros(num_iters, 1);
[cost, grad] = logReg_costFunction(theta, X, y); %valores iniciales

for iter = 1:num_iters

    %Perform gradient descent step
    theta = theta - alpha*grad; %simultaneously update parameter vector
    [cost, grad] = logReg_costFunction(theta, X, y); %calculate new cost and gradient
    
% Save the cost J in every iteration    
    cost_history(iter) = cost;
    grad_history(iter) = grad'*grad;
  

end

end
