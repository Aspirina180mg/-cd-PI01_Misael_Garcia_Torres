# Commented out IPython magic to ensure Python compatibility.
# %autosave 60
#from google.colab import drive
#drive.mount('/content/drive', force_remount = True)
# %cd /content/drive/MyDrive/Github/PI01_Misael_Garcia_Torres

"""**Importación de librerías y descarga de recursos necesarios para el proyecto:**

*   `zipfile` para desempaquetar archivos .zip.
*   `gzip` para procesar archivos .gz.
*   `json` para procesar archivos .json.
*   `pandas` para realisar análisis de datos.
*   `numpy` para realisar cálculos matemáticos y estadísticos.
*   `matplotlib` para realisar gráficos de los datos.
*   `ast` para evaluar expresiones literales.
*   `nltk`, `SentimentIntensityAnalyser` y descarga del `vader_lexicon` para realizar análisis de sentimientos.
"""

import zipfile, gzip, json, ast, nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

"""**Extracción de ficheros del archivo PI MLOps - STEAM.zip.**"""

zipfile.ZipFile('PI MLOps - STEAM.zip', 'r').extractall()

"""**Definición de funciones extraer_json y extraer_ast, que ayudarán con la extracción de datos de los archivos .gz:**


*   `extraer_json()` hace uso de la función `json.loads()` para hacer la carga de datos al DataFrame.
*   `extraer_ast()` hace uso de la función `ast_literal_eval()` para hacer la carga de datos al DataFrame.
"""

def extraer_json(ruta):
    with gzip.open(ruta, 'rb') as archivo:
        data = [json.loads(line) for line in archivo]
    return pd.DataFrame(data)

def extraer_ast(ruta):
    with gzip.open(ruta, 'rb') as archivo:
        data = [ast.literal_eval(line.decode('utf-8')) for line in archivo]
    return pd.DataFrame(data)

"""**Importación de datos a sus respectivos DataFrames.**

(adicionalmente se han creado archivos de backup de los dataframes originales)
"""

df_juegos = extraer_json('PI MLOps - STEAM/steam_games.json.gz')
df_juegos_backup = df_juegos.copy()
df_reviews = extraer_ast('PI MLOps - STEAM/user_reviews.json.gz')
df_reviews_backup = df_reviews.copy()
df_items = extraer_ast('PI MLOps - STEAM/users_items.json.gz')
df_items_backup = df_items.copy()

"""**Limpieza de DataFrames.**
*   Registros totalmente vacíos.
*   Registros duplicados.
"""

''' para depuración, eliminar al enviar a prod'''
if not df_juegos_backup.empty:
    df_juegos = df_juegos_backup.copy()

if not df_reviews_backup.empty:
    df_reviews = df_reviews_backup.copy()

if not df_items_backup.empty:
    df_items = df_items_backup.copy()

df_juegos.dropna(how="all", inplace=True)
df_reviews.dropna(how="all", inplace=True)
df_items.dropna(how="all", inplace=True)
df_juegos.drop_duplicates(subset=['title'], inplace=True)
df_reviews.drop_duplicates(subset=['user_id'], inplace=True)
df_items.drop_duplicates(subset=['user_id'], inplace=True)

"""**Modificaciones aplicadas para manejo de errores:**

*   Reemplazo de datos faltantes y erroneos en `df_juegos.publisher` por valor nulo ("none").
*   Reemplazo de datos faltantes en `df_juegos.genres` por valor nulo ("[ ]").
*   Reemplazo de datos faltantes en `df_juegos.app_name` por valor correspondiente en `df_juegos.title`.
*   Reemplazo de datos faltantes en `df_juegos.title` por el valor correspondiente `df_juegos.app_name`.
*   Reemplazo de datos faltantes en `df_juegos.url` por valor nulo ("").
*   Corrección de datos incorrectos en `df_juegos.release_date` al formato (año-mes-día).
*   Reemplazo de Datos faltantes e inválidos en `df_juegos.release_date` por la fecha de creación de steam (2003-09-12).
*   Reemplazo de datos faltantes en `df_juegos.tags` por valor nulo ("[ ]").
*   Reemplazo de datos faltantes en `df_juegos.reviews_url` por el enlace a la página oficial de Steam ("https://store.steampowered.com").
*   Reemplazo de datos faltantes en `df_juegos.specs` por valor nulo ("[ ]").
*   Reemplazo de datos faltantes en `df_juegos.price` por "-1", mientras que "Free", "Free to play" y variaciones se identificaron con "0".
*   Reemplazo de datos faltantes en `df_juegos.developer` por un valor nulo ("[ ]").
*   Eliminción de registro si `df_juegos.app_name` y `df_juegos.title` no presentan datos.
*   Conversión de los datos en `df_juegos.id` a valores numéricos
*   Corrección de datos faltantes en `df_juegos.id`, creando nuevas "id" continuando la numeración máxima del registro.
*   cambio de nombre de columna de `df_juegos.id` de "id" a "item_id"
*   Unión y ordenamiento (alfabético) de `df_juegos.tags` y `df_juegos.genres`, se mantendrá sólo `df_juegos.tags`
*   Ordenamiento de `df_juegos.specs` por orden alfabético
<br><br>
*   Desempaquetado de datos de `df_reviews.reviews`, creando las columnas `df_reviews.funny`, `df_reviews.posted`, `df_reviews.last_edited`, `df_reviews.item_id`, `df_reviews.helpful`, `df_reviews.recommend` y `df_reviews.review`, además, se elimina la columna original `df_reviews.reviews`.
*   Reemplazo de datos de `df_reviews.funny` por sólo valores numéricos.
*   Reemplazo de valores vacío en `df_reviews.last_edited` por "not edited".
<br><br>
*   Desempaquetado de datos de `df_items.items`, creando las columnas `df_items.item_id`, `df_items.item_name`, `df_items.playtime_forever` y `df_items.playtime_2weeks`, además, se elimina la columna original `df_items.items`.
"""

