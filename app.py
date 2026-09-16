import streamlit as st
from weather_api import get_weather
from weather_utils import get_weather_icon

st.set_page_config(
    page_title="SkySense",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ SkySense")
st.subheader("Smart Weather Application")

st.write("Get real-time weather information for any city.")

city = st.text_input(
    "Enter City Name",
    placeholder="Example: Chennai"
)

if st.button("Check Weather"):

    if not city.strip():
        st.warning("Please enter a city name.")

    else:
        with st.spinner("Fetching weather..."):

            data = get_weather(city)

        if data:

            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]

            condition = data["weather"][0]["main"]
            description = data["weather"][0]["description"]

            wind_speed = data["wind"]["speed"]

            icon = get_weather_icon(condition)

            st.success(
                f"Weather found for {data['name']}, {data['sys']['country']}"
            )

            st.markdown(f"# {icon} {temperature}°C")

            st.write(
                f"**Condition:** {description.title()}"
            )

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Feels Like", f"{feels_like}°C")
            col2.metric("Humidity", f"{humidity}%")
            col3.metric("Wind Speed", f"{wind_speed} m/s")
            col4.metric("Pressure", f"{pressure} hPa")

        else:
            st.error(
                "Unable to find weather data. "
                "Check the city name or API key."
            )