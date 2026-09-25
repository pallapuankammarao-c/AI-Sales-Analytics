# Power BI 4-Page Dashboard Design & Visual Specifications

**Project:** AI-Powered Sales & Customer Analytics System  
**Canvas Dimensions:** Standard 16:9 (1280 x 720 px or 1920 x 1080 px)  
**Visual Style:** Modern Corporate Minimalist (Clean Card Glassmorphism, Cohesive Palette, High Information Density)  

---

## Global Color Palette & Theming Tokens

| Purpose | Color Hex | Sample Swatch | Description |
| :--- | :--- | :--- | :--- |
| **Primary Brand / Headers** | `#1A2B4C` | Deep Navy | High-contrast visual anchor for titles and banners |
| **Primary Visual Accent** | `#2E5B88` | Steel Blue | Primary bar, column, and line charts |
| **Positive / Healthy Profit** | `#2E7D32` | Emerald Green | Positive KPIs, healthy margins, profitable products |
| **Warning / At Risk** | `#F57C00` | Warm Amber | Moderately dormant accounts, warning thresholds |
| **Danger / Outright Loss** | `#C62828` | Crimson Red | Negative profit bars, high-discount erosion, churn risks |
| **Neutral Background** | `#F4F6F9` | Cloud Gray | Canvas background reducing eye fatigue |
| **Card / Container Fill** | `#FFFFFF` | Pure White | Elevated metric cards with subtle drop shadow |

---

## Global Filter & Slicer Panel (Synchronized Across All Pages)

Place in a collapsible left sidebar or compact horizontal top banner:
1. **Date Range Slicer:** Between slider (Jan 1, 2023 – Dec 31, 2024).
2. **Region Dropdown:** North, South, East, West, Central (Multi-select enabled).
3. **Category Dropdown:** Technology, Furniture, Office Supplies.
4. **Customer Type Dropdown:** Consumer, Corporate, Small Business.

---

## PAGE 1 — EXECUTIVE DASHBOARD (High-Level Commercial Scorecard)

### Objective:
Give C-suite executives and business leaders an immediate 10-second pulse check on enterprise financial performance, revenue trajectory, and territory returns.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ TOP BANNER: AI-Powered Sales & Customer Analytics — Executive Performance Dashboard    │
├──────────────┬──────────────┬──────────────┬──────────────┬─────────────┬──────────────┤
│ TOTAL SALES  │ TOTAL PROFIT │ PROFIT MARGIN│ TOTAL ORDERS │ AVG ORDER   │ UNITS SOLD   │
│ $2,961,670   │ $423,672     │ 14.31%       │ 5,486        │ $539.86     │ 12,219       │
├──────────────┴──────────────┴──────────────┼──────────────┴─────────────┴──────────────┤
│ VISUAL 1: Monthly Sales & Profit Trend     │ VISUAL 2: Regional Performance (Matrix)   │
│ (Dual-Axis Line & Clustered Column Chart)  │ (Revenue, Profit, Margin % with heatmaps) │
│ - Line: Monthly Revenue                    │ - North: $845k / $135k (16.0%)            │
│ - Bar: Monthly Net Profit                  │ - West:  $620k / $98k  (15.8%)            │
│                                            │ - East:  $590k / $89k  (15.1%)            │
│                                            │ - South: $510k / $58k  (11.4%) ◄ Highlight│
│                                            │ - Central: $396k / $44k (11.1%)           │
├────────────────────────────────────────────┼───────────────────────────────────────────┤
│ VISUAL 3: Sales by Product Category        │ VISUAL 4: Payment Mode Breakdown          │
│ (Horizontal Bar Chart with Margin % tags)  │ (Donut Chart with % of Total)             │
│ - Technology:     $1.41M (Margin: 23.4%)   │ - Credit Card (38%)                       │
│ - Furniture:      $1.11M (Margin: -2.5%) ◄ │ - UPI (25%)                               │
│ - Office Supplies:$441k  (Margin: 39.1%)   │ - Debit Card / Net Banking (37%)          │
└────────────────────────────────────────────┴───────────────────────────────────────────┘
```

### Visual Specifications:
1. **Top KPI Ribbon (6 Card Visuals):**
   - Background: White `#FFFFFF`, Border: 1px `#E0E0E0`, Corner Radius: 8px.
   - Values: Bold 24pt `#1A2B4C`, Labels: 10pt `#757575`.
2. **Visual 1 (Line & Stacked Column):**
   - X-Axis: `Dim_Date[YearMonth]`.
   - Column values: `[Total Profit]` (Conditional color: Green if >0, Red if <0).
   - Line values: `[Total Revenue]` (Navy line, 3pt).
