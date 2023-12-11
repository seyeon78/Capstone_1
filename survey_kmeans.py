import pandas as pd
from sklearn.preprocessing import LabelEncoder
df=pd.read_excel("C:/Users/lucy8/PycharmProjects/Capstone_1/economy_survey_2.xlsx")

# 범주형 컬럼 선택 (이 예제에서는 'income', 'consumption', 'purpose', 'knowledge')
categorical_columns = ['age','income','consumption','purpose',	'rate',	'investment_1','investment_2','investment_3','investment_4','investment_5','duration','knowledge','investment_rate']

# 새로운 변수를 담을 딕셔너리 생성
encoded_columns = {}

# LabelEncoder 인스턴스 생성 및 fit_transform 적용
label_encoder = LabelEncoder()
for column in categorical_columns:
    encoded_columns[column + '_encoded'] = label_encoder.fit_transform(df[column])

# 새로운 데이터프레임 생성
encoded_df = pd.DataFrame(encoded_columns)

# 결과 확인
print(encoded_df)

# 새로운 Excel 파일로 저장
encoded_df.to_excel('encoded_columns.xlsx', index=False)


