"""
대학생 설문조사 Kmeans 결과를 바탕으로 각 클러스터간의 특징을 파악하기 위해 결과 해석 시각화
클러스터는 0,1,2 로 구분하였고 각 클러스터의 특징은 아래와 같음
0: 기본적인 금융 지식 부족, 1: 안정적인, 장기적인 재테크(예금) 관심 있음, 2: 주식 등과 같은 다양한 재테크 관심 있음
"""

# 필요한 라이브러리 호출
import pandas as pd
import matplotlib.pyplot as plt

# xlsx 파일(설문조사 인코딩 후 클러스터링 결과)을 불러오기
visual=pd.read_excel("./../project_data/encoded_cluster.xlsx")

# 클러스터의 개수
num_clusters = 3

# 클러스터의 개수만큼 반복
for cluster_number in range(num_clusters):
    # 클러스터 선택 (0,1,2)
    cluster_data = visual[visual['cluster'] == cluster_number]

    # purpose_encoded, investment_1_encoded, investment_2_encoded, knowledge_encoded 값 세기
    purpose_counts = cluster_data['purpose_encoded'].value_counts()
    investment_1_counts = cluster_data['investment_1_encoded'].value_counts()
    investment_2_counts = cluster_data['investment_2_encoded'].value_counts()
    knowledge_counts = cluster_data['knowledge_encoded'].value_counts()

    # 막대그래프 그리기
    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(4, 8))

    purpose_counts.plot(kind='bar', ax=axes[0], color='skyblue', edgecolor='black')
    axes[0].set_title(f'Count of purpose_encoded (cluster {cluster_number})')
    axes[0].set_xlabel('purpose_encoded')
    axes[0].set_ylabel('Count')

    investment_1_counts.plot(kind='bar', ax=axes[1], color='lightcoral', edgecolor='black')
    axes[1].set_title(f'Count of investment_1_encoded (cluster {cluster_number})')
    axes[1].set_xlabel('investment_1_encoded')
    axes[1].set_ylabel('Count')

    investment_2_counts.plot(kind='bar', ax=axes[2], color='lightyellow', edgecolor='black')
    axes[2].set_title(f'Count of investment_2_encoded (cluster {cluster_number})')
    axes[2].set_xlabel('investment_2_encoded')
    axes[2].set_ylabel('Count')

    knowledge_counts.plot(kind='bar', ax=axes[3], color='lightgreen', edgecolor='black')
    axes[3].set_title(f'Count of knowledge_encoded (cluster {cluster_number})')
    axes[3].set_xlabel('knowledge_encoded')
    axes[3].set_ylabel('Count')

    plt.tight_layout()

# 그래프 한 눈에 확인하기
plt.show()


