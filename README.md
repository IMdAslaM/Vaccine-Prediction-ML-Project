# Vaccine Prediction

Project Summary: This project aims to predict the likelihood of people taking an H1N1 flu vaccine using Logistic Regression. I have analyzed a dataset containing various features related to individuals’ behaviors, perceptions, and demographics, and built a predictive model to determine vaccine acceptance.

1) Load the CSV file, check for any NULL values in all columns and drop the columns which is useless for model training.
2) In Vaccine data, we have more NULL values in columns such as "dr_recc_h1n1_vacc", "dr_recc_seasonal_vacc", "chronic_medic_condition", "cont_child_undr_6_mnths", "is_health_worker". So dropping NULL values will not be a good idea, since it may lead to loss of more data. So, iam filling '0' in place of NULL, since all these columns are categorical.
3) For 'sex' column, converting categorical categorical value to numerical value by assigning 'Female=0' & 'Male=1' using map function instead of directly using label encoding. Like this i have done encoding for 'race' , 'age_bracket', 'census_msa' columns. Why iam not using label encoding is, if we use label encoding, it will randomly assign some values to ech category, that's why iam using map function to assign numerical value of my choice.
4) Since, each columns in the data are categorical(0 or 1), no need to check for skewness(log transform). But it is better to check for outliers in each column, but in this data there is no outliers.
5) Done hypothesis testing, to check which columns are having relationship with target(h1n1 vaccine).
6) I have plotted box plots using plotly to visualize data between h1n1_vaccine and h1n1_awareness, dr_recc_h1n1_vacc, is_h1n1_vacc_effective, sick_from_h1n1_vacc and h1n1_worry columns to get insights.
7) Creating a 'X' dataframe for the features, initially i had 25 features. So, i though to reduce some features without affecting the model performance/accuracy. For that, i have trained model with different columns to identify whcih columns are important for model performance.
8) Craeted 'y' dataframe for target(h1n1_vaccine).
9) Splitted the data for train and test.
10) Handled imbalanced data by doing half over sampling and half under sampling.
11) Here, no need to do apply any regularization techniques such as scaling, ridge, lasso. Since, we only have '0' and '1' in ech column.
12) Trained model using logistic regression and got 79% accuracy.
13) To increase the accuracy, i have applied threshold adjusting, Since '0.5' is the default threshold value, i have adjusted the threshold value to '0.721' and got 84% accuracy.
14) I have trained model with 'Random Forest Classifier', 'XGBoost Classifier', ExtraTrees Classifier and Logistic regression.
15) In logistic regression only, got highest accuracy as 84% by doing threshold value adjusting. So, implmented the project with Logistic Regression.
