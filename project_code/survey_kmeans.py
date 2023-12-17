import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

df=pd.read_excel("C:/Users/lucy8/PycharmProjects/Capstone_1/economy_survey_2.xlsx")


# 범주형 컬럼 선택 (이 예제에서는 'income', 'consumption', 'purpose', 'knowledge')
categorical_columns = ['age', 'income', 'consumption', 'purpose', 'rate', 'investment_1', 'investment_2', 'investment_3', 'investment_4', 'investment_5', 'duration', 'knowledge', 'investment_rate']

# 새로운 변수를 담을 딕셔너리 생성
encoded_columns = {}

# LabelEncoder 인스턴스 생성 및 fit_transform 적용
label_encoder = LabelEncoder()
for column in categorical_columns:
    encoded_columns[column + '_encoded'] = label_encoder.fit_transform(df[column])

# 새로운 데이터프레임 생성
encoded_df = pd.DataFrame(encoded_columns)

# KMeans 클러스터링
kmeans = KMeans(n_clusters=3, random_state=42)
encoded_df['cluster'] = kmeans.fit_predict(encoded_df)

# 결과 확인
print(encoded_df)
encoded_df.to_excel('encoded_cluster.xlsx', index=False)

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# PCA를 사용하여 데이터를 2차원으로 축소
pca = PCA(n_components=2)
encoded_2d = pca.fit_transform(encoded_df.drop('cluster', axis=1))

# 시각화
plt.figure(figsize=(8, 6))

# 각 클러스터에 대해 다른 색상 사용
for cluster_label in encoded_df['cluster'].unique():
    cluster_data = encoded_2d[encoded_df['cluster'] == cluster_label]
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Cluster {cluster_label}')

plt.title('KMeans Clustering Result')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()
