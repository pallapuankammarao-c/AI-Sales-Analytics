"""
AI-Powered Sales & Customer Analytics System
Module: generate_dataset.py
Purpose: Generates a realistic synthetic sales dataset (5,500+ records)
         with realistic business relationships, seasonality, customer purchasing
         behavior, and controlled real-world data quality anomalies for cleaning.

Author: Senior Data Analyst Mentor & Fresher Candidate
Date: 2026-09-25
"""

import os
import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set random seed for full reproducibility
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

def get_product_catalog():
    """
    Returns a curated product catalog with realistic base prices,
    costs, and category assignments.
    """
    products = [
        # Technology (High revenue, moderate-to-high profit margin)
        {"Product_ID": "TEC-PH-1001", "Product_Category": "Technology", "Unit_Price": 850.0, "Unit_Cost": 600.0},
        {"Product_ID": "TEC-LP-1002", "Product_Category": "Technology", "Unit_Price": 1200.0, "Unit_Cost": 900.0},
        {"Product_ID": "TEC-MN-1003", "Product_Category": "Technology", "Unit_Price": 300.0, "Unit_Cost": 210.0},
        {"Product_ID": "TEC-AC-1004", "Product_Category": "Technology", "Unit_Price": 45.0, "Unit_Cost": 22.0},
        {"Product_ID": "TEC-PR-1005", "Product_Category": "Technology", "Unit_Price": 250.0, "Unit_Cost": 190.0},
        {"Product_ID": "TEC-HD-1006", "Product_Category": "Technology", "Unit_Price": 110.0, "Unit_Cost": 70.0},

        # Furniture (Bulky, higher logistical cost, thin margins, vulnerable to discounts)
        {"Product_ID": "FUR-CH-2001", "Product_Category": "Furniture", "Unit_Price": 180.0, "Unit_Cost": 140.0},
        {"Product_ID": "FUR-TB-2002", "Product_Category": "Furniture", "Unit_Price": 450.0, "Unit_Cost": 390.0}, # Thin margin
        {"Product_ID": "FUR-BK-2003", "Product_Category": "Furniture", "Unit_Price": 220.0, "Unit_Cost": 175.0},
        {"Product_ID": "FUR-DS-2004", "Product_Category": "Furniture", "Unit_Price": 320.0, "Unit_Cost": 260.0},
        {"Product_ID": "FUR-SF-2005", "Product_Category": "Furniture", "Unit_Price": 650.0, "Unit_Cost": 550.0}, # Sensitive to discount

        # Office Supplies (High volume, low unit price, stable margins)
        {"Product_ID": "OFF-PA-3001", "Product_Category": "Office Supplies", "Unit_Price": 18.0, "Unit_Cost": 9.0},
        {"Product_ID": "OFF-BI-3002", "Product_Category": "Office Supplies", "Unit_Price": 12.0, "Unit_Cost": 5.0},
        {"Product_ID": "OFF-ST-3003", "Product_Category": "Office Supplies", "Unit_Price": 25.0, "Unit_Cost": 14.0},
        {"Product_ID": "OFF-AP-3004", "Product_Category": "Office Supplies", "Unit_Price": 85.0, "Unit_Cost": 55.0},
        {"Product_ID": "OFF-EN-3005", "Product_Category": "Office Supplies", "Unit_Price": 8.0, "Unit_Cost": 3.0},
        {"Product_ID": "OFF-LA-3006", "Product_Category": "Office Supplies", "Unit_Price": 15.0, "Unit_Cost": 7.0},
    ]
    return products

