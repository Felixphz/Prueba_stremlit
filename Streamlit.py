import pandas as pd
import streamlit as st
import numpy as np

#nombre en la pestaña
st.set_page_config(layout="centered", page_title="Dashboard",page_icon=":smile:")

#titulo de la pagina
t1,t2 = st.columns([1, 2])
t1.image("R.jpeg", width=500)
t2.title("My primer tablero de control")
t2.markdown("**tel:**123456789**| email:** juanfelipe @ejemplo.com")
#secciones
steps=st.tabs(["Datos", "Gráficos", "Mapas", "Modelos","listas","diagramas"])
with steps[0]:
    st.write("Datos")
    data={"nombre": ["Juan", "Felipe", "Maria", "Jose"],
            "edad": [25, 30, 22, 28],}
    df=pd.DataFrame(data)
    st.table(df)
    st.dataframe(df)
    camp_df=pd.read_csv("campanhas.csv",encoding="latin-1", sep=";")
    camp=st.selectbox("Selecciona una campaña", (camp_df["ID_Campana"]), help="muestra las campañas existentes")
    met_def=pd.read_csv("Metricas.csv", encoding="latin-1", sep=";")
    st.dataframe(met_def)
    m1,m2,m3=st.columns([1,1,1])
    id1 = met_def[met_def["ID_Campana"] == camp]
    if not id1.empty:
        conversiones = int(sum(id1["Conversiones"]))
        rebotes = int(sum(id1["Rebotes"]))
        
        m1.write("Métrica 1")
        m1.metric(label="Métrica 1", value=conversiones, 
                delta=f"{rebotes} Número de rebotes", delta_color="inverse")
    else:
        m1.warning(f"No se encontraron datos para la campaña '{camp}'")

    maximo = int(max(id1["Impresiones"]))
    m2.write("metrica 2")
    m2.metric(label="ingresos", value=maximo, 
              delta="Cambio 2", delta_color="normal")
    
with steps[1]:
    st.write("Gráficos")
    x = np.random.randn(100)
    y = np.random.randn(100)
    st.line_chart(pd.DataFrame({"x": x, "y": y}))

with steps[2]:
    st.write("Mapas")
    st.map(pd.DataFrame({
        'lat': [37.76, 37.77, 37.78],
        'lon': [-122.45, -122.46, -122.47]
    }))
with steps[3]:
    st.write("Modelos")
    st.markdown("Aquí puedes agregar tus modelos de machine learning o análisis estadístico.")
    st.text_input("Ingrese un modelo", "Modelo de ejemplo")
    n=st.button("Ejecutar modelo")
    if n:
        st.write("Modelo ejecutado con éxito")
with steps[4]:
    st.write("Listas")
    items = st.multiselect("Selecciona tus elementos", ["Elemento 1", "Elemento 2", "Elemento 3"])
    if items:
        st.write("Has seleccionado:", items)
    else:
        st.write("No has seleccionado ningún elemento")
    st.selectbox("Selecciona una opción", ["Opción 1", "Opción 2", "Opción 3"])

