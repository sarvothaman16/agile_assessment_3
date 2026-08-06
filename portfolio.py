portfolio = [
    {
        "Investor ID": 101,
        "Stock Symbol": "TCS",
        "Quantity": 50,
        "Buy Price": 3200,
        "Current Price": 3600,
        "Sector": "IT",
        "Dividend": 5000
    },
    {
        "Investor ID": 102,
        "Stock Symbol": "INFY",
        "Quantity": 80,
        "Buy Price": 1450,
        "Current Price": 1600,
        "Sector": "IT",
        "Dividend": 3000
    },
    {
        "Investor ID": 103,
        "Stock Symbol": "HDFCBANK",
        "Quantity": 60,
        "Buy Price": 1500,
        "Current Price": 1420,
        "Sector": "Banking",
        "Dividend": 2000
    },
    {
        "Investor ID": 104,
        "Stock Symbol": "RELIANCE",
        "Quantity": 40,
        "Buy Price": 2500,
        "Current Price": 2800,
        "Sector": "Energy",
        "Dividend": 4000
    },
    {
        "Investor ID": 105,
        "Stock Symbol": "SUNPHARMA",
        "Quantity": 70,
        "Buy Price": 900,
        "Current Price": 980,
        "Sector": "Healthcare",
        "Dividend": 2500
    }
]

sector_exposure = {}

print("\n========== STOCK PORTFOLIO REPORT ==========")

for stock in portfolio:

    investment = stock["Quantity"] * stock["Buy Price"]

    current_value = stock["Quantity"] * stock["Current Price"]

    profit_loss = current_value - investment + stock["Dividend"]

    percentage_return = (profit_loss / investment) * 100

    stock["Investment"] = investment
    stock["Current Value"] = current_value
    stock["Profit"] = profit_loss
    stock["Return"] = percentage_return

    print("\nInvestor ID :", stock["Investor ID"])
    print("Stock :", stock["Stock Symbol"])
    print("Investment Value : ₹", investment)
    print("Current Value : ₹", current_value)
    print("Profit/Loss : ₹", profit_loss)
    print("Percentage Return : {:.2f}%".format(percentage_return))

    sector_exposure[stock["Sector"]] = sector_exposure.get(
        stock["Sector"], 0) + current_value

best = max(portfolio, key=lambda x: x["Return"])
worst = min(portfolio, key=lambda x: x["Return"])

print("\nBest Performing Stock")
print(best["Stock Symbol"], "- {:.2f}%".format(best["Return"]))

print("\nWorst Performing Stock")
print(worst["Stock Symbol"], "- {:.2f}%".format(worst["Return"]))

print("\nSector-wise Exposure")
for sector, value in sector_exposure.items():
    print(sector, ": ₹", value)

portfolio.sort(key=lambda x: x["Return"], reverse=True)

print("\nInvestor Ranking by Portfolio Return")
rank = 1
for stock in portfolio:
    print(rank, ".", stock["Investor ID"],
          "-", stock["Stock Symbol"],
          "- {:.2f}%".format(stock["Return"]))
    rank += 1

# Generate Report

with open("portfolio_report.txt", "w") as file:

    file.write("SMART STOCK PORTFOLIO REPORT\n\n")

    for stock in portfolio:
        file.write(
            f"Investor ID : {stock['Investor ID']}\n"
            f"Stock : {stock['Stock Symbol']}\n"
            f"Investment : ₹{stock['Investment']}\n"
            f"Current Value : ₹{stock['Current Value']}\n"
            f"Profit/Loss : ₹{stock['Profit']}\n"
            f"Return : {stock['Return']:.2f}%\n"
            "---------------------------------\n"
        )

print("\nPortfolio Report Generated Successfully.")

print("\nReading Portfolio Report...\n")

with open("portfolio_report.txt", "r") as file:
    print(file.read())
