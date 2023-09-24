import pandas as pd
import numpy as np
import joblib as jb
import streamlit as stl
import warnings
warnings.filterwarnings('ignore')


model = jb.load('Package.pkl')
df = pd.read_csv('train.csv')

def model_prediction(age, job, marital, education, default, balance, housing,loan, contact, day, month, duration, campaign, pdays,previous, poutcome):
    new = [age, job, marital, education, default, balance, housing,loan, contact, day, month, duration, campaign, pdays,previous, poutcome]
    new = pd.DataFrame([new])
    new.columns = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
       'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays',
       'previous', 'poutcome']
    prediction = model.predict(new)
    return prediction
    
def main():
    stl.title("Hackathon")
    
    html_tmp = """
    <div style ='background-color:red;'>
    <h2 style = 'color:white;text-align:centre;'>Term Plan Prediction Application</h2>
    </div
    """
    stl.markdown(html_tmp, unsafe_allow_html = True)
    
    age = stl.number_input("Enter Age",min_value =1, max_value = 100)
    job = stl.selectbox("select the job",pd.unique(df['job']))
    marital = stl.selectbox("select the marital status",pd.unique(df['marital']))
    education = stl.selectbox("select the education status",pd.unique(df['education']))
    default = stl.selectbox("select the default status",pd.unique(df['default']))
    balance = stl.number_input("Enter Balance",min_value =0)
    housing = stl.selectbox("select the housing status",pd.unique(df['housing']))
    loan = stl.selectbox("select the loan status",pd.unique(df['loan']))
    contact = stl.selectbox("select the contact ",pd.unique(df['contact']))
    day = stl.number_input("Enter day ",min_value =0)
    month = stl.selectbox("select the month ",pd.unique(df['month']))
    duration = stl.number_input("Enter Duration",min_value =0)
    campaign = stl.number_input("Enter campaign",min_value =0)
    pdays = stl.number_input("Enter pdays",min_value =0)
    previous = stl.number_input("Enter previous",min_value =0)
    poutcome = stl.selectbox("select the poutcome ",pd.unique(df['poutcome']))
    
    result = ""
    if stl.button("Want to find if the customer is a potential customer ?"):
        result = model_prediction(age, job, marital, education, default, balance, housing,loan, contact, day, month, duration, campaign, pdays,previous, poutcome)
    
    if(result == 0):
        stl.success('Sorry! Not a Potential Customer')
    elif(result ==1):
        stl.success('Hold the Customer! He might be a Potential customer')
    
if __name__ =='__main__':
    main()