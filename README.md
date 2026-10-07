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

El calcio es la variable más importante: la
