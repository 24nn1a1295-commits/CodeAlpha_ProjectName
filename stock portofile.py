# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

# Number of stocks
n = int(input("Enter the number of stocks: "))

# User input
for i in range(n):
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not available in the price list.")

# Calculate total investment
print("\nPortfolio Summary")
print("-" * 30)

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

print("-" * 30)
print("Total Investment Value = $", total_investment)

# Save to a text file
with open("portfolio.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-" * 30 + "\n")

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}\n")

    file.write("-" * 30 + "\n")
    file.write(f"Total Investment Value = ${total_investment}")

print("Portfolio saved to portfolio.txt")
