import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def load_and_clean_data(filepath):
    """
    Load the dataset and perform basic cleaning, such as handling missing values.
    
    Parameters:
    - filepath: str, path to the dataset

    Returns:
    - df: pandas DataFrame, cleaned dataset
    """
    df = pd.read_csv(filepath)
    df.fillna(0, inplace=True)  # Fill missing values
    return df

def filter_columns(df):
    """
    Filter the DataFrame to retain only specified columns.
    
    Parameters:
    - df: pandas DataFrame
    
    Returns:
    - df_filtered: pandas DataFrame, filtered DataFrame
    """
    columns_to_keep = [
        'solar_electricity', 'wind_electricity', 'biofuel_electricity', 'hydro_electricity',
        'population', 'gdp', 'electricity_demand', 'energy_per_capita', 'energy_per_gdp',
        'solar_consumption', 'wind_consumption', 'biofuel_consumption', 'hydro_consumption',
        'country', 'iso_code'  # Ejemplo de columnas categóricas
    ]
    return df[columns_to_keep]

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def apply_label_encoding(df):
    """
    Apply Label Encoding to categorical columns in the DataFrame.
    
    Parameters:
    - df: pandas DataFrame
    """
    le = LabelEncoder()
    # Aplicar Label Encoding a las columnas categóricas y mantener las columnas originales
    df['country_encoded'] = le.fit_transform(df['country'])
    df['iso_code_encoded'] = le.fit_transform(df['iso_code'])
    
    return df

def plot_correlation_heatmap(df):
    """
    Generate a correlation heatmap from the DataFrame.
    
    Parameters:
    - df: pandas DataFrame
    """
    # Generar la matriz de correlación solo con columnas numéricas
    corr_matrix = df.corr()

    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Matriz de Correlación Mejorada")
    plt.show()

def plot_energy_consumption(df):
    """
    Plot total energy consumption by country.
    
    Parameters:
    - df: pandas DataFrame
    """
    # Columnas de consumo
    consumo_columns = ['solar_consumption', 'wind_consumption', 'biofuel_consumption', 'hydro_consumption']

    # Verificar si 'country' está en el DataFrame
    if 'country' not in df.columns:
        raise KeyError("La columna 'country' no se encuentra en el DataFrame.")

    # Sumar el consumo por país
    df_consumo = df.groupby('country')[consumo_columns].sum().reset_index()

    # Calcular el consumo total de energía para cada país
    df_consumo['total_consumption'] = df_consumo[consumo_columns].sum(axis=1)

    # Filtrar los países con mayor consumo total (por ejemplo, los 10 primeros)
    df_top_countries = df_consumo.nlargest(10, 'total_consumption')

    # Estilo: Gráfico de Barras Horizontales
    plt.figure(figsize=(15, 10))
    df_top_countries.set_index('country')[consumo_columns].plot(kind='barh', stacked=True)
    plt.title('Consumo de energía renovable por países (Top 10)')
    plt.xlabel('Consumo (TWh)')
    plt.ylabel('Países')
    plt.legend(title='Tipo de energía')
    plt.show()


def save_cleaned_data(df, output_filepath):
    """
    Save the cleaned DataFrame to a CSV file.
    
    Parameters:
    - df: pandas DataFrame
    - output_filepath: str, path to save the cleaned dataset
    """
    df.to_csv(output_filepath, index=False)
    print("Archivo limpio guardado en:", output_filepath)
