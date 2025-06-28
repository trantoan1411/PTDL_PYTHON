
from google.cloud import bigquery
import pandas as pd
import os

# Kết nối đến BigQuery thông qua credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "powerbi-2474725-83fdee3ff325.json"

# Tạo client BigQuery
client = bigquery.Client()

# Bảng đích: 'project_id.dataset.table_name'
table_id = "powerbi-2474725.PowerBI_Data.Sales"

# Đọc dữ liệu từ file CSV
df = pd.read_csv("D:/Power_BI_PL300_Datapot/Dataset/LAB_2/OneDrive_1_4-21-2025/USSales/sales.csv")

# Upload dữ liệu lên bảng đã tạo
job = client.load_table_from_dataframe(df, table_id)
job.result()  # Chờ quá trình upload hoàn tất

print("✅ Upload thành công!")
