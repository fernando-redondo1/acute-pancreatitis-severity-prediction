import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from imblearn.over_sampling import SMOTE
import os

df = pd.read_csv('../data/clean/pancreatitis_clean.csv')
print(f"Dataset: {len(df)} patients")

features = ['crp', 'glucose', 'creatinine', 'calcium', 'wbc', 'amylase', 'ldh', 'albumin', 'total_bilirubin']
X = df[features]
y = df['severity']  # 0=severe, 1=mild

# SMOTE oversamples the minority class to address class imbalance before splitting.
smote = SMOTE(random_state=42)
X_bal, y_bal = smote.fit_resample(X, y)
print(f"After SMOTE → Severe: {(y_bal==0).sum()} | Mild: {(y_bal==1).sum()}")

X_train, X_test, y_train, y_test = train_test_split(
    X_bal, y_bal, test_size=0.2, random_state=42, stratify=y_bal
)
print(f"Train: {len(X_train)} | Test: {len(X_test)}")

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    class_weight='balanced',
    random_state=42
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("\n=== RESULTS ===")
print(classification_report(y_test, y_pred, target_names=['Severe', 'Mild']))
print(f"AUC-ROC: {roc_auc_score(y_test, y_prob):.4f}")

print("\n=== CONFUSION MATRIX ===")
cm = confusion_matrix(y_test, y_pred)
print(f"               Predicted Severe  Predicted Mild")
print(f"Actual Severe       {cm[0][0]}                {cm[0][1]}")
print(f"Actual Mild         {cm[1][0]}               {cm[1][1]}")

importances = pd.DataFrame({
    'feature': features,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\n=== FEATURE IMPORTANCE ===")
print(importances.to_string(index=False))

plt.figure(figsize=(10, 6))
plt.barh(importances['feature'], importances['importance'], color='steelblue')
plt.xlabel('Importance')
plt.title('Feature importance for severity prediction')
plt.gca().invert_yaxis()
plt.tight_layout()
os.makedirs('../dashboard', exist_ok=True)
plt.savefig('../dashboard/feature_importance.png')
print("\nChart saved to dashboard/feature_importance.png")

df_out = df.copy()
X_orig = df_out[features]
df_out['prediction'] = model.predict(X_orig)
df_out['prob_severe'] = model.predict_proba(X_orig)[:, 0]
df_out['prediction_label'] = df_out['prediction'].map({0: 'severe', 1: 'mild'})

df_out.to_csv('../dashboard/predictions.csv', index=False)
print("Predictions exported to dashboard/predictions.csv")
