from random import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import openpyxl

pd.set_option('display.max_columns', 8)

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

prenatal = prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'})
sports = sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'})

df = pd.concat([general, prenatal, sports], ignore_index=True)

df.drop('Unnamed: 0', inplace=True, axis=1)

df.dropna(axis=0, how='all', inplace=True)

column_list = ['gender', 'bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
for i in column_list:
    df[i] = df[i].fillna(0)

df['gender'] = df['gender'].replace([0], 'f')
df['gender'] = df['gender'].replace(['male', 'man'], 'm')
df['gender'] = df['gender'].replace(['female', 'woman'], 'f')

# ===1===
#What is the most common age of a patient among all hospitals?
#Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80
plt.figure(1)

years_cut = [0-15, 15-35, 35-55, 55-70, 70-80]
data_1 = df.loc[:,'age']

data_0_15 = []
data_15_35 = []
data_35_55 = []
data_55_70 = []
data_70_80 = []

for i in data_1.items():
    if 0 <= i[1] <= 15:
        data_0_15.append(i[1])
    if 15 <= i[1] <= 35:
        data_15_35.append(i[1])
    if 35 <= i[1] <= 55:
        data_35_55.append(i[1])
    if 55 <= i[1] <= 70:
        data_55_70.append(i[1])
    if 70 <= i[1] <= 88:
        data_70_80.append(i[1])

total_1 = {'0-15':len(data_0_15), '15-35': len(data_15_35), '35-55':len(data_35_55), '55-70':len(data_55_70), '70-80':len(data_70_80)}

max_ages_name = ''
max_ages_amount = 0
for i in total_1.items():
    if i[1] > max_ages_amount:
        max_ages_amount = i[1]
        max_ages_name = i[0]

plt.hist(data_15_35, color="blue", edgecolor="white")
plt.title("Ages statistics")
plt.ylabel("Number of people")
plt.xlabel("Age")

print(f'The answer to the 1st question: {max_ages_name}')
# ===1===


# ===2===
#What is the most common diagnosis among patients in all hospitals? Create a pie chart
plt.figure(2)

disease = ['cold' 'stomach' 'dislocation' 'heart' 'sprain' 'fracture' 'pregnancy']
data_2 = df['diagnosis'].value_counts(normalize=True)
text_answer_2 = data_2.index
data = data_2
labels = data_2.keys()
plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.title='Diagnosis distribution'

print(f'The answer to the 2nd question: {text_answer_2[0]}')
# ===2===

# ===3===
# Build a violin plot of height distribution by hospitals

hospital_height_general = df.loc[df.hospital == 'general', ['hospital', 'height']]
hospital_height_general = hospital_height_general.to_numpy()
general_heights = []
for i in hospital_height_general:
    general_heights.append(i[1])

hospital_height_sports = df.loc[df.hospital == 'sports', ['hospital', 'height']]
hospital_height_sports = hospital_height_sports.to_numpy()
sports_heights = []
for i in hospital_height_sports:
    i = i[1]
    i = (i * 2.54) * 0.10
    sports_heights.append(i)

hospital_height_prenatal = df.loc[df.hospital == 'prenatal', ['hospital', 'height']]
hospital_height_prenatal = hospital_height_prenatal.to_numpy()
prenatal_heights = []
for i in hospital_height_prenatal:
    prenatal_heights.append(i[1])

all_hospital_heights = general_heights + sports_heights + prenatal_heights


fig, axes = plt.subplots()
heights = plt.violinplot([general_heights, sports_heights, prenatal_heights], showextrema=True, quantiles=([0.25, 0.75, 0.5], [0.25, 0.75, 0.5], [0.25, 0.75, 0.5]))
heights['cquantiles'].set_color('y')
axes.set_xticks((1, 2, 3))
axes.set_xticklabels(("General","Sports","Prenatal"))
print(f"The answer to the 3rd question: It's because the amount of data is available in each hospital")

plt.show()
# ===3===


plt.show()
# df.to_excel(r'C:\Users\Sergio Nicolas\PycharmProjects\Data Analysis for Hospitals\Data Analysis for Hospitals\task\joinedd.xlsx', index = False)
