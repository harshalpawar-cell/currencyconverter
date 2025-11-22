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

















# print("Available currencies:","\n","1: USD","\n","2: INR","\n","3: EUR")
# h=int(input("Enter the no. of currency:"))
# m=int(input("Enter the no. of currency:"))
# p=int(input("Enter amount:"))
# if h==1 and m==2:
#     print(p,"USD is equal to",p*87,"INR")
# elif h==1 and m==3:
#     print(p,"USD is equal to",p*0.87,"EUR")
# elif h==2 and m==3:
#     print(p,"INR is equal to",p*0.0097,"EUR")
# elif h==3 and m==1:
#     print(p,"EUR is equal to",p*1.15,"USD")
# elif h==3 and m==2:
#     print(p,"EUR is equal to",p*102.97,"INR")
# elif h==2 and m==1:
#     print(p,"INR is equal to",p*0.011,"USD")
# else: print("None")