# Manejo de datos faltantes
df_juegos['publisher'].fillna('(none)', inplace=True)
df_juegos['publisher'].replace('-', '(none)', inplace=True)
df_juegos['publisher'].replace('---', '(none)', inplace=True)
df_juegos['genres'].fillna('[]', inplace=True)
df_juegos['app_name'].fillna(df_juegos['title'], inplace=True)
df_juegos['title'].fillna(df_juegos['app_name'], inplace=True)
df_juegos['url'].fillna('', inplace=True)
df_juegos['release_date'] = pd.to_datetime(df_juegos['release_date'], format='%d.%m.%Y', errors='coerce').dt.strftime('%Y-%m-%d')
#df_juegos['release_date'].fillna('2003-09-12', inplace=True)
df_juegos['release_date'].fillna('', inplace=True)
df_juegos['tags'].fillna('', inplace=True)
df_juegos['reviews_url'].fillna('https://store.steampowered.com', inplace=True)
df_juegos['specs'].fillna('[]', inplace=True)
df_juegos['price'].fillna(-1, inplace=True)
df_juegos['price'].replace({'Free': 0, 'Free To Play': -0, 'Free Demo': 0, 'Free HITMAN™ Holiday Pack': 0, 'Free Mod': 0, 'Free Movie': 0, 'Free to Play': 0, 'Free to Try': 0, 'Free to Use': 0, 'Install Now': 0, 'Install Theme': 0, 'Play Now': -2, 'Play WARMACHINE: Tactics Demo': 0, 'Play for Free!': 0, 'Play the Demo': 0, 'Starting at $449.00': -2, 'Starting at $499.00': -2, 'Third-party': -2}, inplace=True)
df_juegos['developer'].fillna('[]', inplace=True)

# Eliminación de registro en ausencia de app_name y title
df_juegos.dropna(subset=['app_name', 'title'], how='all', inplace=True)

# conversión de "id" a valores numéricos
df_juegos['id'] = pd.to_numeric(df_juegos['id'], errors='coerce')

# Generación de nuevos "id"
max_id = df_juegos['id'].max()
filas_sin_id = df_juegos[df_juegos['id'].isna()]
nuevas_id = range(int(max_id) + 1, int(max_id) + 1 + len(filas_sin_id))
df_juegos.loc[df_juegos['id'].isna(), 'id'] = nuevas_id

# Cambio de nombre de columna "id"
df_juegos.rename(columns={'id': 'item_id'}, inplace=True)


# Union y ordenamiento de genres y tags
df_juegos['genres'] = df_juegos['genres'].apply(sorted).apply(str)
df_juegos['tags'] = df_juegos['tags'].apply(sorted).apply(str)
df_juegos['tags'] = df_juegos[['genres', 'tags']].agg(' '.join, axis=1)
df_juegos.drop(columns=['genres'], inplace=True)

# Ordenamiento de specs
df_juegos['specs'] = df_juegos['specs'].apply(sorted).apply(str)

# Desempaquetado de columna reviews
reviews_data = []
for index, row in df_reviews.iterrows():
    user_id = row['user_id']
    user_url = row['user_url']
    reviews_data.extend([{'user_id': user_id, 'user_url': user_url, **review_value} for review_value in row['reviews']])
df_reviews = pd.DataFrame(reviews_data)

# Manejo de datos de la columna funny a valores numéricos
df_reviews['funny'] = df_reviews['funny'].replace('', '0')
df_reviews['funny'] = df_reviews['funny'].str.extract('(\d+)').astype(int)

