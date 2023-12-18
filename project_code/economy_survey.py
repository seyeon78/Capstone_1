# 필요한 라이브러리 호출
import pandas as pd

# xlsx 파일(설문조사 결과)을 불러오기
file_path = "./../project_data/economy_survey.xlsx"
df = pd.read_excel(file_path)

# 데이터 확인
print("불러온 데이터:", df)

# 각 질문에 대해 컬럼명 변경 (설문조사 질문>영어단어)
df.rename(columns={'연령대는 어떻게 되시나요?': 'age'}, inplace=True)
df.rename(columns={'현재 고정수입은 얼마인가요?': 'income'}, inplace=True)
df.rename(columns={'한달 평균 총 소비금액은 얼마인가요?': 'consumption'}, inplace=True)
df.rename(columns={'투자의 목적은 무엇인가요?': 'purpose'}, inplace=True)
df.rename(columns={'선호하는 저축과 소비의 비율을 선택해주세요.': 'rate'}, inplace=True)
df.rename(columns={'이 중에서 선호하는 투자 1순위를 골라주세요.': 'investment_1'}, inplace=True)
df.rename(columns={'이 중에서 선호하는 투자 2순위를 골라주세요.': 'investment_2'}, inplace=True)
df.rename(columns={'이 중에서 선호하는 투자 3순위를 골라주세요.': 'investment_3'}, inplace=True)
df.rename(columns={'이 중에서 선호하는 투자 4순위를 골라주세요.': 'investment_4'}, inplace=True)
df.rename(columns={'이 중에서 선호하는 투자 5순위를 골라주세요.': 'investment_5'}, inplace=True)
df.rename(columns={'투자하고자 하는 자금의 투자가능기간은 얼마나 되시나요?': 'duration'}, inplace=True)
df.rename(columns={'금융상품 투자에 대한 본인의 지식수준이 어느 정도라고 생각하시나요?': 'knowledge'}, inplace=True)
df.rename(columns={'투자하고자 하는 자금은 고객님의 전체 금융자산(부동산 등을 제외) 중 어느 정도의 비중을 차지하시나요?': 'investment_rate'}, inplace=True)

# 변경된 데이터 확인
# print(df)

# 불필요한 '전화번호를 입력해주세요. (기프티콘 제공 위함)','타임 스탬프' 열 삭제
df.drop(columns=['전화번호를 입력해주세요. (기프티콘 제공 위함)'], inplace=True)
df.drop(columns=['타임스탬프'], inplace=True)
print(df)

# xlsx 파일(컬럼명 수정)을 저장하기
file_path = './../project_data/economy_survey_2.xlsx'
df.to_excel(file_path, index=False, encoding='utf-8-sig')

