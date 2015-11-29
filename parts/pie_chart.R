library(httr)
library(stringr)
library(jsonlite)

url = "http://www.ibillionaire.me/funds/1/warren-buffett/berkshire-hathaway"
res_text <- content(GET(url), "text")

res_json_1 <- str_match(res_text, pattern = "data: eval\\('(.*)'\\)")[,2]
res_json_2 <- str_match(res_text, pattern = "sectors_for_fund_secs = (.*);")[,2]

fromJSON(res_json_1)
fromJSON(res_json_2)

