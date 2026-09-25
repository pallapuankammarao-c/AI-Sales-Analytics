-- ==============================================================================
-- AI-Powered Sales & Customer Analytics System
-- Production Analytical SQL Queries
-- Target Database: ai_sales_analytics
-- Target Table: sales
-- ==============================================================================

USE ai_sales_analytics;

-- ------------------------------------------------------------------------------
-- 1. TOTAL REVENUE
-- Business Context: Measures top-line financial turnover across all territories.
-- ------------------------------------------------------------------------------
SELECT 
    ROUND(SUM(Sales), 2) AS Total_Revenue
FROM sales;

-- ------------------------------------------------------------------------------
-- 2. TOTAL PROFIT
-- Business Context: Net operating financial margin realized after COGS & discounts.
-- ------------------------------------------------------------------------------
SELECT 
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales;

-- ------------------------------------------------------------------------------
-- 3. TOTAL ORDERS
-- Business Context: Total transactional checkout count.
-- ------------------------------------------------------------------------------
SELECT 
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM sales;

-- ------------------------------------------------------------------------------
-- 4. TOTAL QUANTITY
-- Business Context: Cumulative volume of physical goods moved through distribution.
-- ------------------------------------------------------------------------------
SELECT 
    SUM(Quantity) AS Total_Units_Sold
FROM sales;

-- ------------------------------------------------------------------------------
-- 5. AVERAGE ORDER VALUE (AOV)
-- Business Context: Average gross spend per order transaction basket.
-- ------------------------------------------------------------------------------
SELECT 
    ROUND(SUM(Sales) / COUNT(DISTINCT Order_ID), 2) AS Average_Order_Value
FROM sales;

-- ------------------------------------------------------------------------------
-- 6. MONTHLY REVENUE
-- Business Context: Analyzes revenue pace and seasonality month by month.
-- ------------------------------------------------------------------------------
SELECT 
    DATE_FORMAT(Order_Date, '%Y-%m') AS Order_Month,
    ROUND(SUM(Sales), 2) AS Monthly_Revenue
FROM sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Order_Month ASC;

-- ------------------------------------------------------------------------------
-- 7. MONTHLY PROFIT
-- Business Context: Evaluates bottom-line health across operating seasons.
-- ------------------------------------------------------------------------------
SELECT 
    DATE_FORMAT(Order_Date, '%Y-%m') AS Order_Month,
    ROUND(SUM(Profit), 2) AS Monthly_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct
FROM sales
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY Order_Month ASC;

-- ------------------------------------------------------------------------------
-- 8. REVENUE BY REGION
-- Business Context: Identifies geographic commercial market leaders.
-- ------------------------------------------------------------------------------
SELECT 
    Region,
    ROUND(SUM(Sales), 2) AS Regional_Revenue,
    ROUND((SUM(Sales) / (SELECT SUM(Sales) FROM sales)) * 100, 2) AS Revenue_Share_Pct
FROM sales
GROUP BY Region
ORDER BY Regional_Revenue DESC;

-- ------------------------------------------------------------------------------
-- 9. PROFIT BY REGION
-- Business Context: Evaluates net margin conversion across territories.
-- ------------------------------------------------------------------------------
SELECT 
    Region,
    ROUND(SUM(Profit), 2) AS Regional_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct
FROM sales
GROUP BY Region
ORDER BY Regional_Profit DESC;

-- ------------------------------------------------------------------------------
-- 10. TOP 10 PRODUCTS BY REVENUE
-- Business Context: High-velocity flagship items driving core business volume.
-- ------------------------------------------------------------------------------
SELECT 
    Product_ID,
    Product_Category,
    SUM(Quantity) AS Total_Units_Sold,
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Product_ID, Product_Category
ORDER BY Total_Revenue DESC
LIMIT 10;

