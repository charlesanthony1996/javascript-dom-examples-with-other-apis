import requests

# Update the URL with additional required parameters like location
url = "https://api.yelp.com/v3/businesses/search?location=NewYork&sort_by=best_match&limit=20"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer HupqS1suMvvTiIKD3P52WCLQyRJUOEwOhGIghMaUoOejbYSyCREATi1Fgi1fw13j_I_Rbs4AOukCU14ZUZQPQFjwaX6wrt-zVhZ84slCpHIq9knmib4nkNTG7MGVZXYx"  # Replace YOUR_API_KEY with your actual API key
}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
except Exception as e:
    print("An error occurred:", e)



# HupqS1suMvvTiIKD3P52WCLQyRJUOEwOhGIghMaUoOejbYSyCREATi1Fgi1fw13j_I_Rbs4AOukCU14ZUZQPQFjwaX6wrt-zVhZ84slCpHIq9knmib4nkNTG7MGVZXYx