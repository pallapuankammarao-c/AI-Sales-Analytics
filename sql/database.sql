-- ==============================================================================
-- AI-Powered Sales & Customer Analytics System
-- Database Definition & DDL Script
-- Target RDBMS: MySQL 8.0+
-- Database: ai_sales_analytics
-- ==============================================================================

-- 1. Create Database
CREATE DATABASE IF NOT EXISTS ai_sales_analytics
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE ai_sales_analytics;

-- 2. Drop existing table if recreating
DROP TABLE IF EXISTS sales;

-- 3. Create Sales Table with Production Constraints and Indexes
CREATE TABLE sales (
    Order_ID           VARCHAR(30)     NOT NULL,
    Order_Date         DATE            NOT NULL,
    Customer_ID        VARCHAR(20)     NOT NULL,
    Product_ID         VARCHAR(30)     NOT NULL,
    Product_Category   VARCHAR(50)     NOT NULL,
    Quantity           INT             NOT NULL,
    Sales              DECIMAL(10, 2)  NOT NULL,
    Discount           DECIMAL(4, 2)   NOT NULL DEFAULT 0.00,
    Profit             DECIMAL(10, 2)  NOT NULL,
    Region             VARCHAR(50)     NOT NULL,
    Customer_Type      VARCHAR(50)     NOT NULL,
    Payment_Mode       VARCHAR(50)     NOT NULL,
    Created_At         TIMESTAMP       DEFAULT CURRENT_TIMESTAMP,
    
    -- Primary & Functional Indexes for Optimized Analytical Querying
    PRIMARY KEY (Order_ID),
    INDEX idx_order_date (Order_Date),
    INDEX idx_customer_id (Customer_ID),
    INDEX idx_product_id (Product_ID),
    INDEX idx_category (Product_Category),
    INDEX idx_region (Region),
    INDEX idx_customer_type (Customer_Type)
) ENGINE=InnoDB;

-- ==============================================================================
-- 4. Analytical Views for Business Intelligence & Power BI DirectQuery
-- ==============================================================================

-- View 1: Monthly Sales & Profit Performance
CREATE OR REPLACE VIEW monthly_sales AS
SELECT 
    DATE_FORMAT(Order_Date, '%Y-%m') AS Year_Month,
    YEAR(Order_Date) AS Sales_Year,
    MONTH(Order_Date) AS Sales_Month,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Quantity) AS Total_Units_Sold,
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct,
    ROUND(AVG(Sales), 2) AS Avg_Order_Value
FROM sales
GROUP BY 
    DATE_FORMAT(Order_Date, '%Y-%m'),
    YEAR(Order_Date),
    MONTH(Order_Date);

-- View 2: Regional Performance Summary
CREATE OR REPLACE VIEW regional_performance AS
SELECT 
    Region,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    COUNT(DISTINCT Customer_ID) AS Unique_Customers,
    SUM(Quantity) AS Total_Units_Sold,
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct,
    ROUND(AVG(Discount) * 100, 2) AS Avg_Discount_Pct
FROM sales
GROUP BY Region;

-- View 3: Product Category & SKU Performance
CREATE OR REPLACE VIEW product_performance AS
SELECT 
    Product_ID,
    Product_Category,
    COUNT(Order_ID) AS Times_Ordered,
    SUM(Quantity) AS Total_Quantity_Sold,
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct,
    ROUND(AVG(Discount) * 100, 2) AS Avg_Discount_Pct
FROM sales
GROUP BY Product_ID, Product_Category;

-- View 4: Customer Lifetime Summary & RFM Precursors
CREATE OR REPLACE VIEW customer_summary AS
SELECT 
    Customer_ID,
    MAX(Customer_Type) AS Customer_Type,
    MAX(Region) AS Primary_Region,
    COUNT(DISTINCT Order_ID) AS Lifetime_Orders,
    SUM(Quantity) AS Total_Items_Purchased,
    ROUND(SUM(Sales), 2) AS Lifetime_Spend,
    ROUND(SUM(Profit), 2) AS Lifetime_Profit,
    ROUND(AVG(Sales), 2) AS Avg_Order_Value,
    ROUND(AVG(Discount) * 100, 2) AS Avg_Discount_Received,
    MIN(Order_Date) AS First_Purchase_Date,
    MAX(Order_Date) AS Last_Purchase_Date,
    DATEDIFF('2024-12-31', MAX(Order_Date)) AS Days_Since_Last_Purchase
FROM sales
GROUP BY Customer_ID;
