import requests

EUR = 'EUR'
HUF = 'HUF'
MXN = 'MXN'
USD = 'USD'
base = 1 

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={base}&from={EUR}&to{HUF}")

print("Show my interest currency conversion")
print("Euro to Hungarian Forin")
print(f"{base} {EUR} is {response.json()['rates'][HUF]} {HUF}")

print("Euro to Mexican peso")
print(f"{base} {EUR} is {response.json()['rates'][MXN]} {MXN}")

print("Euro to Dollar")
print(f"{base} {EUR} is {response.json()['rates'][USD]} {USD}")

question=input("Do you want another conversion (Y/N): ")
s
if question=="Y":
    from_currency = str(
        input("Enter the name of the currency (3 letters) you'd like to convert from:")).upper()

    to_currency = str(
        input("Enter int he currency (3 letters) you'd like to convert to ")).upper()

    amount = float(input("Enter inthe amount of money: "))

    response = requests.get(
        f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to{to_currency}")

    #print(response.status_code) #Return integer values

    print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
else:
    print("Thank you to use our servers :)")

