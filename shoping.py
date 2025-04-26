import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide",page_title='simple DashBoard')
html_title = """<h1 style="white:red;text-align:center;"> Shopping cart EDA Project </h1>"""
st.markdown(html_title,unsafe_allow_html=True)

df=pd.read_csv('cleaned_df.csv',index_col=0)
st.dataframe(df.head(10))

st.sidebar.write(' # Page')
page=st.sidebar.radio('pages',['Univariate','Bivariate','Multivariate'])

if page =='Univariate': 
        for i in df.columns:
                st.plotly_chart (px.histogram(df,x=i,title=i ))
elif page =='Bivariate' :
        x= st.selectbox('X',df.columns)
        y= st.selectbox('Y',df.columns)
        chart= st.selectbox('Chart',['Scatter','Line','box','strip'])
        if chart  == 'box':
                st.plotly_chart( px.box(df,x=x,y=y))
        elif chart  == 'Scatter':
                st.plotly_chart( px.scatter(df,x=x,y=y))
        elif chart  == 'Line':
                st.plotly_chart( px.line(df.sort_values(by='order_month').head(100),x=x,y=y))  
        elif chart  == 'strip':
                st.plotly_chart( px.strip(df,x=x,y=y))  
elif page =='Multivariate' :
        st.subheader('Is there any correlation betwen numerical columns?') 
        st.plotly_chart(px.imshow(df.corr(numeric_only=True).round(1),text_auto=True))
        st.subheader('What is the distribution of revenue each month per Product Type?')
        st.plotly_chart (px.box(df,x='order_month',y='total_price',color='product_type',width=1000))           
