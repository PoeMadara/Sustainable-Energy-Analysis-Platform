# Sustainable Energy Analysis Platform (SEAP)

*Predicting Future Energy Efficiency and Demand in Clean Energy Transitions Using Machine Learning and Deep Learning Techniques*

## Author

**Carlos Vergara Gámez**  
- [LinkedIn](https://www.linkedin.com/in/carlosvergaragamez)

## Presentation Link

- [Canvas Presentation Link](#)

## Project Overview

The **Sustainable Energy Analysis Platform (SEAP)** is the final project of the Data Analytics Bootcamp at Ironhack, focusing on predicting renewable energy generation trends, including solar, wind, hydroelectric, and biofuel energy. By leveraging **Machine Learning** and **Deep Learning** techniques, the project aims to assess energy efficiency and demand during the transition to clean energy sources.

**Key Models:**
- **Random Forest with GridSearchCV** for Machine Learning.
- **Multi-Layer Perceptron (MLP)** for multivariate time series forecasting in Deep Learning.

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
- **Geopandas** for spatial data analysis.

## Data Source

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

## Machine Learning and Deep Learning Models

### 1. Random Forest with GridSearchCV

**Description:**  
Random Forest combines multiple decision trees for improved predictions, reducing overfitting risks. GridSearchCV optimizes hyperparameters for enhanced performance.

### 2. Multi-Layer Perceptron (MLP)

**Description:**  
An MLP is designed for multivariate time series forecasting, capturing complex patterns in energy data over time.

## Forecasting

The model predicts significant growth in renewable energy sources over the next 50 years, with **hydroelectric** energy expected to grow the fastest, while **biofuel** energy generation is projected to decline.

## Results and Visualizations

### Performance Graphs
<!-- Placeholder for performance metrics graphs -->

### Energy Production Trends
<!-- Placeholder for prediction graphs over time -->

### Interactive Maps
<!-- Placeholder for interactive map visualizations -->

## Future Directions

I aim to develop an **AI** system for managing larger datasets, integrating **APIs** for real-time data analysis to enhance energy management solutions.

## Acknowledgements

Thank you to **Ironhack Bootcamp** for the invaluable knowledge gained and to my mentors, **Santiago, Antonio,** and **Nicolás**, for their exceptional guidance and support.
