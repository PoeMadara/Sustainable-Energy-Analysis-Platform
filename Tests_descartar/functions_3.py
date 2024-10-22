import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

def load_and_clean_data(filepath, scale=True):
    '''
    Carga, limpia y escala el dataset.
    '''
    # Cargar el dataset
    df = pd.read_csv(filepath)

    # Seleccionar columnas clave
    columns_to_keep = [
        'year', 'country', 'iso_code', 'population', 'gdp', 'electricity_demand',
        'electricity_generation', 'electricity_share_energy',
        'energy_cons_change_twh', 'energy_per_capita', 'energy_per_gdp', 
        'solar_consumption', 'wind_consumption', 'biofuel_consumption', 'biofuel_electricity', 
        'hydro_electricity', 'solar_electricity', 'wind_electricity', 
        'solar_cons_change_twh', 'wind_cons_change_twh', 
        'biofuel_cons_change_pct', 'solar_share_elec', 'wind_share_elec'
    ]
    
    # Filtrar solo las columnas útiles
    df = df[columns_to_keep]

    # Manejar valores nulos para columnas numéricas
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Aplicar Label Encoding a las columnas categóricas
    categorical_cols = ['country', 'iso_code']
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Escalar datos si es necesario
    if scale:
        scaler = StandardScaler()
        columns_to_scale = df.columns.difference(['year'])
        df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

    return df

'''
def split_data(df):
    ''
    Divide el dataframe en características y variable objetivo.
    ''
    # Variables predictoras (X) y objetivo (y)
    X = df.drop(columns=['solar_electricity'])
    y = df['solar_electricity']

    # Dividir los datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

'''

def save_clean_data(df, filepath):
    '''
    Guarda el dataframe limpio en un archivo CSV.
    '''
    df.to_csv(filepath, index=False)








# Functions original sin gráficos

'''

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_and_clean_data(filepath, scale=True):
    ''
    Carga, limpia y escala el dataset.
    ''
    # Cargar el dataset
    df = pd.read_csv(filepath)

    # Seleccionar columnas clave
    columns_to_keep = [
        'year', 'country', 'iso_code', 'population', 'gdp', 'electricity_demand',
        'electricity_generation', 'electricity_share_energy',
        'energy_cons_change_twh', 'energy_per_capita', 'energy_per_gdp', 
        'solar_consumption', 'wind_consumption', 'biofuel_consumption', 'biofuel_electricity', 
        'hydro_electricity', 'solar_electricity', 'wind_electricity', 
        'solar_cons_change_twh', 'wind_cons_change_twh', 
        'biofuel_cons_change_pct', 'solar_share_elec', 'wind_share_elec'
    ]

    # Filtrar solo las columnas útiles
    df = df[columns_to_keep]

    # Manejar valores nulos para columnas numéricas
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Aplicar One-Hot Encoding a las columnas categóricas
    categorical_cols = ['country', 'iso_code']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Verificar los tipos de datos después de la transformación
    print("Data types after encoding:")
    print(df.dtypes)

    # Escalar datos si es necesario
    if scale:
        scaler = StandardScaler()
        columns_to_scale = df.columns.difference(['year'])
        df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

    return df

def split_data(df):
    ''
    Divide el dataframe en características y variable objetivo.
    ''
    from sklearn.model_selection import train_test_split

    # Variables predictoras (X) y objetivo (y)
    X = df.drop(columns=['solar_electricity'])
    y = df['solar_electricity']

    # Dividir los datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def save_clean_data(df, filepath):
    ''
    Guarda el dataframe limpio en un archivo CSV.
    ''
    df.to_csv(filepath, index=False)

'''


'''

import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def load_trained_model(filepath):

    return joblib.load(filepath)

def plot_predictions_vs_actual(model_path, X_test, y_test, target_columns):
    # Cargar el modelo entrenado
    model = load(model_path)
    
    # Realizar predicciones
    y_pred = pd.DataFrame(model.predict(X_test), columns=target_columns)

    # Graficar las predicciones vs valores reales
    for col in target_columns:
        plt.figure(figsize=(10, 6))
        plt.scatter(y_test[col], y_pred[col], alpha=0.5)
        plt.plot([y_test[col].min(), y_test[col].max()], [y_test[col].min(), y_test[col].max()], 'k--', lw=2)
        plt.xlabel(f"Valores Reales de {col}")
        plt.ylabel(f"Predicciones de {col}")
        plt.title(f"Predicciones vs Valores Reales para {col}")
        plt.show()

def plot_feature_importance(importances, feature_names):

    feature_importances = pd.DataFrame(importances, index=feature_names, columns=["Importance"]).sort_values("Importance", ascending=False)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=feature_importances["Importance"].head(10), y=feature_importances.index[:10])
    plt.title("Importancia de las características")
    plt.xlabel("Importancia")
    plt.ylabel("Características")
    plt.show()

def plot_time_series(df, energy_columns, country_col='country'):

    for country in df[country_col].unique():
        country_data = df[df[country_col] == country]
        for energy in energy_columns:
            plt.figure(figsize=(10, 6))
            plt.plot(country_data['year'], country_data[energy], label=f'{energy} en {country}')
            plt.title(f'{energy} a lo largo del tiempo en {country}')
            plt.xlabel('Año')
            plt.ylabel(energy)
            plt.legend()
            plt.show()

'''
