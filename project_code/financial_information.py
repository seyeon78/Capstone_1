"금융관련 키워드 랜덤으로 제공 및 클러스터 특징에 따른 알맞은 금융 꿀팁 제공"
import pandas as pd
import random

word=pd.read_csv("/Capstone_1/project_data/combined_data.csv")
tip=pd.read_excel("/Capstone_1/project_data/finacial_tip_level.xlsx")

# 데이터프레임에서 랜덤으로 10개 행 선택
random_rows = word.sample(n=10)

# 결과 출력
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

    # 출력 옵션 변경
    pd.set_option('display.max_colwidth', None)

    result = tip[tip.iloc[:, 2] == user_input].iloc[:, [0, 1]].sample(n=3)

    if result.empty:
        print(f"입력값 {user_input}에 해당하는 행이 없습니다.")
    else:
        print(result)

    # 출력 옵션 초기화
    pd.reset_option('display.max_colwidth')
