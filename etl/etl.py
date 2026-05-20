import pandas as pd
import os

# ETL pipeline for acute pancreatitis dataset.
# Extracts raw Excel data, cleans it, and exports a CSV ready for modeling.

# --- EXTRACT ---
raw_path = '../data/raw/data_V7.0-non-normalize.xlsx'
df = pd.read_excel(raw_path)
print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# --- TRANSFORM ---
df = df.drop(columns=['Name'])

df = df.rename(columns={
    'ID No. '           : 'patient_id',
    'Gender'            : 'sex',
    'CRP'               : 'crp',
    'Glu'               : 'glucose',
    'Cr'                : 'creatinine',
    'Ca'                : 'calcium',
    'WBC'               : 'wbc',
    'AMY'               : 'amylase',
    'LDH'               : 'ldh',
    'ALB'               : 'albumin',
    'TBIL'              : 'total_bilirubin',
    'Na⁺'          : 'sodium',
    'K⁺'           : 'potassium',
    'Diagnostic Result' : 'severity'
})

df['sex'] = df['sex'].map({1: 'male', 2: 'female'})

# severity: 0 = severe, 1 = mild (original dataset encoding)
df['severity_label'] = df['severity'].map({0: 'severe', 1: 'mild'})

# Amylase < 50 U/L suggests non-pancreatic aetiology; records removed as clinically suspicious.
before = len(df)
df = df[df['amylase'] >= 50]
print(f"Rows removed (amylase < 50 U/L): {before - len(df)}")

df = df.reset_index(drop=True)

print(f"Clean data: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"Severe: {(df['severity']==0).sum()} | Mild: {(df['severity']==1).sum()}")

# --- LOAD ---
clean_path = '../data/clean/pancreatitis_clean.csv'
os.makedirs('../data/clean', exist_ok=True)
df.to_csv(clean_path, index=False, encoding='utf-8')
print(f"\nFile saved to: {clean_path}")
