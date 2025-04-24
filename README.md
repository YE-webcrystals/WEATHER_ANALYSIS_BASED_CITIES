# 🌤️ Indian Cities Weather Dashboard

An interactive Streamlit web application for visualizing real-time and historical weather data across various Indian cities. The dashboard showcases temperature trends, air quality indices, and weather correlations to help users understand the environmental conditions in any selected city.

---

# Group Members 🤝 : 
1. Megh Shah [ KU2407U332 ]
2. Naitik Jha [ KU2407U336 ]
3. Prince Patel [ KU2407U356 ]
4. Bhupesh Singh Chundawat [ KU2407U267 ]
5. Aswini Jena [ KU2407U259 ]


## 📊 Features

- Select any Indian city and view its detailed weather metrics
- Visualize:
  - 📈 Temperature over time (Line chart)
  - 🔵 Air quality comparison between PM2.5 and PM10 (Scatter plot)
  - 🟠 Correlation heatmap of weather & air quality parameters
- Live weather summary using the latest data snapshot

---

## 📁 Dataset

The app uses a cleaned CSV file named `IndianWeatherRepository.csv` containing:

- Location and timestamp info
- Weather attributes: temperature, humidity, pressure, wind speed
- Air quality metrics: PM2.5, PM10

> **Note**: Ensure your dataset includes columns like `location_name`, `last_updated`, `temperature_celsius`, `humidity`, `pressure_mb`, `wind_kph`, `air_quality_PM2.5`, and `air_quality_PM10`.

---

✅ Requirements:

- Python 3.7+

- pandas

- streamlit

- matplotlib

- seaborn

- plotly

- scikit-learn (optional, if using regression)

📌 Future Improvements:

- Add forecasting models (ANN, RNN)

- Real-time API integration

- Location-based filtering and prediction

- Alerts and insights based on thresholds

