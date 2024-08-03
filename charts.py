import streamlit as st
#import streamlit.plotly_chart as px
import plotly.express as px
import pandas as pd



def fig_h1n1_awareness_h1n1_vaccine(new_df):

    grouped_mode_1 = new_df.groupby('h1n1_awareness')['h1n1_vaccine'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
    
    # Reset index to turn the grouped data into a DataFrame
    grouped_mode_df_1 = grouped_mode_1.reset_index()
    
    # print(grouped_mode_df)
    # Create bar plot

    fig_h1n1_awareness_h1n1_vaccine = px.box(grouped_mode_df_1, x='h1n1_awareness', y='h1n1_vaccine',
                labels={'h1n1_awareness': 'Respondent\'s Awareness on H1N1', 'h1n1_vaccine': 'Mode of H1N1 Vaccine'},
                title='Mode of H1N1 Vaccine for Each H1N1 Awareness Level')
    annotations = [ dict( text='Low Awareness', x=0.07, y=0.1, font_size=12, showarrow=False ), 
                    dict( text='Medium Awareness', x=0.98, y=0.1, font_size=12, showarrow=False ), 
                    dict( text='High Awareness', x=2, y=0.1, font_size=12, showarrow=False ) ]
    # Define the annotation for the paragraph 
    #annotation = dict( text=paragraph, x=0.5, y=-0.2, font=dict(size=12), showarrow=False, align='center', xref='paper', yref='paper' )
    fig_h1n1_awareness_h1n1_vaccine.update_layout(annotations=annotations)
        
    st.plotly_chart(fig_h1n1_awareness_h1n1_vaccine, use_container_width=True)

def fig_dr_recc_h1n1_vacc_h1n1_vaccine(new_df):

    grouped_mode_2 = new_df.groupby('dr_recc_h1n1_vacc')['h1n1_vaccine'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
    
    # Reset index to turn the grouped data into a DataFrame
    grouped_mode_df_2 = grouped_mode_2.reset_index()
    
    #print(grouped_mode_df)
    # Create bar plot
    fig_dr_recc_h1n1_vacc_h1n1_vaccine = px.box(grouped_mode_df_2, x='dr_recc_h1n1_vacc', y='h1n1_vaccine',
                labels={'dr_recc_h1n1_vacc': 'Doctor Recommended h1n1_vaccine or not', 'h1n1_vaccine': 'Mode of H1N1 Vaccine'},
                title='Mode of H1N1 Vaccine for Each dr_recc_h1n1_vacc Level')

    annotations = [ dict( text='Doctor Recommended h1n1_vaccine', x=1, y=0.92, font_size=12, showarrow=False ), 
                    dict( text='Doctor not Recommended h1n1_vaccine', x=0.01, y=0.099, font_size=12, showarrow=False ) ]
    # Define the annotation for the paragraph 
    fig_dr_recc_h1n1_vacc_h1n1_vaccine.update_layout(annotations=annotations)
    st.plotly_chart(fig_dr_recc_h1n1_vacc_h1n1_vaccine, use_container_width=True)


def fig_is_h1n1_vacc_effective(new_df):
    grouped_mode_3 = new_df.groupby('is_h1n1_vacc_effective')['h1n1_vaccine'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
    
    # Reset index to turn the grouped data into a DataFrame
    grouped_mode_df_3 = grouped_mode_3.reset_index()
    
    #print(grouped_mode_df)
    # Create bar plot
    fig_is_h1n1_vacc_effective = px.box(grouped_mode_df_3, x='is_h1n1_vacc_effective', y='h1n1_vaccine',
                labels={'is_h1n1_vacc_effective': 'Respondent\'s level whose thinking H1N1 Vaccine is effective or not', 'h1n1_vaccine': 'Mode of H1N1 Vaccine'},
                title='Mode of H1N1 Vaccine for Each is_h1n1_vacc_effective Level')


    annotations = [ dict( text='Thinks not effective at all', x=1, y=0.001, font_size=12, showarrow=True), 
                    dict( text='Thinks it is not very effective', x=2, y=0.007, font_size=12, showarrow=True),
                    dict( text='Doesn\'t know if it is effective or not', x=3, y=0.014, font_size=12, showarrow=True),
                    dict( text='Thinks it is somewhat effective', x=4, y=0.001, font_size=12, showarrow=True),
                    dict( text='5 - Thinks it is highly effective', x=5, y=0.1, font_size=12, showarrow=False)
                    ]
    # # Define the annotation for the paragraph 
    fig_is_h1n1_vacc_effective.update_layout(annotations=annotations) 
    st.plotly_chart(fig_is_h1n1_vacc_effective, use_container_width=True)


def fig_sick_from_h1n1_vacc(new_df):
    grouped_mode_4 = new_df.groupby('sick_from_h1n1_vacc')['h1n1_vaccine'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
    
    # Reset index to turn the grouped data into a DataFrame
    grouped_mode_df_4 = grouped_mode_4.reset_index()
    
    #print(grouped_mode_df)
    # Create bar plot
    fig_sick_from_h1n1_vacc = px.box(grouped_mode_df_4, x='sick_from_h1n1_vacc', y='h1n1_vaccine',
                labels={'sick_from_h1n1_vacc': 'Respondent\'s worry level on Getting sick by taking H1N1 Vaccine', 'h1n1_vaccine': 'Mode of H1N1 Vaccine'},
                title='Mode of H1N1 Vaccine for Each sick_from_h1n1_vacc Level')

    annotations = [ dict( text='Respondent not worried at all', x=1, y=0.5, font_size=12, showarrow=False), 
                    dict( text='Respondent is not very worried', x=2, y=0.4, font_size=12, showarrow=False),
                    dict( text='Respondent have No idea', x=3, y=0.3, font_size=12, showarrow=False),
                    dict( text='Respondent is somewhat worried', x=4, y=0.2, font_size=12, showarrow=False),
                    dict( text='Respondent is very worried', x=5, y=0.1, font_size=12, showarrow=False)
                    ]
    # # Define the annotation for the paragraph 
    fig_sick_from_h1n1_vacc.update_layout(annotations=annotations)
    st.plotly_chart(fig_sick_from_h1n1_vacc, use_container_width=True)

def fig_h1n1_worry_h1n1_vaccine(new_df):
    grouped_mode_5 = new_df.groupby('h1n1_worry')['h1n1_vaccine'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
    
    # Reset index to turn the grouped data into a DataFrame
    grouped_mode_df_5 = grouped_mode_5.reset_index()
    
    # print(grouped_mode_df)
    # Create bar plot
    fig_h1n1_worry_h1n1_vaccine = px.box(grouped_mode_df_5, x='h1n1_worry', y='h1n1_vaccine',
                labels={'h1n1_worry': 'Respondent\'s Fear level on h1n1 flu', 'h1n1_vaccine': 'Mode of H1N1 Vaccine'},
                title='Mode of H1N1 Vaccine for Each h1n1_worry Level')

    annotations = [ dict( text='Respondent not worried at all', x=0, y=1, font_size=12, showarrow=False), 
                    dict( text='Respondent is not very worried', x=1, y=1, font_size=12, showarrow=False),
                    dict( text='Respondent is somewhat worried', x=2, y=1, font_size=12, showarrow=False),
                    dict( text='Respondent is very worried', x=3, y=1, font_size=12, showarrow=False)
                    ]
    # # Define the annotation for the paragraph 
    fig_h1n1_worry_h1n1_vaccine.update_layout(annotations=annotations)
    st.plotly_chart(fig_h1n1_worry_h1n1_vaccine, use_container_width=True)