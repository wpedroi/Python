import pandas as pd
from sqlalchemy import create_engine

# 1. Load CSV (use FULL path)
df = pd.read_csv(r"C:\Users\pcu\Desktop\كميات المخزون.csv")

# 2. Create connection to SQL Server
engine = create_engine(
    "mssql+pyodbc://.\SQLEXPRESS/PortfolioProject?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

# 3. Send data to SQL Server (auto-create table)
df.to_sql("darkam_06_09_2026_الكميات_في_المتجر_quantities", engine, if_exists="replace", index=False)

print("Import completed successfully")