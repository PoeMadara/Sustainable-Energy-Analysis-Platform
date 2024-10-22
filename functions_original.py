import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(filepath, scale=True):
    '''
    Carga y limpia el dataset, maneja los valores nulos, selecciona las columnas relevantes,
    escala los datos numéricos y devuelve el dataframe listo para usar.
    '''
    # Cargar el dataset
    df = pd.read_csv(filepath)
    
    # Seleccionar columnas clave (incluso year)
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
    
    # Manejo de valores nulos para columnas numéricas
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    # Escalado de datos (excepto la columna 'year') si se requiere
    if scale:
        scaler = StandardScaler()
        columns_to_scale = df.columns.difference(['year', 'country', 'iso_code'])
        df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
    
    return df



def split_data(df):
    '''
    Divide el dataframe en conjuntos de entrenamiento y prueba.
    
    Parámetros:
    df: DataFrame a dividir.
    
    Devuelve:
    X_train, X_test, y_train, y_test
    '''
    from sklearn.model_selection import train_test_split
    
    # Definir variable objetivo y características
    X = df.drop(columns=['solar_electricity'])  # Variable objetivo: solar_electricity
    y = df['solar_electricity']
    
    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

