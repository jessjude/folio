import requests

# Step 1: send the request
response = requests.get("https://zenquotes.io/api/random", timeout=10)

# Step 2: raise an error if the server failed (4xx/5xx status)
response.raise_for_status()

# Step 3: parse the JSON body into Python data
data = response.json()

# This is the line that handles printing the output!
print(data[0]["q"])  # the quote text
