import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(filepath):
    '''
    Carga y limpia el dataset, maneja los valores nulos, selecciona las columnas relevantes,
    escala los datos numéricos y devuelve el dataframe listo para usar.
    
    Parámetros:
    filepath: Ruta del archivo CSV.
    
    Devuelve:
    DataFrame limpio y listo para usar.
    '''
    
    # Cargar el dataset
    df = pd.read_csv(filepath)
    
    # Seleccionar columnas clave (incluso year)
    columns_to_keep = [
        'year', 'solar_consumption', 'wind_consumption', 'biofuel_consumption', 
        'hydro_electricity', 'solar_electricity', 'wind_electricity', 'solar_cons_change_twh', 
        'wind_cons_change_twh', 'biofuel_cons_change_pct', 'solar_share_elec', 'wind_share_elec',
        'population', 'gdp'
    ]
    
    # Filtrar solo las columnas útiles
    df = df[columns_to_keep]
    
    # Manejo de valores nulos (imputación con la media en este caso)
    df = df.fillna(df.mean())
    
    # Escalado de datos (excepto la columna 'year')
    scaler = StandardScaler()
    columns_to_scale = df.columns.difference(['year'])  # Escalamos todo menos 'year'
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
