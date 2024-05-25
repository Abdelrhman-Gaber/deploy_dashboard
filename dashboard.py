
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout='wide' ,page_title = 'Dashboard')

df = px.data.tips()
box = st.sidebar.checkbox('data_sample')
day = st.sidebar.selectbox('select day', df['day'].unique())
time = st.sidebar.selectbox('select time' , df['time'].unique())

if box:
    st.header('sample data')
    st.dataframe(df.head(10))
    
col1, col2 , col3 = st.columns(3)

with col1:
    new_df = df[df['day'] == day]
    fig1 = px.histogram(new_df, x ='total_bill', color ='sex' , title = f'total_bill for {day} day'.title())
    st.plotly_chart(fig1,use_container_width=True)
    fig2 = px.bar(new_df, x = 'time', y ='total_bill', color = 'sex',barmode='group' ,title = f'time and total bill for {day} day'.title())
    st.plotly_chart(fig2 , use_container_width=True)
    
with col3:
    new_df2 =  df[df['time'] == time]
    fig3 = px.scatter(new_df2 , x ='total_bill', y ='tip' ,color ='sex', title = f'corleation between total bill and tip {time}'.title())
    st.plotly_chart(fig3,use_container_width=True)
    fig4 = px.bar(new_df2, x ='day', y ='total_bill' , color ='sex' , barmode='group', title = f'day and total bill for {time} time'.title())
    st.plotly_chart(fig4,use_container_width=True)
