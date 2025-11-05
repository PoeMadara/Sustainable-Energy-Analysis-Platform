<img width="1010" height="260" alt="SEAP LOGO" src="https://github.com/user-attachments/assets/fc13ebd4-94d4-4ae0-818b-525c2c4ab527" />

# Sustainable Energy Analysis Platform (SEAP) 

*Historical Trends and Predicting Future Energy Efficiency and Demand in Clean Energy Transitions Using Machine Learning and Deep Learning Techniques between 1900 to 2074.*
*Optimized for execution on AWS SageMaker (model training), Redshift (data analysis), and S3 (dataset storage).*
  
### Author

 *Carlos Vergara Gámez*
 
[Github](https://github.com/PoeMadara) - [LinkedIn](https://www.linkedin.com/in/carlosvergaragamez)

E-mail: carlos.poemadara@gmail.com


---

## Readme (Language)

<img src="https://flagcdn.com/es.svg" width="20" alt="ES"> [Español](https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/README_ES.md) <img src="https://flagcdn.com/es.svg" width="20" alt="ES">

<img src="https://flagcdn.com/gb.svg" width="23" alt="UK"> [English](https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform) <img src="https://flagcdn.com/gb.svg" width="23" alt="UK">


---


## Presentation Link

<img src="https://flagcdn.com/es.svg" width="20" alt="Spain Flag"> [Canvas Presentation (Only in Spanish)](https://www.canva.com/design/DAGUhRaaOmw/aEQhV185tQSanPWRcP_Y2w/view?utm_content=DAGUhRaaOmw&utm_campaign=designshare&utm_medium=link&utm_source=editor) <img src="https://flagcdn.com/es.svg" width="20" alt="Spain Flag">


---

## A Quick Overview

![SEAP Quick overview final](https://github.com/user-attachments/assets/1cf40e8a-5b70-4edd-91d1-8f60b9ad4ec6)

> 🗺 In this project, you can generate a **fully interactive**  **world map** and  **Europe map** to explore renewable energy usage in an engaging way!

---

## Project Overview

The **Sustainable Energy Analysis Platform (SEAP)** is my final project from the Data Analytics Bootcamp at Ironhack. The project focuses on predicting **renewable energy generation trends** for solar, wind, hydroelectric, and biofuel sources. By leveraging **Machine Learning** and **Deep Learning**, the goal is to assess energy efficiency and demand during the transition to clean energy sources.


### **Key Models**:
- 📂 **Multi-Output Random Forest for Multivariate Time Series Forecasting Optimized with Grid Search** (MO-RF-MTSF-GS).
- 📂 **Recurrent Neural Network with Multilayer Perceptron for Multivariate Time Series Forecasting** (RNN-MLP-MTSF). 


<img width="826" height="610" alt="output 1" src="https://github.com/user-attachments/assets/3a11e125-342b-42db-97ab-a69c97ad95c6" />

---

## Objectives
-  Predict future energy production trends for renewable sources.
-  Analyze energy demand and efficiency in clean energy transitions.
-  Provide **interactive visualizations** for data exploration and predictions.
-  Develop advanced AI models for **real-time** energy insights.

---

##  Technologies Used
This project leverages a variety of tools:
-  **Python**, **Pandas**, **NumPy** for data processing.
-  **Matplotlib**, **Seaborn**, **Plotly** for visualizations.
-  **Scikit-Learn** for Machine Learning models.
-  **TensorFlow/Keras** for Deep Learning.
-  **Geopandas** and **Folium** for spatial data analysis.

---

##  Data Source

<img width="250" height="142" alt="Our_World_in_Data_logo" src="https://github.com/user-attachments/assets/7be520c5-8b56-45ac-a727-6b1b209284b7" />

The dataset used in this project comes from:

> Ritchie, H., Rosado, P., & Roser, M. (2023). *Energy*. Published at **OurWorldinData.org**. [Link](https://ourworldindata.org/energy)

---

## Repository Structure
- 📂 **SEAP_01_EDA_map_and_cleaning.ipynb**: Exploratory Data Analysis and cleaning, including map visualizations.
- 📂 **SEAP_02_Machine_Learning_and_Deep_Learning.ipynb**: Implementation of Machine Learning and Deep Learning models for energy prediction.

---

## Usage Instructions

1. Clone the repository and set up the environment:
   ```bash
   conda env create -f ml-dp.yml
   conda activate ml-dp
   ```

2. Download necessary folders: `data` and `shapefiles`.

3. Open and run the notebooks:
   - `SEAP_01_EDA_map_and_cleaning.ipynb`
   - `SEAP_02_Machine_Learning_and_Deep_Learning.ipynb`

4. Generated models and maps will be saved in the `final_models` and `maps` folders.

---

## Some Visualizations (Check out the notebooks for more!)

- **Global Renewable Energy Trends**:
  
  <img width="600" height="378" alt="output 3" src="https://github.com/user-attachments/assets/39603822-8a62-43bc-9861-b06fc4e6ccd8" />

  > The graph shows a significant increase in renewable electricity production, with solar and wind energy growing over time, while hydroelectric power remains dominant. It also shows an exponential increase in electricity demand since 2000, making renewable energy sources currently insufficient to fully replace non-renewable energy.

  
- **Energy Demand vs. Supply**:
  
  <img width="600" height="378" alt="output 9" src="https://github.com/user-attachments/assets/08559039-2ff2-4b01-ad88-162bd5615ae3" />

  > The chart compares predicted and actual electricity demand, highlighting the model's accuracy.

---

## Future Directions

Looking ahead, my goal is to develop an **AI system** capable of managing larger datasets through **Deep Learning** techniques. This AI will provide **real-time predictions** and enable **interactive communication**, allowing users to explore energy-related challenges and propose sustainable solutions.

---

## Acknowledgements

I would like to express my heartfelt gratitude to **Ironhack Bootcamp** for all the invaluable knowledge and skills I've acquired throughout this journey. The experience has not only been educational but also incredibly enriching on a personal level.

A special thanks to my amazing mentors, **Santiago, Antonio,** and **Nicolás**, whose guidance and support have been instrumental in my learning process. Your insights and encouragement have motivated me to push my limits and strive for excellence.

I also want to extend my appreciation to all my fellow classmates. Thank you for the countless moments of laughter, collaboration, and hard work we shared together. These memories will stay with me as a testament to our collective journey.

*Thank you all for being a part of this transformative experience!*

**Carlos Vergara Gámez**

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/LICENSE) file for details.
