import requests

#  1a A simple api query
root_url = "https://country-leaders.onrender.com"

status_url = f"{root_url}/status"

req = requests.get(status_url)

if req.status_code == 200:
    print(req.text)
else:
    print(f"Error: Status code {req.status_code}")


#  1b Dealing with JSON
countries_url = "https://country-leaders.onrender.com/countries"

req = requests.get(countries_url)

countries = req.json()

print(req.status_code, countries)


# 1c Cookies anyone
cookie_url = "https://country-leaders.onrender.com/cookie"

req = requests.get(cookie_url)
cookies = req.cookies
print(cookies)
