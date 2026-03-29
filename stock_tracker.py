print("📊 Stock Portfolio Tracker")
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 300
}
portfolio ={}
total_value = 0
while True:
    stock = input("\nEnter stock symbol (or 'done'): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("⚠️Stock not found. Available stocks:", ", ".join(stock_prices.keys()))
        continue
    while True:
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            break
        except ValueError:
            print("⚠️ Please enter a valid number.")
    portfolio[stock] = portfolio.get(stock, 0) + quantity
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock} -> {qty} shares -× ${price} = ${value}")
print(f"\nTotal Investment: ${total_value}")
save = input("Save to file? (yes/no): ")
if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("--------------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock} -> {qty}  × ${price} = ${value}\n")
        file.write(f"\nTotal = ${total_value}")
    print("✅ Portfolio saved to 'portfolio.txt'")
else:
    print("👍 Data not saved.")