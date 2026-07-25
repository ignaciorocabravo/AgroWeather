def display_header():
    print("""
Project: Agroweather
Version: 0.1
Author: Ignacio Roca Bravo

Weather data analysis for agricultural decision support.
"""
    )

weather_data = {
    "location" : "Barcelona",
    "temperature" : 7.5, 
    "humidity" : 81,
    "wind_speed" : 18.0,
    "rainfall" : 4.2
}

def display_weather(data):
    print(f"Location: {data['location']}")

def generate_alerts(data):
    print("--------------------")
    print("Alerts")
    if data['temperature'] < 3 :
        print("Warning: Frost risk")
    if data["wind_speed"] > 15 :
        print("Unfavorable conditions for spraying")
    if data["rainfall"] > 10 :
        print("Review or postpone irrigation")
    if data['humidity'] > 80 :
        print("High humidity: possible fungal disease risk")

def display_footer():
    print("""
---------------------
End of Report
---------------------
    """)

def main():
    display_header()
    display_weather(weather_data)
    generate_alerts(weather_data)
    display_footer()

main()