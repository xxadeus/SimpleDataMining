import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# -----------------------------
# 1. Veriyi oku
# -----------------------------
df = pd.read_excel("orders_anonymized.xlsx")


order_features = (
    df.groupby("OrderID")
    .agg(
        TotalAmount=("TotalAmount", "sum"),
        Quantity=("Quantity", "sum"),
        UniqueCategories=("ProductCategory", "nunique")
    )
    .reset_index()
)

print("Sipariş bazlı özellikler:")
print(order_features.head())


X = order_features[["TotalAmount", "Quantity", "UniqueCategories"]]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


kmeans = KMeans(n_clusters=3, random_state=42)
order_features["Cluster"] = kmeans.fit_predict(X_scaled)

# -----------------------------
# 6. Cluster özetleri (SADECE NUMERIC)
# -----------------------------
cluster_summary = (
    order_features
    .groupby("Cluster")[["TotalAmount", "Quantity", "UniqueCategories"]]
    .mean()
    .round(2)
)

print("\nCluster Özeti (Ortalama Değerler):")
print(cluster_summary)

# -----------------------------
# 7. Cluster dağılımı
# -----------------------------
print("\nCluster Dağılımı (Sipariş Sayısı):")
print(order_features["Cluster"].value_counts())
