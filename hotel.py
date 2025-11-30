import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Hotel Booking Dashboard",
    page_icon="🏨",
    layout="wide"
)

# --- CARGA DE DATOS ---
@st.cache_data
def load_data():
    # Cargamos el archivo CSV
    df = pd.read_csv("hotel_booking.csv")
    
    # Limpieza básica y manejo de tipos de datos
    # Llenar nulos en niños con 0 para poder sumar
    df['children'] = df['children'].fillna(0)
    
    # Crear una columna de fecha completa para ordenamiento (aproximada al día 1)
    month_map = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    df['month_num'] = df['arrival_date_month'].map(month_map)
    
    # Columna total de personas
    df['total_guests'] = df['adults'] + df['children'] + df['babies']
    
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Por favor, asegúrate de que el archivo 'hotel_booking.csv' esté en la misma carpeta.")
    st.stop()

# --- TÍTULO Y RESUMEN ---
st.title("🏨 Dashboard de Análisis de Reservas Hoteleras")
st.markdown("Este tablero interactivo explora el comportamiento de las reservas, cancelaciones y demografía de los huéspedes.")
st.markdown("---")

# --- 4 MÉTRICAS PRINCIPALES (KPIs) ---
total_bookings = len(df)
cancellation_rate = (df['is_canceled'].mean() * 100)
avg_adr = df['adr'].mean()
avg_stay_nights = (df['stays_in_weekend_nights'] + df['stays_in_week_nights']).mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total de Reservas", value=f"{total_bookings:,.0f}")
with col2:
    st.metric(label="Tasa de Cancelación", value=f"{cancellation_rate:.1f}%")
with col3:
    st.metric(label="Tarifa Promedio (ADR)", value=f"${avg_adr:.2f}")
with col4:
    st.metric(label="Estancia Promedio (Noches)", value=f"{avg_stay_nights:.1f}")

st.markdown("---")

# --- 6 VISUALIZACIONES PRINCIPALES ---

st.subheader("📊 Análisis Visual de Tendencias")

# Fila 1 de Gráficos
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    # 1. Comparación de tipos de Hotel
    fig_hotel = px.pie(df, names='hotel', title='Distribución de Reservas por Tipo de Hotel',
                       color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_hotel, use_container_width=True)

with row1_col2:
    # 2. Estado de la Reserva (Cancelado vs No Cancelado)
    # Mapeamos 0 y 1 a texto para mejor lectura
    df['status_text'] = df['is_canceled'].map({0: 'Check-Out (No Canceló)', 1: 'Cancelado'})
    fig_cancel = px.bar(df, x='status_text', color='status_text', 
                        title='Conteo de Cancelaciones vs. Reservas Exitosas',
                        color_discrete_map={'Cancelado': '#EF553B', 'Check-Out (No Canceló)': '#636EFA'})
    st.plotly_chart(fig_cancel, use_container_width=True)

# Fila 2 de Gráficos
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    # 3. Estacionalidad: Reservas por Mes
    # Agrupamos para ordenar por número de mes, no alfabéticamente
    monthly_counts = df.groupby(['month_num', 'arrival_date_month'])['hotel'].count().reset_index()
    monthly_counts.columns = ['month_num', 'Month', 'Bookings']
    monthly_counts = monthly_counts.sort_values('month_num')
    
    fig_month = px.line(monthly_counts, x='Month', y='Bookings', markers=True,
                        title='Fluctuación de Reservas por Mes (Estacionalidad)')
    st.plotly_chart(fig_month, use_container_width=True)

with row2_col2:
    # 4. Segmento de Mercado
    fig_segment = px.bar(df, x='market_segment', title='Reservas por Segmento de Mercado',
                         color='market_segment')
    fig_segment.update_layout(showlegend=False)
    st.plotly_chart(fig_segment, use_container_width=True)

# Fila 3 de Gráficos
row3_col1, row3_col2 = st.columns(2)

with row3_col1:
    # 5. Top 10 Países de Origen
    top_countries = df['country'].value_counts().head(10).reset_index()
    top_countries.columns = ['Country', 'Count']
    fig_country = px.bar(top_countries, x='Count', y='Country', orientation='h',
                         title='Top 10 Países de Origen de los Huéspedes',
                         color='Count', color_continuous_scale='Viridis')
    st.plotly_chart(fig_country, use_container_width=True)

with row3_col2:
    # 6. Distribución de Precio (ADR) por Tipo de Habitación Asignada
    # Filtramos valores extremos de ADR para que el gráfico se vea bien (menores a 500)
    filtered_adr = df[df['adr'] < 500]
    fig_adr = px.box(filtered_adr, x='assigned_room_type', y='adr', color='hotel',
                     title='Distribución de Precios (ADR) por Tipo de Habitación')
    st.plotly_chart(fig_adr, use_container_width=True)

st.markdown("---")

# --- DATAFRAME RELEVANTE ---
st.subheader("📋 Detalle de Datos Recientes")
st.markdown("A continuación se muestran las columnas más relevantes para la operación diaria.")

# Seleccionamos columnas útiles para mostrar
cols_to_show = ['hotel', 'arrival_date_year', 'arrival_date_month', 'is_canceled', 
                'lead_time', 'adr', 'market_segment', 'country', 'total_guests']

st.dataframe(df[cols_to_show].head(100), use_container_width=True)

st.markdown("---")

# --- CONCLUSIONES DEL ANÁLISIS ---
st.subheader("💡 Conclusiones Clave")

col_c1, col_c2, col_c3 = st.columns(3)

with col_c1:
    st.info("**1. Alta Tasa de Cancelación**")
    st.write(f"Con una tasa de cancelación del **{cancellation_rate:.1f}%**, es vital revisar las políticas de depósito. Una gran parte del inventario queda bloqueada y luego se libera, lo que afecta la eficiencia de ingresos.")

with col_c2:
    st.info("**2. Estacionalidad Marcada**")
    st.write("Se observa un pico claro de reservas en los meses de verano (Julio y Agosto). Esto sugiere la necesidad de estrategias de 'pricing' dinámico más agresivas en temporada alta y promociones para meses valle como Enero.")

with col_c3:
    st.info("**3. Dominio de Agencias (TA/TO)**")
    st.write("El segmento de 'Travel Agents/Operators' domina las reservas. Aunque traen volumen, suelen tener márgenes menores. Sería beneficioso incentivar el canal 'Direct' para mejorar la rentabilidad neta por habitación.")