3. **Visual 2 (Regional Table / Heatmap Matrix):**
   - Rows: `sales[Region]`.
   - Values: `[Total Revenue]`, `[Total Profit]`, `[Profit Margin %]`.
   - Conditional Formatting: Background color scale on `[Profit Margin %]` (Red to Green).
4. **Visual 3 (Category Bar Chart):**
   - Y-Axis: `sales[Product_Category]`.
   - X-Axis: `[Total Revenue]`. Data labels enabled.

---

## PAGE 2 — PRODUCT & PRICING ANALYSIS (SKU Profitability & Discount Sensitivity)

### Objective:
Empower merchandising and pricing managers to detect margin leakage, identify loss-making products, and calibrate promotional discount policies.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ TOP BANNER: Product Portfolio & Promotional Discount Sensitivity Analysis              │
├────────────────────────────────────────────┬───────────────────────────────────────────┤
│ VISUAL 1: Top 10 SKUs by Revenue           │ VISUAL 2: Bottom 10 SKUs by Net Profit    │
│ (Horizontal Bar Chart)                     │ (Horizontal Bar Chart with Negative Fills)│
│ - TEC-LP-1002 (Laptops):     $680k         │ - FUR-TB-2002 (Tables):    -$14.5k ◄ LOSS │
│ - TEC-PH-1001 (Phones):      $520k         │ - FUR-BK-2003 (Bookcases): -$8.2k  ◄ LOSS │
│ - FUR-SF-2005 (Sofas):       $390k         │ - FUR-DS-2004 (Desks):     -$4.5k  ◄ LOSS │
│ ...                                        │ ...                                       │
├────────────────────────────────────────────┴───────────────────────────────────────────┤
│ VISUAL 3: Discount Tier vs Net Profit Margin (The 25% Threshold)                       │
│ (Clustered Column Chart with Average Profit per Order)                                 │
│ - Tier 0-5%:   Avg Profit = +$112.50 per order (Healthy)                               │
│ - Tier 6-15%:  Avg Profit = +$84.20 per order                                          │
│ - Tier 16-25%: Avg Profit = +$32.10 per order                                          │
│ - Tier >25%:   Avg Profit = -$48.30 per order ◄ NEGATIVE RETURN (Margin Destruction)   │
├────────────────────────────────────────────┬───────────────────────────────────────────┤
│ VISUAL 4: Scatter Plot (Price vs Units)    │ VISUAL 5: SKU Margin Detail Table         │
│ (Bubble chart: Price x Qty x Bubble=Profit)│ (Interactive drill-through table)         │
└────────────────────────────────────────────┴───────────────────────────────────────────┘
```

### Visual Specifications:
1. **Visual 1 & 2 (Top/Bottom Products):**
   - Filters: Top N by `[Total Revenue]` (Top 10) / Bottom N by `[Total Profit]` (Bottom 10).
   - Formatting: Red fill `#C62828` on negative profit bars, Blue fill `#2E5B88` on revenue.
2. **Visual 3 (Discount Sensitivity Columns):**
   - X-Axis: Discount Tier (`0-5%`, `6-15%`, `16-25%`, `>25%`).
   - Y-Axis: `Average Profit per Order ($)`.
   - Reference Line: Dotted Black line at Y = 0.

---

## PAGE 3 — CUSTOMER RISK & VALUE ANALYTICS (RFM Segmentation)

### Objective:
Equip account management and CRM retention teams with clear visibility into high-value VIP accounts and at-risk dormant customers requiring urgent win-back campaigns.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ TOP BANNER: Customer Portfolio Segmentation & Recency Risk Engine                      │
├──────────────────────────┬─────────────────────────────┬───────────────────────────────┤
│ HIGH-VALUE ACCOUNTS (VIP)│ AT-RISK ACCOUNTS (>120 DAYS)│ REVENUE AT RISK               │
│ 156 (59.4% Total Revenue)│ 41 Dormant Accounts         │ $188,690 Historical Spend     │
├──────────────────────────┴──────────────┬──────────────┴───────────────────────────────┤
│ VISUAL 1: Customer Segmentation Donut   │ VISUAL 2: Recency vs Lifetime Spending       │
│ - High Value (156)                      │ (Scatter Plot with 120-Day Inactivity Fence) │
│ - Regular (342)                         │ - X-Axis: Days Since Last Purchase (0-350)   │
│ - Dormant / Low (97)                    │ - Y-Axis: Lifetime Spending ($0 - $14k)      │
│ - At Risk (41)                          │ - Color: Customer Segment                    │
│ - New (6)                               │ - Vertical Constant Line at X = 120 Days     │
├─────────────────────────────────────────┴──────────────────────────────────────────────┤
│ VISUAL 3: Priority Retention Outreach List (At-Risk High-Value Accounts)              │
│ (Table with Customer_ID, Type, Region, Lifetime Spend, Inactivity Days, Action Needed) │
│ - CUST-0104 | Corporate | South | $7,840.50 | 242 Days Inactive | "Schedule Call"     │
│ - CUST-0219 | Consumer  | North | $6,920.00 | 185 Days Inactive | "Send Win-Back 15%" │
│ - CUST-0082 | Small Biz | West  | $6,450.20 | 192 Days Inactive | "Review Contract"   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Visual Specifications:
1. **Visual 1 (Donut Chart):**
   - Legend: `customer_features[Customer_Segment]`.
   - Values: Count of `Customer_ID`.
   - Colors: High Value (Blue), Regular (Green), At Risk (Red/Orange), Dormant (Gray).
