# Sustainable Energy Analysis Platform (SEAP)

*Predicting Future Energy Efficiency and Demand in Clean Energy Transitions Using Machine Learning and Deep Learning Techniques*

## Author

**Carlos Vergara Gámez**  
- [LinkedIn](https://www.linkedin.com/in/carlosvergaragamez)

## Presentation Link

- [Canvas Presentation Link](#)


## Project Overview

The **Sustainable Energy Analysis Platform (SEAP)** is the final project of the Data Analytics Bootcamp at Ironhack. This project focuses on predicting the future of renewable energy generation, including solar, wind, hydroelectric, and biofuel energy. By leveraging both **Machine Learning** and **Deep Learning** techniques, the goal is to assess energy efficiency and demand during the transition to clean energy sources over the coming decades.

Key models used in this project:
- **Random Forest with GridSearchCV** for Machine Learning.
- **Multi-Layer Perceptron (MLP)** for multivariate time series forecasting in Deep Learning.

Both models aim to forecast renewable energy trends and facilitate the analysis of sustainable energy development, making the project a valuable tool for energy policymakers and stakeholders.

## Objectives

- Predict future energy production trends for different renewable sources.
- Analyze energy demand and efficiency in clean energy transitions.
- Provide interactive visualizations to explore the data and prediction results.
- Develop advanced AI models to enable real-time energy insights.

## Technologies Used

This project leverages the following technologies and libraries:

- **Python** for data processing, analysis, and model implementation.
- **Pandas** and **NumPy** for data manipulation and analysis.
- **Matplotlib** and **Seaborn** for data visualization.
- **Scikit-Learn** for Machine Learning models (Random Forest, GridSearchCV).
- **TensorFlow/Keras** for Deep Learning models (Multivariate Time Series).
- **Geopandas** and **Shapely** for spatial data analysis and interactive maps.
- **Plotly** for interactive visualizations.
- **Joblib** for saving Machine Learning models.
- **Folium** for map visualizations.

## Data Source

The dataset used for this research comes from:

> Ritchie, H., Rosado, P., & Roser, M. (2023). *Energy*. Published online at **OurWorldinData.org**. Retrieved from: [https://ourworldindata.org/energy](https://ourworldindata.org/energy) [Online Resource]

This resource provided comprehensive energy data, allowing for thorough analysis and robust predictions in the project.


## Repository Structure

- **SEAP_01_EDA_map_and_cleaning.ipynb**: Exploratory Data Analysis and cleaning process, including map visualizations of energy consumption and production across countries.
- **SEAP_02_Machine_Learning_and_Deep_Learning.ipynb**: Implementation of Machine Learning and Deep Learning models for energy prediction.

## Usage Instructions

1. Ensure you have cloned the repository and installed the environment:
   ```bash
   conda env create -f ml-dp.yml
   conda activate ml-dp
   ```

2. Download the necessary folders:
   - `data`: Contains the cleaned and raw energy datasets used in this analysis.
   - `shapefiles`: Contains the shapefiles for interactive map visualizations.

3. Open and run the two Jupyter Notebooks:
   - `SEAP_01_EDA_map_and_cleaning.ipynb`: Run this notebook to visualize the initial analysis and clean data.
   - `SEAP_02_Machine_Learning_and_Deep_Learning.ipynb`: Execute this notebook to train and save the Machine Learning and Deep Learning models.

4. The generated Machine Learning models and interactive maps will be automatically saved in the appropriate folders (`final_models` and `maps`).


## Machine Learning and Deep Learning Models:

### 1. Machine Learning Model: Random Forest with GridSearchCV

**Description:**  
The Random Forest model consists of multiple decision trees, each contributing a prediction, with the final output being the average of all predictions. As a "bagging" method, Random Forest reduces the risk of overfitting often seen in individual decision trees. In this project, GridSearchCV was employed to find the best hyperparameters, such as maximum tree depth and the number of estimators, ensuring the model is optimized for predicting renewable energy generation.

**Justification:**  
I chose Random Forest for its ability to handle high-dimensional data and its robustness against overfitting, which is crucial for multivariable prediction problems. It is a fast and efficient model that captures complex relationships between features without extensive manual data adjustments. Additionally, GridSearchCV automates hyperparameter optimization for optimal performance.


### 2.  Deep Learning Model: Multi-Layer Perceptron (MLP) for Time Series Forecasting

**Description:**  
The Multi-Layer Perceptron (MLP) is a feedforward neural network with multiple layers of neurons, where each layer transforms input data using non-linear activation functions. This MLP is specifically designed to predict multivariate time series, capturing patterns in renewable energy data over time and across various sources (solar, wind, hydro, biofuel). This approach is suitable for making continuous predictions on sequential and temporal data.

**Justification:**  
I opted for the MLP because energy generation data is structured as a multivariate time series, where future values depend on past ones. MLPs effectively model these complex dependencies and are more flexible than traditional time series methods, allowing for the capture of non-linear relationships between variables. Furthermore, neural networks can be adjusted to enhance accuracy through experimentation with architecture and hyperparameters, which is essential for the prediction level sought in this project.


## Forecasting

The forecasting model predict substantial growth in renewable energy sources over the next 50 years. **Hydroelectric energy** is expected to grow the fastest, supported by technological advancements that enhance efficiency. **Solar** and **wind energy** will also see significant increases due to rising investments and adoption.

Conversely, **biofuel energy generation** is projected to decline, reflecting a global shift towards cleaner technologies and changing consumer preferences. The MLP model's ability to analyze complex data patterns allows for accurate projections, providing valuable insights for stakeholders to adapt and invest strategically in the evolving energy landscape.


## Results and Visualizations

Below, space is reserved for future graphs and visualizations. This will include performance metrics of the models and interactive maps representing energy trends.

### Performance Graphs
<!-- Placeholder for performance metrics graphs (e.g., RMSE, MAE, R2) -->

### Energy Production Trends
<!-- Placeholder for energy prediction graphs over time -->

### Interactive Maps
<!-- Placeholder for interactive map visualizations -->

## Final Conclusions

In this project, both the **Random Forest/GridSearchCV (Machine Learning)** and **Multi-Layer Perceptron for Multivariate Time Series Forecasting (Deep Learning)** models demonstrated their effectiveness in predicting renewable energy generation.

### Performance Overview
- **Random Forest Model**: This model exhibited notable strengths, particularly in training speed and prediction accuracy. Its capability to handle high-dimensional data and capture complex interactions among features resulted in low error rates, establishing it as a reliable choice for this analysis. However, indications of overfitting were observed, which can be addressed through careful tuning of parameters such as `max_depth`, `min_samples_split`, and `min_samples_leaf`.
- **Time Series Model**: Although slightly slower in training, this model also delivered satisfactory results. Neural networks are adept at modeling intricate relationships within data, and this project underscored their potential in energy predictions. There remains ample opportunity for further optimization, particularly through hyperparameter tuning and experimentation with diverse architectures.

### Final Conclusions on Renewable Energy Forecasting
The analysis predicts a promising outlook for renewable energy sources over the next 50 years. Hydroelectric energy is expected to lead in growth, followed by significant increases in solar and wind energy. Conversely, biofuel generation is anticipated to decline steadily. This trend reflects a broader commitment to cleaner and more sustainable energy solutions as the transition away from fossil fuels progresses. To actualize this potential, it is crucial to implement supportive government policies, foster technological advancements in efficiency and storage, and invest in infrastructure, all while ensuring equitable benefits during the energy transition.

### Future Directions
Looking ahead, my goal is to advance this work by developing an **Artificial Intelligence** system capable of managing larger datasets through **Deep Learning** techniques. This AI will not only provide predictions but also facilitate interactive communication, empowering users to discuss energy-related challenges and propose actionable solutions for a more sustainable future.
To augment the capabilities of this AI, I plan to integrate **APIs** that deliver real-time data feeds, allowing the system to continuously update and refine its understanding of energy dynamics. By leveraging these data streams, the AI will be positioned to analyze trends, identify inefficiencies, and recommend improvements, ultimately contributing to the creation of smarter energy management solutions.

### Summary
While the current models have performed admirably, addressing overfitting in the Random Forest model and optimizing the deep learning model are key steps for enhancement. This vision of a conversational, data-driven AI specialized in energy solutions presents an exciting avenue for future exploration.

## Acknowledgements

I would like to express my heartfelt gratitude to **Ironhack Bootcamp** for all the invaluable knowledge and skills I've acquired throughout this journey. The experience has not only been educational but also incredibly enriching on a personal level. 

A special thanks to my amazing mentors, **Santiago, Antonio,** and **Nicolás**, whose guidance and support have been instrumental in my learning process. Your insights and encouragement have motivated me to push my limits and strive for excellence.