# Manejo de datos faltantes
df_reviews['last_edited'] = df_reviews['last_edited'].replace('', 'Not edited')

# Desempaquetado de columna items
items_data = []
for index, row in df_items.iterrows():
    user_id = row['user_id']
    user_url = row['user_url']
    if 'items' in row and isinstance(row['items'], list):
        items_data.extend([{'user_id': user_id, 'user_url': user_url, **item_value} for item_value in row['items']])
df_items = pd.DataFrame(items_data)

"""**Revisión de tipo de datos por columna**"""

df_juegos.info()

df_reviews.info()

df_items.info()

"""**Según lo visualizado, se harán las siguientes conversiones a los tipos de datos:**
*   `df_juegos.release_date` será cambiado de object a datetime
*   `df_juegos.early_access` será cambiado de object a booleano
*   `df_reviews.item_id` será cambiado de object a integer
*   `df_reviews.recommend` será cambiado de object a booleano
*   `df_items.item_id` será cambiado de object a integer
"""

df_juegos['release_date'] = pd.to_datetime(df_juegos['release_date'], errors='coerce')
df_juegos['early_access'] = df_juegos['early_access'].astype(bool)
df_reviews['item_id'] = df_reviews['item_id'].astype(int)
df_reviews['recommend'] = df_reviews['recommend'].astype(bool)
df_items['item_id'] = df_items['item_id'].astype(int)

"""**Analisis de sentimiento**

Se realiza analisis de sentimiento sobre los reviews en df_reviews.review, los resultados se almacenarán como valores entre -1 y 1, aplicando el lexicón Vader ya que está diseñado para realizar análisis de sentimientos de reseñas considerando el comportamiento en redes sociales y la forma de escritura en las mismas.

(Fuente: https://www.kaggle.com/datasets/nltkdata/vader-lexicon)

**Creación de la columna "sentiment_analysis" en "df_reviews"**
"""

sid = SentimentIntensityAnalyzer()
df_reviews['sentiment_analysis'] = df_reviews['review'].apply(lambda x: sid.polarity_scores(x)['compound'])

"""**Exploración de datos estadísticos de `df_reviews.sentiment_analysis`**
*   Máximo
*   Mínimo
*   Promedio
*   Desviación estándar
*   Varianza
"""

print("Valor Máximo:", df_reviews['sentiment_analysis'].max())
print("Valor Mínimo:", df_reviews['sentiment_analysis'].min())
print("Valor Mediana:", df_reviews['sentiment_analysis'].median())
print("Valor Promedio:", df_reviews['sentiment_analysis'].mean())
print("Desviación Estándar:", df_reviews['sentiment_analysis'].std())
print("Variabilidad:", np.ptp(df_reviews['sentiment_analysis']))

"""**Se observa que los datos están más alineados hacia el lado positivo, esto considerando que el valor máximo es 1 y el valor mínimo es -1, por lo que el punto medio sería 0, y la mediana tiene un valor por sobre el punto medio (0.4588), y el promedio también tiene un valor superior a este (0.345), la varianza es igual al rango (2) de los datos, por lo que la dispersión es notable.**

*   Se realizará un histograma segmentado en 18 bins, para poder identificar patrones y visualizar la distribución más facilmente.
*   Se realizará un diagrama de caja y bigotes para visualizar la dispersión de los datos.
"""

# Histograma
plt.hist(df_reviews['sentiment_analysis'], bins=27, color='green', edgecolor='black')
plt.xlabel('Sentiment Analysis')
plt.ylabel('Frecuencia')
plt.title('Histograma de Sentiment Analysis')
plt.show()

# Diagrama de Caja y bigotes
plt.boxplot(df_reviews['sentiment_analysis'])
plt.ylabel('Sentiment Analysis')
plt.title('Diagrama de Caja y Bigotes de Sentiment Analysis')
plt.show()

"""Desde el histograma es notable que existen 3 divisiones identificables, los valores inferiores a -0.25, los valores superiores a 0.11 y los valores entre estos 2 números.
Dado lo anterior, se clasificarán los reviews de la siguiente manera:
*   Review Positiva: Valores superiores a 0.11 , se les asignará un valor de 2
*   Review Neutral: Valores menores o iguales a 0.11 y mayores o iguales a -0.25, se les asignará un valor de 1
*   Review Negativa: Valores menores a -0.25, se les asignará un valor de 0.

Desde el diagrama de caja y bigotes se puede concluir rápidamente que menos del 25% de las reseñas serían negativas, mientras que más del 50% de ellas está en la categoría de positivas.
"""

conditions = [df_reviews['sentiment_analysis'] > 0.11,
              df_reviews['sentiment_analysis'] < -0.25]
