# Vanguard A/B Test Analysis

## Problema de negocio

Vanguard rediseñó su interfaz digital con el objetivo de mejorar la experiencia del usuario y aumentar la tasa de finalización del proceso online.

La empresa necesita determinar si el nuevo diseño realmente funciona mejor que la interfaz tradicional.

---

## Objetivo del proyecto

El objetivo de este proyecto es analizar el experimento A/B de Vanguard para evaluar si la nueva experiencia digital:

- mejora la tasa de finalización,
- reduce la fricción,
- disminuye errores de usuario,
- y optimiza la experiencia general del cliente.

---

## Datasets utilizados

### 1. Client Profiles
Contiene:
- edad
- género
- balances
- antigüedad
- información de cuentas

### 2. Digital Footprints
Contiene:
- navegación digital completa,
- pasos del proceso,
- timestamps,
- sesiones,
- comportamiento de usuario.

### 3. Experiment Clients
Contiene:
- asignación de grupos,
- Control vs Test.

---

## Workflow del proyecto

Problema de negocio  
↓  
Hipótesis  
↓  
Enfoque analítico  
↓  
Comprensión de datos  
↓  
Limpieza de datos  
↓  
Transformación de datos  
↓  
EDA  
↓  
Análisis de KPIs  
↓  
Hypothesis Testing  
↓  
Visualización y Dashboard  
↓  
Insights y Recomendaciones  

---

## Herramientas utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Tableau
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## KPIs analizados

### Completion Rate
Porcentaje de usuarios que llegan al paso de confirmación.

### Average Time Between Steps
Tiempo promedio entre pasos del proceso.

### Error Rate
Usuarios que retroceden pasos durante el proceso.

### Funnel Analysis
Abandono de usuarios a lo largo del flujo digital.

---

## Hypothesis Testing

### Hipótesis nula ($H_0$)

La tasa de finalización del grupo Test es igual a la del grupo Control.

### Hipótesis alternativa ($H_a$)

El grupo Test presenta mejor rendimiento que el grupo Control.

### Métodos estadísticos

- Two-Proportion Z-Test
- Comparación A/B
- Análisis de performance

---

## Insights principales

- El grupo Test obtuvo una mayor tasa de finalización respecto al grupo Control.
- Existe una pérdida progresiva de usuarios a lo largo del funnel.
- Algunos pasos generan mayor fricción y abandono.
- El rediseño mejora el rendimiento general del proceso digital.

---

## Dashboard Tableau

El dashboard incluye:

- Completion Rate
- Comparación Test vs Control
- Funnel Analysis
- Average Time Between Steps
- Filtros interactivos
- Segmentación de usuarios

---

## Estructura del proyecto

```bash
vanguard-ab-test/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── tableau/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_kpis_hypothesis_testing.ipynb
│   └── 05_final_analysis.ipynb
│
├── tableau/
│
├── slides/
│
├── README.md
│
└── requirements.txt
```

---

## Instalación

Clonar repositorio:

```bash
git clone https://github.com/yourusername/vanguard-ab-test.git
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar notebooks:

```bash
jupyter notebook
```

---

## Conclusiones

El análisis sugiere que el nuevo diseño digital mejora el rendimiento del proceso y genera una experiencia más eficiente para el usuario.

La variación Test superó al grupo Control en los principales KPIs del experimento.

---

## Próximos pasos

Posibles mejoras futuras:

- Segmentación avanzada
- Behavioral Analysis
- Session Path Analysis
- Power Analysis
- Modelos predictivos
- Streamlit App

---