-- ------------------------------------------------------------------------------
-- 11. BOTTOM 10 PRODUCTS BY PROFIT
-- Business Context: Identifies underperforming SKUs eroding portfolio returns.
-- ------------------------------------------------------------------------------
SELECT 
    Product_ID,
    Product_Category,
    SUM(Quantity) AS Total_Units_Sold,
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct
FROM sales
GROUP BY Product_ID, Product_Category
ORDER BY Total_Profit ASC
LIMIT 10;

-- ------------------------------------------------------------------------------
-- 12. CATEGORY PERFORMANCE
-- Business Context: High-level macro view of product families and their returns.
-- ------------------------------------------------------------------------------
SELECT 
    Product_Category,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Quantity) AS Total_Units_Sold,
    ROUND(SUM(Sales), 2) AS Category_Revenue,
    ROUND(SUM(Profit), 2) AS Category_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct,
    ROUND(AVG(Discount) * 100, 2) AS Avg_Discount_Pct
FROM sales
GROUP BY Product_Category
ORDER BY Category_Revenue DESC;

-- ------------------------------------------------------------------------------
-- 13. TOP CUSTOMERS (HIGH VALUE ACCOUNTS)
-- Business Context: Key enterprise and consumer VIPs who contribute top revenue.
-- ------------------------------------------------------------------------------
SELECT 
    Customer_ID,
    Customer_Type,
    Region,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Spend,
    ROUND(SUM(Profit), 2) AS Total_Profit_Contributed
FROM sales
GROUP BY Customer_ID, Customer_Type, Region
ORDER BY Total_Spend DESC
LIMIT 15;

-- ------------------------------------------------------------------------------
-- 14. CUSTOMER SPENDING TIERS
-- Business Context: Segmenting accounts by lifetime gross order revenue brackets.
-- ------------------------------------------------------------------------------
WITH CustomerSpend AS (
    SELECT 
        Customer_ID,
        SUM(Sales) AS Total_Spend
    FROM sales
    GROUP BY Customer_ID
)
SELECT 
    CASE 
        WHEN Total_Spend >= 10000 THEN 'Tier 1 ($10,000+)'
        WHEN Total_Spend >= 5000  THEN 'Tier 2 ($5,000 - $9,999)'
        WHEN Total_Spend >= 2000  THEN 'Tier 3 ($2,000 - $4,999)'
        ELSE 'Tier 4 (< $2,000)'
    END AS Spend_Tier,
    COUNT(Customer_ID) AS Customer_Count,
    ROUND(SUM(Total_Spend), 2) AS Tier_Revenue,
    ROUND(AVG(Total_Spend), 2) AS Avg_Spend_Per_Customer
FROM CustomerSpend
GROUP BY Spend_Tier
ORDER BY Tier_Revenue DESC;

-- ------------------------------------------------------------------------------
-- 15. NEW VS RETURNING CUSTOMERS
-- Business Context: Cohort segmentation evaluating customer retention dynamics.
-- ------------------------------------------------------------------------------
WITH CustomerFirstOrder AS (
    SELECT 
        Customer_ID,
        MIN(Order_Date) AS First_Order_Date
    FROM sales
    GROUP BY Customer_ID
),
OrderClassification AS (
    SELECT 
        s.Order_ID,
        s.Customer_ID,
        s.Sales,
        s.Profit,
        CASE 
            WHEN s.Order_Date = cfo.First_Order_Date THEN 'First-Time Purchase'
            ELSE 'Repeat Purchase'
        END AS Purchase_Type
    FROM sales s
    JOIN CustomerFirstOrder cfo ON s.Customer_ID = cfo.Customer_ID
)
SELECT 
    Purchase_Type,
    COUNT(DISTINCT Order_ID) AS Order_Count,
    ROUND(SUM(Sales), 2) AS Revenue_Generated,
    ROUND(SUM(Profit), 2) AS Profit_Generated,
    ROUND((SUM(Sales) / (SELECT SUM(Sales) FROM sales)) * 100, 2) AS Revenue_Share_Pct
FROM OrderClassification
GROUP BY Purchase_Type;

