import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


df = pd.read_excel("orders_anonymized.xlsx")


basket = (
    df.groupby(["OrderID", "ProductName"])["Quantity"]
    .sum()
    .unstack()
    .fillna(0)
)

# Quantity > 0 olanları 1 yap (binary sepet)
basket = basket.applymap(lambda x: 1 if x > 0 else 0)

print("Sepet örneği:")
print(basket.head())


frequent_itemsets = apriori(
    basket,
    min_support=0.05,   # %5 yeterli (veri küçük olduğu için)
    use_colnames=True
)

print("\nSık geçen ürün kümeleri:")
print(frequent_itemsets)


rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.3   # %30 güven eşiği
)


rules = rules[
    ["antecedents", "consequents", "support", "confidence", "lift"]
]


rules = rules[rules["lift"] > 1]


rules = rules.sort_values(by="confidence", ascending=False)

print("\nAssociation Rules (Anlamlı Kurallar):")
print(rules)
