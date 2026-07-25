import json

def display_header():
    print("""
Project: Agroweather
Version: 0.1
Author: Ignacio Roca Bravo

Weather data analysis for agricultural decision support.
"""
    )

def load_weather_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def display_weather(data):
    print(f"Location: {data['location']}")
    print(f"Temperature: {data['temperature']} ºC")
    print(f"Humidity: {data['humidity']} %")
    print(f"Wind Speed: {data['wind_speed']} km/h")
    print(f"Rainfall: {data['rainfall']} mm")

def generate_alerts(data):
    alerts = []

    if data['temperature'] < 3 :
        alerts.append("Frost risk")

    if data["wind_speed"] > 15 :
        alerts.append("Unfavorable conditions for spraying")

    if data["rainfall"] > 10 :
        alerts.append("Review or postpone irrigation")

    if data['humidity'] > 80 :
        alerts.append("High humidity: possible fungal disease risk")

    return alerts

def display_summary(alerts):
    print("------------------")
    print("Summary")
    for item in alerts:
        print(f"- {item}")

def display_footer():
    print("""
---------------------
End of Report
---------------------
    """)

def main():
    weather_data = load_weather_data("data/weather_data.json")

    display_header()
    display_weather(weather_data)

    alerts = generate_alerts(weather_data)

    display_summary(alerts)
    display_footer()
    

main()