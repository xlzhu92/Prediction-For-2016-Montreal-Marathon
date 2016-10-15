%%%% Applied Machine Learning - Project 1, Task 1: Logistic Regression
% Coded by Orestes Manzanilla (M.Sc.)
% orestes.manzanilla@polymtl.ca
% orestes.manzanilla@gerad.ca
%
%%K-FOLD CROSSVALIDATION 
%
%This script runs experiments of logistic regression
%with k-fold crossvalidation
%
%
fprintf('K-fold Crossvalidation of Logistic Regression with Gradient Descent \n');
%% Load Data
%  The first n-1 columns contains features X
%  the n-th contains the label y

data = load('marathonData_y15.txt'); %FIRST REPRESENTATION
%data = load('marathonData_y15_ageCats.txt'); %SECOND REPRESENTATION
%data = load('ex2data1_logReg.txt'); %simple 2D data to test the algorithm


%data = datasample(data,4000,'Replace',false); %sampling to study effect of
%data size.

[rows cols] = size(data);
X = data(:, [1:cols-1]); y = data(:, cols);
[m, n] = size(X);

fprintf('1. Data has been loaded \n');

%% Initialization
%  Setup the data matrix and a column of ones for the intercept term
% Indicate here the conditions of the experiments

initial_theta = ones(n + 1, 1) %vector or parameters to be fit (initial sol)
alpha = 0.01 %Indicate here Learning rate or Step size
iter = 1000  %Indicate here limit on number of iterations
norm = 1 %Indicate a value of 1 if the data is to be normalized
             %or 0 otherwise

%Normalize the matrix of features
if norm == 1
    [X mu sigma] = featureNormalize(X);
    fprintf('2. Features have been Normalized \n');
end

% Add intercept term to x and X_test
X = [ones(m, 1) X];

% Initialize fitting parameters
fprintf('3. Parameters initialized \n');

%% Prepare the crossvalidation 
 disp('3. Parameters for Testing:');
 disp('Choose the number of folds "K" for the crossvalidation (Default is 5 folds)')
 NumFolds = input('K = ');
 if (isempty(NumFolds)) | (NumFolds< 0) | (NumFolds> m) 
     NumFolds = 5;
 end
  
 
 %Generate labels to assign each data to a fold
 %Modification of code submitted by user "Im so confused" in the following
 %url: http://stackoverflow.com/questions/12630293
 %.../matlab-10-fold-cross-validation-without-using-existing-functions
 
 indexes = randperm(m); %indexes to assign labels randomly 
 fold = 1; %the first fold for which a datum will be assigned
 labels = zeros(m,1); %initialize vector with labels
 for i=1:m
    labels( indexes(i) ) = fold; %datum in random position is asigned to fold
    fold = fold + 1; %next fold
    if fold == NumFolds+1
        fold = 1; %start again asigning a datum to the first fold
    end
 end
 
%% Perform the K validation experiments

%initialize matrixes for posterior statistics and analysis
cost_history_matrix = [];
grad_history_matrix = [];
accuracies_train = zeros(NumFolds,1);
accuracies_val = zeros(NumFolds,1);

for fold = 1:NumFolds
    fprintf('Running experiment for fold: %f\n', fold);
    %Pick Training set
    X_train = X( (labels ~= fold) , : );
    y_train = y( (labels ~= fold) , : );
    
    %Pick Validation set
    X_val = X( (labels == fold) , : );
    y_val = y( (labels == fold) , : );
 
    
    % Compute and display initial cost and gradient
    theta = initial_theta
    [cost, grad] = logReg_costFunction(theta, X_train, y_train);

    %Optimize (fit) parameters via Gradient Descent
    [theta, cost_history, grad_history] = logRegGradientDescentMulti(X_train, y_train, theta, alpha, iter);
    
    % Print theta to screen
    fprintf('Cost function value for the value of theta: %f\n', cost);
    fprintf('theta: \n');
    fprintf(' %f \n', theta);
    
    %Calculate accuracy in Training set
    prediction = predict(theta, X_train);
    accuracy_train = mean(double(y_train == prediction));
    
    %Calculate accuracy in Validation set
    prediction = predict(theta, X_val);
    accuracy_val = mean(double(y_val == prediction));
    
    %save history of costs, grads and accuracies
    cost_history_matrix = [cost_history_matrix, cost_history];
    grad_history_matrix = [grad_history_matrix, grad_history];
    accuracies_train(fold) = accuracy_train;
    accuracies_val(fold) = accuracy_val;
   
end
    
%% Some statistics
mean_error_train = 1-mean(accuracies_train)
mean_error_val = 1-mean(accuracies_val)

%% train on whole Data to predict new data

theta = initial_theta
[cost, grad] = logReg_costFunction(theta, X_train, y_train);

%Optimize (fit) parameters via Gradient Descent
[theta_final, cost_history, grad_history] = logRegGradientDescentMulti(X_train, y_train, theta, alpha, iter);
    
% Print theta to screen
fprintf('Cost function value for the value of theta: %f\n', cost);
fprintf('theta fitted with whole training set: \n');
fprintf(' %f \n', theta_final);

%load new data
data_new = load('marathonData_predict16.txt');

[rows_new cols] = size(data_new);
X_new = data_new;
[m_new, n] = size(X);

for dim=1:size(X_new,2)
    %normalize data in the same way as the training set data
    X_new_norm(:,dim) = (X_new(:,dim)-mu(1,dim))/sigma(1,dim);
end

X_new = X_new_norm;

X_new = [ones(m_new, 1) X_new]; %add column for intercept

%Calculate predictions on new data
prediction_new = predict(theta_final, X_new);

fprintf('\nPress key to continue to the plots.\n');
pause;

%% Analyzing performance 
%Choose fold to plot:
plottingFold = 1;

plot( cost_history_matrix( : , plottingFold ) )
% Put some labels 
hold on;
% Labels and Legend
xlabel('iterations')
ylabel('cost function')
hold off;

fprintf('\nPress key to continue to the next plot.\n');
pause;

%% PART 4.b: Analyzing gradient convergence
plot(grad_history_matrix( : , plottingFold ) );
% Put some labels 
hold on;
% Labels and Legend
xlabel('iterations')
ylabel('2-norm of gradient vector')
hold off;

  
