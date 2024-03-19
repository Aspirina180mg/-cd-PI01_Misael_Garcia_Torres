# Proyecto de Ciencia de Datos para Steam

Este proyecto de ciencia de datos se centra en el análisis de datos relacionados con Steam, la plataforma de distribución de videojuegos de Valve Corporation. El objetivo principal es realizar análisis y extracciones de información relevante para la recomendación de juegos al usuario, entregando más valor a su experiencia en la plataforma
 
 (tambien se pueden poner badges https://github.com/badges/shields)
# Tabla de contenidos
1. [Introduction](#introduction)
2. [Some paragraph](#paragraph1)
    1. [Sub paragraph](#subparagraph1)
3. [Another paragraph](#paragraph2)

## This is the introduction <a name="introduction"></a>
Some introduction text, formatted in heading 2 style

## Some paragraph <a name="paragraph1"></a>
The first paragraph text

### Sub paragraph <a name="subparagraph1"></a>
This is a sub paragraph, formatted in heading 3 style

## Another paragraph <a name="paragraph2"></a>
The second paragraph text



1. [Cómo Ejecutar el Proyecto](#ejecutar)
## Requisitos del Sistema
## Guía de uso rápido
## Data Engineering
### Repositorio y Conjuntos de Datos
### Preprocesamiento de Datos
## Análisis de Datos
### Descripción del Proyecto
## Deployment y la API
## Funciones de la API
## Archivos Generados
## Contribuciones y Colaboraciones
## Links
## Licencia
## Contacto
## Menciones y agradecimientos
------------------------------------------------------------------------------------------------------------------------------------

## Cómo Ejecutar el Proyecto <a name="ejecutar"></a>

Para ejecutar el proyecto localmente, sigue estos pasos:

1. Clona el repositorio desde [GitHub](https://github.com/soyHenry/PI_ML_OPS/tree/PT?tab=readme-ov-file).
2. Instala las dependencias del proyecto utilizando el archivo `requirements.txt`.
3. Ejecuta el archivo `PI01_Misael_Garcia_Torres.ipynb` en un entorno de Jupyter Notebook o Google Colab.
4. Explora y ejecuta las celdas según sea necesario para realizar análisis y obtener resultados.

### Requisitos del Sistema
El proyecto se ha desarrollado y probado en un entorno con las siguientes especificaciones:

- Sistema Operativo: Windows 10
- Memoria RAM: 16 GB
- Procesador: Intel Core i7-9700K

## Guía de uso rápido
Hay que redactar una forma rápida de cargar modificaciones a la base de datos y generar resultados que se puedan subir a la api.




## Data Engineering

### Repositorio y Conjuntos de Datos

- El repositorio del proyecto se encuentra disponible en [GitHub](https://github.com/soyHenry/PI_ML_OPS/tree/PT?tab=readme-ov-file).
- Los conjuntos de datos utilizados se encuentran disponibles en [Google Drive](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj).

### Preprocesamiento de Datos

- Se realiza la carga y limpieza de los conjuntos de datos utilizando Python y las siguientes librerías:
  - Pandas
  - NumPy
  - Matplotlib
  - NLTK

## Análisis de Datos

### Descripción del Proyecto

El proyecto se divide en las siguientes secciones principales:

1. **Exploración de Datos:** Análisis inicial de los conjuntos de datos para comprender su estructura y características.
2. **Limpieza de Datos:** Proceso de limpieza y preprocesamiento de los datos para eliminar valores nulos, duplicados y realizar correcciones.
3. **Transformación de Datos:** Conversión de tipos de datos, extracción de información relevante y preparación de los datos para su análisis.
4. **Análisis de Sentimientos:** Utilización de análisis de sentimientos para evaluar las opiniones de los usuarios en las reseñas de juegos.
5. **Generación de Reportes:** Creación de visualizaciones y reportes estadísticos para identificar patrones y tendencias en los datos.

## Deployment y la API
La API puede ser probada en local utilizando uvicorn con el siguiente comando dentro de la carpeta raíz del proyecto:

```bash
uvicorn main:app --reload
```

la API está deployada en Render, cada modificación hecha en el archivo `main.py` se verá de forma automática en uvicor, pero debe ser actualizada manualmente en el Deploy de Render.

## Funciones de la API

El proyecto también incluye la implementación de una API para proporcionar acceso a datos procesados y funcionalidades específicas. Las principales funciones de la API incluyen:

1. **UserForGenre():** Devuelve el año con más horas jugadas para un género específico.
2. **UsersRecommend():** Proporciona información sobre los usuarios que recomiendan un juego.
3. **UsersNotRecommend():** Proporciona información sobre los usuarios que no recomiendan un juego.
4. **SentimentAnalysis():** Realiza análisis de sentimientos en las reseñas de los usuarios.

para más información se puede consultar la documentación de la api en :
Ingresar enlace de Render/Docs

## Archivos Generados

El proyecto genera varios archivos CSV con datos preprocesados y resultados de análisis para su posterior uso y visualización.

- `PlayTimeGenre.csv`: Contiene información sobre el tiempo de juego por género y año.
- Otros archivos CSV generados para cada función de la API con los resultados correspondientes.

## Contribuciones y Colaboraciones

¡Las contribuciones al proyecto son bienvenidas! Si deseas colaborar, no dudes en enviar una solicitud de extracción (pull request) o abrir un problema (issue) en el repositorio de GitHub.

## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Project homepage: https://your.github.com/awesome-project/
- Repository: https://github.com/your/awesome-project/
- Issue tracker: https://github.com/your/awesome-project/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    my@email.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects:
  - Your other project: https://github.com/your/other-project/
  - Someone else's project: https://github.com/someones/awesome-project/


## Licencia

Este proyecto se distribuye bajo la [licencia MIT](https://choosealicense.com/licenses/mit/). Consulta el archivo `LICENSE.txt` para obtener más detalles.


## Contacto

Para obtener más información o realizar preguntas sobre el proyecto, puedes ponerte en contacto con el autor:

- Nombre: Misael García Torres
- Teléfono: +56 931 854 247
- Correo Electrónico: [misagtor@gmail.com)
- LinkedIn: [linkedin.com/in/mgarciat](https://www.linkedin.com/in/mgarciat/)

## Menciones y agradecimientos

Para la realización de este proyecto se utilizaron los conocimientos adquiridos en el Bootcamp de Data Science del Equipo de "[Henry](https://web.soyhenry.com/about-us)", agradezco también a mis TAs Roberto y Rafa, quienes me acompañaron durante todo el proceso, son unos cracks.
