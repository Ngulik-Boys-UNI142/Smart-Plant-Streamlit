import streamlit as st
import pandas as pd
import requests
import time

class DashboardPage:
    def __init__(self):
        self.title = 'Dashboard'
        self.__url = 'https://coherent-classic-platypus.ngrok-free.app/find/data'

    def show(self):
        st.title('Dashboard Overview🌱🌍')
        st.write('Welcome to the main dashboard')
        st.markdown('Tekan tombol "Pemantauan" untuk melihat data.')

        if st.button('Pemantauan 👀'):
            col1, col2 = st.columns(2)

            with col1:
                self.__ph = st.empty()

            with col2:
                self.__soil = st.empty()

            self.__chart_placeholder = st.empty()
            
            self.__update_data()

    def __update_data(self):
        while True:
            try:
                response = requests.get(self.__url)
                data = response.json()

                if data:
                    last_data = data[-1]
                    ph = last_data.get("ph", "N/A")
                    soil = last_data.get("soil", "N/A")

                    self.__ph.metric('pH Level 🌱', f'{ph}', "Updated 📈")
                    self.__soil.metric('Soil Level 🌍', f'{soil}', "Updated 🌿")

                    df = pd.DataFrame(data)
                    self.__chart_placeholder.line_chart(df[['ph', 'soil']])

            except Exception as e:
                st.error(f"Error fetching data: {e}")

            time.sleep(10)

