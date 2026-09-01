from portfolioTracking import PortfolioTracker

"""
CLI for Portfolio Tracker
"""

def main():
    tracker = PortfolioTracker()

    while True:
        # List of options for the user to choose from
        print("Choose an option:")
        print("1: Create portfolio")
        print("2: List portfolios")
        print("3: Create instrument")
        print("4: List instruments")
        print("5: Record trade")
        print("6: List trades") # Note to self: Add filter by portfolio or instrument
        print("7. Calculate P&L for a portfolio")
        print("8: Exit")
        
        # User input from options
        choice = input("Enter an option (1-8): ").strip()

        try:
                
            # If create portforlio: Ask for protfolio name and currency
            if choice == "1":
                portfolio_name = input("Enter portfolio name: ").strip()
                
                currency = input("Enter currency: ").strip()
                try:    # Check if currency is a number
                    currency = float(currency)
                except ValueError:
                    print("Currency must be a number")
                    continue

                tracker.create_portfolio(portfolio_name, currency)
                print(f"Portfolio {portfolio_name} created with currency {currency}.")
            
            # If list portfolios: List all portfolios
            elif choice == "2":
                portfolios = tracker.list_portfolios()

                if not portfolios:
                    print("No portfolios found")
                else:
                    print("Portfolios: (Name: Currency)")
                    for name, currency in portfolios.items():
                        print(f"{name}: {currency}")
            
            # If create instrument: Ask for instrument name and type
            elif choice == "3":
                instrument_name = input("Enter instrument name: ").strip()
                instrument_type = input("Enter instrument type: ").strip()
                tracker.create_instrument(instrument_name, instrument_type)
                print(f"Instrument {instrument_name} created with type {instrument_type}.")
            
            # If list instruments: List all instruments
            elif choice == "4":
                instruments = tracker.list_instruments()

                if not instruments:
                    print("No instruments found")
                else:
                    print("Instruments:")
                    for name, instrument_type in instruments.items():
                        print(f"{name}: {instrument_type}")
            
            # If record trade: Ask for instrument, portfolio, quantity, price, direction (buy/sell)
            elif choice == "5":
                instrument_name = input("Enter instrument name: ").strip()
                portfolio_name = input("Enter portfolio name: ").strip()
                
                quantity = input("Enter quantity: ").strip()
                try:
                    quantity = float(quantity)
                except ValueError:
                    print("Quantity must be a number")
                    continue
                if quantity <= 0:
                    print("Quantity must be greater than 0")
                    continue
                
                price = input("Enter price: ").strip()
                try:
                    price = float(price)
                except ValueError:
                    print("Price must be a number")
                    continue
                if price <= 0:
                    print("Price must be greater than 0")
                    continue
                
                direction = input("Enter direction (buy/sell): ").strip()

                tracker.record_trade(instrument_name, portfolio_name, quantity, price, direction)
                print(f"Trade recorded: {direction} {quantity} of {instrument_name} at price {price} in portfolio {portfolio_name}.")

            # If list trades: List all trades
            elif choice == "6":
                trades = tracker.list_trades()

                if not trades:
                    print("No trades found")
                else:
                    print("Trades:")
                    for trade in trades:
                        print(trade)
            
            # If calculate P&L: Ask for portfolio name and calculate P&L for that portfolio
            elif choice == "7":
                portfolio_name = input("Enter portfolio name: ").strip()
                pnl = tracker.calculate_pnl(portfolio_name)
                print(f"PnL for portfolio {portfolio_name}: {pnl}")

            # If exit: Exit the CLI
            elif choice == "8":
                print("Exiting")
                break

            else:
                print("Invalid option. Please try again")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()