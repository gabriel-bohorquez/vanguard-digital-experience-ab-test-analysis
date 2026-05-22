"""

============
Funciones reutilizables para el análisis del experimento A/B de Vanguard.
Proyecto 2 - Data Analytics Bootcamp - Ironhack 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

# 1. CARGA DE DATOS

def load_clean_data(data_path: Path) -> tuple:
    """
    Carga los datasets limpios generados en 02_data_cleaning.ipynb.

    Parámetros:
        data_path (Path): Ruta a la carpeta data_raw.

    Retorna:
        tuple: (df_demo, df_experiment, df_web)
    """
    df_demo       = pd.read_csv(data_path / "df_demo_clean.csv")
    df_experiment = pd.read_csv(data_path / "df_experiment_clean.csv")
    df_web        = pd.read_csv(data_path / "df_web_clean.csv")

    df_web["date_time"] = pd.to_datetime(df_web["date_time"])

    return df_demo, df_experiment, df_web


# 2. INSPECCIÓN DE DATASETS

def inspect_datasets(dataframes: list, names: list) -> None:
    """
    Imprime las columnas de cada dataset para verificar su estructura.

    Parámetros:
        dataframes (list): Lista de DataFrames a inspeccionar.
        names (list): Lista de nombres de los DataFrames.
    """
    for df, name in zip(dataframes, names):
        print(f"\n--- Columnas en {name} ---")
        print(list(df.columns))


def check_content(dataframes: list, names: list) -> None:
    """
    Muestra las primeras filas de cada dataset de forma organizada.

    Parámetros:
        dataframes (list): Lista de DataFrames.
        names (list): Lista de nombres de los DataFrames.
    """
    for df, name in zip(dataframes, names):
        print(f"\n{'='*10} Contenido de {name} {'='*10}")
        print(df.head(3))


# 3. MÉTRICAS / KPIs

def get_completion_rate(df_web: pd.DataFrame, df_experiment: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula la tasa de completado (completion rate) por grupo (Test/Control).
    Un cliente se considera que completó el proceso si llegó al paso 'confirm'.

    Parámetros:
        df_web (pd.DataFrame): Dataset de interacciones web limpio.
        df_experiment (pd.DataFrame): Dataset del experimento con columna 'Variation'.

    Retorna:
        pd.DataFrame: Tabla con completion rate por grupo.
    """
    df_web = df_web.copy()
    df_web["is_completed"] = (df_web["process_step"] == "confirm").astype(int)
    df_conversion = df_web.groupby("client_id")["is_completed"].max().reset_index()
    df_merged = pd.merge(df_conversion, df_experiment, on="client_id")

    completion_rate = (
        df_merged.groupby("Variation")["is_completed"]
        .agg(["sum", "count", "mean"])
        .rename(columns={"sum": "completados", "count": "total", "mean": "completion_rate"})
    )
    completion_rate["completion_rate"] = completion_rate["completion_rate"].round(4)

    return completion_rate


def get_error_rate(df_web: pd.DataFrame, df_experiment: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula la tasa de errores por grupo (Test/Control).
    Un error se define como un paso hacia atrás en el proceso
    (de un paso posterior a uno anterior).

    Parámetros:
        df_web (pd.DataFrame): Dataset de interacciones web limpio.
        df_experiment (pd.DataFrame): Dataset del experimento con columna 'Variation'.

    Retorna:
        pd.DataFrame: Tabla con error rate por grupo.
    """
    step_order = {"start": 0, "step_1": 1, "step_2": 2, "step_3": 3, "confirm": 4}

    df = df_web.copy()
    df["step_num"] = df["process_step"].map(step_order)
    df = df.sort_values(["visit_id", "date_time"])
    df["prev_step"] = df.groupby("visit_id")["step_num"].shift(1)
    df["is_error"] = (df["step_num"] < df["prev_step"]).astype(int)

    df_merged = pd.merge(df, df_experiment, on="client_id")

    error_rate = (
        df_merged.groupby("Variation")["is_error"]
        .agg(["sum", "count", "mean"])
        .rename(columns={"sum": "errores", "count": "total_pasos", "mean": "error_rate"})
    )
    error_rate["error_rate"] = error_rate["error_rate"].round(4)

    return error_rate


def get_time_per_step(df_web: pd.DataFrame, df_experiment: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el tiempo medio que los usuarios pasan en cada paso del proceso,
    separado por grupo (Test/Control).

    Parámetros:
        df_web (pd.DataFrame): Dataset de interacciones web limpio (con date_time como datetime).
        df_experiment (pd.DataFrame): Dataset del experimento con columna 'Variation'.

    Retorna:
        pd.DataFrame: Tabla con tiempo medio por paso y grupo.
    """
    df = df_web.copy()
    df = df.sort_values(["visit_id", "date_time"])
    df["time_diff"] = df.groupby("visit_id")["date_time"].diff().dt.total_seconds()
    df_merged = pd.merge(df, df_experiment, on="client_id")

    time_per_step = (
        df_merged.groupby(["Variation", "process_step"])["time_diff"]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={"time_diff": "tiempo_medio_segundos"})
    )

    return time_per_step


