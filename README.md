# Acute Pancreatitis Severity Prediction
### Big Data & AI Case Study · 1,206 real patients · AUC-ROC 0.92

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-green?logo=scikit-learn&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi&logoColor=white)

---

## Overview

Acute pancreatitis carries high mortality risk when not detected early. Current clinical scoring systems (Ranson, APACHE II) require **48-hour observation** before a severity assessment can be made.

This project applies machine learning to **routine admission blood tests** to predict whether a patient will follow a severe or mild clinical course — at the moment of first contact, not 48 hours later.

---

## Key Results

| KPI | Value |
|---|---|
| AUC-ROC | **0.92** |
| Precision (Severe) | 0.91 |
| Recall (Severe) | 0.93 |
| Patients analysed | 1,206 |
| Biomarkers used | 9 |

> An AUC-ROC of 0.92 means the model correctly ranks a severe case above a mild case **92% of the time** — diagnostic-grade accuracy using only standard lab values.

---

## Top Predictive Features

| Rank | Biomarker | Importance |
|---|---|---|
| 1 | Calcium | 22% |
| 2 | Glucose | 15% |
| 3 | CRP | 13% |
| 4 | Bilirubin | 11% |
| 5 | LDH | 10% |
| 6 | Albumin | 9% |
| 7 | WBC | 8% |
| 8 | Total Bilirubin | 7% |
| 9 | Creatinine | 5% |

Calcium leads — hypocalcemia is a direct marker of pancreatic necrosis and is independently confirmed here as the strongest early-warning signal.

---

## Pipeline

```
Raw Excel (1,206 patients)
       │
       ▼
  ETL — Python / pandas
  · Remove patient identifiers
  · Standardize clinical column names
  · Filter anomalous records (amylase < 50 U/L)
       │
       ▼
  MySQL Database
  · Structured storage of clean patient data
  · Source for Power BI connectivity
       │
       ▼
  Random Forest Classifier
  · 9 biomarker features
  · SMOTE for class imbalance
  · 80/20 stratified train-test split
       │
       ▼
  Power BI Dashboard
  · Visión General · Análisis Clínico
  · Resultados IA · Predicciones por Paciente
  · Real-time filters by sex and prediction type
```

---

## Project Structure

```
├── notebooks/
│   └── acute_pancreatitis_severity_prediction.ipynb  ← executive report
├── etl/
│   ├── etl.py           ← extract, clean, export CSV
│   └── cargar_mysql.py  ← load clean data into MySQL
├── modelo/
│   └── modelo_rf.py     ← train Random Forest, export predictions
├── data/
│   ├── raw/             ← original Excel dataset
│   └── clean/           ← processed CSV
└── dashboard/
    ├── pancreatitis.pbix      ← Power BI dashboard (open with Power BI Desktop)
    ├── feature_importance.png
    └── predictions.csv
```

> **Power BI Dashboard:** download `dashboard/pancreatitis.pbix` and open it with [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free). Includes 4 pages: General Overview · Clinical Analysis · AI Results · Patient Predictions — with real-time filters by sex and prediction type.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Data processing | Python · pandas |
| Database | MySQL |
| Machine learning | scikit-learn · imbalanced-learn (SMOTE) |
| Visualization | Power BI · matplotlib |

---

## Author

**Fernando Redondo Pérez**  
University capstone project · Artificial Intelligence & Big Data  
2026
