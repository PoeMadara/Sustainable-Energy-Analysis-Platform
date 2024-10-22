import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

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
    '''
    Divide el dataframe en características y variable objetivo.
    '''
    from sklearn.model_selection import train_test_split
    
    # Variables predictoras (X) y objetivo (y)
    X = df.drop(columns=['solar_electricity'])
    y = df['solar_electricity']
    
    # Dividir los datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test


def save_clean_data(df, filepath):
    '''
    Guarda el dataframe limpio en un archivo CSV.
    '''
    df.to_csv(filepath, index=False)

