# R/data_loading.R

#' Load Telco Customer Churn Data
#'
#' Loads the Telco Customer Churn dataset from a CSV file.
#'
#' @param file_path Path to the CSV file.
#' @return A data frame containing the churn data.
#' @examples
#' churn_data <- load_churn_data("data/raw/Telco-Customer-Churn.csv")
load_churn_data <- function(file_path) {
  tryCatch({
    churn_data <- read.csv(file_path, stringsAsFactors = FALSE) #Load as character strings initially
    message("Data loaded successfully from ", file_path)
    return(churn_data)
  }, error = function(e) {
    stop("Error loading data: ", e$message)
  })
}