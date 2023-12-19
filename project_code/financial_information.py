"""금융관련 키워드 랜덤으로 제공 및 클러스터 특징에 따른 알맞은 금융 꿀팁 제공
금융 단어는 랜덤으로 10개 제공, 금융관련 꿀팁은 클러스터의 특징에 따라 0,1,2로 구분하여 맞춤형 정보 3개 제공
0: 기초적인 금융 꿀팁, 1: 안정적인, 장기적인 재테크(예금) 관련 꿀팁, 2: 주식 등과 같은 다양한 재테크 관련 꿀팁 """

#필요한 라이브러리 호출
import pandas as pd

# xlsx 파일(금융단어, 금융 꿀팁)을 불러오기
word=pd.read_csv("./../project_data/combined_data.csv")
tip=pd.read_excel("./../project_data/financial_tip_level.xlsx")

# word에서 랜덤으로 10개 행 선택
random_rows = word.sample(n=10)

# 용어와 설명 출력
print(random_rows.to_markdown(index=False))
print()

# 사용자에게 클러스터 값 입력 받기
user_input = input("0, 1, 2 중 하나를 입력하세요: ")

# 입력값이 유효한지 확인
valid_inputs = ['0', '1', '2']
if user_input not in valid_inputs:
    print("올바른 입력값이 아닙니다. 0, 1, 2 중 하나를 입력하세요.")
else:
    user_input = int(user_input)  # 입력값을 정수로 변환

    # 링크 전체가 출력될 수 있도록 출력 옵션 변경
    pd.set_option('display.max_colwidth', None)
    # 입력한 클러스터 값에 해당하는 행을 랜덤으로 3개 선택
    result = tip[tip.iloc[:, 2] == user_input].iloc[:, [0, 1]].sample(n=3)

    if result.empty:
        print(f"입력값 {user_input}에 해당하는 행이 없습니다.")
    else:
        print(result) # title과 link 출력

    # 출력 옵션 초기화
    pd.reset_option('display.max_colwidth')
