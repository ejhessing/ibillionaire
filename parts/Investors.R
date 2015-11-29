library(XML)
library(RCurl)
url <- 'http://www.ibillionaire.me/billionaires/'
html <- htmlParse(getURL(url))
href <- xpathSApply(html, "//div[@class='investor col-md-2']/a[@href]", xmlAttrs)
name <- xpathSApply(html, "//div[@class='investor col-md-2']/a/span/h2", xmlValue)
Investor = vector()
for (i in 1:length(name)){
  Investor[i] <- strsplit(name[i], " ")[[1]][1]
}
Investor
InvestorHref <- data.frame(Investor, href)
