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