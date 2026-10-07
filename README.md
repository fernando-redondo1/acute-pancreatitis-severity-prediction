# Predicción de la gravedad de la pancreatitis aguda
### Caso práctico de Big Data e IA · 1.206 pacientes reales · AUC-ROC 0,92

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-green?logo=scikit-learn&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi&logoColor=white)

---

## Resumen

La pancreatitis aguda tiene un alto riesgo de mortalidad si no se detecta a tiempo. Los sistemas de puntuación clínica actuales (Ranson, APACHE II) necesitan **48 horas de observación** antes de poder valorar la gravedad.

Este proyecto aplica Machine Learning a los **análisis de sangre rutinarios del ingreso** para predecir si un paciente evolucionará hacia un cuadro grave o leve en el primer contacto, no 48 horas después.

---

## Motivación

Este proyecto tiene un significado personal para mí. Mi padre estuvo hospitalizado por una pancreatitis aguda, y vivir esas primeras horas de incertidumbre, mientras los médicos esperaban para saber hasta qué punto sería grave, me hizo entender de primera mano por qué importa la predicción temprana. Esas 48 horas se hacen muy largas cuando el paciente es alguien a quien quieres.

Es mi forma de aplicar lo que he aprendido en ciencia de datos e IA a un problema que sé que es real.

---

## Resultados principales

| Indicador | Valor |
|---|---|
| AUC-ROC | **0,92** |
| Precisión (graves) | 0,91 |
| Sensibilidad / Recall (graves) | 0,93 |
| Pacientes analizados | 1.206 |
| Biomarcadores utilizados | 9 |

> Un AUC-ROC de 0,92 significa que el modelo ordena correctamente un caso grave por encima de uno leve el **92 % de las veces**, usando solo valores de laboratorio estándar. Son resultados sobre un conjunto de prueba interno; un uso clínico real requeriría validación externa.

---

## Variables más predictivas

| Posición | Biomarcador | Importancia |
|---|---|---|
| 1 | Calcio | 22 % |
| 2 | Glucosa | 15 % |
| 3 | PCR | 13 % |
| 4 | Bilirrubina | 11 % |
| 5 | LDH | 10 % |
| 6 | Albúmina | 9 % |
| 7 | Leucocitos | 8 % |
| 8 | Bilirrubina total | 7 % |
| 9 | Creatinina | 5 % |

El calcio es la variable más importante: la hipocalcemia es un marcador directo de necrosis pancreática y aquí se confirma como la señal de alerta temprana más fuerte.

---

## Pipeline

```
Excel original (1.206 pacientes)
       │
       ▼
  ETL — Python / pandas
  · Eliminación de identificadores de pacientes
  · Normalización de los nombres de columnas clínicas
  · Filtrado de registros anómalos (amilasa < 50 U/L)
       │
       ▼
  Base de datos MySQL
  · Almacenamiento estructurado de los datos limpios
  · Fuente de datos para Power BI
       │
       ▼
  Clasificador Random Forest
  · 9 biomarcadores como variables
  · SMOTE para el desequilibrio de clases
  · División estratificada 80/20 entre entrenamiento y prueba
       │
       ▼
  Cuadro de mando en Power BI
  · Visión general · Análisis clínico
  · Resultados IA · Predicciones por paciente
  · Filtros en tiempo real por sexo y tipo de predicción
```

---

## Estructura del proyecto

```
├── notebooks/
│   └── acute_pancreatitis_severity_prediction.ipynb  ← informe ejecutivo
├── etl/
│   ├── etl.py           ← extracción, limpieza y exportación a CSV
│   └── cargar_mysql.py  ← carga de los datos limpios en MySQL
├── modelo/
│   └── modelo_rf.py     ← entrenamiento del Random Forest y exportación de predicciones
└── dashboard/
    ├── pancreatitis.pbix          ← cuadro de mando (se abre con Power BI Desktop)
    └── feature_importance.png     ← gráfico de importancia de variables
```

> **Cuadro de mando de Power BI:** descarga `dashboard/pancreatitis.pbix` y ábrelo con [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (gratuito). Tiene 4 páginas: Visión general · Análisis clínico · Resultados IA · Predicciones por paciente, con filtros en tiempo real por sexo y tipo de predicción.

---

## Tecnologías

| Capa | Tecnología |
|---|---|
| Procesamiento de datos | Python · pandas |
| Base de datos | MySQL |
| Machine Learning | scikit-learn · imbalanced-learn (SMOTE) |
| Visualización | Power BI · matplotlib |

---

## Datos

Dataset público obtenido de Kaggle, procedente del estudio *Accurate prediction of acute pancreatitis severity with integrative blood molecular measurements* (Sun et al., Aging, 2021; DOI: [10.18632/aging.202689](https://doi.org/10.18632/aging.202689)). Los datos fueron publicados ya anonimizados; los identificadores de paciente son los del dataset original.

---

## Autor

**Fernando Redondo Pérez**
Proyecto final · Inteligencia Artificial y Big Data
2026
