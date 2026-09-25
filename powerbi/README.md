# Power BI Connection, Data Modeling & DAX Guide

**Project:** AI-Powered Sales & Customer Analytics System  
**Application:** Power BI Desktop  
**Data Sources Supported:** Clean CSV (`data/clean_sales_data.csv`) OR MySQL Database (`ai_sales_analytics`)  

---

## 1. Connecting Data to Power BI

You can build this portfolio dashboard using either of the following two data source options:

### Option A: Clean Flat File Connection (CSV) - Recommended for Offline & Sharing
1. Open **Power BI Desktop**.
2. On the Home ribbon, click **Get Data** > select **Text/CSV** > click **Connect**.
3. Navigate to and select `data/clean_sales_data.csv`.
4. In the preview dialog, ensure:
   - File Origin: `65001: Unicode (UTF-8)`
   - Delimiter: `Comma`
5. Click **Transform Data** to open Power Query Editor.
6. Verify Column Data Types:
   - `Order_ID`, `Customer_ID`, `Product_ID`, `Product_Category`, `Region`, `Customer_Type`, `Payment_Mode` -> **Text**
   - `Order_Date` -> **Date**
   - `Quantity` -> **Whole Number**
   - `Sales`, `Profit` -> **Fixed Decimal Number ($)**
   - `Discount` -> **Percentage (%)** or **Decimal Number**
7. Also import `data/customer_features.csv` (used for Page 3 Customer Analytics).
8. Click **Close & Apply**.

---

### Option B: Live Relational Connection (MySQL Database)
1. On the Home ribbon, click **Get Data** > select **Database** > **MySQL database**.
2. Enter Server: `localhost:3306` (or your remote host).
3. Enter Database: `ai_sales_analytics`.
4. Select Data Connectivity mode:
   - **Import** (Best performance, enables full DAX capabilities).
   - **DirectQuery** (Live queries sent to MySQL server on each user interaction).
5. Enter your database username (`root`) and password.
6. Select tables/views: `sales`, `monthly_sales`, `regional_performance`, `product_performance`, `customer_summary`.
7. Click **Load**.

---

## 2. Recommended Data Model & Relationships

For an enterprise-grade portfolio model, link transactional facts to dimensions:

```
        ┌─────────────────────────┐
        │       Dim_Date          │
        │ ─────────────────────── │
        │ [Date] (PK)             │
        └────────────┬────────────┘
                     │ 1
                     │
                     │ *
        ┌────────────┴────────────┐            ┌─────────────────────────┐
        │       Fact_Sales        │ *        1 │      Dim_Customer       │
        │ ─────────────────────── │────────────│ ─────────────────────── │
        │ [Order_ID] (PK)         │            │ [Customer_ID] (PK)      │
        │ [Order_Date] (FK)       │            │ [Customer_Segment]      │
        │ [Customer_ID] (FK)      │            │ [Lifetime_Spending]     │
        │ [Product_ID]            │            └─────────────────────────┘
        │ [Sales], [Profit]...    │
        └─────────────────────────┘
```

### DAX Calendar Table Generation:
In Power BI Modeling ribbon, click **New Table** and paste:
```dax
Dim_Date = 
ADDCOLUMNS (
    CALENDAR ( DATE(2023, 1, 1), DATE(2024, 12, 31) ),
    "Year", YEAR ( [Date] ),
    "YearMonth", FORMAT ( [Date], "YYYY-MM" ),
    "MonthName", FORMAT ( [Date], "MMM" ),
    "MonthNumber", MONTH ( [Date] ),
    "Quarter", "Q" & FORMAT ( [Date], "Q" ),
    "DayOfWeek", FORMAT ( [Date], "dddd" ),
    "IsWeekend", IF ( WEEKDAY ( [Date], 2 ) >= 6, "Weekend", "Weekday" )
)
```
*Mark this table as the official Date Table in Power BI.*

---

## 3. Core DAX Measures (KPI Library)

Create a dedicated measure table called `_KeyMeasures` and insert the following production-grade formulas:

### 1. Total Revenue
```dax
Total Revenue = SUM(sales[Sales])
```
*Format: Currency ($), 0 decimal places.*

### 2. Total Profit
```dax
Total Profit = SUM(sales[Profit])
```
*Format: Currency ($), 0 decimal places.*

### 3. Total Orders
```dax
Total Orders = DISTINCTCOUNT(sales[Order_ID])
```
*Format: Whole Number with thousands separator.*

### 4. Total Quantity Sold
```dax
Total Units Sold = SUM(sales[Quantity])
```
*Format: Whole Number.*

### 5. Average Order Value (AOV)
```dax
Average Order Value = 
DIVIDE( [Total Revenue], [Total Orders], 0 )
```
*Format: Currency ($), 2 decimal places.*

### 6. Operating Profit Margin %
```dax
Profit Margin % = 
DIVIDE( [Total Profit], [Total Revenue], 0 )
```
*Format: Percentage (%), 2 decimal places.*

### 7. Average Discount %
```dax
Average Discount % = 
AVERAGE(sales[Discount])
```
*Format: Percentage (%), 1 decimal place.*

### 8. Month-over-Month (MoM) Sales Growth
```dax
Previous Month Sales = 
CALCULATE(
    [Total Revenue],
    DATEADD(Dim_Date[Date], -1, MONTH)
)

MoM Sales Growth % = 
DIVIDE(
    [Total Revenue] - [Previous Month Sales],
    [Previous Month Sales],
    0
)
```
*Format: Percentage (%), 2 decimal places.*

### 9. High Discount Order Count
```dax
High Discount Orders = 
CALCULATE(
    [Total Orders],
    sales[Discount] >= 0.25
)
```

---

## 4. How to Explain This in an Interview

> *"For the Power BI implementation, I designed a clean dimensional star schema centered on `Fact_Sales` connected to an automated DAX calendar dimension and customer feature table. I built a structured `_KeyMeasures` library using `DIVIDE` functions to prevent division-by-zero errors, time intelligence for Month-over-Month growth, and dynamic margin percentages."*
