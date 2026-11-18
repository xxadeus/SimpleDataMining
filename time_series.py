import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("orders_anonymized.xlsx")


df["OrderDate"] = pd.to_datetime(df["OrderDate"])


monthly_sales = (
    df.groupby("OrderMonth")["TotalAmount"]
    .sum()
    .reset_index()
)
monthly_sales = monthly_sales.sort_values("OrderMonth")
print("Aylık Toplam Harcama:")
print(monthly_sales)



plt.figure(figsize=(8, 5))
plt.plot(
    monthly_sales["OrderMonth"],
    monthly_sales["TotalAmount"],
    marker="o"
)
plt.title("Aylık Toplam Harcama")
plt.xlabel("Ay")
plt.ylabel("Toplam Harcama (TL)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


platform_monthly = (
    df.groupby(["OrderMonth", "Platform"])["TotalAmount"]
    .sum()
    .reset_index()
)

print("\nPlatform Bazlı Aylık Harcama:")
print(platform_monthly)


plt.figure(figsize=(8, 5))

for platform in platform_monthly["Platform"].unique():
    data = platform_monthly[platform_monthly["Platform"] == platform]
    plt.plot(
        data["OrderMonth"],
        data["TotalAmount"],
        marker="o",
        label=platform
    )

plt.title("Platform Bazlı Aylık Harcama")
plt.xlabel("Ay")
plt.ylabel("Toplam Harcama (TL)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
