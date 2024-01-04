import requests 

target_ip = input("Enter a target IP address: ")

response = requests.get(f"https://geolocation-db.com/json/{target_ip}").json() 

print(f'''The address for the IP address {response["IPv4"]} is the following:
Country: {response["country_name"]}
City: {response["city"]}
Postcode: {response["postal"]}
Latitude: {response["latitude"]}
Longitude: {response["longitude"]}
''')


