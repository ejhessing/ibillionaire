library(httr)
library(XML)

url <- "http://www.ibillionaire.me/funds/1/berkshire-hathaway/warren-buffett/2015-0"

tablePath <- "//table/tbody/tr/td[%s]"
res <- content(GET(paste0(url, 9)))
df <- data.frame(NA)
for (i in 1:5) {
  if (i==1 || i==2) {
    path <- paste0(sprintf(tablePath, i), "/a[1]")
  } else {
    path <- sprintf(tablePath, i)
  }
  
  temp <- xpathSApply(res, path, xmlValue)
  df <- cbind(df, temp)
}
df <- df[,colSums(is.na(df))<nrow(df)]
names(df) <- c("Company", "Ticker", "Activity", "P_Fund", "Avg_Cost")

