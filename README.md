# Capstone_1_2조

### 파일명 및 데이터 설명 

- merge_word.py : ‘중소기업은행_금융용어 해설.csv’, + ‘한국산업은행_금융 관련 용어.csv’ + ‘한국자산관리공사_공사홈페이지_용어사전.csv’ merge하는 코드
- combined_data.csv: ‘중소기업은행_금융용어 해설_20201231.csv'’ + ‘한국산업은행_금융 관련 용어_20151231.csv’ + ‘한국자산관리공사_공사홈페이지_용어사전_20230823.csv’ merge한 파일
- financial_information.py : ‘merge_word.py’ 와 'financial_tip.csv'를 랜덤으로 제공하는 코드를 merge한 코드 > 금융 정보 제공 


- financial_tip_crawling.py: 금융 꿀팁 크롤링 코드
- financial_tip.csv : 금융 꿀팁
- level을 나눠서 클러스터별로 제공 파일


- economy_survey.xlsx : 설문조사 결과 원본
- survey_visualization: 설문조사 결과 시각화
- economy_survey_2.xlsx : economy_survey.xlsx 칼럼명 영어로 변경
- encoded_columns.xlsx : kmeans를 위해 레이블 인코딩한 설문조사 결과


- survery_kmeans.py : 설문 조사 결과를 바탕으로 kmeans 및 시각화
- cluster 기준으로 시각화 : 해석한 결과를 시각화한 자료
- encoded_cluster.xlsx : encoded_columns에 클러스터 결과를 추가한 파일