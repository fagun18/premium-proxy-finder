import requests
from bs4 import BeautifulSoup
import json

# Make a request to the website
response = requests.get("https://www.example.com/proxy-list")

# Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the proxy server information
table = soup.find('table')

# Create an empty list to store the proxy server information
proxy_list = []

# Iterate through the rows of the table
for row in table.find_all('tr'):
    # Find the cells in the row
    cells = row.find_all('td')
    if cells:
        # Extract the proxy server information from the cells
        ip_address = cells[0].text
        port = cells[1].text
        protocol = cells[2].text
        anonymity = cells[3].text
        location = cells[4].text
        
        # Append the proxy server information to the list
        proxy_list.append({
            'ip_address': ip_address,
            'port': port,
            'protocol': protocol,
            'anonymity': anonymity,
            'location': location
        })

# Write the proxy server information to a JSON file
with open('proxy_list.json', 'w') as outfile:
    json.dump(proxy_list, outfile)
