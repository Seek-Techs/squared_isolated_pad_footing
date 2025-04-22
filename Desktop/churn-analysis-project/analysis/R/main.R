# R/main.R

# Source the necessary scripts
source("R/data_loading.R")
source("R/preprocessing.R")
source("R/utils.R")

# 1. Load the data
churn <- load_churn_data("data/raw/Telco-Customer-Churn.csv")

# 2. Preprocess the data
churn <- handle_missing_total_charges(churn)

# 3. Specify column to rename
cols_recode1 <- c("OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies")
churn <- recode_categorical_columns(churn, cols_recode1)

#Add columns that are needed for the cleaning/
churn <- remove_col(churn)

#4 tranform it.

colss <- c("Contract","PaymentMethod","gender","tenure_group","MultipleLines","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","PaperlessBilling")
churn <- ohe(churn, colss)

#5 remove that that is no long used after one hot econding
removeCols <- c("Contract","PaymentMethod","gender","tenure_group","MultipleLines","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","PaperlessBilling")

# Ensure those codes has data and it the data work properly.
for (col in removeCols) {
  # Ensure those codes has data and it the data work properly.
  if (col %in% colnames(churn)) {
    churn[col] <- NULL
  }
}
#To add code that will ensure and run well.



# 7. Correct variable types to all dataset after transformation
churn<- correct_variable_types(churn)

# 8. Save the processed data
save_data_to_csv(churn, "data/processed/churn_clean.csv")

message("Data cleaning and preprocessing complete.")

# Load the processed data
churn <- read.csv("data/processed/churn_clean.csv")