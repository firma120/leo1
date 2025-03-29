
# Tu Préstamo Express 💸

Aplicación en Python + Streamlit para la gestión de préstamos personales.

## 🚀 Funcionalidades

- Registro de clientes con validación.
- Creación de préstamos hasta $500.000 con interés mensual del 15%.
- Cuotas quincenales (máximo 4).
- Registro de pagos automáticos por cuota.
- Consulta detallada del historial del cliente.
- Actualización de datos del cliente.
- Exportación a Excel (.xlsx).
- Gráficas de crecimiento por mes y total de dinero prestado.

## 🛠️ Tecnologías

- Python
- Streamlit
- pandas
- openpyxl
- matplotlib

## 📦 Instalación

```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Estructura

```
├── app.py
├── db/
│   └── data.xlsx
├── utils/
│   ├── logic.py
│   ├── registro_cliente.py
│   ├── registro_prestamo.py
│   ├── registro_pago.py
│   ├── consulta_cliente.py
│   ├── actualizar_cliente.py
│   └── consulta_general.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ✨ Autor

Hecho con ❤️ por [Tu Nombre].  
