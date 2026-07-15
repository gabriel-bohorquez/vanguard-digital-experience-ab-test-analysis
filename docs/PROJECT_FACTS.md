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

## Backlog priorizado de profesionalización

### Prioridad alta

1. Definir una única fuente de datos válida para el análisis.
2. Separar datos originales, intermedios y procesados.
3. Corregir todas las rutas absolutas y sustituirlas por rutas relativas robustas.
4. Recalcular los KPIs desde una única lógica reproducible.
5. Unificar la definición de Completion Rate.
6. Revisar la definición y el denominador de Error Rate.
7. Revisar el cálculo de tiempo entre pasos y el tratamiento de outliers.
8. Validar el Two-Proportion Z-Test y documentar correctamente hipótesis, alternativa y p-value.
9. Resolver las inconsistencias entre `04_kpis_ab_testing.ipynb`, `05_hypothesis_testing.ipynb` y `06_final_analysis.ipynb`.
10. Verificar si `vanguard_cleaned_todos unidos_(Gabriel).csv` es incompleto, intermedio u obsoleto.
11. Verificar si `vanguard_tableau_ready.csv` coincide con las métricas finales validadas.
12. Auditar y, si corresponde, rehacer el dashboard Tableau.
13. Eliminar outputs de errores y warnings guardados en notebooks.
14. Asegurar que cada notebook pueda ejecutarse de principio a fin.
15. Corregir claims públicos que no estén respaldados por evidencia verificable.

### Prioridad media

1. Renombrar notebooks con convención profesional y consistente.
2. Reorganizar el repositorio con una estructura `data/raw`, `data/interim`, `data/processed`, `reports/figures` y `tableau`, solo si cada carpeta tiene una función real.
3. Renombrar artefactos genéricos como `Proyecto.twbx`, `output.png` y `output4.png`.
4. Revisar y refactorizar `src/functions.py`.
5. Crear `requirements.txt` con versiones probadas.
6. Crear `LICENSE`.
7. Añadir descripción, topics y metadata profesional en GitHub.
8. Reescribir el README después de validar todos los hechos.
9. Documentar limitaciones metodológicas, sesgos y alcance real del experimento.

### Prioridad baja

1. Evaluar si conviene mantener el repositorio como fork o migrarlo a un repositorio propio.
2. Renombrar el repositorio con una denominación profesional.
3. Preparar capturas finales para README y portfolio.
4. Alinear posteriormente portfolio, LinkedIn, CV y respuestas de entrevista.

## Criterio de cierre de la Fase 1

La Fase 1 se considerará cerrada cuando:

- el estado original esté preservado;
- exista un inventario verificable;
- los principales riesgos estén documentados;
- el backlog esté priorizado;
- y el repositorio esté limpio y sincronizado.

## Definición estratégica validada

### Problema de negocio

Vanguard necesita determinar si una nueva interfaz digital mejora el rendimiento del proceso online frente a la experiencia tradicional.

### Usuario principal

Equipos de producto digital, experiencia de usuario y negocio responsables de decidir si el rediseño debe mantenerse, iterarse o ampliarse.

### Decisión apoyada

Evaluar si la nueva experiencia digital debe adoptarse, ajustarse o someterse a nuevas pruebas antes de una implementación más amplia.

### KPI principal

Completion Rate por grupo experimental, medido como la proporción de clientes asignados a Test o Control que alcanzan al menos una vez el paso `confirm`.

### KPIs secundarios

- Error Rate o tasa de retrocesos, pendiente de definición final del denominador.
- Tiempo entre pasos, pendiente de validación metodológica y tratamiento de valores extremos.
- Funnel de progresión y abandono.
- Balance demográfico entre grupos.

### Formato final previsto

Proyecto de Data Analytics y A/B Testing compuesto por:

- notebooks reproducibles;
- análisis estadístico;
- dashboard Tableau;
- README profesional;
- repositorio GitHub;
- documentación para portfolio, CV, LinkedIn e entrevista.

### Alcance real

El proyecto evalúa asociación y diferencias observadas entre grupos dentro del experimento. No debe presentarse como una prueba absoluta de mejora de experiencia sin considerar fricción, errores, tiempos y limitaciones metodológicas.

## Fuentes de datos y artefactos autorizados

### Datos fuente originales

Los siguientes archivos se consideran datos originales y deben preservarse sin sobrescritura:

- `data_raw/df_final_demo.txt`
- `data_raw/df_final_experiment_clients.txt`
- `data_raw/df_final_web_data_pt_1.txt`
- `data_raw/df_final_web_data_pt_2.txt`

Aunque tienen extensión `.txt`, su contenido es CSV.

### Datos procesados actuales

Los siguientes archivos se consideran versiones procesadas provisionales:

- `data_raw/df_demo_clean.csv`
- `data_raw/df_experiment_clean.csv`
- `data_raw/df_web_clean.csv`

Estos archivos todavía deben auditarse para documentar exactamente:

