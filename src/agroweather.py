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

def validate_weather_data(data):
    required_fields = [
        "location",
        "temperature",
        "humidity",
        "wind_speed",
        "rainfall"
    ]

    for field in required_fields:
        if field not in data:
            print(f"Missing required field: {field}")
            return False

    if not isinstance(data["location"], str):
        print("Invalid location")
        return False

    if not data["location"].strip():
        print("Location cannot be empty")
        return False

    if not isinstance(data["temperature"], (int, float)):
        print("Invalid temperature")
        return False

    if not -20 <= data["temperature"] <= 60:
        print("Temperature out of range")
        return False

    if not isinstance(data["humidity"], (int, float)):
        print("Invalid humidity")
        return False

    if not 0 <= data["humidity"] <= 100:
        print("Humidity out of range")
        return False

    if not isinstance(data["wind_speed"], (int, float)):
        print("Invalid wind speed")
        return False

    if not 0 <= data["wind_speed"] <= 100:
        print("Wind speed out of range")
        return False

    if not isinstance(data["rainfall"], (int, float)):
        print("Invalid rainfall")
        return False

    if data["rainfall"] < 0:
        print("Rainfall out of range")
        return False

    return True

def display_weather(data):
    print(f"Location: {data['location']}")
    print(f"Temperature: {data['temperature']} ºC")
    print(f"Humidity: {data['humidity']} %")
    print(f"Wind Speed: {data['wind_speed']} km/h")
    print(f"Rainfall: {data['rainfall']} mm")

def generate_alerts(data):
    alerts = []

    if data['temperature'] < 3:
        alerts.append("Frost risk")

    if data["wind_speed"] > 15:
        alerts.append("Unfavorable conditions for spraying")

    if data["rainfall"] > 10:
        alerts.append("Review or postpone irrigation")

    if data['humidity'] > 80:
        alerts.append("High humidity: possible fungal disease risk")

    return alerts

def display_summary(alerts):
    print("------------------")
    print("Summary")

    if alerts:
        for item in alerts:
            print(f"- {item}")

    else:
        print("- No agricultural alerts")

def display_footer():
    print("""
---------------------
End of Report
---------------------
    """)

def main():
    weather_data = load_weather_data("data/weather_data.json")
    
    is_valid = validate_weather_data(weather_data)

    if not is_valid:
        print("Weather data validation failed.")
        return

    display_header()
    display_weather(weather_data)

    alerts = generate_alerts(weather_data)

    display_summary(alerts)
    display_footer()
    

main()