# MySQL Data Import Guide & Setup Instructions

**Project:** AI-Powered Sales & Customer Analytics System  
**Database:** `ai_sales_analytics`  
**Target Table:** `sales`  
**Source Data File:** `data/clean_sales_data.csv`  

---

## 1. Prerequisites

1. **MySQL Server 8.0+** installed and running on your system (or accessible via Cloud/Docker).
2. **MySQL Workbench** or command-line client (`mysql`).
3. Ensure the database and schema have been initialized using:
   ```sql
   SOURCE sql/database.sql;
   ```
   *(Or open `sql/database.sql` in MySQL Workbench and execute all statements).*

---

## 2. Import Method A: MySQL Workbench GUI Wizard (Recommended for Beginners)

This is the simplest, most intuitive method:

1. Open **MySQL Workbench** and connect to your local MySQL instance.
2. In the **Schemas** panel on the left, right-click the database `ai_sales_analytics` and click **Refresh All**.
3. Expand `ai_sales_analytics` > right-click **Tables** > select **Table Data Import Wizard**.
4. Click **Browse** and select `data/clean_sales_data.csv`. Click **Next**.
5. Select **Use existing table** and choose `sales`. Click **Next**.
6. Verify the column mapping:
   - Ensure `Order_Date` is mapped to `Order_Date` (type `date` or `text`).
   - Verify `Quantity` -> integer, `Sales` / `Profit` / `Discount` -> double/decimal.
7. Click **Next** to run the import.
8. Once finished, verify the row count:
   ```sql
   USE ai_sales_analytics;
   SELECT COUNT(*) AS total_rows FROM sales;
   -- Expected output: 5,486 rows
   ```

---

## 3. Import Method B: High-Performance `LOAD DATA LOCAL INFILE` (CLI)

For large-scale production analytics, command-line bulk loading is orders of magnitude faster.

### Step 1: Enable Local Infile in MySQL
In MySQL Command Line Client or Workbench:
```sql
SET GLOBAL local_infile = 1;
```

### Step 2: Run the Bulk Load Statement
> **Note for Windows paths:** Replace `d:/AI_Data_Analyst_Agent/data/clean_sales_data.csv` with your exact forward-slash path.

```sql
USE ai_sales_analytics;

LOAD DATA LOCAL INFILE 'd:/AI_Data_Analyst_Agent/data/clean_sales_data.csv'
INTO TABLE sales
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(
    Order_ID,
    Order_Date,
    Customer_ID,
    Product_ID,
    Product_Category,
    Quantity,
    Sales,
    Discount,
    Profit,
    Region,
    Customer_Type,
    Payment_Mode
);
```

*(If you are running on macOS or Linux, change `LINES TERMINATED BY '\r\n'` to `LINES TERMINATED BY '\n'`)*.

---

## 4. Import Method C: Automated Programmatic Ingestion via Python

You can also push the cleaned dataset directly into MySQL using Pandas and SQLAlchemy without touching the GUI:

```python
import pandas as pd
from sqlalchemy import create_engine

# Connection URL format: mysql+mysqlconnector://<username>:<password>@<host>:<port>/<database>
engine = create_engine("mysql+mysqlconnector://root:YOUR_PASSWORD@localhost:3306/ai_sales_analytics")

# Read clean dataset
df = pd.read_csv("data/clean_sales_data.csv")

# Append into MySQL
df.to_sql("sales", con=engine, if_exists="append", index=False)
print(f"Successfully loaded {len(df)} rows into MySQL!")
```

---

## 5. Troubleshooting Common Gotchas

| Error / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| `ERROR 2068 (HY000): LOAD DATA LOCAL INFILE file request rejected` | Local file transfer disabled in client/server | Run `mysql --local-infile=1 -u root -p` and set `SET GLOBAL local_infile=1;` |
| `ERROR 1292 (22007): Incorrect date value` | Date format mismatch | Our clean dataset is pre-formatted in strict ISO `YYYY-MM-DD`, eliminating this issue. |
| `ERROR 1062: Duplicate entry for key 'PRIMARY'` | Re-importing without clearing table | Run `TRUNCATE TABLE sales;` before re-running the import. |
| Double quotes in text fields | CSV quotes not stripped | Verify `OPTIONALLY ENCLOSED BY '"'` is included in your `LOAD DATA` statement. |

---

## 6. Interview Talking Point

> *"In enterprise analytics, loading CSV files into MySQL is a fundamental ingestion workflow. I documented both GUI-based loading for ad-hoc exploration and `LOAD DATA LOCAL INFILE` with parameterized delimiters, character encoding, and index-optimized staging for high-performance pipelines."*
