import pandas as pd
df = pd.read_csv('task\\stackoverflow_qa.csv')
creationdate=df['creationdate']
filtered=df['creationdate']<'2024-01-01'
print(filtered);
score=df['score']
pinned=df['score']>50
print(pinned);
between=df['score']>=50 & df['score']<=100
print(between);
answer=df['answerer_id']
scott_id=6361531
scot_answers=df[df['answerer_id']==scott_id]
print(scot_answers);
user_ids=df['id']
filtered_df=df[df['answerer_id'].isin(user_ids)]
print(filtered_df);
unutbu_id = 190597

# Convert 'creationdate' to datetime and 'score' to numeric
df['creationdate'] = pd.to_datetime(df['creationdate'], errors='coerce')
df['score'] = pd.to_numeric(df['score'], errors='coerce')

# Filter the DataFrame
filtered_df = df[
    (df['creationdate'].dt.month.isin([3, 4, 5, 6, 7, 8, 9, 10])) &
    (df['creationdate'].dt.year == 2014) &
    (df['answerer_id'] == unutbu_id) &
    (df['score'] < 5)
]

print(filtered_df);
df['score'] = pd.to_numeric(df['score'], errors='coerce')
df['viewcount'] = pd.to_numeric(df['viewcount'], errors='coerce')

# Filter the DataFrame
filtered_df = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) |
    (df['viewcount'] > 10000)
]

print(filtered_df);
scott_boston_id = 6361531

# Filter the DataFrame
filtered_df = df[df['answerer_id'] != scott_boston_id]

print(filtered_df);
titanic_df = pd.read_csv("task\\titanic.csv")
titanic_df.head();
female_class1_age20_30 = df[(df['Sex'] == 'female') &   (df['Pclass'] == 1) & (df['Age'] >= 20) &  (df['Age'] <= 30)];
print(female_class1_age20_30);
paid_over_100 = df[df['Fare'] > 100]
print(paid_over_100);
df['Alone'] = (df['SibSp'] + df['Parch']) == 0
survived_alone = df[(df['Survived'] == 1) & (df['Alone'] == True)]
print(survived_alone);
embarked_C_paid50 = df[(df['Embarked'] == 'C') & (df['Fare'] > 50)]
print(embarked_C_paid50);
with_family = df[(df['SibSp'] > 0) & (df['Parch'] > 0)]
print(with_family);
young_non_survivors = df[(df['Age'] <= 15) & (df['Survived'] == 0)]
print(young_non_survivors);
high_fare_with_cabin = df[(df['Fare'] > 200) & (df['Cabin'].notna())]
print(high_fare_with_cabin);
odd_passenger_ids = df[df['PassengerId'] % 2 != 0]
print(odd_passenger_ids);
unique_tickets = df[df['Ticket'].map(df['Ticket'].value_counts()) == 1]
print(unique_tickets);
miss_in_class1 = df[(df['Sex'] == 'female') & 
                    (df['Name'].str.contains('Miss')) & 
                    (df['Pclass'] == 1)]
print(miss_in_class1);
