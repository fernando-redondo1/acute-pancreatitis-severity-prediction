import pandas as pd
import mysql.connector

# Loads the cleaned pancreatitis CSV into a MySQL table.

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pancreatitis'
)
cursor = conn.cursor()

df = pd.read_csv('../data/clean/pancreatitis_clean.csv')
print(f"Rows to load: {len(df)}")

# --- CREATE TABLE ---
cursor.execute("DROP TABLE IF EXISTS patients")
cursor.execute("""
    CREATE TABLE patients (
        patient_id      BIGINT PRIMARY KEY,
        sex             VARCHAR(10),
        crp             FLOAT,
        glucose         FLOAT,
        creatinine      FLOAT,
        calcium         FLOAT,
        wbc             FLOAT,
        amylase         FLOAT,
        ldh             FLOAT,
        albumin         FLOAT,
        total_bilirubin FLOAT,
        severity        INT,
        severity_label  VARCHAR(10)
    )
""")
print("Table created")

# --- INSERT ---
rows = []
for _, row in df.iterrows():
    rows.append((
        int(row['patient_id']),
        row['sex'],
        float(row['crp']),
        float(row['glucose']),
        float(row['creatinine']),
        float(row['calcium']),
        float(row['wbc']),
        float(row['amylase']),
        float(row['ldh']),
        float(row['albumin']),
        float(row['total_bilirubin']),
        int(row['severity']),
        row['severity_label']
    ))

insert_query = """
    INSERT INTO patients (
        patient_id, sex, crp, glucose, creatinine, calcium,
        wbc, amylase, ldh, albumin, total_bilirubin,
        severity, severity_label
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

cursor.executemany(insert_query, rows)
conn.commit()
print(f"Inserted {len(rows)} rows")

cursor.close()
conn.close()
