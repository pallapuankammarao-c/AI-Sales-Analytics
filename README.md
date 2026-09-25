# AI-Powered Sales & Customer Analytics System

A production-grade, end-to-end Data Analytics, Machine Learning, and Generative AI portfolio project built for commercial retail intelligence.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3+-150458.svg)](https://pandas.pydata.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1.svg)](https://www.mysql.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.7+-F7931E.svg)](https://scikit-learn.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-Desktop-F2C811.svg)](https://powerbi.microsoft.com/)
[![Generative AI](https://img.shields.io/badge/GenAI-Grounded_Analytics-9cf.svg)](ai/ai_insights.py)
[![Tests](https://img.shields.io/badge/Automated_Tests-100%25_Passing-brightgreen.svg)](tests/test_project_validation.py)

---

## 1. Project Overview

In commercial retail and e-commerce, organizations generate millions of transactional rows but often struggle to translate raw logs into actionable profit growth. High gross revenues frequently mask hidden margin destruction—such as uncontrolled promotional discounts, regional demand softening, and quiet churn among high-value accounts.

The **AI-Powered Sales & Customer Analytics System** is a complete, enterprise-caliber analytics pipeline that transforms over 5,500 raw transactions into structured commercial intelligence. The system automates data sanitization, executes relational SQL analytics, uncovers non-linear margin loss, forecasts daily demand via Machine Learning, and leverages Generative AI with strict anti-hallucination guardrails to brief executives on strategic actions.

---

## 2. Business Problem

1. **Top-Line Illusion vs. Bottom-Line Reality:** While total sales turnover reached nearly $3.0M, overall net operating margin was constrained to 14.31% due to massive profit erosion in specific categories (notably Furniture at -2.46%).
2. **Promotional Margin Destruction:** Discretionary discounting lacked automated guardrails; discounts exceeding 25% led to a 100% loss rate on orders.
3. **Territory Contraction:** The South sales territory suffered an unmonitored 19.5% sales drop in late 2024, heavily concentrated in high-ticket Technology hardware (-41.8%).
4. **Customer Dormancy Exposure:** 41 formerly high-value customer accounts ceased purchasing for >120 days, putting over $188,000 in historical spend at risk of defection without CRM detection.

---

## 3. Project Objectives

- **Data Ingestion & Cleaning:** Clean and validate raw operational data (deduplication, business-rule imputation, outlier filtering).
- **Relational SQL Database:** Structure production tables, functional indexes, and analytical views in MySQL.
- **Exploratory Data Analysis (EDA):** Identify revenue, profit, and seasonal patterns using publication-ready visualizations.
- **Automated Business Diagnostics:** Automatically calculate evidence-grounded problems across regions, products, and discounts.
- **Customer Portfolio Analytics:** Build an RFM feature store and categorize accounts into actionable risk segments.
- **Predictive Demand Modeling:** Build a leak-free Random Forest time-series regression model predicting daily sales turnover.
- **Grounded Generative AI:** Feed structured JSON metrics into an LLM engine separating calculated FACT from speculative HYPOTHESIS.
- **Business Intelligence Reporting:** Architect a 4-page Power BI dashboard design with executive KPIs and actionable drill-throughs.
- **Automated Validation:** Enforce 100% test coverage across data invariants, calculations, and model deserialization.

---

## 4. Technologies Used

| Domain | Technology | Purpose in Project |
| :--- | :--- | :--- |
| **Data Processing** | Python 3.10+, Pandas, NumPy | Automated data cleaning, feature engineering, and statistical aggregations |
| **Relational Database** | SQL, MySQL 8.0+, SQLite (in-memory test engine) | Production DDL schemas, indexing, CTEs, Window functions (`LAG`), analytical views |
| **Data Visualization** | Matplotlib | Generating 10 high-resolution (300 DPI) publication-grade charts |
| **Business Intelligence** | Power BI Desktop, DAX | Dimensional modeling (Star Schema), 4-page executive dashboard design |
| **Machine Learning** | Scikit-learn, Joblib | Time-series feature engineering, Random Forest Regressor, baseline evaluation |
| **Generative AI** | Python, Google Gemini / OpenAI API, python-dotenv | Ground-truth telemetry extraction, structured prompt guardrails, fallback synthesis |
| **Testing & Quality** | Python `unittest` / Assertion Suite | Automated invariant validation, financial reconciliation, schema auditing |
| **Version Control** | Git, GitHub | Source code tracking, `.gitignore` credential protection, open-source licensing |

---

## 5. End-to-End System Architecture

```
                       ┌───────────────────────────────┐
                       │     Raw Sales Data (CSV)      │
                       │     (5,500+ Transactions)     │
                       └───────────────┬───────────────┘
                                       │
                                       ▼
                       ┌───────────────────────────────┐
                       │    Python Data Cleaning       │
                       │   (Deduplication, Impute,     │
                       │    IQR Outlier Filtering)     │
                       └───────────────┬───────────────┘
                                       │
                     ┌─────────────────┴─────────────────┐
                     ▼                                   ▼
      ┌───────────────────────────────┐   ┌───────────────────────────────┐
      │      Clean CSV Dataset        │   │    MySQL Relational DB        │
      │   (data/clean_sales_data.csv) │   │ (ai_sales_analytics, 4 Views) │
      └──────────────┬────────────────┘   └───────────────┬───────────────┘
                     │                                    │
                     ├─────────────────┬──────────────────┤
                     ▼                 ▼                  ▼
      ┌─────────────────────────┐ ┌───────────────┐ ┌───────────────────┐
      │   Exploratory Analysis  │ │ Customer RFM  │ │ Automated Problem │
      │   (KPIs & 8 Matplotlib  │ │ Analytics &   │ │ Diagnostic Engine │
      │          Charts)        │ │ Segmentation  │ │ (business_        │
      │                         │ │ (feature store│ │  analysis.py)     │
      └──────────────┬──────────┘ └───────┬───────┘ └─────────┬─────────┘
                     │                    │                   │
                     ▼                    ▼                   ▼
      ┌─────────────────────────┐ ┌───────────────┐ ┌───────────────────┐
      │   Demand Forecasting    │ │ Customer Risk │ │ Grounded GenAI    │
      │     (Random Forest      │ │ Analysis      │ │ Insights Engine   │
      │    Scikit-learn Model)  │ │ (41 At-Risk)  │ │ (FACT vs ACTION)  │
      └──────────────┬──────────┘ └───────┬───────┘ └─────────┬─────────┘
                     │                    │                   │
                     └────────────────────┼───────────────────┘
                                          ▼
                       ┌─────────────────────────────────────┐
                       │   Power BI 4-Page BI Dashboard      │
                       │ (Executive, Product, Customer, AI)  │
                       └──────────────────┬──────────────────┘
                                          ▼
                       ┌─────────────────────────────────────┐
                       │ Commercial Business Recommendations │
                       └─────────────────────────────────────┘
```

---

## 6. Dataset Structure

- **Raw Dataset:** `data/raw_sales_data.csv` (5,545 records)
- **Clean Dataset:** `data/clean_sales_data.csv` (5,486 records)

| Field Name | Type | Description |
| :--- | :--- | :--- |
| `Order_ID` | String | Unique purchase order identifier (`ORD-YYYY-XXXXX`) |
| `Order_Date` | Date | Order placement date in strict ISO `YYYY-MM-DD` |
| `Customer_ID` | String | Unique customer account key (`CUST-XXXX`) |
| `Product_ID` | String | Unique SKU identifier (e.g. `TEC-LP-1002`, `FUR-TB-2002`) |
| `Product_Category` | String | Department: `Technology`, `Furniture`, `Office Supplies` |
| `Quantity` | Integer | Units ordered ($Q \ge 1$) |
| `Sales` | Decimal | Net revenue realized after discount ($) |
| `Discount` | Decimal | Promotional discount percentage ($0.00$ to $1.00$) |
| `Profit` | Decimal | Net margin realized ($Sales - Cost$) ($) |
| `Region` | String | Sales territory: `North`, `South`, `East`, `West`, `Central` |
| `Customer_Type` | String | Segment: `Consumer`, `Corporate`, `Small Business` |
| `Payment_Mode` | String | Method: `Credit Card`, `Debit Card`, `UPI`, `Net Banking`, `Cash on Delivery` |

---

## 7. Data Cleaning Pipeline

Executed via `python/data_cleaning.py`, producing `reports/data_quality_report.md`:

1. **Deduplication:** Identified and eliminated 45 exact duplicate transmissions.
2. **Missing Value Imputation:**
   - `Discount`: Missing values assigned `0.0` (standard retail assumption: no discount tag = full price).
   - `Payment_Mode` & `Customer_Type`: Imputed modal categories (`Credit Card` and `Consumer`).
   - `Region`: Imputed via existing customer historical profile; fallback to regional mode.
3. **Quantity Sanitization:** Filtered out 12 records containing non-positive quantities ($\le 0$).
4. **Date Harmonization:** Parsed mixed format date strings (`DD/MM/YYYY` and `YYYY-MM-DD`) into uniform ISO `YYYY-MM-DD`.
5. **Outlier Mitigation:** Detected 2 extreme typo records ($> \$20,000$ on single items) using IQR fencing and catalog price constraints.
6. **Data Retention:** Retained **5,486 validated rows (98.94% data retention)**.

---

## 8. Relational SQL Analysis

Stored in `sql/database.sql` and `sql/sales_analysis.sql`:

- **Production DDL Table:** Fully constrained `sales` table with functional indexes on `Order_Date`, `Customer_ID`, `Product_ID`, and `Region`.
- **4 Relational Views:**
  - `monthly_sales`: Aggregated monthly revenue, profit, units, and margin percentage.
  - `regional_performance`: Territory breakdown of sales, profit, unique accounts, and discount rates.
  - `product_performance`: SKU level velocity, total sales, and profit margin.
  - `customer_summary`: RFM precursors including lifetime spend, order count, and recency.
- **20 Analytical SQL Queries:** Total revenue, profit, AOV, monthly trends, regional share, top/bottom SKUs, customer spending tiers (CTEs), new vs repeat cohorts, discount impact, dormant accounts, and Month-over-Month growth using window functions (`LAG() OVER ()`).

---

## 9. Exploratory Data Analysis (EDA) Highlights

Executed via `python/eda.py`, generating `reports/eda_report.md` and 8 charts in `reports/charts/`:

- **Gross Revenue:** **$2,961,669.95** across 5,486 orders.
- **Net Operating Profit:** **$423,672.35** with a healthy baseline margin of **14.31%**.
- **Average Order Value (AOV):** **$539.86**; Total Units Sold: **12,219 units**.
- **Seasonality:** Strong annual acceleration in **Q4 (October – December)**; consistent mid-year slowdown in May–July.
- **Discount Non-Linearity:** Discounts under 15% deliver average profits of **+$84 to +$112 per order**. Discounts $\ge 25\%$ produce **negative average profit**, with orders $>35\%$ discount suffering an average operating loss of **-$48.30 per order**.

---

## 10. Quantified Business Problems Identified

Automated via `python/business_analysis.py` (`reports/business_findings.md`):

1. **South Territory Contraction:** Sales decreased by **19.5%** in H2 2024 vs H2 2023 (-$40,423.70 delta), driven by a severe **41.8% drop in Technology hardware**.
2. **Furniture Category Margin Loss:** Furniture operated at an overall margin of **-2.46%** (generating a net loss of -$27,331.00), contrasted with Technology (23.4%) and Office Supplies (39.1%).
3. **Unprofitable Discount Threshold:** 100% of orders with discounts $\ge 25\%$ operated at an outright financial loss due to thin gross wholesale margins.
4. **Customer Attrition Exposure:** 41 formerly high-value accounts have gone inactive for $>120$ days, placing **$188,689.85** in historical spend at risk.
5. **Loss-Leader SKU:** SKU `FUR-TB-2002 (Conference Tables)` generates massive revenue ($213k+) but operates at negative margins due to high unit cost and excessive discounting.
6. **Post-Holiday Demand Cliff:** Sales drop by over 45% between peak December holiday volume and January.

---

## 11. Customer Portfolio & Risk Analytics

Executed via `python/customer_analysis.py` (`data/customer_features.csv`):

Features engineered per account: `Total_Orders`, `Total_Spending`, `Average_Order_Value`, `Days_Since_Last_Purchase`, `Purchase_Frequency`, `Average_Discount`, `Total_Profit`.

| Segment | Account Count | Total Revenue | Revenue Share | Avg Spend / Account | Avg Recency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **High Value (VIP)** | 156 | $1,759,198.80 | **59.40%** | $11,276.92 | 18 days |
| **Regular** | 342 | $906,009.60 | **30.59%** | $2,649.15 | 37 days |
| **At Risk (>120d Inactive)** | 41 | $188,689.85 | **6.37%** | $4,602.19 | 216 days |
| **Dormant / Low Engagement** | 97 | $107,262.80 | **3.63%** | $1,105.80 | 280 days |
| **New Accounts** | 6 | $508.90 | **0.02%** | $84.82 | 24 days |

---

## 12. Machine Learning Demand Forecasting

Executed via `python/sales_prediction.py` (`reports/ml_report.md`):

- **Target:** Daily Sales Revenue ($).
- **Leak-Free Temporal Split:** Trained on first 20 months (595 days); tested out-of-time on final 4 months (122 holdout days from Sept to Dec 2024).
- **Architecture:** Random Forest Regressor (150 estimators, max depth 7).

| Model Architecture | Test MAE ($) | Test RMSE ($) | Test R² Score | Evaluation Note |
| :--- | :--- | :--- | :--- | :--- |
| **Naive 7-Day Persistence** | $3,480.66 | $5,335.03 | -0.128 | Simple weekly persistence |
| **Linear Regression** | $3,005.65 | $4,259.62 | 0.281 | Linear parametric benchmark |
| **Random Forest Regressor** | **$3,113.27** | **$4,058.42** | **0.347** | **Best non-linear holdout fit** |

- **Top Predictor:** `Sales_Rolling_7_Mean` accounted for over 38% of relative Gini importance.
- **Model Artifact:** Serialized to `models/sales_prediction_model.pkl` (984 KB).

---

## 13. Grounded Generative AI Engine

Executed via `ai/ai_insights.py` (`reports/ai_business_insights.md`):

- **Architecture:** Anti-Hallucination Triad. Python calculates 100% of mathematical telemetry before feeding JSON payloads to the LLM.
- **Epistemic Triad Schema:**
  - `FACT:` Verified mathematical truth computed from transactional logs.
  - `POSSIBLE EXPLANATION:` AI commercial hypotheses requiring operational verification.
  - `SUGGESTED BUSINESS ACTION:` Actionable strategic interventions.
- **Reproducibility:** Equipped with zero-dependency deterministic synthesis fallback if no API key is configured.

---

## 14. Power BI Dashboard Architecture

Documented in `powerbi/README.md` and `powerbi/dashboard_design.md`:

- **Page 1: Executive Dashboard:** Core KPI ribbon, monthly sales/profit dual-axis trend, regional matrix heatmap, category revenue.
- **Page 2: Product & Pricing Analysis:** Top 10 revenue SKUs, bottom 10 profit SKUs, discount sensitivity curve illustrating the 25% profit drop-off.
- **Page 3: Customer Risk & Value Analytics:** RFM segment donut, recency vs lifetime spend scatter plot with 120-day inactivity threshold, prioritized customer win-back list.
- **Page 4: AI Strategic Business Briefing:** Grounded diagnostic briefing cards presenting facts, hypotheses, and suggested actions.

---

## 15. Key Commercial Recommendations

1. **Implement Automated 20% Discount Ceiling:** Hard-code rules in the e-commerce checkout blocking discounts $>20\%$ on Furniture without managerial approval.
2. **Re-align Sales Incentives:** Change sales rep commission compensation from Gross Revenue to Gross Margin contribution.
3. **Launch Day-90 Win-Back Workflows:** Trigger automated CRM replenishment reminders at 90 days of inactivity before accounts migrate into the $>120$ day At-Risk bracket.
4. **MSRP Adjustment on SKU `FUR-TB-2002`:** Increase list price from $450 to $495 to restore baseline wholesale margin buffer.
5. **South Territory Hardware Push:** Deploy regional B2B trade-in programs in Southern metro centers to reverse the 41.8% Technology contraction.

---

## 16. Project Limitations

1. **Synthetic Dataset Grounding:** The data was synthetically modeled to exhibit realistic retail dynamics without exposing private customer PII.
2. **Forecast Horizon:** The Random Forest demand model is calibrated for short-term operational replenishment (1-7 days); long-range quarterly forecasts require external macroeconomic indicators.
3. **Non-Contractual Churn:** In retail e-commerce, customers do not explicitly cancel subscriptions; our framework measures **Behavioral Dormancy Risk** rather than guaranteed defection.

---

## 17. How to Run the Project

### Step 1: Clone Repository & Create Virtual Environment
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI_Data_Analyst_Agent

# Create and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Complete Analytical Pipeline
```bash
# 1. Regenerate raw synthetic dataset (5,500+ records)
python python/generate_dataset.py

# 2. Execute automated data cleaning & quality audit
python python/data_cleaning.py

# 3. Run Exploratory Data Analysis & generate 8 charts
python python/eda.py

# 4. Run automated business problem detection engine
python python/business_analysis.py

# 5. Compute customer RFM features & segmentation
python python/customer_analysis.py

# 6. Train Machine Learning sales demand forecasting model
python python/sales_prediction.py

# 7. Generate grounded AI strategic business insights
python ai/ai_insights.py

# 8. Run automated end-to-end project validation test suite
python tests/test_project_validation.py
```

---

## 18. Future Improvements

1. **Airflow / Prefect Orchestration:** Schedule automated daily ingestion, cleaning, and model re-training DAGs.
2. **Real-Time Stream Ingestion:** Ingest order events in real time using Apache Kafka.
3. **Advanced Customer Lifetime Value (CLV):** Implement BG/NBD and Gamma-Gamma probabilistic models for transaction prediction.
4. **Live Power BI Embedded Portal:** Host the interactive dashboard in a secure web application container.

---

## 19. Author & Portfolio Contact

- **Candidate:** Fresher Data Analyst & Analytics Engineer
- **Project Repository:** [AI-Powered Sales & Customer Analytics System](https://github.com/YOUR_USERNAME/AI-Sales-Analytics)
- **Comprehensive Interview Cheat Sheet:** See [`INTERVIEW_GUIDE.md`](INTERVIEW_GUIDE.md) for 60-second pitches, architectural rationales, and 20 interviewer Q&A.
