import pandas as pd
from sklearn.preprocessing import LabelEncoder
df=pd.read_excel("C:/Users/lucy8/PycharmProjects/Capstone_1/economy_survey_2.xlsx")

# 범주형 컬럼 선택 (이 예제에서는 'income', 'consumption', 'purpose', 'knowledge')
categorical_columns = ['age','income','consumption','purpose',	'rate',	'investment_1','investment_2','investment_3','investment_4','investment_5','duration','knowledge','investment_rate']

# LabelEncoder 인스턴스 생성 및 fit_transform 적용
label_encoder = LabelEncoder()
for column in categorical_columns:
    df[column + '_encoded'] = label_encoder.fit_transform(df[column])

# 결과 확인
print(df)
df.to_excel('survey_label.xlsx', index=False)