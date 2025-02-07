import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import tensorflow

st.title('Churn Modelling')
from tensorflow.keras.models import load_model

# Load the model
model = load_model('model.h5')
with open('ohe_gender.pkl','rb') as file:
    ohe_gender=pickle.load(file)
with open('ohe_geo.pkl','rb') as file:
    ohe_geo=pickle.load(file)
with open('scaler.pkl','rb') as file:
    scaler=pickle.load(file)

credit_score=st.number_input('Credit Score')
age=st.number_input('Age')
tenure=st.slider('Tenure',0,10)
balance=st.number_input('Balance')
Number_of_products=st.slider('Number Of Products',0,4)
credit_card=st.selectbox('Has Credit Card',[0,1])
active_member=st.selectbox('Is Active Member',[0,1])
estimated_salary=st.number_input('Estimated Salary')
geography=st.selectbox('Geography',ohe_geo.categories_[0])
gender=st.selectbox('Gender',ohe_gender.categories_[0])

input_data=pd.DataFrame({
    'CreditScore':[credit_score], 
    'Age':[age], 
    'Tenure':[tenure], 
    'Balance':[balance], 
    'NumOfProducts':[Number_of_products], 
    'HasCrCard':[credit_card],
    'IsActiveMember':[active_member], 
    'EstimatedSalary':[estimated_salary]
})


geo=ohe_geo.transform([[geography]]).toarray()
gen=ohe_gender.transform([[gender]]).toarray()
geo=pd.DataFrame(geo,columns=ohe_geo.get_feature_names_out(['Geography']))
gen=pd.DataFrame(gen,columns=ohe_gender.get_feature_names_out(['Gender']))
input_data=pd.concat([input_data,geo,gen],axis=1)


input_scaled=scaler.transform(input_data)
pro=model.predict(input_scaled)[0][0]
if pro>0.5:
    st.write('Exited:1')
else:
    st.write('Not exited:0') 



