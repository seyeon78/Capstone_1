"금융관련 키워드 랜덤으로 제공"
import pandas as pd
import random

word=pd.read_csv("/Capstone_1/project_data/combined_data.csv")

# 데이터프레임에서 랜덤으로 10개 행 선택
random_rows = word.sample(n=10)

# 결과 출력
print(random_rows.to_markdown(index=False))