# 4. TESTS DE HIPÓTESIS

def ztest_completion_rate(df_web: pd.DataFrame, df_experiment: pd.DataFrame,
                           alternative: str = "larger") -> dict:
    """
    Realiza un Z-test de dos proporciones para comparar la tasa de completado
    entre el grupo Test y el grupo Control.

    Parámetros:
        df_web (pd.DataFrame): Dataset de interacciones web limpio.
        df_experiment (pd.DataFrame): Dataset del experimento.
        alternative (str): Dirección del test ('larger', 'smaller', 'two-sided').

    Retorna:
        dict: Resultados del test (z_stat, p_value, tasas, conclusión).
    """
    completion = get_completion_rate(df_web, df_experiment)

    count_test    = int(completion.loc["Test", "completados"])
    count_control = int(completion.loc["Control", "completados"])
    nobs_test     = int(completion.loc["Test", "total"])
    nobs_control  = int(completion.loc["Control", "total"])

    z_stat, p_value = proportions_ztest(
        count=[count_test, count_control],
        nobs=[nobs_test, nobs_control],
        alternative=alternative
    )

    rate_test    = completion.loc["Test", "completion_rate"]
    rate_control = completion.loc["Control", "completion_rate"]

    resultado = {
        "tasa_test":    round(rate_test, 4),
        "tasa_control": round(rate_control, 4),
        "diferencia":   round(rate_test - rate_control, 4),
        "z_statistic":  round(z_stat, 4),
        "p_value":      round(p_value, 4),
        "significativo": p_value < 0.05
    }

    return resultado


def check_cost_effectiveness(df_web: pd.DataFrame, df_experiment: pd.DataFrame,
                              threshold: float = 0.05) -> dict:
    """
    Comprueba si la mejora en la tasa de completado supera el umbral
    de rentabilidad definido por Vanguard (por defecto 5%).

    Parámetros:
        df_web (pd.DataFrame): Dataset de interacciones web limpio.
        df_experiment (pd.DataFrame): Dataset del experimento.
        threshold (float): Umbral mínimo de mejora requerido (por defecto 0.05 = 5%).

    Retorna:
        dict: Resultados del análisis de rentabilidad.
    """
    completion = get_completion_rate(df_web, df_experiment)

    rate_test    = completion.loc["Test", "completion_rate"]
    rate_control = completion.loc["Control", "completion_rate"]
    diferencia   = rate_test - rate_control

    resultado = {
        "tasa_test":    round(rate_test, 4),
        "tasa_control": round(rate_control, 4),
        "diferencia":   round(diferencia, 4),
        "umbral":       threshold,
        "supera_umbral": diferencia >= threshold
    }

    return resultado


def ttest_age(df_web: pd.DataFrame, df_experiment: pd.DataFrame,
              df_demo: pd.DataFrame) -> dict:
    """
    Realiza un T-test para comparar la edad media entre los clientes
    que completaron el proceso y los que no, dentro del grupo Test.

    Parámetros:
        df_web (pd.DataFrame): Dataset de interacciones web limpio.
        df_experiment (pd.DataFrame): Dataset del experimento.
        df_demo (pd.DataFrame): Dataset demográfico.

    Retorna:
        dict: Resultados del T-test.
    """
    df_web = df_web.copy()
    df_web["is_completed"] = (df_web["process_step"] == "confirm").astype(int)
    df_conversion = df_web.groupby("client_id")["is_completed"].max().reset_index()

    df_segmented = pd.merge(df_conversion, df_demo, on="client_id")
    df_segmented = pd.merge(df_segmented, df_experiment, on="client_id")

    test_group = df_segmented[df_segmented["Variation"] == "Test"]

    completed     = test_group[test_group["is_completed"] == 1]["clnt_age"]
    not_completed = test_group[test_group["is_completed"] == 0]["clnt_age"]

    t_stat, p_value = stats.ttest_ind(completed, not_completed, equal_var=False)

    resultado = {
        "edad_media_completado":     round(completed.mean(), 1),
        "edad_media_no_completado":  round(not_completed.mean(), 1),
        "t_statistic":               round(t_stat, 4),
        "p_value":                   round(p_value, 4),
        "significativo":             p_value < 0.05
    }

    return resultado


# 5. SEGMENTACIÓN

def add_age_groups(df: pd.DataFrame) -> pd.DataFrame:
    """
    Añade una columna 'age_group' al DataFrame con grupos de edad.
    Grupos: 18-30, 31-50, 51-70, 70+

    Parámetros:
        df (pd.DataFrame): DataFrame con columna 'clnt_age'.

    Retorna:
        pd.DataFrame: DataFrame con columna 'age_group' añadida.
    """
    df = df.copy()
    df["age_group"] = pd.cut(
        df["clnt_age"],
        bins=[0, 30, 50, 70, 100],
        labels=["18-30", "31-50", "51-70", "70+"]
    )
    return df
