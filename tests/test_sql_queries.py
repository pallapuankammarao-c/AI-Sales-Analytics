"""
AI-Powered Sales & Customer Analytics System
Test Module: test_sql_queries.py
Purpose: Loads cleaned dataset into an in-memory SQL database and validates
         core analytical queries and views for syntax, execution, and numeric integrity.

Author: Senior Data Analyst Mentor & Fresher Candidate
Date: 2026-09-25
"""

import sqlite3
import pandas as pd

def test_sql_execution():
    print("=" * 60)
    print("TESTING SQL QUERIES & ANALYTICAL LOGIC")
    print("=" * 60)

    # 1. Load clean data
    csv_path = "data/clean_sales_data.csv"
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df):,} records for SQL database testing.")

    # 2. Ingest into in-memory SQLite database
    conn = sqlite3.connect(":memory:")
    df.to_sql("sales", conn, index=False, if_exists="replace")
    cursor = conn.cursor()

    # Query 1: Total Revenue
    cursor.execute("SELECT ROUND(SUM(Sales), 2) FROM sales")
    rev = cursor.fetchone()[0]
    print(f"Query 1 (Revenue): ${rev:,.2f}")
    assert rev is not None and rev > 2000000, "Revenue calculation error!"

    # Query 2: Total Profit
    cursor.execute("SELECT ROUND(SUM(Profit), 2) FROM sales")
    profit = cursor.fetchone()[0]
    print(f"Query 2 (Profit): ${profit:,.2f}")
    assert profit is not None and profit > 100000, "Profit calculation error!"

    # Query 3: Total Orders
    cursor.execute("SELECT COUNT(DISTINCT Order_ID) FROM sales")
    orders = cursor.fetchone()[0]
    print(f"Query 3 (Orders): {orders:,}")
    assert orders == len(df), "Order count mismatch!"

    # Query 4: Total Quantity
    cursor.execute("SELECT SUM(Quantity) FROM sales")
    qty = cursor.fetchone()[0]
    print(f"Query 4 (Units Sold): {qty:,}")
    assert qty == df["Quantity"].sum(), "Quantity mismatch!"

    # Query 5: Average Order Value
    cursor.execute("SELECT ROUND(SUM(Sales) / COUNT(DISTINCT Order_ID), 2) FROM sales")
    aov = cursor.fetchone()[0]
    print(f"Query 5 (AOV): ${aov:.2f}")

    # Query 6: Regional Performance
    cursor.execute("""
        SELECT Region, ROUND(SUM(Sales), 2), ROUND(SUM(Profit), 2)
        FROM sales
        GROUP BY Region
        ORDER BY SUM(Sales) DESC
    """)
    reg_rows = cursor.fetchall()
    print(f"Query 8/9 (Regions evaluated): {len(reg_rows)} territories.")
    assert len(reg_rows) == 5, "Expected 5 regions!"

    # Query 10: Top Products
    cursor.execute("""
        SELECT Product_ID, Product_Category, ROUND(SUM(Sales), 2)
        FROM sales
        GROUP BY Product_ID, Product_Category
        ORDER BY SUM(Sales) DESC
        LIMIT 5
    """)
    top_prods = cursor.fetchall()
    print(f"Query 10 (Top 5 Products): {[p[0] for p in top_prods]}")

    # Query 14: Customer Spending Tiers (CTE)
    cursor.execute("""
        WITH CustomerSpend AS (
            SELECT Customer_ID, SUM(Sales) AS Total_Spend
            FROM sales
            GROUP BY Customer_ID
        )
        SELECT 
            CASE 
                WHEN Total_Spend >= 10000 THEN 'Tier 1'
                WHEN Total_Spend >= 5000  THEN 'Tier 2'
                ELSE 'Tier 3'
            END AS Spend_Tier,
            COUNT(Customer_ID) AS Cust_Count
        FROM CustomerSpend
        GROUP BY Spend_Tier
    """)
    spend_tiers = cursor.fetchall()
    print(f"Query 14 (Spending Tiers): {spend_tiers}")

    # Query 20: MoM Growth via Window Function (LAG)
    cursor.execute("""
        WITH MonthlyTotals AS (
            SELECT substr(Order_Date, 1, 7) AS Order_Month, ROUND(SUM(Sales), 2) AS Sales
            FROM sales
            GROUP BY substr(Order_Date, 1, 7)
        ),
        Lagged AS (
            SELECT 
                Order_Month,
                Sales,
                LAG(Sales, 1) OVER (ORDER BY Order_Month) AS Prev_Sales
            FROM MonthlyTotals
        )
        SELECT 
            Order_Month, 
            Sales, 
            Prev_Sales,
            ROUND(((Sales - Prev_Sales) / Prev_Sales) * 100, 2) AS Growth_Pct
        FROM Lagged
        LIMIT 6
    """)
    mom_sample = cursor.fetchall()
    print("Query 20 (MoM Growth sample first 6 months):")
    for row in mom_sample:
        print(f"   Month: {row[0]} | Sales: ${row[1]:,.2f} | Growth: {row[3]}%")

    conn.close()
    print("\nALL SQL QUERY LOGIC TESTS PASSED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    test_sql_execution()
