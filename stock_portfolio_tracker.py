PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "MSFT": 310.0,
    "AMZN": 190.0,
    "GOOG": 150.0,
}


def get_portfolio():
    portfolio = {}

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").strip().upper()
        if stock == "DONE":
            break

        if stock not in PRICES:
            print(f"Stock '{stock}' is not in the price list.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    return portfolio


def calculate_total(portfolio):
    total = 0.0
    for stock, quantity in portfolio.items():
        total += PRICES[stock] * quantity
    return total


def save_report(portfolio, total):
    format_choice = input("Save report as txt or csv? (txt/csv): ").strip().lower()

    if format_choice == "txt":
        file_name = "portfolio_report.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("Stock Portfolio Report\n")
            file.write("=====================\n")
            for stock, quantity in portfolio.items():
                file.write(f"{stock}: {quantity} shares @ ${PRICES[stock]:.2f} each\n")
            file.write(f"\nTotal investment: ${total:.2f}\n")
        print(f"Report saved to {file_name}.")

    elif format_choice == "csv":
        file_name = "portfolio_report.csv"
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            file.write("stock,quantity,price_per_share,total\n")
            for stock, quantity in portfolio.items():
                stock_total = PRICES[stock] * quantity
                file.write(f"{stock},{quantity},{PRICES[stock]:.2f},{stock_total:.2f}\n")
            file.write(f"TOTAL,,,{total:.2f}\n")
        print(f"Report saved to {file_name}.")

    else:
        print("Invalid choice. Report not saved.")


def main():
    print("Welcome to the Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(PRICES.keys()))

    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Nothing to calculate.")
        return

    total = calculate_total(portfolio)
    print("\nPortfolio summary:")
    for stock, quantity in portfolio.items():
        print(f"- {stock}: {quantity} shares")
    print(f"\nTotal investment value: ${total:.2f}")

    save_choice = input("Do you want to save this result? (y/n): ").strip().lower()
    if save_choice == "y":
        save_report(portfolio, total)


if __name__ == "__main__":
    main()
