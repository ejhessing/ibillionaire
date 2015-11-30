# ibillionaire
# Purpose
	crawl the data of http://www.ibillionaire.me/billionaires/
	v1: input a number to get each billionaire investor's portfolio, such as Warren Buffett = 0
	v2: based on stock types to get a summary of all billionaire investors' portfolio, export to json
# User Statement
	When you use , you agree to all of the results must be responsible for your own
# Install

### Python Package
	1. virtualenv venv
	2. source venv/bin/activate
	3. pip install -r requirements.txt

# Execution
	V1: input a number 0 ~ 15, other parameters will quit
	V2: output a json file

### Start
  - python ETF_trading_system.py
  - python ETF_trading_systemV2.py

# Issue
	the portfolio percentage does not match, but it is designer's problem, I can't fix