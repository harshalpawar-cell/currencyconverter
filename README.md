Currency Converter


## Overview
This project is a simple Python-based currency converter that allows users to convert an amount from one currency to another using predefined exchange rates. The program uses NumPy for efficient array handling and matrix-based conversion.


## Features
- Predefined list of supported currencies (USD, INR, EUR, GBP)
- Exchange rate matrix for fast lookups
- User input for selecting source and target currencies
- Calculates and displays converted currency amount
- Easy-to-understand console-based interface


## Technologies / Tools Used
- Python 3
- NumPy (for matrix operations)
- Console/Terminal for input/output


## Installation & Setup
1. Ensure Python 3 is installed on your system.
2. Install NumPy using the command:
   bash
   pip install numpy
3. Download or clone the repository:
   bash
   git clone <your-repository-link>
4. Navigate to the project folder:
   bash
   cd currency-converter
   

## How to Run
Run the Python script using:
bash
python currency_converter.py


## Instructions for Testing
- When prompted, enter the currency number to convert *from* (0–3).
- Enter the currency number to convert *to* (0–3).
- Enter the amount you want to convert.
- Verify if the output matches manual calculations using the predefined rates.


## Example Output 
Available currencies:
0: USD
1: INR
2: EUR
3: GBP
Enter no. for currency to convert: 0
Enter no. for currency to convert: 1
Enter amount in USD: 5
5 USD is equal to 416.0 INR


## Project Code:
import numpy as np
currency=['USD', 'INR', 'EUR', 'GBP']
rate=np.array([
    [1, 83.2, 0.92, 0.79],
    [0.012, 1, 0.011, 0.0095],
    [1.09, 90.3, 1, 0.86],
    [1.27, 105.1, 1.16, 1]])
print("Available currencies:")
for i in range(len(currency)):
    print(str(i) + ": " + currency[i])
n=int(input("Enter no. for currency to convert: "))
m=int(input("Enter no. for currency to convert: "))
amount=float(input("Enter amount in " + currency[n] + ": "))
k=amount*rate[n][m]
print(amount, currency[n], "is equal to", k, currency[m])
