"""Verificación del entorno del curso: Python, librerías y conexión a PosgreSQL."""

import getpass
import sys

import matplotlib
import numpy
import pandas
import psycopg
import seaborn
import sklearn
import sqlalchemy

print(f"Python         {sys.version.split()[0]}")
print(f"matplotlib     {sys.executable}")

for librería in [matplotlib, numpy, pandas, psycopg, seaborn, sklearn, sqlalchemy]:
    print(f"{librería.__name__:<14}{librería.__version__}")
print()

contraseña = getpass.getpass("Contraseña del usurario postgres: ")

with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="curso_data_analytics",
    user="postgres",
    password=contraseña,
) as conexion:
    version = conexion.execute("SELECT version()").fetchone()[0]

    tablas = conexion.execute("""
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_type = 'BASE TABLE'
        ORDER BY table_schema, table_name
    """).fetchall()

    fila = conexion.execute(
        "SELECT mensaje FROM public.prueba_entorno"
    ).fetchone()

    print("Tablas disponibles:", tablas)
    print("Fila de prueba:", fila)

print(f"PostgreSQL: {version}")
print()
print("Entorno listo para el curso")
