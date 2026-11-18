import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Veriyi oku
df = pd.read_excel("orders_anonymized.xlsx")


basket = (
    df.groupby(["OrderID", "ProductCategory"])["Quantity"]
    .sum()
    .unstack()
    .fillna(0)
)


basket = basket.applymap(lambda x: True if x > 0 else False)

print("Kategori bazlı sepet örneği:")
print(basket.head())


frequent_itemsets = apriori(
    basket,
    min_support=0.10,   
    use_colnames=True
)

print("\nSık geçen kategori kümeleri:")
print(frequent_itemsets)

# Association rules
rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.3
)

rules = rules[
    ["antecedents", "consequents", "support", "confidence", "lift"]
]

rules = rules[rules["lift"] > 1].sort_values(
    by="confidence", ascending=False
)

print("\nKategori Bazlı Association Rules:")
print(rules)