- transformaciones aplicadas;
- exclusiones;
- tratamiento de nulos;
- eliminación de duplicados;
- cambios de tipos;
- consistencia entre claves.

### Artefactos no autorizados como fuente de verdad

Los siguientes archivos no deben utilizarse como fuente principal de KPIs o conclusiones hasta que sean validados:

- `data_raw/vanguard_cleaned_todos unidos_(Gabriel).csv`
- `vanguard_tableau_ready.csv`
- `Proyecto.twbx`

Motivos:

- el dataset unido parece contener solo una parte del comportamiento web;
- conserva duplicados;
- presenta tipos mixtos en `Variation`;
- no existe todavía trazabilidad completa de su construcción;
- Tableau puede estar alimentado por métricas no validadas.

### Fuente de verdad provisional

La fuente de verdad provisional para reconstruir el análisis será:

1. datos originales preservados;
2. lógica de limpieza validada;
3. datasets procesados regenerados de forma reproducible;
4. KPIs recalculados desde una única definición;
5. dataset final de Tableau generado únicamente después de validar métricas.

### Regla operativa

Ningún resultado público podrá considerarse definitivo hasta que pueda reproducirse desde los datos originales mediante notebooks o scripts ejecutables de principio a fin.

## Linaje actual de los datos procesados

### Datos demográficos

- Fuente: `data_raw/df_final_demo.txt`
- Generado por: `notebooks/02_data_cleaning.ipynb`
- Salida actual: `data_raw/df_demo_clean.csv`
- Transformación principal: eliminación de todas las filas que contienen al menos un valor nulo mediante `dropna()`.
- Estado: provisional.
- Riesgo pendiente: cuantificar filas eliminadas, columnas responsables y posible sesgo de selección.

### Asignación experimental

- Fuente: `data_raw/df_final_experiment_clients.txt`
- Generado por: `notebooks/02_data_cleaning.ipynb`
- Salida actual: `data_raw/df_experiment_clean.csv`
- Transformación principal: eliminación de clientes sin valor en `Variation`.
- Estado: provisional.
- Validaciones pendientes:
  - valores permitidos de `Variation`;
  - unicidad de `client_id`;
  - número de clientes excluidos;
  - distribución final entre Test y Control.

### Comportamiento web

- Fuentes:
  - `data_raw/df_final_web_data_pt_1.txt`
  - `data_raw/df_final_web_data_pt_2.txt`
- Generado por: `notebooks/02_data_cleaning.ipynb`
- Salida actual: `data_raw/df_web_clean.csv`
- Transformaciones principales:
  - eliminación de duplicados dentro de cada archivo;
  - unión vertical mediante `pd.concat`;
  - reinicio del índice.
- Estado: provisional.
- Riesgo pendiente: el notebook no elimina explícitamente duplicados después de concatenar ambas partes.
- Validaciones pendientes:
  - duplicados cruzados entre archivos;
  - tipos de fecha;
  - valores permitidos de `process_step`;
  - consistencia de `client_id`, `visitor_id` y `visit_id`;
  - orden temporal dentro de cada visita.

### Regla futura de reconstrucción

Los datasets procesados definitivos deberán regenerarse exclusivamente desde los archivos fuente originales, con controles de calidad visibles y métricas de filas antes y después de cada transformación.

## Validación cuantitativa de la limpieza actual

### Datos demográficos

- Filas originales: 70.609
- Filas procesadas: 70.591
- Filas eliminadas: 18
- Porcentaje eliminado: aproximadamente 0,03 %
- Duplicados originales: 0
- Duplicados procesados: 0
- `client_id` es único en ambos datasets.

Los 18 registros eliminados contienen valores nulos en variables demográficas. La pérdida cuantitativa es mínima, pero debe quedar documentada.

### Asignación experimental

- Filas originales: 70.609
- Filas procesadas: 50.500
- Clientes sin asignación experimental: 20.109
- Duplicados: 0
- `client_id` es único.

Distribución del experimento:

- Test: 26.968 clientes, aproximadamente 53,40 %
- Control: 23.532 clientes, aproximadamente 46,60 %

La diferencia entre grupos debe documentarse como una limitación del diseño, aunque no invalida por sí sola el análisis.

Los valores nulos de `Variation` representan clientes no incluidos en el experimento y no deben interpretarse automáticamente como errores de calidad.

### Comportamiento web

Parte 1:

- Filas originales: 343.141
- Duplicados eliminados: 2.095
- Filas finales: 341.046

Parte 2:

- Filas originales: 412.264
- Duplicados eliminados: 8.669
- Filas finales: 403.595

Dataset concatenado:

- Filas finales: 744.641
- Duplicados después del `concat`: 0
- Nulos: 0

No se detectaron duplicados cruzados entre ambas partes web.

Claves únicas:

- `client_id`: 120.157
- `visitor_id`: 130.236
- `visit_id`: 158.095

Distribución de eventos:

- `start`: 234.999
- `step_1`: 162.797
- `step_2`: 132.750
- `step_3`: 111.589
- `confirm`: 102.506

