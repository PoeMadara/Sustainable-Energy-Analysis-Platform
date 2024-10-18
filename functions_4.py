import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_clean_data(filepath, scale=True):
    '''
    Carga, limpia y escala el dataset.
    '''
    # Cargar el dataset
    df = pd.read_csv(filepath)

    # Mostrar valores nulos antes de limpiar
    print("Valores nulos antes de limpiar:")
    print(df.isnull().sum())

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

    # Verificar valores nulos después de limpiar
    print("Valores nulos después de limpiar:")
    print(df.isnull().sum())

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
def load_and_clean_data(filepath, scale=True, max_len=10):
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

    # Imprimir tipos de datos y contenido del DataFrame
    print("Data types:")
    print(df.dtypes)
    print("\nDataFrame head:")
    print(df.head())

    # Aplicar Tokenizer para convertir las categorías en secuencias de enteros
    categorical_cols = ['country', 'iso_code']
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(df[categorical_cols].astype(str).values.flatten())
    
    # Convertir a secuencias y aplicar padding
    for col in categorical_cols:
        sequences = tokenizer.texts_to_sequences(df[col].astype(str))
        padded_sequences = pad_sequences(sequences, maxlen=max_len)
        df[col] = padded_sequences.tolist()  # Asegúrate de convertir a lista

    # Escalar datos si es necesario
    if scale:
        scaler = StandardScaler()
        columns_to_scale = df.select_dtypes(include=['float64', 'int64']).columns.difference(['year'])
        df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

    return df, tokenizer
'''


'''
def load_and_clean_data(filepath, scale=True, max_len=10):
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

    # Imprimir tipos de datos y contenido del DataFrame
    print("Data types:")
    print(df.dtypes)
    print("\nDataFrame head:")
    print(df.head())

    # Aplicar Tokenizer para convertir las categorías en secuencias de enteros
    categorical_cols = ['country', 'iso_code']
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(df[categorical_cols].astype(str).values.flatten())
    
    # Convertir a secuencias y aplicar padding
    for col in categorical_cols:
        sequences = tokenizer.texts_to_sequences(df[col].astype(str))
        padded_sequences = pad_sequences(sequences, maxlen=max_len)
        df[col] = padded_sequences.tolist()  # Asegúrate de convertir a lista

    # Escalar datos si es necesario
    if scale:
        scaler = StandardScaler()
        columns_to_scale = df.select_dtypes(include=['float64', 'int64']).columns.difference(['year'])
        df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

    return df, tokenizer

'''
