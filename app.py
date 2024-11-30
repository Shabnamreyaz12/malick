import re

# Currency conversion rates
PKR_TO_USD_RATE = 0.0036  # Example rate (1 PKR = 0.0036 USD)
USD_TO_PKR_RATE = 280.0   # Example rate (1 USD = 280 PKR)

def get_numeric_input(prompt):
    """Extract numeric input from a string."""
    while True:
        user_input = input(prompt)
        # Use regex to extract numbers from the input
        match = re.search(r'\d+(\.\d+)?', user_input)
        if match:
            return float(match.group())  # Convert the matched number to float
        else:
            print("Invalid input. Please enter a numeric value.")

def convert_currency():
    print("Currency Converter")
    print("1. Convert PKR to USD")
    print("2. Convert USD to PKR")
    
    choice = int(input("Choose an option (1 or 2): "))
    
    if choice == 1:
        # Convert PKR to USD
        amount_pkr = get_numeric_input("Enter amount in PKR: ")
        amount_usd = amount_pkr * PKR_TO_USD_RATE
        print(f"{amount_pkr} PKR = {amount_usd:.2f} USD")
    
    elif choice == 2:
        # Convert USD to PKR
        amount_usd = get_numeric_input("Enter amount in USD: ")
        amount_pkr = amount_usd * USD_TO_PKR_RATE
        print(f"{amount_usd} USD = {amount_pkr:.2f} PKR")
    
    else:
        print("Invalid option. Please choose 1 or 2.")

# Run the currency converter
convert_currency()
