import pandas as pd
from my_eda_tools import missing_report

df = pd.read_excel("data/data.xlsx")

print("Нийт мөр:", len(df))
print("\nХоосон утгын тоо:")
print(missing_report(df))
from my_eda_tools import remove_duplicates

test_df = pd.DataFrame({
    "Нэр": ["Бат", "Сараа", "Бат"],
    "Нас": [20, 25, 20]
})

clean_df = remove_duplicates(test_df)

print("\nЦэвэрлэхийн өмнө:", len(test_df))
print("Цэвэрлэсний дараа:", len(clean_df))
print(clean_df)