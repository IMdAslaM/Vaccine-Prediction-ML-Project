#try this in Visual Code Stidio, it will not work in colab
#import dash
# from dash import Dash
# from dash import dcc
# from dash import html
import streamlit as st
#import streamlit.plotly_chart as px
import plotly.express as px
import pandas as pd
import time
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle
from charts import fig_h1n1_awareness_h1n1_vaccine,fig_dr_recc_h1n1_vacc_h1n1_vaccine,fig_is_h1n1_vacc_effective,fig_sick_from_h1n1_vacc,fig_h1n1_worry_h1n1_vaccine
import base64


# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.




df= pd.read_csv('https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/Vaccine.csv')

new_df=df[['h1n1_worry','h1n1_awareness','antiviral_medication','contact_avoidance','bought_face_mask','wash_hands_frequently',
'avoid_large_gatherings','reduced_outside_home_cont','avoid_touch_face','dr_recc_h1n1_vacc','dr_recc_seasonal_vacc','chronic_medic_condition','cont_child_undr_6_mnths',
'is_health_worker','is_h1n1_vacc_effective','is_h1n1_risky','sick_from_h1n1_vacc','is_seas_vacc_effective','is_seas_risky','sick_from_seas_vacc',
'no_of_adults','no_of_children','age_bracket','race','sex','census_msa','h1n1_vaccine']]

new_df["dr_recc_h1n1_vacc"]=new_df["dr_recc_h1n1_vacc"].fillna(0)
new_df["dr_recc_seasonal_vacc"]=new_df["dr_recc_seasonal_vacc"].fillna(0)
new_df["chronic_medic_condition"]=new_df["chronic_medic_condition"].fillna(0)
new_df["cont_child_undr_6_mnths"]=new_df["cont_child_undr_6_mnths"].fillna(0)
new_df["is_health_worker"]=new_df["is_health_worker"].fillna(0)

new_df=new_df.dropna()

#Converting Categorical value to numerical value by mNUlly assigning int value instead of directly using label encoding 
gender_mapping={'Female':0,'Male':1}
new_df['sex']=new_df['sex'].map(gender_mapping)
#new_df['sex'].value_counts()

#Converting race column from categorical to numerical
race_mapping={'White':1,'Black':2,'Hispanic':3,'Other or Multiple':4}
new_df['race']=new_df['race'].map(race_mapping)
#new_df['race'].value_counts()

#Converting age_bracket column from categorical to numerical
age_mapping={'18 - 34 Years':1,'35 - 44 Years':2,'45 - 54 Years':3,'55 - 64 Years':4,'65+ Years':5}
new_df['age_bracket']=new_df['age_bracket'].map(age_mapping)
#new_df['age_bracket'].value_counts()

#Converting census_msa column from categorical to numerical
census_mapping={'Non-MSA':1,'MSA, Not Principle  City':2,'MSA, Principle City':3}
new_df['census_msa']=new_df['census_msa'].map(census_mapping)
#new_df['census_msa'].value_counts()


 
# print(grouped_mode_df)
# Create bar plot





