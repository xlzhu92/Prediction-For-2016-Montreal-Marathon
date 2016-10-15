function [X_norm, mu, sigma] = featureNormalize(X)
%%%% Applied Machine Learning - Project 1, Task 1: Logistic Regression
% Coded by Orestes Manzanilla (M.Sc.)
% orestes.manzanilla@polymtl.ca
% orestes.manzanilla@gerad.ca
%
%FEATURENORMALIZE performs normalization of the features in X 
%the resulting matrix, for each feature, is centered around mu, and
%scaled by the standard deviation of the feature.

X_norm = X;
mu = zeros(1, size(X, 2));
sigma = zeros(1, size(X, 2));

for dim=1:size(X,2)
    mu(1,dim) = mean(X(:,dim)); 
    sigma(1,dim) = std(X(:,dim));
    X_norm(:,dim) = (X(:,dim)-mu(1,dim))/sigma(1,dim);
end

end