2. **Visual 2 (Scatter Plot):**
   - X-Axis: `customer_features[Days_Since_Last_Purchase]`.
   - Y-Axis: `customer_features[Total_Spending]`.
   - Legend: `Customer_Segment`.
   - Reference line: Dotted Red vertical line at X = 120.
3. **Visual 3 (Outreach Table):**
   - Filtered dynamically to `Customer_Segment = "At Risk"`.
   - Sort: `Total_Spending` DESC.

---

## PAGE 4 — AI STRATEGIC BUSINESS INSIGHTS (Executive Briefing Room)

### Objective:
Present the automated Generative AI diagnostic findings in an executive briefing format, bridging the gap between raw dashboards and concrete strategic decision-making.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ TOP BANNER: AI-Powered Strategic Diagnostic & Recommended Operational Interventions    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ ARCHITECTURE PRINCIPLE: Mathematical Grounding -> Schema Separation                    │
│ [FACT: Computed by SQL/Python] ──► [POSSIBLE EXPLANATION: AI Hypothesis] ──► [ACTION]  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ CARD 1: TERRITORY CONTRACTION — SOUTH REGION                                           │
│ ┌────────────────────────────────────────────────────────────────────────────────────┐ │
│ │ • FACT: South sales dropped -19.5% in H2 2024; Tech hardware contracted -41.8%.     │ │
│ │ • POSSIBLE EXPLANATION: Competitor hub expansion or regional procurement delays.   │ │
│ │ • RECOMMENDED ACTION: Deploy regional trade-in promotions & audit logistics NPS.   │ │
│ └────────────────────────────────────────────────────────────────────────────────────┘ │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ CARD 2: PROMOTIONAL MARGIN EROSION — FURNITURE CATEGORY                                │
│ ┌────────────────────────────────────────────────────────────────────────────────────┐ │
│ │ • FACT: Furniture margin is -2.46%; 100% of orders with Discount >=25% lost money.  │ │
│ │ • POSSIBLE EXPLANATION: Reps giving deep discretionary discounts on bulky tables.  │ │
│ │ • RECOMMENDED ACTION: Implement 20% discount cap and shift commission to Margin.   │ │
│ └────────────────────────────────────────────────────────────────────────────────────┘ │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ CARD 3: RETENTION VULNERABILITY — AT-RISK DORMANT ACCOUNTS                             │
│ ┌────────────────────────────────────────────────────────────────────────────────────┐ │
│ │ • FACT: 41 mature accounts inactive for >120 days ($188,690 revenue at risk).      │ │
│ │ • POSSIBLE EXPLANATION: Lack of automated CRM replenishment notifications.         │ │
│ │ • RECOMMENDED ACTION: Trigger 3-part win-back email sequence & assign reps to top 10│ │
│ └────────────────────────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Visual Specifications:
1. **Container Cards (Multi-Row Cards or Text Shape Cards):**
   - 3 clean white cards with bold colored accent bars on the left (Navy, Amber, Emerald).
   - Dynamic DAX measures or pre-formatted markdown text blocks.
2. **Interactive Cross-Filtering:**
   - Selecting a card filters the underlying dataset in a linked drill-through modal.

---

## 5. How to Explain This in an Interview

> *"Rather than building a standard one-page chart dump, I designed a structured 4-page narrative dashboard aligned to user personas. Page 1 delivers high-level financial health for executives; Page 2 guides merchandising managers on SKU profitability and discount caps; Page 3 provides CRM teams with an operational priority outreach list for at-risk accounts; and Page 4 translates AI telemetry into structured executive briefings separating factual ground truth from suggested strategic interventions."*
