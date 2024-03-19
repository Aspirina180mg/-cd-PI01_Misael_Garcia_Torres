# Proyecto de Ciencia de Datos para Steam

Este proyecto de ciencia de datos se centra en el análisis de datos relacionados con la plataforma de distribución de videojuegos Steam, propiedad de Valve Corporation. El objetivo principal es realizar análisis y extracciones de información relevante para mejorar la experiencia del usuario y las operaciones de la plataforma.

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

## Funciones de la API

El proyecto también incluye la implementación de una API para proporcionar acceso a datos procesados y funcionalidades específicas. Las principales funciones de la API incluyen:

1. **UserForGenre():** Devuelve el año con más horas jugadas para un género específico.
2. **UsersRecommend():** Proporciona información sobre los usuarios que recomiendan un juego.
3. **UsersNotRecommend():** Proporciona información sobre los usuarios que no recomiendan un juego.
4. **SentimentAnalysis():** Realiza análisis de sentimientos en las reseñas de los usuarios.

## Archivos Generados

El proyecto genera varios archivos CSV con datos preprocesados y resultados de análisis para su posterior uso y visualización.

- `PlayTimeGenre.csv`: Contiene información sobre el tiempo de juego por género y año.
- Otros archivos CSV generados para cada función de la API con los resultados correspondientes.

## Cómo Ejecutar el Proyecto

Para ejecutar el proyecto localmente, sigue estos pasos:

1. Clona el repositorio desde [GitHub](https://github.com/soyHenry/PI_ML_OPS/tree/PT?tab=readme-ov-file).
2. Instala las dependencias del proyecto utilizando el archivo `requirements.txt`.
3. Ejecuta el archivo `PI01_Misael_Garcia_Torres.ipynb` en un entorno de Jupyter Notebook o Google Colab.
4. Explora y ejecuta las celdas según sea necesario para realizar análisis y obtener resultados.

## Requisitos del Sistema

El proyecto se ha desarrollado y probado en un entorno con las siguientes especificaciones:

- Sistema Operativo: Windows 10
- Memoria RAM: 16 GB
- Procesador: Intel Core i7-9700K

## Contribuciones y Colaboraciones

¡Las contribuciones al proyecto son bienvenidas! Si deseas colaborar, no dudes en enviar una solicitud de extracción (pull request) o abrir un problema (issue) en el repositorio de GitHub.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

## Contacto

Para obtener más información o realizar preguntas sobre el proyecto, puedes ponerte en contacto con el autor:

- Nombre: Misael García Torres
- Teléfono: +56 931 854 247
- Correo Electrónico: [misagtor@gmail.com)
- LinkedIn: [linkedin.com/in/mgarciat](https://www.linkedin.com/in/mgarciat/)

¡Gracias por tu interés en este proyecto! Esperamos que sea útil y beneficioso para la comunidad de Steam y la ciencia de datos en general.
