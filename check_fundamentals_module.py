import pandas as pd
import time
from finvizfinance.quote import finvizfinance

# ROE_5%	ROE_15%	Debt/Asset	DividendYield	Debt/Equity	NetMargin_10%	NetMargin_20%	ROA	IROR	QOE	PB	PE

def get_description(ticker):

    stock_description_list = []

    try:
        stock = finvizfinance(ticker)

        try:
            stock_description = stock.ticker_description()

            stock_description_list.append(stock_description)

        except Exception as e:

            stock_description = "NIL"

            stock_description_list.append(stock_description)

    except Exception as e:

        stock_description = "error"

        stock_description_list.append(stock_description)

    return stock_description_list

#--------------check returns of equity criteria--------------
#-------------- greater equal YES5%--------------
#-------------- greater equal 5%--------------

def check_roe(metric):

    if metric >= 15:

        roe15 = "YES"
        roe5 = "YES"

    elif metric >= 5:

        roe15 = "NO"
        roe5 = "YES"

    else:

        roe15 = "NO"
        roe5 = "NO"

    return roe5, roe15

#--------------check dividend yield criteria--------------
#-------------- greater equal 2%--------------

def check_dividend(metric):

    if metric >= 2:

        dividend = "YES"

    else:

        dividend = "NO"

    return dividend

#--------------check debt to equity ratio criteria--------------
#-------------- less than NO.5--------------
def check_debt_equity(metric):
    if metric < 0.5:

        de = "YES"

    else:

        de = "NO"

    return de

#--------------check net margin criteria--------------
#-------------- greater equal 2NO%--------------
#-------------- greater equal YESNO%--------------

def check_profit(metric):
    if metric >= 20:

        profit20 = "YES"
        profit10 = "YES"

    elif metric >= 10:

        profit20 = "NO"
        profit10 = "YES"

    else:

        profit20 = "NO"
        profit10 = "NO"

    return profit10, profit20

#--------------check returns of asset criteria--------------
#-------------- greater equal 7%--------------
#-------------- greater equal 5%--------------
def check_roa(metric):
    if metric >= 7:

        roa7 = "YES"
        roa5 = "YES"

    elif metric >= 5:

        roa7 = "NO"
        roa5 = "YES"

    else:

        roa7 = "NO"
        roa5 = "NO"

    return roa5, roa7

#--------------check price to book ratio--------------
#-------------- less than 1--------------
def check_pb(metric):
    if metric < 1:

        pb = "YES"

    else:

        pb = "NO"

    return pb

def check_peg(metric):

    if metric <= 1:

        peg = "YES"

    else:

        peg = "NO"

    return peg

