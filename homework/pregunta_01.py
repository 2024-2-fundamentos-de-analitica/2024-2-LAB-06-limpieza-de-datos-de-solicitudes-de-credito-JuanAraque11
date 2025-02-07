"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    datos = "files/input/solicitudes_de_credito.csv"
    df = pd.read_csv(datos, sep=";", index_col=0)

    reemplazar = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "monto_del_credito", "línea_credito"]
    for columna in reemplazar:
        if columna in df:
            df[columna] = df[columna].str.lower().str.strip()
            df[columna] = df[columna].str.replace("_", " ").str.replace("-", " ")
            df[columna] = df[columna].str.replace(",", "").str.replace("$", "")
            df[columna] = df[columna].str.replace(".00", "").str.strip()

    if "barrio" in df.columns:
        df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")

    if "comuna_ciudadano" in df.columns:
        df["comuna_ciudadano"] = pd.to_numeric(df["comuna_ciudadano"], errors="coerce", downcast="integer")

    if "monto_del_credito" in df.columns:
        df["monto_del_credito"] = pd.to_numeric(df["monto_del_credito"], errors="coerce")

    if "fecha_de_beneficio" in df.columns:
        df["fecha_de_beneficio"] = pd.to_datetime(
            df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
        ).combine_first(
            pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
        )

    df = df.drop_duplicates().dropna()

    datos_salida = "files/output/solicitudes_de_credito.csv"
    df.to_csv(datos_salida, sep=";", index=False)


pregunta_01()
