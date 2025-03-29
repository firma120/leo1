
import streamlit as st
import pandas as pd
import os
from utils.logic import init_db
from utils.registro_cliente import registrar_cliente
from utils.registro_prestamo import registrar_prestamo
from utils.registro_pago import registrar_pago
from utils.consulta_cliente import consultar_cliente
from utils.actualizar_cliente import actualizar_cliente
from utils.consulta_general import consulta_general

st.set_page_config(page_title="Tu Préstamo Express", layout="wide")
st.title("💸 Tu Préstamo Express")

# Inicializar DB
db_path = "db/data.xlsx"
if not os.path.exists(db_path):
    init_db(db_path)

# Menú lateral
menu = st.sidebar.radio("Menú", [
    "🏠 Inicio",
    "🧾 Registrar Cliente",
    "💰 Registrar Préstamo",
    "📥 Registrar Pago",
    "🔍 Consultar Cliente",
    "🛠️ Actualizar Cliente",
    "📊 Estadísticas y Exportación"
])

# Cargar secciones
if menu == "🏠 Inicio":
    st.info("Bienvenido a la app de gestión de préstamos")
elif menu == "🧾 Registrar Cliente":
    registrar_cliente(db_path)
    st.subheader("Registro de Cliente")
    # ... formulario
elif menu == "💰 Registrar Préstamo":
    registrar_prestamo(db_path)
    st.subheader("Registro de Préstamo")
elif menu == "📥 Registrar Pago":
    registrar_pago(db_path)
    st.subheader("Registro de Pago")
elif menu == "🔍 Consultar Cliente":
    consultar_cliente(db_path)
    st.subheader("Consultar Cliente e Historial")
elif menu == "🛠️ Actualizar Cliente":
    actualizar_cliente(db_path)
    st.subheader("Actualizar Datos del Cliente")
elif menu == "📊 Estadísticas y Exportación":
    consulta_general(db_path)
    st.subheader("Estadísticas de crecimiento")
