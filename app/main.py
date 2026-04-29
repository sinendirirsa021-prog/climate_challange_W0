import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Climate Analysis Dashboard", layout="wide")

# Theme Colors
GLOBAL_BLACK = "#000000"
TEMP_LINE_COLOR = "#AEEAFF" # Blue-White
RAIN_BAR_COLOR = "#00796B" # Slate-Teal
COMPARISON_PALETTE = ['#1565C0', '#6D4C41', '#00796B', '#455A64', '#2E7D32']

@st.cache_data
def load_data():
    path = 'data/master_climate_data.csv'
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

try:
    df = load_data()
    countries = sorted(df['Country'].unique())

    tab1, tab2 = st.tabs(["Single Country View", "Regional Comparison"])

    with tab1:
        st.sidebar.header("Filter Options")
        selected_country = st.sidebar.selectbox("Select Country", countries)
        date_range = st.sidebar.date_input("Select Date Range", [df['Date'].min(), df['Date'].max()])

        if len(date_range) == 2:
            mask = (df['Country'] == selected_country) & \
                   (df['Date'] >= pd.Timestamp(date_range[0])) & \
                   (df['Date'] <= pd.Timestamp(date_range[1]))
            filtered_df = df.loc[mask]
        else:
            filtered_df = df[df['Country'] == selected_country]

        st.title(f"Climate Risk: {selected_country}")

        # Metrics Row
        m1, m2, m3 = st.columns(3)
        m1.metric("Avg Temp", f"{filtered_df['T2M'].mean():.2f} C")
        m2.metric("Max Temp", f"{filtered_df['T2M_MAX'].max():.2f} C")
        m3.metric("Avg Rainfall", f"{filtered_df['PRECTOTCORR'].mean():.2f} mm")

        # 1. Temperature Trend
        st.subheader("Temperature Trend Over Time")
        fig_temp = px.line(filtered_df, x='Date', y='T2M', color_discrete_sequence=[TEMP_LINE_COLOR])
        fig_temp.update_layout(
            paper_bgcolor=GLOBAL_BLACK, plot_bgcolor=GLOBAL_BLACK, font=dict(color='white'),
            xaxis=dict(showgrid=True, gridcolor='#222222'), yaxis=dict(showgrid=True, gridcolor='#222222')
        )
        st.plotly_chart(fig_temp, use_container_width=True)

        # 2. Precipitation Distribution (Added back)
        st.subheader("Precipitation Distribution")
        fig_rain = px.bar(filtered_df, x='Date', y='PRECTOTCORR', color_discrete_sequence=[RAIN_BAR_COLOR])
        fig_rain.update_layout(
            paper_bgcolor=GLOBAL_BLACK, plot_bgcolor=GLOBAL_BLACK, font=dict(color='white'),
            xaxis=dict(showgrid=True, gridcolor='#222222'), yaxis=dict(showgrid=True, gridcolor='#222222')
        )
        st.plotly_chart(fig_rain, use_container_width=True)

        # 3. Regional Vulnerability Context (Added back)
        st.write("---")
        st.subheader("Regional Vulnerability Context")
        st.write(f"""
        The data for **{selected_country}** is derived from NASA POWER atmospheric records. 
        As climate patterns shift, this dashboard supports the **Addis Ababa Declaration** by providing 
        local evidence for adaptation strategies. These insights are critical for managing water resources 
        and protecting agricultural livelihoods against extreme weather events.
        """)

    with tab2:
        st.title("Regional Comparative Analysis")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader("Mean Temperature by Country")
            avg_comp = df.groupby('Country')['T2M'].mean().reset_index().sort_values('T2M')
            fig_bar = px.bar(avg_comp, x='Country', y='T2M', color='Country', color_discrete_sequence=COMPARISON_PALETTE)
            fig_bar.update_layout(paper_bgcolor=GLOBAL_BLACK, plot_bgcolor=GLOBAL_BLACK, font=dict(color='white'))
            st.plotly_chart(fig_bar, use_container_width=True)

        with col_b:
            st.subheader("Rainfall Volatility")
            std_comp = df.groupby('Country')['PRECTOTCORR'].std().reset_index().sort_values('PRECTOTCORR')
            fig_std = px.bar(std_comp, x='Country', y='PRECTOTCORR', color='Country', color_discrete_sequence=COMPARISON_PALETTE)
            fig_std.update_layout(paper_bgcolor=GLOBAL_BLACK, plot_bgcolor=GLOBAL_BLACK, font=dict(color='white'))
            st.plotly_chart(fig_std, use_container_width=True)

        st.subheader("Regional Temperature Overlays")
        fig_multi = px.line(df, x='Date', y='T2M', color='Country', color_discrete_sequence=COMPARISON_PALETTE)
        fig_multi.update_layout(hovermode="x unified", paper_bgcolor=GLOBAL_BLACK, plot_bgcolor=GLOBAL_BLACK, font=dict(color='white'))
        st.plotly_chart(fig_multi, use_container_width=True)

except FileNotFoundError:
    st.error("The master dataset was not found. Please ensure 'data/master_climate_data.csv' exists.")