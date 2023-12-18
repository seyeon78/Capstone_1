#필요한 라이브러리 호출

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.font_manager as fm

# 폰트 설정
plt.rcParams['font.family'] = 'NanumGothic'

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'  #font 경로 설정
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)
# xlsx 파일 읽기
df = pd.read_excel("./../project_data/economy_survey_2.xlsx")
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 'income'와 'consumption' 칼럼만 선택
df_2 = df[['income', 'consumption']]

# 시각화 설정
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

# 소비와 소득 시각화 (점 그래프)
sns.scatterplot(x='income', y='consumption', data=df_2, s=100, color='blue', edgecolor='black')

# y축 역순으로 설정
plt.gca().invert_yaxis()

# 축 레이블에 사용되는 폰트 설정
plt.xlabel('소득', fontsize=12)
plt.ylabel('소비', fontsize=12)

# 시각화 출력
plt.show()


#2
#
# import matplotlib.pyplot as plt
# import pandas as pd
#
# df = pd.read_excel("C:/Users/lucy8/PycharmProjects/Capstone_1/.xlsx")
# # 'purpose' 칼럼을 기준으로 빈도수 계산
# purpose_counts = df['purpose'].value_counts()
#
# # 선택지가 6개라 상위 6개를 추출
# top6_purposes = purpose_counts.head(6)
#
# # 시각화 설정
# plt.figure(figsize=(8, 8))
#
# # 원 그래프 그리기
# plt.pie(top6_purposes, labels=top6_purposes.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
#
# # 그래프 타이틀 설정
# plt.title('Investment Purpose', fontsize=16)
#
# # 그래프 표시
# plt.show()

#
# #3
#
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # 'knowledge' 칼럼을 기준으로 빈도수 계산
# knowledge_counts = df['knowledge'].value_counts()
#
# # 선택지가 4개라 상위 4개를 추출
# top4_purposes = knowledge_counts.head(4)
#
# # 시각화 설정
# plt.figure(figsize=(8, 8))
#
# # 원 그래프 그리기
# plt.pie(top4_purposes, labels=top4_purposes.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
#
# # 그래프 타이틀 설정
# plt.title('Investment Knowledge', fontsize=16)
#
# # 그래프 표시
# plt.show()
