import requests

# Step 1: send the request
response = requests.get("https://zenquotes.io/api/random", timeout=10)

# Step 2: raise an error if the server failed (4xx/5xx status)
response.raise_for_status()

# Step 3: parse the JSON body into Python data
data = response.json()

# This is the line that handles printing the output!
print(data[0]["q"])  # the quote text
# Purpose: Daily Summary Bot
# Fetches: weather (wttr.in) & a quote (zenquotes.io)
# Runs:    every day at 8 AM IST via GitHub Actions

import requests
from datetime import date
def get_weather(city="Thiruvananthapuram"):
    """Fetch today's weather as a one-line text summary."""
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip() # remove trailing newline
    except Exception as e:
        return f"Weather unavailable ({e})"
def get_quote():
    """Fetch a random motivational quote from zenquotes."""
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()       # JSON -> Python list
        quote = data[0]["q"]
        author = data[0]["a"]
        return f'"{quote}" — {author}'
    except Exception as e:
        return f"Quote unavailable ({e})"
def build_summary():
    """Assemble the full daily summary from all data sources."""
    today = date.today().strftime("%A, %d %B %Y")
    weather = get_weather()
    quote = get_quote()
    
    summary = f"""---------------------------------
PULSE - Daily Summary
{today}
---------------------------------

WEATHER
{weather}

TODAY'S QUOTE
{quote}

---------------------------------"""
    return summary  
def run():
    """Main entry point, called by GitHub Actions."""
    summary = build_summary()
    print(summary)
    
    # Save a copy to a local file
    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
        print("Pulse ran successfully.")

if __name__ == "__main__":
    run()
# Create the summary string
summary_data = """
PULSE - Daily Summary
Friday, 12 June 2026

WEATHER
Thiruvananthapuram: 86°F

TODAY'S QUOTE
"Against the assault of laughter nothing can stand." - Mark Twain
"""

# Open a file in write mode and save it
with open("daily_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary_data)

print("Pulse ran successfully and file saved.")