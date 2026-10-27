import pandas as pd
from my_eda_tools import missing_report

df = pd.read_excel("data/data.xlsx")

print("Нийт мөр:", len(df))
print("\nХоосон утгын тоо:")
print(missing_report(df))