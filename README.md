# AP7-coding-assignment

### Prerequisites:
* Python 3.x
* No external dependencies

### Execution
* Run 'main.py'


## Code Structure
* 'portfolioTracking.py': Contains the PortfolioTracker class. This class is responsbile for the portfolio logic.
* 'main.py': The CLI that handles user input

## Key Assumption and Design Choices
1. I used standard Python data structures such as dictionaries and lists as my in-memory storage. Dictionaries were used for instruments and portfolios since I could use instrument_name and portfolio_name as unique identifiers. Lists were used to save the trade records which was nice since the items are then also already stored sequentially.

2. I interperated the currency field for portfolios to act like the balance of the profolios. This allowed me to implement logic concerning if portfolio had sufficient fund to make a specific buy trade for example.

3. PnL is calculated to take into account unrealized positions. E.g. if a portfolio in holding 10 units of a stock, it is considered at the moment of calculation to be equal to last_known_price * quantity.

4. As for the trade filtering in list_trades(), I delibertely only made it possible to filter by either instrument, portfolio or none.

## Trade-offs and Prioritization
Priority was put into the logic and meeting the basic functionality first. When that was done I kept implementing new features with the time I had. E.g. I added a more sophisticated PnL calculation, error handling and input validation.

## Given more time, I would...
* Implement data persistence and better storage. For example I could use an external SQL-based database for storage and to keep persistence of data.
* Add unit testing as mentioned in the problem description to make testing the individual functions and modules much easier.
* Better validation if trades are valid or not. E.g enough quantity currently being held of an instrument to sell or if it is valid to sell at the current time.
* Better CLI or GUI. Right now it is not very user friendly at all. E.g. if a user does an incorrect input they will be thrown back to the initial menu instead of just repeating that input.
* More advanced input sanitization, for example by adding canse-insensivity to protfolio and instrument names.