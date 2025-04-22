# let build model

# Load libraries
library(dplyr)
library(caret)
library(pROC)

# Assume train_data, test_data, target_variable, and features are provided by the other team

# Function for training and evaluating models
train_and_evaluate_model <- function(train_data, test_data, model_type, target_variable, features, probability_threshold = 0.5) {
  # Args:
  #   train_data: Training dataset (data.frame).
  #   test_data: Testing dataset (data.frame).
  #   model_type: Type of model ('logistic_regression' or 'random_forest').
  #   target_variable: Name of the target variable (string).
  #   features: Vector of feature names (character vector).
  #   probability_threshold: Threshold for converting probabilities to class labels (numeric, default 0.5).
  #
  # Returns:
  #   A list containing the trained model, confusion matrix, evaluation metrics, predictions, and predicted classes.
  
  # Input validation
  if (!model_type %in% c("logistic_regression", "random_forest", "gbm")) { #Added gbm as potential method
    stop("Invalid model_type. Choose from 'logistic_regression', 'random_forest', or 'gbm'.")
  }
  
  # Convert target to factor (ensure consistent factor levels)
  train_data[[target_variable]] <- as.factor(train_data[[target_variable]])
  test_data[[target_variable]]  <- as.factor(test_data[[target_variable]])
  
  # Formula for the model
  formula <- as.formula(paste(target_variable, "~", paste(features, collapse = "+")))
  
  # Model Training using caret::train
  if (model_type == "logistic_regression") {
    model <- caret::train(formula, data = train_data, method = "glm", family = binomial(), trControl = trainControl(method = "cv", number = 10))
  } else if (model_type == "random_forest") {
    model <- caret::train(formula, data = train_data, method = "rf", trControl = trainControl(method = "cv", number = 10))
  }  else if (model_type == "gbm") {
    model <- caret::train(formula, data = train_data, method = "gbm", trControl = trainControl(method = "cv", number = 10)) #Example GBM
  }
  
  # Print model summary
  print(summary(model))
  
  # Prediction
  predictions <- predict(model, newdata = test_data, type = "prob")[, 2]  # Probabilities of class 1
  
  predicted_classes <- ifelse(predictions > probability_threshold, 1, 0)  # Convert probabilities to class labels
  
  # Evaluation
  cm <- confusionMatrix(data = factor(predicted_classes), reference = factor(test_data[[target_variable]]))
  
  # Extract metrics from the confusion matrix
  accuracy <- cm$overall["Accuracy"]       # Overall accuracy
  precision <- cm$byClass["Pos Pred Value"]  # Precision (Positive Predictive Value)
  recall <- cm$byClass["Sensitivity"]        # Recall (Sensitivity, TPR)
  f1 <- cm$byClass["F1"]                   # F1-score
  
  # Calculate AUC
  roc_obj <- roc(test_data[[target_variable]], predictions)
  auc_value <- auc(roc_obj)
  
  # Return Results
  results <- list(
    model = model,
    confusion_matrix = cm,
    accuracy = accuracy,
    precision = precision,
    recall = recall,
    f1 = f1,
    auc = auc_value,
    predictions = predictions,
    predicted_classes = predicted_classes
  )
  
  return(results)
}

# Example usage:
target_variable <- "Churn" # Or whatever the column is called
features <-  c("gender", "SeniorCitizen", "Partner", "Dependents", "PhoneService",
               "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup",
               "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies",
               "Contract", "PaperlessBilling", "PaymentMethod", "tenure_group","MonthlyCharges") # Adapt to your actual feature names

#Run the code
logistic_results <- train_and_evaluate_model(
  train_data = train_data,
  test_data = test_data,
  model_type = "logistic_regression",
  target_variable = target_variable,
  features = features
)

print("Logistic Regression Results:")
print(logistic_results$confusion_matrix)
print(paste("Accuracy:", logistic_results$accuracy))
print(paste("Precision:", logistic_results$precision))
print(paste("Recall:", logistic_results$recall))
print(paste("F1-score:", logistic_results$f1))
print(paste("AUC:", logistic_results$auc))

random_forest_results <- train_and_evaluate_model(
  train_data = train_data,
  test_data = test_data,
  model_type = "random_forest",
  target_variable = target_variable,
  features = features
)

print("Random Forest Results:")
print(logistic_results$confusion_matrix)
print(paste("Accuracy:", logistic_results$accuracy))
print(paste("Precision:", logistic_results$precision))
print(paste("Recall:", logistic_results$recall))
print(paste("F1-score:", logistic_results$f1))
print(paste("AUC:", logistic_results$auc))

gbm_results <- train_and_evaluate_model(
  train_data = train_data,
  test_data = test_data,
  model_type = "gbm",
  target_variable = target_variable,
  features = features
)

print("GBM Results:")
print(logistic_results$confusion_matrix)
print(paste("Accuracy:", logistic_results$accuracy))
print(paste("Precision:", logistic_results$precision))
print(paste("Recall:", logistic_results$recall))
print(paste("F1-score:", logistic_results$f1))
print(paste("AUC:", logistic_results$auc))