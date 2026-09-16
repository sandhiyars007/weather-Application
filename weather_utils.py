def get_weather_icon(condition):
    icons = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Mist": "🌫️",
        "Haze": "🌫️",
        "Fog": "🌫️"
    }

    return icons.get(condition, "🌤️")