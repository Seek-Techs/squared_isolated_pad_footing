# R/utils.R

#' Save Data to CSV
#'
#' Saves a data frame to a CSV file.
#'
#' @param data A data frame.
#' @param file_path Path to the output CSV file.
#' @param row_names Whether to include row names in the CSV file (default: FALSE).
#' @examples
#' save_data_to_csv(churn_data, "data/processed/churn_clean.csv")
save_data_to_csv <- function(data, file_path, row_names = FALSE) {
  tryCatch({
    write.csv(data, file_path, row.names = row_names)
    message("Data saved successfully to ", file_path)
  }, error = function(e) {
    stop("Error saving data: ", e$message)
  })
}