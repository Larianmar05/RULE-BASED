def evaluate_humidity(humidity):
    if humidity > 80:
        return "High humidity"
    elif humidity < 40:
        return "Low humidity"
    else:
        return "Moderate humidity"

def evaluate_cloudiness(cloudiness):
    if cloudiness > 70:
        return "Very cloudy"
    elif cloudiness < 30:
        return "Mostly clear"
    else:
        return "Partly cloudy"

def evaluate_temperature(temperature):
    if temperature > 30:
        return "Hot temperature"
    elif temperature < 15:
        return "Cool temperature"
    else:
        return "Moderate temperature"

def should_bring_umbrella(humidity, cloudiness):
    if humidity > 80 and cloudiness > 70:
        return "Rainy conditions. Bring an umbrella!"
    elif cloudiness > 50:
        return "Cloudy skies. Umbrella optional, just in case."
    else:
        return "No umbrella needed."

def main():
    print("Rule-Based Weather Evaluator")

    try:
        humidity = float(input("Enter humidity (%)     : "))
        cloudiness = float(input("Enter cloudiness (%)  : "))
        temperature = float(input("Enter temperature (°C): "))

        humidity_result = evaluate_humidity(humidity)
        cloudiness_result = evaluate_cloudiness(cloudiness)
        temperature_result = evaluate_temperature(temperature)
        umbrella_advice = should_bring_umbrella(humidity, cloudiness)

        print("\nWeather Component Assessments:")
        print(f"Humidity    : {humidity_result}")
        print(f"Cloudiness  : {cloudiness_result}")
        print(f"Temperature : {temperature_result}")
        print(f"\nUmbrella Advice: {umbrella_advice}")

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
