<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/repository_images/SEAP%20LOGO.png" alt="SEAP" width="810" height="478" />

# Plataforma de Análisis de Energía Sostenible (SEAP)

*Predicción de la Eficiencia Energética y Demanda Futura en Transiciones a Energías Limpias Usando Técnicas de Machine Learning y Deep Learning*

### 🧑 Autor
 **Carlos Vergara Gámez** [LinkedIn](https://www.linkedin.com/in/carlosvergaragamez)

---

## Readme (Idioma)

<img src="https://flagcdn.com/gb.svg" width="23" alt="UK"> [English](https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform) <img src="https://flagcdn.com/gb.svg" width="23" alt="UK">

<img src="https://flagcdn.com/es.svg" width="20" alt="ES"> [Español](https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/README_ES.md) <img src="https://flagcdn.com/es.svg" width="20" alt="ES">


---


## ⭐ Enlace a la Presentación

<img src="https://flagcdn.com/es.svg" width="20" alt="Bandera de España"> [Presentación en Canvas (En Español)](https://www.canva.com/design/DAGUhRaaOmw/aEQhV185tQSanPWRcP_Y2w/view?utm_content=DAGUhRaaOmw&utm_campaign=designshare&utm_medium=link&utm_source=editor) <img src="https://flagcdn.com/es.svg" width="20" alt="Bandera de España">

---

## 👀 Resumen Rápido

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/repository_images/SEAP.gif" alt="SEAP" width="800" height="500" />

> 🗺 En este proyecto, puedes generar un **mapa mundial** y **mapa de Europa** completamente interactivos para explorar el uso de energías renovables de una manera atractiva.

---

## 📊 Descripción del Proyecto

La **Plataforma de Análisis de Energía Sostenible (SEAP)** es mi proyecto final del Bootcamp de Data Analytics en Ironhack. El proyecto se enfoca en predecir las **tendencias de generación de energía renovable** para fuentes solares, eólicas, hidroeléctricas y biocombustibles. Aprovechando **Machine Learning** y **Deep Learning**, el objetivo es evaluar la eficiencia energética y la demanda durante la transición a fuentes de energía limpia.

### **Modelos Clave**:
- 🌲 **Random Forest** con **GridSearchCV** para Machine Learning.
- 🧠 **Perceptrón Multicapa (MLP)** para predicción de series temporales multivariadas en Deep Learning.

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%201.png" alt="SEAP" width="810" height="478" />

---

## 🎯 Objetivos
-  Predecir las tendencias futuras de producción de energía de fuentes renovables.
-  Analizar la demanda de energía y la eficiencia en transiciones a energías limpias.
-  Proporcionar **visualizaciones interactivas** para la exploración de datos y predicciones.
-  Desarrollar modelos avanzados de IA para obtener **insights en tiempo real** sobre energía.

---

## 🛠️ Tecnologías Utilizadas
Este proyecto utiliza diversas herramientas:
-  **Python**, **Pandas**, **NumPy** para procesamiento de datos.
-  **Matplotlib**, **Seaborn**, **Plotly** para visualizaciones.
-  **Scikit-Learn** para modelos de Machine Learning.
-  **TensorFlow/Keras** para Deep Learning.
-  **Geopandas** y **Folium** para análisis de datos espaciales.

---

## 🗂️ Fuente de Datos
<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/repository_images/Our_World_in_Data_logo.png" alt="SEAP" width="250" height="142" />

El conjunto de datos utilizado en este proyecto proviene de:

> Ritchie, H., Rosado, P., & Roser, M. (2023). *Energy*. Publicado en **OurWorldinData.org**. [Enlace](https://ourworldindata.org/energy)

---

## 📁 Estructura del Repositorio
- 📂 **SEAP_01_EDA_map_and_cleaning.ipynb**: Análisis Exploratorio de Datos y limpieza, incluyendo visualizaciones de mapas.
- 📂 **SEAP_02_Machine_Learning_and_Deep_Learning.ipynb**: Implementación de modelos de Machine Learning y Deep Learning para la predicción de energía.

---

## 💻 Instrucciones de Uso

1. Clonar el repositorio y configurar el entorno:
   ```bash
   conda env create -f ml-dp.yml
   conda activate ml-dp
   ```

2. Descargar las carpetas necesarias: `data` y `shapefiles`.

3. Abrir y ejecutar los notebooks:
   - `SEAP_01_EDA_map_and_cleaning.ipynb`
   - `SEAP_02_Machine_Learning_and_Deep_Learning.ipynb`

4. Los modelos generados y mapas se guardarán en las carpetas `final_models` y `maps`.

---

## 📊 Algunas Visualizaciones (¡Revisa los notebooks!)

- **Tendencias Globales de Energía Renovable**:
  
  <img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%2010.png" alt="SEAP" width="600" height="378" />
  
  > El gráfico muestra un aumento significativo en la producción de electricidad renovable, con la energía solar y eólica dominando.

- **Demanda vs. Suministro de Energía**:
  
  <img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%209.png" alt="SEAP" width="600" height="378" />
  
  > El gráfico compara la demanda de electricidad predicha y real, destacando la precisión del modelo.

---

## 🔮 Direcciones Futuras

Mirando hacia adelante, mi objetivo es desarrollar un **sistema de IA** capaz de gestionar conjuntos de datos más grandes mediante técnicas de **Deep Learning**. Esta IA proporcionará **predicciones en tiempo real** y permitirá una **comunicación interactiva**, permitiendo a los usuarios explorar desafíos relacionados con la energía y proponer soluciones sostenibles.

---

## ❤️ Agradecimientos

Quisiera expresar mi más sincero agradecimiento a **Ironhack Bootcamp** por todo el conocimiento y habilidades que he adquirido a lo largo de esta experiencia. No solo ha sido educativo, sino también increíblemente enriquecedor a nivel personal.

Un agradecimiento especial a mis increíbles mentores, **Santiago, Antonio** y **Nicolás**, cuyo apoyo y orientación han sido fundamentales en mi proceso de aprendizaje. Sus ideas y aliento me han motivado a superar mis límites y esforzarme por la excelencia.

También quiero extender mi aprecio a todos mis compañeros de clase. Gracias por los innumerables momentos de risa, colaboración y esfuerzo que compartimos juntos. Estos recuerdos permanecerán conmigo como un testimonio de nuestro viaje colectivo.

*¡Gracias a todos por ser parte de esta experiencia transformadora!*

**Carlos Vergara Gámez**
