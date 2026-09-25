# Data Quality & Cleaning Audit Report

**Project:** AI-Powered Sales & Customer Analytics System  
**Pipeline:** Stage 2 Data Ingestion & Sanitization  
**Status:** Completed & Validated  

---

## 1. Executive Summary

This report documents the automated data-cleaning protocol executed on the raw sales transaction dataset (`raw_sales_data.csv`). Real-world operational data invariably suffers from duplicate transmissions, human data-entry typos, missing attributes, and measurement outliers. 

The objective of this stage was to enforce strict referential, numeric, and business integrity without discarding valid variance.

| Metric | Raw Dataset | Cleaned Dataset | Variance / Delta |
| :--- | :--- | :--- | :--- |
| **Total Rows** | 5,545 | 5,486 | -59 (-1.06%) |
| **Duplicate Rows** | 45 | 0 | 100% Resolved |
| **Missing Values** | 60 | 0 | 100% Imputed / Resolved |
| **Invalid Quantities (<=0)** | 12 | 0 | Filtered out |
| **Severe Data Entry Outliers** | 2 | 0 | Filtered out |
| **Total Net Sales** | -- | $2,961,669.95 | Verified |
| **Total Net Profit** | -- | $423,672.35 | Verified |
| **Overall Profit Margin** | -- | 14.31% | Healthy Baseline |

---

## 2. Detailed Audit & Remediation Actions

### A. Duplicate Row Detection & Handling
- **Observed:** `45` exact duplicate records were identified across all 12 attribute columns.
- **Root Cause:** Typical of network retry mechanisms or multi-node database replication sync delays.
- **Action Taken:** Executed `drop_duplicates(keep='first')`. No valid customer transactional intent was lost.

### B. Missing Value Imputation
Real-world systems cannot afford to blindly drop rows with single missing categorical attributes. Instead, domain-grounded business rules were applied:

| Field Name | Missing Count | Imputation Strategy | Business Rationale |
| :--- | :--- | :--- | :--- |
| `Discount` | 15 | Imputed `0.0` | In commercial e-commerce, absence of a discount tag signifies standard full-price transaction. |
| `Payment_Mode` | 15 | Mode Imputation | Imputed dominant transactional mode (`Credit Card`) to retain transactional value. |
| `Customer_Type` | 15 | Mode Imputation | Populated with modal category (`Consumer`) reflecting 50%+ customer demographic. |
| `Region` | 15 | Customer-Lookup + Mode | Mapped from existing customer order history; fallback to mode for new customers. |

### C. Quantity Validation
- **Observed:** `12` records had non-positive values (`<= 0`, e.g., -2, -1, 0).
- **Business Rationale:** An e-commerce purchase line item cannot ship non-positive physical units without an associated return transaction ticket (which requires separate schema tracking).
- **Action Taken:** Filtered out invalid non-positive quantity records to prevent negative gross bias in Average Order Value (AOV).

### D. Date Standardization
- **Observed:** Inconsistent temporal formatting (mix of ISO `YYYY-MM-DD` and European `DD/MM/YYYY`).
- **Action Taken:** Parsed using mixed datetime parsing and converted into uniform standard ISO `YYYY-MM-DD` string format, ready for direct MySQL `DATE` ingestion.

### E. Extreme Outlier Audit
- **Methodology:** Applied Interquartile Range (IQR) analysis combined with domain constraint validation (Catalog ceiling: max catalog price = $1,200, max order quantity = 10 -> upper theoretical threshold < $15,000).
- **Observed:** `2` transactions exhibited anomalous sales values (e.g. 25x inflated typos exceeding $20,000 on single items).
- **Action Taken:** Removed isolated data-entry typos to prevent skewing linear regression weights and machine learning variance.

---

## 3. Post-Cleaning Data Health Checklist

- [x] Primary Key / Order IDs conform to schema standards
- [x] Zero null or NaN values in critical analytical columns
- [x] Quantities are strictly positive integers ($Q \ge 1$)
- [x] Discounts are bounded within $[0.0, 1.0]$
- [x] Dates are monotonic and formatted consistently
- [x] Financial consistency verified ($Sales \ge 0$)

---

## 4. How to Explain This in an Interview

> *"In this project, rather than simply dropping missing rows—which distorts sample distribution—I implemented a data audit protocol. I handled exact duplicates caused by system retry lags, mapped missing regional data back to customer historical profiles, treated missing discounts as standard zero-discount transactions, and used domain-bounded IQR fencing to eliminate artificial typos while preserving legitimate high-value purchases."*
