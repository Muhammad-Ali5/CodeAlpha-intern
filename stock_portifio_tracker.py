import yfinance as yf
import datetime

class StockPortfolio:
    def __init__(self):
        # Dictionary to store portfolio: ticker -> {quantity, purchase_price, purchase_date}
        self.portfolio = {}

    def add_stock(self, ticker, quantity, purchase_price, purchase_date=None):
        """Add a stock to the portfolio."""
        ticker = ticker.upper()
        if purchase_date is None:
            purchase_date = datetime.date.today().isoformat()
        
        if ticker in self.portfolio:
            # Update existing stock
            current = self.portfolio[ticker]
            total_quantity = current['quantity'] + quantity
            total_cost = (current['quantity'] * current['purchase_price']) + (quantity * purchase_price)
            new_purchase_price = total_cost / total_quantity
            self.portfolio[ticker] = {
                'quantity': total_quantity,
                'purchase_price': new_purchase_price,
                'purchase_date': current['purchase_date']  # Keep original purchase date
            }
        else:
            # Add new stock
            self.portfolio[ticker] = {
                'quantity': quantity,
                'purchase_price': purchase_price,
                'purchase_date': purchase_date
            }
        print(f"Added {quantity} shares of {ticker} at ${purchase_price:.2f} per share.")

    def remove_stock(self, ticker, quantity=None):
        """Remove a stock or a portion of it from the portfolio."""
        ticker = ticker.upper()
        if ticker not in self.portfolio:
            print(f"{ticker} not found in portfolio.")
            return
        
        if quantity is None or quantity >= self.portfolio[ticker]['quantity']:
            del self.portfolio[ticker]
            print(f"Removed all shares of {ticker} from portfolio.")
        else:
            self.portfolio[ticker]['quantity'] -= quantity
            print(f"Removed {quantity} shares of {ticker}. Remaining: {self.portfolio[ticker]['quantity']}.")
            if self.portfolio[ticker]['quantity'] == 0:
                del self.portfolio[ticker]
                print(f"No shares of {ticker} remain; removed from portfolio.")

    def get_stock_price(self, ticker):
        """Fetch current stock price using yfinance."""
        try:
            stock = yf.Ticker(ticker)
            price = stock.history(period="1d")['Close'].iloc[-1]
            return price
        except Exception as e:
            print(f"Error fetching price for {ticker}: {e}")
            return None

    def track_performance(self):
        """Display portfolio performance with real-time data."""
        if not self.portfolio:
            print("Portfolio is empty.")
            return
        
        total_invested = 0
        total_value = 0
        
        print("\nPortfolio Performance:")
        print(f"{'Ticker':<10} {'Qty':<8} {'Purchase':<12} {'Current':<12} {'Value':<12} {'Gain/Loss':<12}")
        print("-" * 66)
        
        for ticker, data in self.portfolio.items():
            current_price = self.get_stock_price(ticker)
            if current_price is None:
                continue
            
            invested = data['quantity'] * data['purchase_price']
            value = data['quantity'] * current_price
            gain_loss = value - invested
            
            total_invested += invested
            total_value += value
            
            print(f"{ticker:<10} {data['quantity']:<8} ${data['purchase_price']:<11.2f} ${current_price:<11.2f} ${value:<11.2f} ${gain_loss:<11.2f}")
        
        print("-" * 66)
        print(f"{'Total':<10} {'':<8} {'':<12} {'':<12} ${total_value:<11.2f} ${total_value - total_invested:<11.2f}")
        print(f"Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    portfolio = StockPortfolio()
    
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Track performance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            ticker = input("Enter stock ticker (e.g., AAPL): ")
            quantity = float(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price per share: "))
            portfolio.add_stock(ticker, quantity, purchase_price)
        
        elif choice == '2':
            ticker = input("Enter stock ticker to remove: ")
            quantity_input = input("Enter quantity to remove (or press Enter for all): ")
            quantity = float(quantity_input) if quantity_input else None
            portfolio.remove_stock(ticker, quantity)
        
        elif choice == '3':
            portfolio.track_performance()
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()