values = [2, 0]
df_reviews['sentiment_analysis'] = np.select(conditions, values, default=1)

"""**Eliminación de la columna "review" en "df_reviews"**"""

df_reviews.drop('review', axis=1, inplace=True)

"""**Según necesidades del desarrollo de la api, se crearán df sólo con las columnas necesarias para cumplir el requerimiento**

df_juegos
*   app_name
*   release_date (sólo el año)
*   tags
*   id

df_items
*   user_id
*   item_id
*   playrime_forever

df_reviews
*   user_id
*   item_id
*   sentiment_analysis
"""

df_juegos = df_juegos.drop('publisher', axis=1)
df_juegos = df_juegos.drop('title', axis=1)
df_juegos = df_juegos.drop('url', axis=1)
df_juegos = df_juegos.drop('reviews_url', axis=1)
df_juegos = df_juegos.drop('specs', axis=1)
df_juegos = df_juegos.drop('price', axis=1)
df_juegos = df_juegos.drop('early_access', axis=1)
df_juegos = df_juegos.drop('developer', axis=1)
df_items = df_items.drop('user_url', axis=1)
df_items = df_items.drop('item_name', axis=1)
df_items = df_items.drop('playtime_2weeks', axis=1)
df_reviews = df_reviews.drop('user_url', axis=1)
df_reviews = df_reviews.drop('funny', axis=1)
df_reviews = df_reviews.drop('posted', axis=1)
df_reviews = df_reviews.drop('last_edited', axis=1)
df_reviews = df_reviews.drop('helpful', axis=1)

"""**Conversión de todos los datos a minúsculas**"""

def convertir_a_minusculas(elemento):
    if isinstance(elemento, str):
        return elemento.lower()
    else:
        return elemento

df_juegos = df_juegos.applymap(convertir_a_minusculas)
df_reviews = df_reviews.applymap(convertir_a_minusculas)
df_items = df_items.applymap(convertir_a_minusculas)

"""**Desarrollo de funciones para API**
*   PlayTimeGenre(), Devuelve el año con más horas acumuladas para un cierto género.
*   UserForGenre(), Devuelve el usuario con más horas acumuladas para un cierto género y una lista de acumulación anual.
*   UsersRecommend(), Devuelve el top 3 de juegos más recomendados.
*   UsersNotRecommend(), Devuele el top 3 de juegos menos recomendados.
*   Sentiment_Analysis(), Devuelve una lista con la cantidad de reseñas positivas, negativas y neutrales.
"""

def PlayTimeGenre(genre: str):
    juegos_por_genero = df_juegos[df_juegos['tags'].str.contains(genre)]
    juegos_con_horas = pd.merge(juegos_por_genero, df_items, on='item_id')
    juegos_con_horas['release_date'] = pd.to_datetime(juegos_con_horas['release_date'])
    juegos_con_horas['release_year'] = juegos_con_horas['release_date'].dt.year
    horas_por_anio = juegos_con_horas.groupby('release_year')['playtime_forever'].sum()
    año_max_horas = horas_por_anio.idxmax()
    resultado = {"Año de lanzamiento con más horas jugadas para " + genre: año_max_horas}
    return resultado

# Ejemplo de uso
print(PlayTimeGenre('action'))




def UserForGenre(genre: str):
  '''
  def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
  '''
  pass

def UsersRecommend(Año: int):
  '''
  def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
  '''
  pass

def UsersNotRecommend(Año: int):
  '''
  def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
  '''
  pass

def Sentiment_Analysis(Año: int):
  '''
  def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
  '''
  pass

import pandas as pd

# Supongamos que el género específico es 'action' (puedes cambiarlo según tus necesidades)
genre = 'action'

# Filtrar juegos del género específico
filtered_juegos = df_juegos[df_juegos['tags'].apply(lambda x: genre in x)]

# Combinar con DataFrame de items para obtener las horas jugadas
merged_data = pd.merge(filtered_juegos, df_items, on='item_id')

# Convertir la columna 'release_date' a tipo datetime
merged_data['release_date'] = pd.to_datetime(merged_data['release_date'])

# Agrupar por año y sumar las horas jugadas
hours_played_by_year = merged_data.groupby(merged_data['release_date'].dt.year)['playtime_forever'].sum()

# Imprimir el resultado
print(hours_played_by_year)

PlayTimeGenre("action")

'''Para depuración, eliminar al enviar a prod'''

# Exportar df_juegos a CSV
df_juegos.to_csv('df_juegos.csv', index=False)

# Exportar df_reviews a CSV
df_reviews.to_csv('df_reviews.csv', index=False)

# Exportar df_items a CSV
df_items.to_csv('df_items.csv', index=False)

df_juegos.head()
