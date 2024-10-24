# Energy Efficiency and Demand in Clean Energy Transitions.
The Sustainable Energy Analysis Platform employs machine learning and deep learning to enhance the evaluation of sustainable energy practices. It integrates diverse data sources to assess energy consumption, efficiency, and the impact of renewable sources, aiding in informed decision-making for sustainable initiatives.

# Final Project: Energy Efficiency and Demand in Clean Energy Transitions

## Introduction

In this project, I focused on analyzing and predicting trends in energy generation and consumption, with a specific focus on sustainable energy sources such as solar, wind, hydroelectric, and biofuel. My goal was to evaluate the efficiency of these renewable energy sources and predict future energy demands, helping to understand the impact of clean energy transitions on global energy consumption.

## Data Overview

I worked with a dataset that covers global energy data for up to 130 years, including variables like energy generation, energy demand, GDP, population, and various other economic and energy-related indicators. After initial exploration, I decided to focus on the following columns for my analysis:

```python
columns_to_keep = [
    'year', 'country', 'iso_code', 'population', 'gdp', 'electricity_demand',
    'electricity_generation', 'electricity_share_energy',
    'energy_cons_change_twh', 'energy_per_capita', 'energy_per_gdp', 
    'solar_consumption', 'wind_consumption', 'biofuel_consumption', 'biofuel_electricity', 
    'hydro_electricity', 'solar_electricity', 'wind_electricity', 
    'solar_cons_change_twh', 'wind_cons_change_twh', 
    'biofuel_cons_change_pct', 'solar_share_elec', 'wind_share_elec'
]
```

I specifically focused on renewable energy variables such as solar, wind, hydroelectric, and biofuel electricity to assess their growth and impact.

## Data Cleaning and Preprocessing

Data cleaning was an essential step. I cleaned and standardized the raw dataset from "owid-energy-data.csv" to ensure consistency across all countries and time periods. This included handling missing values, normalizing numerical columns, and encoding categorical variables like 'iso_code' and 'country'. To avoid excessive one-hot encoding, which would create too many columns, I opted for label encoding combined with embedding layers for categorical features in my deep learning model.

The cleaned dataset was saved as 'data_cleaned.csv', which I used in the subsequent modeling phase.

## Machine Learning Model: Random Forest

For the machine learning model, I used a **Random Forest** algorithm to predict energy generation from solar, wind, hydroelectric, and biofuel sources. Random Forest was a good choice due to its ability to handle large datasets with multiple features and its effectiveness in regression tasks. I trained the model using the `MultiOutputRegressor` wrapper to handle the multiple output variables.

### Model Performance

The model achieved the following results:

- **MAE (Mean Absolute Error):** 0.01
- **RMSE (Root Mean Squared Error):** 0.12
- **R² (R-Squared):** 0.99

The high R² score (0.99) indicates that the model explains 99% of the variance in the target variables, which means that it fits the data extremely well. The low MAE (0.01) and RMSE (0.12) further confirm that the model makes very accurate predictions, with minimal error.

**Best Parameters:**  
The best hyperparameters I obtained through GridSearch were as follows:

```python
best_params = {
    'estimator__max_depth': None,
    'estimator__min_samples_split': 2,
    'estimator__n_estimators': 100
}
```

These parameters suggest that the Random Forest model benefits from an unlimited tree depth and a higher number of estimators (trees). The use of the `min_samples_split` set to 2 ensures that the model captures even the smallest details in the dataset.

## Deep Learning Model

In addition to Random Forest, I implemented a **Deep Learning model** using a neural network for multivariable prediction. I used Keras with TensorFlow as the backend, experimenting with different architectures to optimize the model's performance.

### Key Improvements

To improve the performance and speed of the deep learning model, I applied several techniques:
1. **Normalization and Standardization:** This helped scale the features, improving both training stability and accuracy.
2. **Regularization:** I used dropout and L2 regularization to prevent overfitting and make the model more generalizable.
3. **Architecture Optimization:** I tested different numbers of layers and neurons, and found that adding more layers and neurons initially improved performance. However, beyond a certain point, adding more complexity did not bring significant gains and actually slowed down training.
4. **ReLU Activation:** I used the ReLU activation function to ensure non-negative predictions, which is important for energy generation predictions.
5. **Cross-validation:** To further validate the model's performance, I applied cross-validation to ensure robustness across different subsets of the data.

### Final Deep Learning Model Performance

The deep learning model also performed well, although not as fast as the Random Forest model. I saved the trained model as 'final_model.keras' for future use. This model is capable of making highly accurate multivariable predictions for energy generation from renewable sources.

## Statistical Analysis and Visualization

Beyond prediction, I performed a comprehensive statistical analysis to understand the relationships between different energy sources and other economic factors. For example, I generated correlation matrices to visualize how different energy sources like solar and wind electricity relate to GDP, population, and energy demand.

The correlation matrix revealed interesting insights:

- **Solar and Wind Electricity:** Both had a strong positive correlation with electricity generation and GDP, indicating that wealthier countries tend to generate more renewable energy.
- **Biofuel and Hydroelectric:** These sources showed moderate correlations with electricity demand but were more country-specific in their impact.

I also created time-series visualizations to show the growth of renewable energy over time, particularly highlighting the rapid increase in solar and wind generation in recent years. These visualizations helped me better understand the long-term trends and the potential future of clean energy transitions.

## Conclusion

Overall, this project provided valuable insights into the potential of renewable energy sources. The machine learning and deep learning models I developed are highly effective in predicting future trends in energy generation, and the statistical analysis allowed me to understand the key drivers of renewable energy growth. The results suggest that with continued investment in clean energy technologies, renewable sources like solar and wind will play an increasingly important role in meeting global energy demand.

I plan to extend this work by exploring additional factors that could influence energy demand, such as government policies, technological advancements, and environmental factors. By incorporating more real-time data and experimenting with alternative models, I hope to further refine my predictions and contribute to the development of sustainable energy solutions.
