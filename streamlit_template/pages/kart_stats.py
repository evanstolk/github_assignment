import streamlit as st
import pandas as pd


st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")



st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('data/kart_stats.csv')
df_kart = df_kart[['Body', 'Weight', 'Acceleration', 'On-Road traction', 'Ground Speed', 'Ground Handling']]

st.dataframe(df_kart.style
             .highlight_max(color = 'lightgreen', axis = 0, subset = ['Weight', 'Acceleration', 'On-Road traction', 'Ground Speed', 'Ground Handling'])
             .highlight_min(color = 'red', axis = 0, subset = ['Weight', 'Acceleration', 'On-Road traction', 'Ground Speed', 'Ground Handling'])
)


st.header("How does weight change acceleration?")
st.area_chart(df_kart.sort_values('Weight', ascending=True), x = 'Acceleration', y = 'Weight')


st.header("Weight, Speed, and Acceleration are all correlated -- the heavier the car, the greater the top speed, but the slower the acceleration.")
st.bar_chart(df_kart, x = 'Weight', y = ['Acceleration', 'Ground Speed'])


chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns = ['Body'])
df_unpivot_kart = df_single_kart.unstack().rename_axis(['Category', 'Row Number']).reset_index().drop(columns = 'Row Number').rename({0:'Strength'}, axis = 1)
st.bar_chart(df_unpivot_kart, x = 'Category', y = 'Strength')