La caída progresiva entre pasos es consistente con un funnel digital y debe analizarse por cliente, visita y grupo experimental antes de derivar KPIs definitivos.

### Conclusión de calidad

Los datasets procesados actuales son estructuralmente utilizables, pero todavía son provisionales. Los principales riesgos pendientes están en los merges posteriores, las definiciones de métricas y la duplicación de lógica entre notebooks.

## Definición oficial provisional de Completion Rate

### Población correcta

La población analítica válida está formada por los 50.500 clientes con asignación experimental:

- Test: 26.968
- Control: 23.532

Todos los clientes experimentales tienen al menos un registro en el dataset web completo.

### Definición oficial

Completion Rate se define como:

> Proporción de clientes asignados a Test o Control que alcanzan al menos una vez el paso `confirm`.

Cada cliente se contabiliza una única vez.

### Resultados validados

Control:

- Total: 23.532 clientes
- Completaron: 15.434
- Completion Rate: 65,59 %

Test:

- Total: 26.968 clientes
- Completaron: 18.687
- Completion Rate: 69,29 %

Diferencia absoluta:

- aproximadamente 3,71 puntos porcentuales a favor de Test.

Mejora relativa:

- aproximadamente 5,65 % respecto a Control.

### Inconsistencia identificada

`04_kpis_ab_testing.ipynb` utiliza `vanguard_cleaned_todos unidos_(Gabriel).csv` y obtiene:

- Control: 63,09 %
- Test: 68,28 %

Este dataset contiene 58.391 clientes, pero solo 40.028 pertenecen realmente al experimento.

Por tanto, esos resultados no representan correctamente la población A/B y no deben utilizarse como métricas oficiales.

### Fuente de verdad provisional

La lógica de `05_hypotesis_testing.ipynb`, reconstruida desde:

- `df_experiment_clean.csv`
- `df_web_clean.csv`

se considera la fuente metodológica provisional para Completion Rate.

El notebook `04_kpis_ab_testing.ipynb` deberá corregirse para utilizar la misma población, definición y lógica.

## Definición oficial provisional de Backtracking Rate

### Corrección terminológica

La métrica denominada anteriormente `Error Rate` no identifica errores técnicos del sistema. Detecta transiciones en las que un usuario vuelve desde un paso más avanzado hacia un paso anterior.

Por claridad metodológica y de negocio, la métrica se denominará:

> Backtracking Rate o Tasa de retroceso.

### Secuencia del funnel

El orden definido de los pasos es:

1. `start`
2. `step_1`
3. `step_2`
4. `step_3`
5. `confirm`

Se considera retroceso cuando, dentro de la misma visita y respetando el orden temporal, el paso actual tiene una posición inferior al paso inmediatamente anterior.

### Métrica principal

Client Backtracking Rate:

> Proporción de clientes experimentales que presentan al menos una transición hacia un paso anterior durante alguna de sus visitas.

Cada cliente se contabiliza una única vez.

Resultados:

Control:

- Clientes con al menos un retroceso: 6.142
- Clientes totales: 23.532
- Backtracking Rate: 26,10 %

Test:

- Clientes con al menos un retroceso: 9.011
- Clientes totales: 26.968
- Backtracking Rate: 33,41 %

Diferencia absoluta:

- aproximadamente 7,31 puntos porcentuales más en Test.

Incremento relativo:

- aproximadamente 28,0 % respecto a Control.

### Métrica diagnóstica secundaria

Transition Backtracking Rate:

> Proporción de transiciones evaluables que representan un movimiento hacia un paso anterior.

Control:

- Retrocesos: 9.581
- Transiciones evaluables: 108.293
- Tasa: 8,85 %

Test:

- Retrocesos: 16.232
- Transiciones evaluables: 139.495
- Tasa: 11,64 %

Diferencia absoluta:

- aproximadamente 2,79 puntos porcentuales más en Test.

Esta métrica se utilizará para analizar la intensidad de la fricción, pero no como KPI experimental principal, porque un mismo cliente puede contribuir con múltiples transiciones.

### Métrica complementaria por visita

Control:

- Visitas con retroceso: 6.520
- Visitas totales: 32.189
- Tasa: 20,26 %

Test:

- Visitas con retroceso: 9.961
- Visitas totales: 37.136
- Tasa: 26,82 %

La métrica por visita será complementaria y no sustituirá la medición principal por cliente.

### Patrones observados

El destino más frecuente de los retrocesos es `start`:

- Control: 4.813
- Test: 10.514

La transición de retroceso más frecuente es `step_1 -> start`:

- Control: 3.490
- Test: 6.404

Este patrón sugiere que la fricción adicional del grupo Test podría concentrarse en las primeras etapas del proceso. La causa concreta no puede determinarse únicamente con los eventos disponibles.

### Interpretación provisional

El rediseño mejora la tasa de finalización, pero también aumenta la proporción de clientes que retroceden durante el proceso.

La significancia estadística de la diferencia en Backtracking Rate todavía debe verificarse antes de formular una conclusión definitiva.