def check_fundamentals(ticker):

    df = pd.DataFrame()

    country_list = []
    sector_list = []
    industry_list = []
    price_list = []

    ticker_list = []
    roe5_list = []
    roe15_list = []
    dividend_list = []
    de_list = []
    profit10_list = []
    profit20_list = []
    roa7_list = []
    roa5_list = []
    pb_list = []
    peg_list = []
    pe_list = []
    insider_own_list = []

    ticker_list.append(ticker)

    try:

        stock = finvizfinance(ticker)

        try:
            country = stock.ticker_fundament()["Country"]

            country_list.append(country)

        except Exception as e:

            country = "NIL"

            country_list.append(country)

        try:
            sector = stock.ticker_fundament()["Sector"]

            sector_list.append(sector)

        except Exception as e:

            sector = "NIL"

            sector_list.append(sector)

        try:
            industry = stock.ticker_fundament()["Industry"]

            industry_list.append(industry)

        except Exception as e:

            industry = "NIL"

            industry_list.append(industry)

        try:
            price = stock.ticker_fundament()["Price"]

            price_list.append(price)

        except Exception as e:

            price = "NIL"

            price_list.append(price)

        try:
            roe5, roe15 = check_roe(float(stock.ticker_fundament()["ROE"].replace("%", "")))

            roe5_list.append(roe5)
            roe15_list.append(roe15)

        except Exception as e:

            roe5 = "NIL"
            roe15 = "NIL"

            roe5_list.append(roe5)
            roe15_list.append(roe15)

        try:
            dividend = check_dividend(float(stock.ticker_fundament()["Dividend %"].replace("%", "")))
            dividend_list.append(dividend)

        except Exception as e:

            dividend = "NIL"

            dividend_list.append(dividend)

        try:
            de = check_debt_equity(float(stock.ticker_fundament()["LT Debt/Eq"]))
            de_list.append(de)

        except Exception as e:

            de = "NIL"
            de_list.append("NIL")

        try:
            profit10, profit20 = check_profit(float(stock.ticker_fundament()["Profit Margin"].replace("%", "")))

            profit10_list.append(profit10)
            profit20_list.append(profit20)

        except Exception as e:

            profit10 = "NIL"
            profit20 = "NIL"

            profit10_list.append(profit10)
            profit20_list.append(profit20)

        try:
            roa5, roa7 = check_roa(float(stock.ticker_fundament()["ROA"].replace("%", "")))

            roa5_list.append(roa5)
            roa7_list.append(roa7)


        except Exception as e:

            roa5 = "NIL"
            roa7 = "NIL"

            roa5_list.append(roa5)
            roa7_list.append(roa7)

        try:

            pb = check_pb(float(stock.ticker_fundament()["P/B"].replace("%", "")))
            pb_list.append(pb)

        except Exception as e:

            pb = "NIL"
            pb_list.append(pb)


        try:

            peg = check_peg(float(stock.ticker_fundament()["PEG"].replace("%", "")))
            peg_list.append(peg)

        except Exception as e:

            peg = "NIL"
            peg_list.append(peg)

        try:
            pe = stock.ticker_fundament()["P/E"]
            pe_list.append(pe)

        except Exception as e:

            pe = "NIL"
            pe_list.append(pe)

        try:
            insider_own = stock.ticker_fundament()["Insider Own"]
            insider_own_list.append(insider_own)

        except Exception as e:

            insider_own = "NIL"
            insider_own_list.append(insider_own)

        try:
            stock_chart_url = stock.ticker_charts()

        except Exception as e:

            error = "error"

        try:
            outer_ratings_df = stock.ticker_outer_ratings()

            outer_ratings_df.to_excel(str(ticker) + "_outer_ratings.xlsx", index=False)

        except Exception as e:

            error = "error"

        print(str(ticker) + "\t" + str(roe5) + "\t" + str(roe15) + "\t" + str(dividend) + "\t" + \
              str(de) + "\t" + str(profit10) + "\t" + str(profit20) + "\t" + str(roa5) + "\t" + \
              str(roa7) + "\t" + str(pb) + "\t" + str(pe))


    except Exception as e:

        country = "error"
        sector = "error"
        industry = "error"
        price = "error"
        roe5 = "error"
        roe15 = "error"
        dividend = "error"
        de = "error"
        profit10 = "error"
        profit20 = "error"
        roa7 = "error"
        roa5 = "error"
        pb = "error"
        peg = "error"
        pe = "error"
        insider_own = "error"

        country_list.append(country)
        sector_list.append(sector)
        industry_list.append(industry)
        price_list.append(price)
        roe5_list.append(roe5)
        roe15_list.append(roe15)
        dividend_list.append(dividend)
        de_list.append(de)
        profit10_list.append(profit10)
        profit20_list.append(profit20)
        roa7_list.append(roa7)
        roa5_list.append(roa5)
        pb_list.append(pb)
        peg_list.append(peg)
        pe_list.append(pe)
        insider_own_list.append(insider_own)

        print(str(ticker) + "\t" + str(roe5) + "\t" + str(roe15) + "\t" + str(dividend) + "\t" + \
                  str(de) + "\t" + str(profit10) + "\t" + str(profit20) + "\t" + str(roa5) + "\t" + \
                  str(roa7) + "\t" + str(pb) + "\t" + str(pe))

    time.sleep(2)

    df["Ticker"] = ticker_list
    df["Country"] = country_list
    df["Sector"] = sector_list
    df["Industry"] = industry_list
    df["Price"] = price_list
    df["ROE_5%"] = roe5_list
    df["ROE_15%"] = roe15_list
    df["DividendYield"] = dividend_list
    df["Debt/Equity"] = de_list
    df["NetMargin_10%"] = profit10_list
    df["NetMargin_20%"] = profit20_list
    df["ROA_5%"] = roa5_list
    df["ROA_7%"] = roa7_list
    df["PB"] = pb_list
    df["PE"] = pe_list
    df["Insider Own"] = insider_own_list
    df["No. of Criteria Met"] = df.apply(lambda row: (row == "YES").sum(), axis=1)

    return df

