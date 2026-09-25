# Customer Portfolio & Risk Analysis Report

**Project:** AI-Powered Sales & Customer Analytics System  
**Feature Store:** `data/customer_features.csv`  
**Total Accounts Audited:** 642 Unique Customers  
**Analysis Cutoff Date:** 2024-12-31  

---

## 1. Executive Summary & Segmentation Overview

Customer analytics is the cornerstone of sustainable commercial growth. In this stage, raw transactional order lines were transformed into a **Customer-Level Feature Store** capturing Recency, Frequency, Monetary Value (RFM), Lifetime Profit, and Average Discount Sensitivity.

Using transparent business criteria, accounts were classified into 5 operational segments:

| Segment | Account Count | Total Revenue | Revenue Share | Avg Spend / Account | Avg Recency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **High Value** | 156 | $1,759,095.95 | 59.4% | $11,276.26 | 18 days |
| **Regular** | 342 | $905,921.90 | 30.6% | $2,648.89 | 37 days |
| **New** | 6 | $508.80 | 0.0% | $84.80 | 24 days |
| **At Risk** | 41 | $188,549.20 | 6.4% | $4,598.76 | 216 days |
| **Dormant / Low Engagement** | 97 | $107,594.10 | 3.6% | $1,109.22 | 280 days |

*(Visual References: `reports/charts/customer_segments.png` and `reports/charts/recency_vs_spending.png`)*

---

## 2. Customer Risk Analysis (Dormancy & Defection Warning)

> **Important Analytical Note:** We deliberately label this framework **Customer Risk Analysis** rather than deterministic churn prediction. In non-contractual e-commerce, customers do not explicitly cancel; prolonged dormancy signals behavioral disengagement that requires immediate retention intervention.

### Quantifying the At-Risk Exposure:
- **At-Risk Accounts:** Accounts with historically proven high spend ($3,500+) or repeated orders (6+ orders) that have gone completely dormant for **over 120 days**.
- **Revenue at Risk:** The At-Risk cohort represents a major slice of cumulative business revenue that has ceased purchasing.
- **Top 5 Priority Accounts Requiring Retention Outreach:**

| Customer ID | Type | Territory | Lifetime Orders | Historical Spend | Days Inactive |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CUST-0149` | Corporate | Central | 3 | $15,789.00 | 212 days |
| `CUST-0062` | Small Business | North | 9 | $13,356.35 | 202 days |
| `CUST-0427` | Consumer | East | 8 | $9,208.50 | 133 days |
| `CUST-0509` | Consumer | North | 8 | $8,866.50 | 366 days |
| `CUST-0008` | Consumer | South | 7 | $8,135.00 | 163 days |

---

## 3. High-Value VIP Cohort Analysis
- **Definition:** Accounts spending $6,000+ with active purchase activity in the past 120 days.
- **Contribution:** This elite tier constitutes a disproportionate percentage of total net operating profit.
- **Strategic Treatment:** Must be protected with dedicated account managers, early-access product drops, and customized enterprise SLA agreements.

---

## 4. Feature Engineering Glossary

The generated feature table (`data/customer_features.csv`) provides 11 analytical attributes:

1. **`Customer_ID`**: Unique primary identifier.
2. **`Total_Orders`**: Lifetime count of distinct transactions.
3. **`Total_Spending`**: Gross lifetime revenue realized.
4. **`Total_Profit`**: Net operating margin contributed.
5. **`Total_Quantity`**: Cumulative physical units purchased.
6. **`Average_Order_Value (AOV)`**: Total Spending divided by Total Orders.
7. **`Days_Since_Last_Purchase`**: Recency in days relative to 2024-12-31.
8. **`Customer_Tenure_Days`**: Elapsed days between first order and reference date.
9. **`Purchase_Frequency`**: Average orders executed per active month.
10. **`Average_Discount`**: Mean promotional discount percentage received.
11. **`Customer_Segment`**: Actionable business classification tag.

---

## 5. Strategic Recommendations

1. **Automated Win-Back Triggers:** Set up automated CRM triggers at Day 90 of dormancy offering an exclusive 10% re-engagement incentive before accounts cross into the critical >120 day At-Risk bracket.
2. **VIP Loyalty Program:** Institute a formal tiers program for the High-Value segment to lock in contract longevity.
3. **Onboarding Sequence for New Buyers:** Accelerate second-order conversion by sending tailored educational content within 21 days of first purchase.

---

## 6. How to Explain This in an Interview

> *"Rather than relying on vague customer descriptions, I built an automated RFM feature engineering pipeline in Pandas. I aggregated over 5,400 transactions into customer-level metrics including recency, frequency, monetary value, and margin contribution. Instead of over-promising a black-box churn model, I designed an explainable Customer Risk Analysis framework that flags dormant high-value accounts at 120 days of inactivity, providing direct outreach lists for the sales team."*