def generate_sales_data(num_records=5500):
    """
    Generates realistic sales transactions with business patterns:
    - 2-year timeline (2023-01-01 to 2024-12-31)
    - 650 unique customers (mix of repeat and one-time buyers)
    - Seasonal surge in Q4 (Nov-Dec festive/holiday period)
    - Regional variation (South experiencing a drop in late 2024 in Technology)
    - Controlled injection of anomalies (missing values, duplicates, outliers, negative quantities)
    """
    products = get_product_catalog()
    num_products = len(products)
    
    # 650 unique customers
    customer_ids = [f"CUST-{i:04d}" for i in range(1, 651)]
    customer_types = ["Consumer", "Corporate", "Small Business"]
    customer_type_weights = [0.50, 0.32, 0.18]
    
    # Pre-assign customer primary attributes for consistency
    customer_profile = {}
    for cid in customer_ids:
        customer_profile[cid] = {
            "type": np.random.choice(customer_types, p=customer_type_weights),
            "preferred_region": np.random.choice(["North", "South", "East", "West", "Central"], p=[0.28, 0.20, 0.22, 0.20, 0.10]),
            "affinity": np.random.choice(["High", "Medium", "Low"], p=[0.15, 0.55, 0.30])
        }

    regions = ["North", "South", "East", "West", "Central"]
    payment_modes = ["Credit Card", "Debit Card", "UPI", "Net Banking", "Cash on Delivery"]
    payment_weights = [0.38, 0.20, 0.25, 0.10, 0.07]

    start_date = datetime(2023, 1, 1)
    total_days = 730  # 2 years

    records = []
    
    # Generate clean base records first
    for i in range(1, num_records + 1):
        order_id = f"ORD-{2023 + (i % 2)}-{10000 + i}"
        
        # Date generation with seasonal weighting (higher weight for Q4: Oct, Nov, Dec)
        day_offset = random.randint(0, total_days - 1)
        order_date = start_date + timedelta(days=day_offset)
        month = order_date.month
        year = order_date.year
        
        # Holiday bump: 30% chance to shift date to Nov/Dec to simulate realistic retail seasonality
        if random.random() < 0.25:
            nov_dec_offset = random.randint(0, 60)
            target_year = 2023 if random.random() < 0.5 else 2024
            order_date = datetime(target_year, 11, 1) + timedelta(days=nov_dec_offset)
            month = order_date.month
            year = order_date.year

        # Customer selection (Power-law: top customers order much more frequently)
        # 15% high-affinity customers generate ~45% of orders
        rand_val = random.random()
        if rand_val < 0.45:
            high_aff_custs = [c for c, p in customer_profile.items() if p["affinity"] == "High"]
            cust_id = random.choice(high_aff_custs)
        elif rand_val < 0.85:
            med_aff_custs = [c for c, p in customer_profile.items() if p["affinity"] == "Medium"]
            cust_id = random.choice(med_aff_custs)
        else:
            low_aff_custs = [c for c, p in customer_profile.items() if p["affinity"] == "Low"]
            cust_id = random.choice(low_aff_custs)

        profile = customer_profile[cust_id]
        customer_type = profile["type"]
        
        # Region selection: 80% customer stays in primary region, 20% traveling/branch order
        if random.random() < 0.80:
            region = profile["preferred_region"]
        else:
            region = random.choice(regions)

        # Business nuance: In late 2024 (H2 2024), South region suffered local competition,
        # leading to lower sales and reduced technology demand.
        prod = random.choice(products)
        if region == "South" and year == 2024 and month >= 7:
            # Reduce technology selection in South H2 2024
            if prod["Product_Category"] == "Technology" and random.random() < 0.40:
                prod = random.choice([p for p in products if p["Product_Category"] != "Technology"])

        product_id = prod["Product_ID"]
        category = prod["Product_Category"]
        unit_price = prod["Unit_Price"]
        unit_cost = prod["Unit_Cost"]

        # Quantity: mostly 1-5, occasionally up to 10
        quantity = int(np.random.choice([1, 2, 3, 4, 5, 8, 10], p=[0.42, 0.28, 0.14, 0.08, 0.05, 0.02, 0.01]))

        # Discount: most orders 0%, 5%, 10%, 15%, 20%, occasional 35-50%
        # Furniture frequently receives higher promotional discounts causing profit erosion
        if category == "Furniture":
            discount = float(np.random.choice([0.0, 0.10, 0.20, 0.30, 0.40, 0.50], p=[0.20, 0.25, 0.25, 0.15, 0.10, 0.05]))
        elif category == "Technology":
            discount = float(np.random.choice([0.0, 0.05, 0.10, 0.15, 0.25], p=[0.45, 0.25, 0.15, 0.10, 0.05]))
        else:  # Office Supplies
            discount = float(np.random.choice([0.0, 0.05, 0.10, 0.20, 0.30], p=[0.40, 0.30, 0.15, 0.10, 0.05]))

        # Mathematical logic:
        # Gross = Quantity * Unit_Price
        # Sales = Gross * (1 - Discount)
        # Cost = Quantity * Unit_Cost
        # Profit = Sales - Cost
        gross_sales = quantity * unit_price
        sales = round(gross_sales * (1.0 - discount), 2)
        total_cost = round(quantity * unit_cost, 2)
        profit = round(sales - total_cost, 2)

        payment_mode = str(np.random.choice(payment_modes, p=payment_weights))

        records.append({
            "Order_ID": order_id,
            "Order_Date": order_date.strftime("%Y-%m-%d"),
            "Customer_ID": cust_id,
            "Product_ID": product_id,
            "Product_Category": category,
            "Quantity": quantity,
            "Sales": sales,
            "Discount": discount,
            "Profit": profit,
            "Region": region,
            "Customer_Type": customer_type,
            "Payment_Mode": payment_mode
        })

    df = pd.DataFrame(records)

    # -------------------------------------------------------------
    # CONTROLLED INJECTION OF REAL-WORLD MESSINESS (For Stage 2 Data Cleaning)
    # -------------------------------------------------------------
    print(f"Base records generated: {len(df)}")

    # 1. Missing Values Injection (~1.5% of rows across different columns)
    missing_indices = np.random.choice(df.index, size=60, replace=False)
    for idx in missing_indices[:15]:
        df.loc[idx, "Payment_Mode"] = np.nan
    for idx in missing_indices[15:30]:
        df.loc[idx, "Customer_Type"] = np.nan
    for idx in missing_indices[30:45]:
        df.loc[idx, "Region"] = np.nan
    for idx in missing_indices[45:60]:
        df.loc[idx, "Discount"] = np.nan

    # 2. Date Formatting Inconsistencies (~15 rows with alternative formats)
    date_noise_indices = np.random.choice(df.index, size=15, replace=False)
    for idx in date_noise_indices:
        val = df.loc[idx, "Order_Date"]
        dt = datetime.strptime(val, "%Y-%m-%d")
        df.loc[idx, "Order_Date"] = dt.strftime("%d/%m/%Y")  # DD/MM/YYYY format

    # 3. Invalid Quantities (~12 rows with negative or 0 values)
    invalid_qty_indices = np.random.choice(df.index, size=12, replace=False)
    for idx in invalid_qty_indices:
        df.loc[idx, "Quantity"] = random.choice([-2, -1, 0])

    # 4. Outliers / Input Typos (~4 rows with 10x or 100x sales)
    outlier_indices = np.random.choice(df.index, size=4, replace=False)
    for idx in outlier_indices:
        df.loc[idx, "Sales"] = round(df.loc[idx, "Sales"] * 25, 2)

    # 5. Duplicates (~45 duplicate rows appended)
    dup_indices = np.random.choice(df.index, size=45, replace=False)
    duplicates = df.loc[dup_indices].copy()
    df = pd.concat([df, duplicates], ignore_index=True)

    # Shuffle to simulate raw ingestion order
    df = df.sample(frac=1.0, random_state=SEED).reset_index(drop=True)

    print(f"Total raw records created with anomalies and duplicates: {len(df)}")
    return df

def main():
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    raw_path = os.path.join("data", "raw_sales_data.csv")

    print("Generating synthetic sales dataset...")
    df = generate_sales_data(num_records=5500)
    df.to_csv(raw_path, index=False)
    print(f"Success! Raw dataset saved to: {raw_path}")
    print(f"Rows: {len(df)}, Columns: {list(df.columns)}")

if __name__ == "__main__":
    main()
