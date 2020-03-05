# initialize the values
countries={"US":"United States",
           "MX":"Mexico",
           "CN":"Canada"}

movies = {"name": "Lord of the Rings", "year": "2000", "rating": "PG-13"}
# read the values
print("Countries", countries)
print("US: ", countries["US"])  #print value

# retrieving countries using IF ELSE, subscripts vs get method
code = "IE"
#print(countries[code])
print("country IE:", countries.get(code))
print("country IE:", countries.get(code, "Unknown"))

if code in countries:
    country = countries.get(code)
    print("country if", country)
else:
    print("there is no such country")

country = countries.get("GB")
print("country", country)

#using for loops to iterate through the countries
#keys, values and items() methods
# #key + value pairs
for key in countries:
    print( "Key:", key)

for key in countries:  # print value using keys
    print( "Value:", countries[key])

for name in countries.values(): #print values
    print("Country name:", name)

for key in countries: #print key value pair
    print("Key/Value:", key, countries[key])

for key, value in countries.items():
    print("Key/Value pair: ", key, ": ", value)

for code, name in countries.items():
    print("Key/Value pair: ", code, ": ", name)
    print("Key/Value pair 2nd: ", code, name)

# add new values
countries["GB"] = "Great Britain"
print(countries)
countries["BZ"] = "Brazil"
print("Brazil added:", countries)

# delete countries
country = countries.pop("BZ")
print("popped country deleted:", country)
print("deleted country:", countries.pop("AB", "None"))

#converting dictionary to lists
codes = list(countries.values())
codes.sort()
print("country values:",codes)

codeskeys = list(countries.keys())
codeskeys.sort()
print("country keys", codeskeys)
for code in codeskeys: #combined a list and a dictionary
    print(code + "   " + countries[code])