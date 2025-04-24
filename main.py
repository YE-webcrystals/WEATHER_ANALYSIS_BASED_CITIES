import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

st.set_page_config(page_title="Indian Weather Dashboard", layout="wide")
st.title("🌤️ Indian Cities Weather Dashboard")                       

@st.cache_data                                                          
def load_data():
    df = pd.read_csv("IndianWeatherRepository.csv")
    df = df.dropna()                                                    
    df['last_updated'] = pd.to_datetime(df['last_updated'])            
    return df

df = load_data()

cities = df['location_name'].unique()                               
selected_city = st.selectbox("Select a City", sorted(cities))       

city_df = df[df['location_name'] == selected_city]
st.subheader(f"📍 Weather Details for {selected_city}")         
st.dataframe(city_df.head(10))

features = ['humidity', 'wind_kph', 'pressure_mb']
target = 'temperature_celsius'                                  


X = city_df[features]
y = city_df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)              

# Actual vs Predicted Temperature Plot with adjusted size
st.subheader("🔵 Actual vs Predicted Temperature: ")                  
fig1, ax1 = plt.subplots(figsize=(6, 4))  # Reduced size
ax1.scatter(y_test, y_pred, alpha=0.6, color='purple', label="Predictions")
ax1.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label="Perfect Prediction")
ax1.set_xlabel("Actual Temperature (°C)", fontsize=10)
ax1.set_ylabel("Predicted Temperature (°C)", fontsize=10)
ax1.set_title("Comparison of Actual vs Predicted Temperature", fontsize=12)
ax1.legend()
st.pyplot(fig1)

# Correlation Heatmap with adjusted size
st.subheader("🟠 Correlation Heatmap: ")                                
fig2, ax2 = plt.subplots(figsize=(7, 5))  # Reduced size (width, height)
corr = city_df[[target] + features + ['air_quality_PM2.5', 'air_quality_PM10']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax2, fmt='.2f', linewidths=1, annot_kws={"size": 8})
ax2.set_title("Correlation Heatmap of Weather and Air Quality Metrics", fontsize=12)
st.pyplot(fig2)


# Temperature Over Time Line Plot
st.subheader("🟣 Temperature Over Time : ")                           
sorted_df = city_df.sort_values('last_updated')
fig3 = px.line(sorted_df, x='last_updated', y='temperature_celsius',
              title=f"Temperature Over Time in {selected_city}", 
              labels={'last_updated': 'Timestamp', 'temperature_celsius': 'Temperature (°C)'},
              line_shape="linear")
fig3.update_layout(title=f"Temperature Fluctuations in {selected_city}", xaxis_title="Date", yaxis_title="Temperature (°C)", title_x=0.5)
st.plotly_chart(fig3, use_container_width=True)

# Air Quality (PM2.5 vs PM10) Scatter Plot
st.subheader("🟡 Air Quality (PM2.5 vs PM10)")                              
fig4 = px.scatter(city_df, x='air_quality_PM2.5', y='air_quality_PM10',
                  color='humidity', size='temperature_celsius',
                  title=f"Air Quality in {selected_city}", 
                  labels={'air_quality_PM2.5': 'PM2.5 Concentration (µg/m³)', 'air_quality_PM10': 'PM10 Concentration (µg/m³)'},
                  color_continuous_scale="Viridis", size_max=15)
fig4.update_layout(title=f"Air Quality Scatter Plot for {selected_city}", xaxis_title="PM2.5 Concentration (µg/m³)", 
                  yaxis_title="PM10 Concentration (µg/m³)", title_x=0.5)
st.plotly_chart(fig4, use_container_width=True)

# Current Summary
st.subheader("📌 Current Summary")                                          
latest = city_df.sort_values('last_updated', ascending=False).iloc[0]
st.metric("Temperature (°C)", f"{latest['temperature_celsius']}°C")
st.metric("Humidity", f"{latest['humidity']}%")
st.metric("Wind Speed", f"{latest['wind_kph']} kph")
st.metric("Pressure", f"{latest['pressure_mb']} mb")
