# 🏨 Dashboard de Análisis de Reservas Hoteleras

Este proyecto es una aplicación interactiva de análisis de datos construida con **Streamlit**. Permite visualizar y explorar el comportamiento de las reservas hoteleras, identificar patrones de cancelación, estacionalidad y demografía de los huéspedes.

![Demo del Dashboard](example.gif)

## 📋 Características del Dashboard

El tablero ofrece una visión integral del negocio hotelero mediante:

### 1. Métricas Clave (KPIs)
Visualización inmediata de los indicadores más importantes:
* **Total de Reservas:** Volumen total del dataset.
* **Tasa de Cancelación:** Porcentaje de reservas que no se concretaron.
* **Tarifa Promedio (ADR):** Average Daily Rate.
* **Estancia Promedio:** Duración media de las visitas.

### 2. Visualizaciones Interactivas (Plotly)
* **Distribución por Tipo de Hotel:** Resort vs. Hotel de Ciudad.
* **Análisis de Cancelaciones:** Comparativa visual entre Check-outs y Cancelaciones.
* **Estacionalidad:** Fluctuación de reservas a lo largo de los meses del año.
* **Segmentación de Mercado:** Origen de la reserva (Agencias, Directo, Corporativo, etc.).
* **Geografía:** Top 10 países de origen de los huéspedes.
* **Análisis de Precios:** Distribución del ADR según el tipo de habitación asignada.

### 3. Conclusiones Automatizadas
Una sección final que destaca insights de negocio, como la dependencia de agencias de viaje o la necesidad de ajustar políticas de cancelación.

## 🛠️ Tecnologías Utilizadas

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/) - Para la interfaz web interactiva.
* [Pandas](https://pandas.pydata.org/) - Para la manipulación y limpieza de datos.
* [Plotly Express](https://plotly.com/python/plotly-express/) - Para gráficos interactivos.

## 🚀 Instalación y Uso

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/hotel-booking-dashboard.git](https://github.com/tu-usuario/hotel-booking-dashboard.git)
    cd hotel-booking-dashboard
    ```

2.  **Crea un entorno virtual (opcional pero recomendado):**
    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En Mac/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install streamlit pandas plotly
    ```

4.  **Asegúrate de tener los datos:**
    * Este proyecto requiere el archivo `hotel_booking.csv` en la carpeta raíz.
    * *Nota: Si el archivo no está incluido en el repo por tamaño, descárgalo de su fuente original (ej. Kaggle) y colócalo en la misma carpeta que `hotel.py`.*

5.  **Ejecuta la aplicación:**
    ```bash
    streamlit run hotel.py
    ```

## 📂 Estructura del Proyecto

```text
├── hotel.py              # Código principal de la aplicación Streamlit
├── hotel_booking.csv     # Dataset (Requerido para funcionar)
├── README.md             # Documentación del proyecto
└── requirements.txt      # Lista de dependencias (opcional)

Contacto:

Camilo Matallana - [www.linkedin.com/in/camilomatallanadataspecialistenglishfinance]


Enlace del Proyecto: https://github.com/CamiloMata/Hotel-Booking
