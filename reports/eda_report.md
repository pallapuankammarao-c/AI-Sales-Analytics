# Exploratory Data Analysis (EDA) Report

**Project:** AI-Powered Sales & Customer Analytics System  
**Dataset:** Cleaned Sales Transactions (`clean_sales_data.csv`)  
**Scope:** 24 Months Operational Performance (2023 - 2024)  

---

## 1. Executive Commercial Scorecard

| Key Performance Indicator (KPI) | Calculated Value | Business Interpretation |
| :--- | :--- | :--- |
| **Gross Revenue** | **$2,961,669.95** | Total transactional revenue across all 5 territories. |
| **Net Operating Profit** | **$423,672.35** | Total profit after cost-of-goods-sold and promotional deductions. |
| **Operating Profit Margin** | **14.31%** | Commercial return on sales; benchmark healthy retail margin is 12-16%. |
| **Total Orders Fulfilled** | **5,486** | Total verified client purchase orders. |
| **Physical Units Sold** | **12,219** | Cumulative unit volume moved through distribution. |
| **Average Order Value (AOV)** | **$539.86** | Average monetary gross realized per individual checkout. |
| **Average Promotional Discount** | **9.74%** | Portfolio-wide discount concession rate. |
| **Active Customer Base** | **642** | Unique buying accounts identified over 2-year lifecycle. |

---

## 2. Temporal & Trend Dynamics

### Monthly Revenue & Profit Patterns
- **Seasonal Acceleration:** Transaction volume experiences a pronounced spike in **Q4 (October through December)** each year, corresponding to holiday promotional cycles and annual enterprise budget clearance.
- **Mid-Year Lulls:** A consistent moderation occurs during **May through July**, indicating seasonality that requires targeted mid-year marketing campaigns.
- **Profit Tracking:** Profit closely tracks revenue trajectories, confirming that core gross margins remain resilient during peak volume periods.

*(Reference visual: `reports/charts/monthly_sales_trend.png` and `reports/charts/monthly_profit_trend.png`)*

---

## 3. Geographic Performance Breakdown

| Region | Sales Revenue | Net Profit | Profit Margin |
| :--- | :--- | :--- | :--- |
| **North** | $885,892.95 | $121,270.95 | 13.69% |
| **East** | $666,463.90 | $99,733.90 | 14.96% |
| **South** | $536,556.60 | $75,266.00 | 14.03% |
| **West** | $525,522.85 | $75,324.85 | 14.33% |
| **Central** | $347,233.65 | $52,076.65 | 15.00% |

### Key Regional Observations:
1. **North Region** dominates overall top-line volume and profitability, driven by strong enterprise and consumer penetration.
2. **South Region** exhibits lower margin realization and experienced softening demand in late 2024, warranting targeted root-cause analysis (see Stage 5 & 8).
3. **Central Region** maintains high operating efficiency despite smaller territory footprint.

*(Reference visual: `reports/charts/sales_by_region.png` and `reports/charts/profit_by_region.png`)*

---

## 4. Product Category Performance

| Product Category | Sales Revenue | Net Profit | Profit Margin |
| :--- | :--- | :--- | :--- |
| **Furniture** | $1,110,094.00 | $-27,331.00 | -2.46% |
| **Office Supplies** | $110,774.70 | $43,326.10 | 39.11% |
| **Technology** | $1,740,801.25 | $407,677.25 | 23.42% |

### Category Dynamics:
- **Technology** generates the largest revenue slice and strong dollar profit, anchored by high unit price items (Laptops, Monitors, Phones).
- **Office Supplies** provides high-frequency recurring volume with predictable positive margins and minimal discount sensitivity.
- **Furniture** exhibits significantly narrower margins. High logistical overhead and frequent discounting above 25% directly erode net margin contribution.

*(Reference visual: `reports/charts/sales_by_category.png` and `reports/charts/top_10_products.png`)*

---

## 5. Discount Impact & Margin Erosion Analysis

A critical discovery of this EDA is the non-linear relationship between promotional discounts and net operating profit:

| Discount Tier | Order Volume | Avg Profit per Order | Total Profit Contribution |
| :--- | :--- | :--- | :--- |
| **0-5%** | 3,055 | $134.29 | $410,264.65 |
| **6-15%** | 1,103 | $91.76 | $101,211.00 |
| **16-25%** | 743 | $-8.21 | $-6,103.50 |
| **26-35%** | 329 | $-87.86 | $-28,905.80 |
| **>35%** | 256 | $-206.23 | $-52,794.00 |

### Crucial Strategic Finding:
> **The 25% Threshold:** When promotional discounts exceed **25%**, the average profit per order plunges, turning **negative** in higher brackets (>35%). High discounting on low-margin products (e.g. Furniture tables and bookcases) fails to generate sufficient incremental volume to compensate for lost margin dollars.

*(Reference visual: `reports/charts/discount_vs_profit.png`)*

---

## 6. Customer Spending & Distribution Profile

- **Median Customer Spend:** $2,969.90
- **Mean Customer Spend:** $4,613.19
- **Distribution Skewness:** Positive right-skewed distribution characteristic of retail sales, where a top tier of high-value accounts drives a disproportionate percentage of gross margin (Pareto principle: ~20% driving ~55% of profit).

*(Reference visual: `reports/charts/customer_spending_distribution.png`)*

---

## 7. How to Explain These Findings in an Interview

> *"During my Exploratory Data Analysis, I looked beyond aggregate revenue to understand margin drivers. While total revenue exceeded $2.9M, I discovered that promotional discounting above 25% was systematically eroding net margins—particularly in Furniture, where products like Tables were frequently sold at a net operating loss. This directly informed the business rules and customer risk segmentation in subsequent stages."*
