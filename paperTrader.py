import yfinance as yf
import pandas as pd

def menu():
    while(True):
        print("\nType:")
        print("ADD to add a stock")
        print("REMOVE to remove a stock")
        print("VIEW to view portfolio")
        #Add updatePortfolio() (+ progress bar)
        #Add checkPortfolio() (Dividends?)
        print("END to finish")
        
        menu_input = input()
        if menu_input == "ADD":
            addStock()
        elif menu_input == "REMOVE":
            removeStock()
        elif menu_input == "VIEW":
            viewPortfolio()
        elif menu_input == "END":
            break
        else:
            print("Invalid menu option.")

def addStock():
    stock = input("Enter stock ticker: ")
    stock_ticker = stock
    stock_ticker = str(stock_ticker)
    units_held = float(input("Enter number of units held: "))
    purchase_price = float(input("Enter purchase price: "))
    purchase_total = units_held * purchase_price

    stock = yf.Ticker(stock)
    stock_price = stock.info['currentPrice']
    stock_price = float(stock_price)
    current_total = units_held * stock_price

    new_row = [stock_ticker, units_held, purchase_total, current_total]
    df.loc[len(df)] = new_row
    df.to_csv(input_path, index=False)

def removeStock():
    def filter_rows_by_values(df, col, values):
        return df[~df[col].isin(values)]
    
    removed_stock = input("Enter stock(s) to remove (separate multiple stocks with a space): ")
    removed_stock_lst = []
    removed_stock_lst = removed_stock.split()
    global df
    df = filter_rows_by_values(df, "Stock", removed_stock_lst)
    df.to_csv(input_path, index=False)

def viewPortfolio():
    print(df)
    #Add P/L per stock in portfolio, maybe a new df
    totalPurchasePrice = round(df['Purchase Total'].sum(), 3)
    print("Total Purchase Price: " + str(totalPurchasePrice))
    totalCurrentPrice = round(df['Current Total'].sum(), 3)
    print("Total Current Price: " + str(totalCurrentPrice))
    returnPercentage = round(((totalCurrentPrice / totalPurchasePrice) * 100), 3)
    print("Return Percentage: " + str(returnPercentage) + "%")

def updatePortfolio():
    pass
    #Update file with current stock prices

def checkPortfolio():
    pass
    #Compare portfolio performance with specified index

    #ASX_200 = yf.Ticker("AXNT")
    #ASX_200_price = ASX_200.info['currentPrice'] (why doesn't this work?)
    #print(ASX_200_price)

print("A compatible CSV file has 4 columns: Stock, Units Held, Purchase Total and Current Total")
input_path = str((input("Please input a path to portfolio (.csv only): ")))
input_path = input_path.replace('\\','/')
df = pd.read_csv(input_path)

menu()
