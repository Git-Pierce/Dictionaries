def display_menu():
    print("Country Menu")
    print("V - View country name")
    print("A - Add a country")
    print("D - Delete country")
    print("X - Exit program")
    print()

def view(countries):
    code = input("Enter country code:").upper()
    if code in countries:
        print("Country name: ", countries.get(code, "None"))
    else:
        print("Code", code, "not found. No country found for this code")

def display_code(countries):
    codes = list(countries.keys())
    line = "Country codes:"
    for code in codes:
        line += code + " "
    print(line)

def main():
    countries = {"CA": "Canada", "US": "USA", "MX":"Mexico"}
    display_menu()
    display_code(countries)
    view(countries)

main()
