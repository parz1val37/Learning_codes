import requests

def get_exchange_rates(base, targets):
    url = f"https://api.frankfurter.app/latest?from={base}&to={','.join(targets)}"
    response = requests.get(url)
    data = response.json()
    return data.get("rates", {})

# List of supported currencies
currencies = ["INR", "USD", "GBP", "EUR", "SAR"]

print("Available currencies:", ", ".join(currencies))
base_currency = input("Choose base currency (e.g., USD): ").upper()

if base_currency not in currencies:
    print("Invalid currency! Please choose from the list.")
else:
    try:
        amount = float(input(f"Enter amount in {base_currency}: "))
    except ValueError:
        print("Invalid amount entered!")
        exit()

    targets = [c for c in currencies if c != base_currency]
    rates = get_exchange_rates(base_currency, targets)

    print(f"\nExchange Rates for {amount} {base_currency}:\n")
    for target, rate in rates.items():
        converted = amount * rate
        print(f"{amount} {base_currency} = {converted:.2f} {target}")