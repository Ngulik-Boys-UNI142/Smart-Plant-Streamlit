import streamlit as st

class DashboardPage:
    def __init__(self):
        self.title = 'Dashboard'

    def show(self):
        st.title('Dashboard Overview')
        st.write('Welcome to the main dashboard')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('Total Users', '1,200', '4%')
        with col2:
            st.metric('Sales', '$45K', '7%')
        with col3:
            st.metric('Orders', '320', '-2%')    