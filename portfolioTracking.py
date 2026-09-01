from datetime import datetime

""""
This class is a simple portfolio tracker.
Functionality:
* Create portfolios with a name and currency
* Create instruments with a name and type
* Record trades with instrument, portfolio, quantity, price, timestamp and direction (buy/sell)
* Calculate PnL for a portfolio based on recorded trades
"""
class PortfolioTracker:
    # Initialize tracker with empy dictionaries for portfolios and instruments and an empty list for trades
    def __init__(self):
        self.portfolios = {}
        self.instruments = {}
        self.trades = []

    # Create a portfolio with a name and currency
    def create_portfolio(self, portfolio_name, currency):
        if portfolio_name in self.portfolios:
            raise ValueError(f"Portfolio with name {portfolio_name} already exists")
        else:
            self.portfolios[portfolio_name] = currency
    
    # List all portfolios
    def list_portfolios(self):
        return self.portfolios
    
    # Create an instrument with a name and type
    def create_instrument(self, instrument_name, instrument_type):
        if instrument_name in self.instruments:
            raise ValueError(f"Instrument with name {instrument_name} already exists")
        else:
            self.instruments[instrument_name] = instrument_type
    
    # List all instruments
    def list_instruments(self):
        return self.instruments
    
    # Record a trade with instrument, portfolio, quantity, price, timestamp and direction (buy/sell)
    def record_trade(self, instrument_name, portfolio_name, quantity, price, direction):
        # Catch errors
        if instrument_name not in self.instruments:
            raise ValueError(f"Instrument: {instrument_name} does not exist")
        if portfolio_name not in self.portfolios:
            raise ValueError(f"Portfolio: {portfolio_name} does not exist")
        if direction not in ["buy", "sell"]:
            raise ValueError("Direction must be 'buy' or 'sell'")
        if direction == "buy" and price * quantity > self.portfolios[portfolio_name]:
            raise ValueError(f"Not enough funds in portfolio {portfolio_name}. Current balance: {self.portfolios[portfolio_name]}, required: {price * quantity}")
        
        # Update portfolio balance based on trade
        if direction == "buy":
            self.portfolios[portfolio_name] -= price * quantity
        elif direction == "sell":
            self.portfolios[portfolio_name] += price * quantity

        # Create a trade dictionary and append it to the trades list
        trade = {
            "portfolio_name": portfolio_name, 
            "instrument_name": instrument_name, 
            "quantity": quantity, 
            "price": price, 
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
            "direction": direction
            }
        
        self.trades.append(trade)
    
    # List all trades
    def list_trades(self, portfolio_name = None, instrument_name = None):
        relevant_trades = []

        if portfolio_name:  # Filter trades by portfolio name
            if portfolio_name not in self.portfolios:
                raise ValueError(f"Portfolio: {portfolio_name} does not exist")
            for trade in self.trades:   
                if trade["portfolio_name"] == portfolio_name:
                    relevant_trades.append(trade)

        if instrument_name:  # Filter trades by instrument name
            if instrument_name not in self.instruments:
                raise ValueError(f"Instrument: {instrument_name} does not exist")
            for trade in self.trades:
                if trade["instrument_name"] == instrument_name:
                    relevant_trades.append(trade)

        if not instrument_name and not portfolio_name:  # If no filters, return all trades
            relevant_trades = self.trades

        return relevant_trades
    

    """
    PnL calculation assumptions:
    1. Current price of each instrument is the price of the last trade recorded for that instrument.
    2. When buy trades are recorded, PnL is reduced by the total cost of the trade (quantity * price).
    3. When sell trades are recorded, PnL is increased by the total revenue of the trade (quantity * price).
    4. For unrealized positions, PnL is adjusted based on the current price of the instrument and the quantity held.
    """
    # Calculate pnl for a portfolio based on recorded trades
    def calculate_pnl(self, portfolio_name):
        
        if portfolio_name not in self.portfolios:
            raise ValueError(f"Portfolio: {portfolio_name} does not exist")
        
        # Create pnl, positions and latest_prices dictionaries
        pnl = 0
        positions = {}
        latest_prices = {}

        # Loop throguh all trades and calculate pnl based on the assumptions above
        for trade in self.trades:
            latest_prices[trade["instrument_name"]] = trade["price"]

            if trade["portfolio_name"] == portfolio_name:

                # Decrease pnl for buy trades and increase pnl for sell trades and also update positions
                if trade["direction"] == "buy":
                    pnl -= trade["quantity"] * trade["price"]
                    positions[trade["instrument_name"]] = positions.get(trade["instrument_name"], 0) + trade["quantity"]
                elif trade["direction"] == "sell":
                    pnl += trade["quantity"] * trade["price"]
                    positions[trade["instrument_name"]] = positions.get(trade["instrument_name"], 0) - trade["quantity"]
        
        # Calculate unrealized PnL based on current positions and latest prices
        for instrument, quantity in positions.items():
            pnl += quantity * latest_prices[instrument]

        return pnl