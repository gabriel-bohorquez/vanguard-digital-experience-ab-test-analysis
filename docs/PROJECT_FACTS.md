# PROJECT_FACTS

## Identidad del proyecto

- Nombre actual del proyecto: Projecto-2-Vanguard-ab-test
- Tipo de proyecto: Análisis A/B de experiencia digital
- Estado: Proyecto existente en proceso de auditoría y profesionalización
- Repositorio: https://github.com/gabriel-bohorquez/Projecto-2-Vanguard-ab-test
- Origen: Fork de un repositorio colaborativo

## Inventario inicial del repositorio

### Carpetas principales

- `Análisis AB Vanguard Nueva Interfaz Digital y Tasas de Finalización/`
- `data_raw/`
- `docs/`
- `notebooks/`
- `src/`

### Archivos en la raíz

- `Proyecto.twbx`
- `README.md`
- `output.png`
- `output4.png`
- `vanguard_tableau_ready.csv`

### Notebooks

- `01_data_understanding_1.ipynb`
- `02_data_cleaning.ipynb`
- `03_eda_client_behavior.ipynb.ipynb`
- `04_kpis_ab_testing.ipynb`
- `05_hypotesis_testing.ipynb`
- `06_final_analysis.ipynb`

### Scripts

- `src/functions.py`

### Documentación de trazabilidad

- `docs/README_ORIGINAL_VANGUARD_AB_TEST.pdf`
- `docs/PROJECT_FACTS.md`

### Estado del inventario

Inventario inicial registrado antes de modificar la estructura, nombres o contenido del proyecto.

## Riesgos iniciales detectados

### Prioridad alta

- El repositorio contiene un archivo `.DS_Store`, que no debe versionarse.
- El README documenta una estructura distinta de la estructura real.
- No existe todavía un archivo `.gitignore`.
- No existe un archivo `requirements.txt` visible en la raíz.
- El dataset `vanguard_tableau_ready.csv` está suelto en la raíz.
- El dashboard Tableau tiene un nombre genérico: `Proyecto.twbx`.

### Prioridad media

- `01_data_understanding_1.ipynb` contiene un sufijo innecesario.
- `03_eda_client_behavior.ipynb.ipynb` tiene doble extensión.
- `05_hypotesis_testing.ipynb` contiene un error ortográfico en inglés.
- `output.png` y `output4.png` no tienen nombres descriptivos.
- La carpeta de imágenes tiene un nombre excesivamente largo y poco mantenible.

### Prioridad baja

- El nombre del repositorio mezcla idiomas y conserva una denominación académica.
- La sección About de GitHub no tiene descripción, sitio web ni topics.
- El repositorio conserva visiblemente su condición de fork.

## Claims y métricas visibles antes de la auditoría

### Completion Rate

Se detectaron resultados inconsistentes entre notebooks:

- `04_kpis_ab_testing.ipynb`:
  - Control: aproximadamente 63%
  - Test: aproximadamente 68%
  - Diferencia: aproximadamente +5 puntos porcentuales

- `05_hypothesis_testing.ipynb`:
  - Control: aproximadamente 65,59%
  - Test: aproximadamente 69,29%
  - Diferencia: aproximadamente +3,70 puntos porcentuales
  - p-value reportado: 0,0000

Estas métricas no se consideran todavía verificadas. Deben recalcularse desde una única fuente de datos y con una definición común de usuario completado.

### Error Rate

Resultados visibles:

- Control: aproximadamente 8,94%
- Test: aproximadamente 11,48%
- Diferencia: Test presenta aproximadamente 2,54 puntos porcentuales más de retrocesos.

Definición utilizada provisionalmente: proporción de registros identificados como retroceso de paso.

La métrica debe revisarse para confirmar si el denominador correcto es evento, transición, sesión o usuario.

### Tiempo entre pasos

Resultados visibles:

- Control: aproximadamente 8,3 minutos por paso.
- Test: aproximadamente 10,1 minutos por paso.

La definición y el tratamiento de valores extremos deben validarse antes de publicar el resultado.

### Umbral estratégico

Un notebook establece un umbral mínimo de mejora absoluta del 5% para justificar una implementación completa.

El origen empresarial de este umbral no está documentado y debe tratarse como supuesto analítico, no como criterio oficial de Vanguard.

### Claims públicos en riesgo

Los siguientes claims del README requieren validación antes de mantenerse:

- El rediseño reduce la fricción.
- El rediseño optimiza la experiencia general del cliente.
- La variación Test superó a Control en los principales KPIs.
- El nuevo diseño presenta mejor rendimiento general.

La evidencia actual sugiere un resultado mixto: mayor finalización, pero también más retrocesos y mayor tiempo por paso.