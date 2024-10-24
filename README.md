<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/repository_images/SEAP%20LOGO.png" alt="SEAP" width="810" height="478" />

# Sustainable Energy Analysis Platform (SEAP)

*Predicting Future Energy Efficiency and Demand in Clean Energy Transitions Using Machine Learning and Deep Learning Techniques*

### Author

**Carlos Vergara Gámez** [LinkedIn](https://www.linkedin.com/in/carlosvergaragamez)


## Presentation Link

- [Canvas Presentation Link](#)


## A quick Overview

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/repository_images/SEAP.gif" alt="SEAP" width="800" height="500" />

> In this project, you can generate fully interactive world and european maps to visualize renewable energy usage!!


## Project Overview

The **Sustainable Energy Analysis Platform (SEAP)** is my final project of the Data Analytics Bootcamp at Ironhack, focusing on predicting renewable energy generation trends, including solar, wind, hydroelectric, and biofuel energy. By leveraging **Machine Learning** and **Deep Learning** techniques, the project aims to assess energy efficiency and demand during the transition to clean energy sources.

**Key Models:**
- **Random Forest with GridSearchCV** for Machine Learning.
- **Multi-Layer Perceptron (MLP)** for multivariate time series forecasting in Deep Learning.

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%201.png" alt="SEAP" width="810" height="478" />

## Objectives

- Predict future energy production trends for renewable sources.
- Analyze energy demand and efficiency in clean energy transitions.
- Provide interactive visualizations for exploring data and predictions.
- Develop advanced AI models for real-time energy insights.

## Technologies Used

This project utilizes:

- **Python**, **Pandas**, **NumPy** for data processing.
- **Matplotlib**, **Seaborn**, **Plotly** for visualizations.
- **Scikit-Learn** for Machine Learning models.
- **TensorFlow/Keras** for Deep Learning.
- **Geopandas** and **Folium** for spatial data analysis.

## Data Source

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/repository_images/Our_World_in_Data_logo.png" alt="SEAP" width="250" height="142" />

The dataset used is from:

> Ritchie, H., Rosado, P., & Roser, M. (2023). *Energy*. Published at **OurWorldinData.org**. [Link](https://ourworldindata.org/energy)

## Repository Structure

- **SEAP_01_EDA_map_and_cleaning.ipynb**: Exploratory Data Analysis and cleaning, including map visualizations.
- **SEAP_02_Machine_Learning_and_Deep_Learning.ipynb**: Implementation of models for energy prediction.

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

4. Generated models and maps will be saved in `final_models` and `maps`.


## Some Visualizations (Feel free to check my notebooks!)

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%203.png" alt="SEAP" width="600" height="378" />
The graph shows a clear upward trend in the production of solar, wind, biofuel, and hydroelectric electricity over the years. This indicates a growing global reliance on renewable energy sources.

---

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%202.png" alt="SEAP" width="600" height="378" /> 
The chart highlights the global dependence on hydroelectricity and the growing role of solar and wind energy.

---

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%204.png" alt="SEAP" width="600" height="378" />
The graph shows a substantial increase in electricity demand and generation over several decades, particularly around the year 2000. This period marks a strong correlation between the two metrics, indicating a simultaneous rise in demand and generation.

---

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%2013.png" alt="SEAP" width="600" height="378" />
The most striking trend observed in the graph is the exponential growth of solar and wind electricity generation. In contrast, hydroelectric and biofuel electricity sources have shown more modest growth or even slight declines. This suggests a clear shift towards renewable energy sources, particularly solar and wind power, in recent decades.

---

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%206.png" alt="SEAP" width="600" height="378" />
This is a predictiving graph, it suggests a promising future for renewable energy, with hydroelectric energy leading the growth. Solar and wind will also see significant increases, while biofuel generation is expected to decline. Successful integration will require policy support and technological advancements.

---

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%209.png" alt="SEAP" width="600" height="378" />

- **Each point**: Represents a pair of values - actual electricity demand and the model's predicted demand at the same time.
- **Red diagonal line**: Ideal scenario where predictions perfectly match actual values. Points on this line indicate no prediction error.
- **Blue points**: Individual model predictions. Their spread around the diagonal line indicates prediction accuracy.

---

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%2010.png" alt="SEAP" width="600" height="378" />

**What does the graph show?**

- **Actual energy consumption**: Blue line with dots
- **Model's predicted values**: Orange line with "x" marks
- **X-axis**: Represents time points
- **Y-axis**: Indicates the amount of energy consumed

**General Interpretation:**

- **Good overall trend capture:** The model generally follows the trend of actual energy consumption, with predictions increasing as actual consumption increases.
- **Systematic underestimation:** The model tends to underestimate energy consumption, especially at peaks, as the orange line is often below the blue line.
- **Seasonal patterns:** The model captures some seasonal or cyclical patterns, though not perfectly.

**Conclusions:**

> The model shows a reasonable trend capture but needs improvement in accuracy, especially for peak predictions. I need to consider exploring different models, adding more relevant variables, tuning hyperparameters, and ensuring high-quality data for better performance.
---

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%2011.png" alt="SEAP" width="600" height="378" />
- The model performs reasonably well, with random residual distribution and no evident patterns.
- Presence of outliers suggests room for improvement in prediction accuracy.

---

<img src="https://github.com/PoeMadara/Sustainable-Energy-Analysis-Platform/blob/main/outputs/output%208.png" alt="SEAP" width="10000" height="778" />

**General Interpretation:**

- **Good overall fit:** The model's predictions (red line) are close to the actual values (blue line) for most cases.
- **Variability in accuracy:** Some discrepancies, especially at peak times, suggest the model struggles with high-precision predictions during these periods.
- **Seasonal patterns:** Evident in solar and wind generation, reflecting their dependence on weather conditions.

---

## Future Directions

Looking ahead, my goal is to advance this work by developing an **Artificial Intelligence** system capable of managing larger datasets through **Deep Learning** techniques. This AI will not only provide predictions but also facilitate interactive communication, empowering users to discuss energy-related challenges and propose actionable solutions for a more sustainable future.
To augment the capabilities of this AI, I plan to integrate **APIs** that deliver real-time data feeds, allowing the system to continuously update and refine its understanding of energy dynamics. By leveraging these data streams, the AI will be positioned to analyze trends, identify inefficiencies, and recommend improvements, ultimately contributing to the creation of smarter energy management solutions.

## Acknowledgements

Thank you to **Ironhack Bootcamp** for the invaluable knowledge gained and to my mentors, **Santiago, Antonio,** and **Nicolás**, for their exceptional guidance and support.
