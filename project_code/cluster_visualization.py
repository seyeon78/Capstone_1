import pandas as pd
import random
import matplotlib.pyplot as plt

visual=pd.read_excel("./../project_data/encoded_cluster.xlsx")

# cluster가 0인 행만 선택
import matplotlib.pyplot as plt

# Number of clusters
num_clusters = 3

# Iterate through clusters
for cluster_number in range(num_clusters):
    # Select data for the current cluster
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

# Display all plots at once
plt.show()


