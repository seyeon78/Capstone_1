import pandas as pd

df1=pd.read_csv("C:/Users/lucy8/PycharmProjects/Capstone_1/project_data/중소기업은행_금융용어 해설.csv", encoding='euc-kr')
df2=pd.read_csv("C:/Users/lucy8/PycharmProjects/Capstone_1/project_data/한국산업은행_금융 관련 용어.csv", encoding='euc-kr')
df3=pd.read_csv("C:/Users/lucy8/PycharmProjects/Capstone_1/project_data/한국자산관리공사_공사홈페이지_용어사전.csv", encoding='utf-8')


# df1, df2, df3을 합치기 위하여 용어와 설명을 제외한 열 삭제

# df1의 '구 분' 열 삭제
df1 = df1.drop('구 분', axis=1)

# df2의 '구분' 이 '퇴직연금' 인 행 삭제 (정보 제공 대상이 대학생)
df2 = df2.drop(df2[df2['구분'] == '퇴직연금'].index, axis=0)

# df2의 '구분', '분류' 열 삭제
df2 = df2.drop(['구분', '분류'], axis=1)


# 열 이름을 '용어'와 '설명'으로 통일
df1.rename(columns={'용 어':'용어','설 명':'설명'},inplace=True)
df3.rename(columns={'단어':'용어'},inplace=True)


# df1, df2, df3 합치기
combined_df = pd.concat([df1, df2,df3], axis=0)
print(combined_df)


# 중복되는 용어 제거
combined_df.drop_duplicates(['용어'], inplace=True)
print(combined_df)

file_path = 'C:/Users/lucy8/PycharmProjects/Capstone_1/project_data/combined_data.csv'
combined_df.to_csv(file_path, index=False, encoding='utf-8-sig')