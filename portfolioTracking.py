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
            "timestamp": datetime.now(), 
            "direction": direction
            }
        
        self.trades.append(trade)
    
    # List all trades
    def list_trades(self): # Add filter by portfolio or instrusment
        return self.trades
    

    """Note to self: to add more sophisticated pnl calculation.
    for now only calculates total pnl for a portfolio based on recorded trades, not
    taking into account current positions etc"""
    # Calculate pnl for a portfolio based on recorded trades
    def calculate_pnl(self, portfolio_name):
        pnl = 0
        if portfolio_name not in self.portfolios:
            raise ValueError(f"Portfolio: {portfolio_name} does not exist")
        
        for trade in self.trades:
            if trade["portfolio_name"] == portfolio_name:
                if trade["direction"] == "buy":
                    pnl -= trade["quantity"] * trade["price"]
                elif trade["direction"] == "sell":
                    pnl += trade["quantity"] * trade["price"]
        return pnl