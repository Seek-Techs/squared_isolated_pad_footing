# tests/test_preprocessing.R
library(testthat)

# Source the preprocessing functions
source("R/preprocessing.R")
source("R/data_loading.R")

# Load test data (replace with a smaller, representative dataset)
test_data <- data.frame(
  TotalCharges = c("10", "20", ""),
  Churn = c("Yes", "No", "Yes"),
  tenure = c(10, 20, 30),
  Contract = c("Month-to-month", "One year", "Two year"),
  stringsAsFactors = FALSE
)
test_data <- load_churn_data("data/raw/Telco-Customer-Churn.csv")


# Test handle_missing_total_charges function
test_that("handle_missing_total_charges handles missing values correctly", {
  expect_no_error(handle_missing_total_charges(test_data)) #Does it run
  
  cleaned_data <- handle_missing_total_charges(test_data)
  expect_equal(sum(is.na(cleaned_data$TotalCharges)), 0) #Are all values removed
  
  #Check the output contains correct
  expect_equal(cleaned_data$tenure,test_data$tenure[1:dim(cleaned_data)[1]]) #
})

#Add more test
# Test group_tenure function
test_that("group_tenure function works correctly", {
  # Call the function
  transformed <- remove_col(test_data)
  
  # Test for expected errors
  expect_no_error(remove_col(test_data))
})

test_that("Ensure function one_hot_encode is able to perform it well", {
  #Define cols
  test_data <- load_churn_data("data/raw/Telco-Customer-Churn.csv")
  
  #Define cols
  colss <- c("Contract","PaymentMethod","gender","tenure_group","MultipleLines","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","PaperlessBilling")
  test30 <- ohe(test_data, colss)
  
  # Test for expected errors
  expect_no_error(ohe(test_data, colss))
  #
  print(colnames(test30)) #What features are shown
  
  #Print out for the right variable
  expect_true("Contract.One.year" %in% colnames(test30)) #Example
  #If the output is not valid then I would test this out.
})