def page_home():
    st.title("Welcome to My ML Application")
    file_ = open("ML_Gif.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)
    st.markdown("""## <span style="color:aqua">Problem Statement of this ML application:</span>""",unsafe_allow_html=True)
    st.markdown('This project aims to predict the likelihood of people taking an H1N1 flu vaccine using Logistic Regression. It involves analyzing a dataset containing various features related to individuals\' behaviors, perceptions, and demographics, and building a predictive model to determine vaccine acceptance.')
    st.markdown('Predict the probability of individuals taking an H1N1 flu vaccine based on theircharacteristics and attitudes. This can help healthcare professionals and policymakers target vaccination campaigns more effectively.')


def page_data(new_df):
    #creating 2 columns in streamlit page for getting input from user
    st.markdown("""# <span style="color:aqua">Data Visualization</span>""",unsafe_allow_html=True)
    file_ = open("data-analysis.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)
    st.markdown("""## <span style="color:aqua">Chart 1:</span>""",unsafe_allow_html=True)
    fig_h1n1_awareness_h1n1_vaccine(new_df)
    st.markdown("""## <span style="color:aqua">Chart 2:</span>""",unsafe_allow_html=True)
    fig_dr_recc_h1n1_vacc_h1n1_vaccine(new_df)
    st.markdown("""## <span style="color:aqua">Chart 3:</span>""",unsafe_allow_html=True)
    fig_is_h1n1_vacc_effective(new_df)
    st.markdown("""## <span style="color:aqua">Chart 4:</span>""",unsafe_allow_html=True)
    fig_sick_from_h1n1_vacc(new_df)
    st.markdown("""## <span style="color:aqua">Chart 5:</span>""",unsafe_allow_html=True)
    fig_h1n1_worry_h1n1_vaccine(new_df)


def page_predict():
    #creating 2 columns in streamlit page for getting input from user
    st.markdown("""# <span style="color:aqua">Predict H1N1 Vaccine Status</span>""",unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    col1,col2 = st.columns(2)
    
    with col1:
        h1n1_worry_pred=st.text_input('Do you Worried about "h1n1 flu"? -- Enter: (0 or 1 or 2 or 3) -- 0=Not worried at all, 1=Not very worried, 2=Somewhat worried, 3=Very Worried')
        h1n1_awareness_pred=st.text_input('What is the amount of knowledge you have on "h1n1flu" ? -- Enter: (0 or 1 or 2) -- 0=No knowledge, 1=little knowledge, 2=good knowledge')#getting a input from User
        #antiviral_medication_pred=st.text_input('Enter  antiviral_medication (Range: 25-113)')
        #contact_avoidance_pred=st.text_input('Enter  contact_avoidance (Range: 0-6)')
        #bought_face_mask_pred=st.text_input('Enter  bought_face_mask (Range: 2-87)')
        #wash_hands_frequently_pred=st.text_input('Enter  wash_hands_frequently')
        avoid_large_gatherings_pred=st.text_input('Are you avoiding large gatherings? -- Enter: (0 or 1) -- 0=No, 1=Yes')
        dr_recc_h1n1_vacc_pred=st.text_input('Is Doctor recommended h1n1 Vaccine? -- Enter: (0 or 1) -- 0=No, 1=Yes')
        dr_recc_seasonal_vacc_pred=st.text_input('Is Doctor recommended Seasonal flu Vaccine? -- Enter: (0 or 1) -- 0=No, 1=Yes')
        cont_child_undr_6_mnths_pred=st.text_input('Are you having regular contact with child at the age of 6 months? -- Enter: (0 or 1) -- 0=No, 1=Yes')
        is_health_worker_pred=st.text_input('Are you a Health Worker? -- Enter: (0 or 1) -- 0=No, 1=Yes')
        is_h1n1_vacc_effective_pred=st.text_input('Do you think that the h1n1 vaccine is effective? -- Enter Values b/w (1-5) -- (1=Thinks not effective at all, 2=Thinks it is not very effective, 3=Doesn\'t know if it is effective or not, 4=Thinks it is somewhat effective, 5=Thinks it is highly effective)')
        is_h1n1_risky_pred=st.text_input('What do yo think about the risk of getting ill with h1n1 in the absence of the vaccine? -- Enter Values b/w (1-5) -- (1=Thinks it is not very low risk, 2=Thinks it is somewhat low risk, 3=don’t know if it is risky or not, 4=Thinks it is somewhat high risk, 5=Thinks it is very highly risky)')
        #reduced_outside_home_cont_pred=st.text_input('Enter  reduced_outside_home_cont (Range: 611728-1722207579)')
        #avoid_touch_face_pred=st.text_input('Enter  avoid_touch_face (Eg.2020)')
    with col2:
        #chronic_medic_condition_pred=st.text_input('Enter  chronic_medic_condition (Eg.2020)') 
        sick_from_h1n1_vacc_pred=st.text_input('Do you worried about getting sick by taking the h1n1 vaccine?  -- Enter Values b/w (1-5) -- (1=Not Worried at all, 2=Not very worried, 3=Doesn\'t know, 4=somewhat worried, 5=very worried)')
        is_seas_vacc_effective_pred=st.text_input('Do you think that the seasonal vaccine is effective? -- Enter Values b/w (1-5) -- (1=Thinks not effective at all, 2=Thinks it is not very effective, 3=Doesn\'t know if it is effective or not, 4=Thinks it is somewhat effective, 5=Thinks it is highly effective)')
        is_seas_risky_pred=st.text_input('What do you think about the risk of getting ill with seasonal flu in the absence of the vaccine? -- Enter Values b/w (1-5) -- (1=Thinks it is not very low risk, 2=Thinks it is somewhat low risk, 3=Doesn\'t know if it is risky or not, 4=Thinks it is somewhat high risk, 5=Thinks it is very highly risky)')
        sick_from_seas_vacc_pred=st.text_input('Do you worried about getting sick by taking seasonal flu vaccine? -- Enter Values b/w (1-5) -- (1=not worried at all, 2=not very worried, 3=Doesn\'t know, 4=somewhat worried, 5=very worried)')
        no_of_children_pred=st.text_input('Enter the no. of children in your house (Range: 0-3)')
        age_bracket_pred=st.text_input('Enter you Age Bracket -- If \'18 - 34 Years\': Enter "1", If \'35 - 44 Years\': Enter "2", If \'45 - 54 Years\': Enter "3", If \'55 - 64 Years\': Enter "4", If \'65+ Years\': Enter "5"')
        race_pred=st.text_input('Enter your race -- If \'White\': Enter "1", If \'Black\': Enter "2", If \'Hispanic\': Enter "3", If \'Other or Multiple\': Enter "4"')
        sex_pred=st.text_input('Enter your Gender -- Enter 0 or 1 -- 0=Female, 1=Male')
        census_msa_pred=st.text_input('Enter the Census MSA -- If \'Non-MSA\':Enter "1", If \'MSA, Not Principle City\': Enter "2", If \'MSA, Principle City\': Enter "3"')


    #loading a knowledge file for LogisticRegression
    with open('knowlege_pkl_model_logistic', 'rb') as file:
        model_logistic=pickle.load(file)

    if st.button('Predict H1N1 Vaccine Status'):#button
                placeholder=st.empty()
                #forming a dataframe p with each input variables 
                p=pd.DataFrame([h1n1_worry_pred,h1n1_awareness_pred,
                avoid_large_gatherings_pred,
                dr_recc_h1n1_vacc_pred,dr_recc_seasonal_vacc_pred,cont_child_undr_6_mnths_pred,
                is_health_worker_pred,is_h1n1_vacc_effective_pred,is_h1n1_risky_pred,sick_from_h1n1_vacc_pred,is_seas_vacc_effective_pred,is_seas_risky_pred
                ,sick_from_seas_vacc_pred,no_of_children_pred,age_bracket_pred,race_pred,sex_pred,census_msa_pred])
                #converting each column's datatype to float
                p=p.astype(float)
                #applying scaling using pipeline function
                pipeline = Pipeline([
                ('std_scalar', StandardScaler())])
                #Adjusting threshold value to 0.2 to get better accuracy
                y_pred = np.where(model_logistic.predict_proba(pipeline.fit_transform([[float(h1n1_worry_pred),float(h1n1_awareness_pred),
                float(avoid_large_gatherings_pred),float(dr_recc_h1n1_vacc_pred),
                float(dr_recc_seasonal_vacc_pred),float(cont_child_undr_6_mnths_pred),
                float(is_health_worker_pred),float(is_h1n1_vacc_effective_pred),float(is_h1n1_risky_pred),float(sick_from_h1n1_vacc_pred),float(is_seas_vacc_effective_pred),float(is_seas_risky_pred),
                float(sick_from_seas_vacc_pred),float(no_of_children_pred),float(age_bracket_pred),float(race_pred),
                float(sex_pred),float(census_msa_pred)]]))[:,1]>0.721,1,0)
                y_pred=int(y_pred[0])
                # HTML and CSS for highlighted text
                highlighted_output = f"""
                <div style="background-color: black; padding: 10px;">
                    {y_pred}
                </div>
                """
                st.write("Predicted Status \"1\" means \"Vaccinated\" and \"0\" means \"Not Vaccinated\"  :- ")
                st.markdown(highlighted_output, unsafe_allow_html=True)
                time.sleep(30)


def main():
    st.sidebar.title("Page Navigation👇")
    selection = st.sidebar.selectbox("",["Home Page 🏠", "Data Visualization", "Predict Vaccine Status"])

    if selection == "Home Page 🏠":
        page_home()
    elif selection == "Data Visualization":
        page_data(new_df)
    elif selection == "Predict Vaccine Status":
        page_predict()

if __name__=="__main__":
    main()


