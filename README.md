# Capstone_1_2조
## 2021110511 김세연, 2022111739 박예진 
## main branch에서 모든 작업 후, 세부 branch로 결과값 분리 

### 파일명  설명 
- merge_word.py : ‘중소기업은행_금융용어 해설.csv’, + ‘한국산업은행_금융 관련 용어.csv’ + ‘한국자산관리공사_공사홈페이지_용어사전.csv’ merge 코드
- financial_information.py : 'financial_tip.csv'를 랜덤 추출하는 코드와 ‘merge_word.py’ merge한 코드 (금융 정보 제공)
- financial_tip_crawling.py : 금융소비자 정보포털 '파인'에서 금융 꿀팁 크롤링 코드
- economy_survey.py : 대학생 대상 투자 성향 설문조사 결과를 전처리
- survery_kmeans.py : 설문 조사 결과를 바탕으로 kmeans 및 시각화 코드
- cluster_visualization.py : 설문 조사 결과를 바탕으로 각 클러스터 간의 특징을 파악하기 위해 결과 해석 시각화


### 데이터명 설명
- combined_data.csv : ‘중소기업은행_금융용어 해설.csv'’ + ‘한국산업은행_금융 관련 용어.csv’ + ‘한국자산관리공사_공사홈페이지_용어사전.csv’ merge한 파일
- financial_tip.csv : 금융소비자 정보포털 '파인'에서 크롤링한 금융 꿀팁

- economy_survey.xlsx : 설문조사 결과 원본
- economy_survey_2.xlsx : economy_survey.xlsx 칼럼명 영어로 변경
- encoded_columns.xlsx : kmeans를 위해 레이블 인코딩한 설문조사 결과
- encoded_cluster.xlsx : encoded_columns.csv에 클러스터 결과를 추가한 파일
- financial_tip_level.xlsx : 각 클러스터 특징에 따른 정보 제공을 위해 크롤링한 금융 꿀팁 분류

  
### 발전 정도
- 데이터사이언스 캡스톤 디자인 1 결과물
    - 선행 연구 정리 및 데이터 수집
        - 금융 용어(용어,설명) 데이터 수집, 대학생 대상 투자 성향 설문 조사 진행
        
- 파이썬을 이용한 데이터사이언스 캡스톤 디자인 1 발전 방향성
    - 설문 조사 결과에 대한 응답자 클러스터링 결과를 해석하여, 집단 특성에 따른 맞춤형 금융 정보 서비스 제공

- 파이썬을 이용한 데이터사이언스 캡스톤 디자인 1 결과물
    - 데이터 수집 및 전처리 : 금융 용어 데이터 전처리 및 merge + 금융소비자 정보포털 '파인'의 금융 꿀팁 크롤링
    - 모델링 : 설문 조사 결과 전처리 후 Kmeans
    - 결과 해석 : 클러스터 결과를 바탕으로 집단 특성을 해석
    - 시각화 : 설문 조사 클러스터 결과 
    - 서비스: 각 클러스터에 금융 용어 랜덤 10개 제공 + 클러스터 특징에 따른 금융 꿀팁을 3개 제공 (금융 용어는 난이도 판별이 어려워 랜덤으로 제공)

### 코드 실행 순서

데이터 수집 및 전처리

- merge_word.py 와 financial_tip_crawling.py로 응답자에게 제공할 정보 취합 및 정리
- economy_survey.py 대학생 대상 투자 성향 설문조사 결과를 전처리 ( 컬럼명 변경)

모델링 및 서비스

- survey_kmeans.py로 클러스터링 후 PCA 시각화
- cluster_visualization.py로 시각화를 바탕으로 각 클러스터 간의 특징 파악 및 해석
- financial_information.py로 금융용어를 랜덤으로 제공하고, 클러스터 특징에 따른 맞춤 금융 꿀팁 제공

