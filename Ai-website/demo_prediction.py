import streamlit as st
import pandas as pd


def display_demo_prediction():
    #โหลดโมเดล

    # กรอกข้อมูลการทำนาย
    st.write("กรุณากรอกข้อมูลที่เกี่ยวข้องกับคุณภาพอากาศ:")
    PM = st.number_input("PM2.5", min_value=0.0)
    PM10 = st.number_input("PM10", min_value=0)
    O3 = st.number_input("O3", min_value=0.0)
    CO = st.number_input("CO", min_value=0.0)
    AQI = st.number_input("AQI", min_value=0.0)
    Humidity = st.number_input("Humidity", min_value=0.0)
    Temperature = st.number_input("Temperature", min_value=0.0)
    Air_Quality = st.number_input("Air_Quality", min_value=0.0)

    input_data = pd.DataFrame([ [PM, PM10, O3, CO, AQI, Humidity, Temperature, Air_Quality]], 
                          columns=['PM2.5', 'PM10', 'O3', 'CO', 'AQI', 'Humidity', 'Temperature', 'Air_Quality'])