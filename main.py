''' Correr api localmente con uvicorn main:app --reload'''
''' Llamar Online con https://pi01-misael-garcia-torres.onrender.com'''
''' Modificar con https://dashboard.render.com/web/srv-cnos3i6d3nmc73do7n9g/deploys/dep-cnosgdud3nmc73do9em0'''

# librerias utilizadas
import pandas as pd
from fastapi import FastAPI

# Creación de API
app = FastAPI()

# lectura de los datos
df_PlayTimeGenre = pd.read_csv('df_PlayTimeGenre.csv')
df_UserForGenre = pd.read_csv('df_UserForGenre.csv')
df_UsersRecommend = pd.read_csv('df_UsersRecommend.csv')
df_UsersNotRecommend = pd.read_csv('df_UsersNotRecommend.csv')
df_sentiment_analysis = pd.read_csv('df_sentiment_analysis.csv')

# Endpoints de la API

# @profile
@app.get('/PlayTimeGenre/{genre}')
async def PlayTimeGenre(genre: str):
    '''
    Debe devolver año con mas horas jugadas para dicho género.
    '''
    # Filtrar el DataFrame por el género proporcionado
    df_genre = df_PlayTimeGenre[df_PlayTimeGenre['genre'] == genre]

    # Calcular la suma de las horas jugadas para cada año
    df_sum_by_year = df_genre.groupby('año')['horas_jugadas'].sum().reset_index()

    # Encontrar el año con la suma más alta de horas jugadas
    year_with_most_playtime = df_sum_by_year.loc[df_sum_by_year['horas_jugadas'].idxmax()]

    # Devolver el año con más horas jugadas para el género dado
    # Devolver el año con más horas jugadas para el género dado
    # Devolver el año con más horas jugadas para el género dado
    return {"Año de lanzamiento con más horas jugadas para Género {}: {}".format(genre, year_with_most_playtime['año'].item())}

@app.get('/UserForGenre/{genre}')
async def UserForGenre(genre: str):
    '''
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
    Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
    '''
    # Filtrar el DataFrame por el género proporcionado
    df_genre = df_UserForGenre[df_UserForGenre['genre'] == genre]

    # Encontrar el usuario con más horas jugadas para el género dado
    user_with_most_playtime = df_genre.groupby('user_id')['horas_jugadas'].sum().idxmax()

    # Filtrar el DataFrame por el usuario con más horas jugadas
    df_user = df_genre[df_genre['user_id'] == user_with_most_playtime]

    # Crear una lista de la acumulación de horas jugadas por año
    hours_played_per_year = df_user.groupby('año')['horas_jugadas'].sum().reset_index().to_dict(orient='records')

    # Devolver el resultado en el formato especificado
    return {"Usuario con más horas jugadas para Género {}:".format(genre): user_with_most_playtime, "Horas jugadas": hours_played_per_year}

@app.get('/UsersRecommend/{year}')
async def UsersRecommend(year: int):
    '''
    Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    '''
    # Filtrar el DataFrame por el año proporcionado y por los juegos recomendados
    df_year = df_UsersRecommend[df_UsersRecommend['año'] == year]

    # Seleccionar los primeros 3 juegos más recomendados
    top_3_games = df_year.head(3).set_index('puesto')['juego'].to_dict()

    # Devolver el resultado en el formato especificado
    return [{"Puesto {}".format(position): game} for position, game in top_3_games.items()]

@app.get('/UsersNotRecommend/{year}')
async def UsersNotRecommend(year: int):
    '''
    Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
    '''
    # Filtrar el DataFrame por el año proporcionado y por los juegos menos recomendados
    df_year = df_UsersNotRecommend[df_UsersNotRecommend['año'] == year]

    # Seleccionar los primeros 3 juegos menos recomendados
    top_3_games = df_year.head(3).set_index('puesto')['juego'].to_dict()

    # Devolver el resultado en el formato especificado
    return [{"Puesto {}".format(position): game} for position, game in top_3_games.items()]

@app.get('/sentiment_analysis/{year}')
async def sentiment_analysis(year: int):
    '''
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
    Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}
    '''
    # Filtrar el DataFrame por el año proporcionado
    df_year = df_sentiment_analysis[df_sentiment_analysis['año'] == year]

    # Calcular la cantidad de registros para cada categoría de sentimiento
    sentiment_counts = df_year.groupby('categoria')['cantidad'].sum().to_dict()

    # Devolver el resultado en el formato especificado
    return sentiment_counts