-- ------------------------------------------------------------------------------
-- 16. AVERAGE DISCOUNT BY CATEGORY
-- Business Context: Audits commercial price concessions across departments.
-- ------------------------------------------------------------------------------
SELECT 
    Product_Category,
    ROUND(AVG(Discount) * 100, 2) AS Avg_Discount_Pct,
    ROUND(MAX(Discount) * 100, 2) AS Max_Discount_Offered,
    COUNT(CASE WHEN Discount > 0.20 THEN 1 END) AS High_Discount_Order_Count
FROM sales
GROUP BY Product_Category
ORDER BY Avg_Discount_Pct DESC;

-- ------------------------------------------------------------------------------
-- 17. HIGH-SALES / LOW-PROFIT PRODUCTS (MARGIN DRAINERS)
-- Business Context: SKUs that generate significant volume but negligible profit.
-- ------------------------------------------------------------------------------
SELECT 
    Product_ID,
    Product_Category,
    SUM(Quantity) AS Total_Units_Sold,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct
FROM sales
GROUP BY Product_ID, Product_Category
HAVING SUM(Sales) > 50000 AND (SUM(Profit) / SUM(Sales)) < 0.08
ORDER BY Profit_Margin_Pct ASC;

-- ------------------------------------------------------------------------------
-- 18. HIGH-DISCOUNT / LOW-PROFIT PRODUCTS (PROMOTIONAL LEAKAGE)
-- Business Context: Identifies where discounting leads to severe margin erosion.
-- ------------------------------------------------------------------------------
SELECT 
    Product_ID,
    Product_Category,
    ROUND(AVG(Discount) * 100, 2) AS Avg_Discount_Pct,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct
FROM sales
GROUP BY Product_ID, Product_Category
HAVING AVG(Discount) >= 0.15 AND (SUM(Profit) / SUM(Sales)) < 0.10
ORDER BY Total_Profit ASC;

-- ------------------------------------------------------------------------------
-- 19. INACTIVE CUSTOMERS (AT-RISK / DORMANT ACCOUNTS)
-- Business Context: Flags accounts without a purchase in the final 120 days.
-- Benchmark Reference Date: 2024-12-31
-- ------------------------------------------------------------------------------
SELECT 
    Customer_ID,
    Customer_Type,
    Region,
    MAX(Order_Date) AS Last_Purchase_Date,
    DATEDIFF('2024-12-31', MAX(Order_Date)) AS Days_Since_Last_Purchase,
    COUNT(DISTINCT Order_ID) AS Lifetime_Orders,
    ROUND(SUM(Sales), 2) AS Lifetime_Spend
FROM sales
GROUP BY Customer_ID, Customer_Type, Region
HAVING DATEDIFF('2024-12-31', MAX(Order_Date)) > 120
ORDER BY Days_Since_Last_Purchase DESC, Lifetime_Spend DESC
LIMIT 20;

-- ------------------------------------------------------------------------------
-- 20. MONTH-OVER-MONTH (MoM) SALES GROWTH RATE
-- Business Context: Evaluates business velocity and month-on-month acceleration.
-- ------------------------------------------------------------------------------
WITH MonthlyTotals AS (
    SELECT 
        DATE_FORMAT(Order_Date, '%Y-%m') AS Order_Month,
        ROUND(SUM(Sales), 2) AS Current_Month_Sales
    FROM sales
    GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
),
LaggedMonthly AS (
    SELECT 
        Order_Month,
        Current_Month_Sales,
        LAG(Current_Month_Sales, 1) OVER (ORDER BY Order_Month) AS Previous_Month_Sales
    FROM MonthlyTotals
)
SELECT 
    Order_Month,
    Current_Month_Sales,
    Previous_Month_Sales,
    ROUND(Current_Month_Sales - Previous_Month_Sales, 2) AS Absolute_Growth,
    ROUND(((Current_Month_Sales - Previous_Month_Sales) / Previous_Month_Sales) * 100, 2) AS MoM_Growth_Pct
FROM LaggedMonthly
ORDER BY Order_Month ASC;
