import os
import requests

# Get the API key and address from environment variables
api_key = os.environ.get("ETHERSCAN_API_KEY")
ethereum_address = os.environ.get("ETHEREUM_ADDRESS")

if api_key is None or ethereum_address is None:
    raise ValueError("Please set ETHERSCAN_API_KEY and ETHEREUM_ADDRESS environment variables.")

# Define the base URL for the Etherscan API
base_url = "https://api.etherscan.io/api"

# Define the query parameters
params = {
    'module': 'account',
    'action': 'tokentx',
    'contractaddress': '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2',
    'address': ethereum_address,
    'page': 1,
    'offset': 20,
    'startblock': 0,
    'endblock': 27025780,
    'sort': 'desc',
    'apikey': api_key
}

# Send a GET request to the Etherscan API
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Process the response data here
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
