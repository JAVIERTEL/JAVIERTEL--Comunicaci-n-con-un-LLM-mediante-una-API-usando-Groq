# Análisis de Texto utilizando Groq y Python

## Descripción

Este proyecto utiliza **Groq** para obtener respuestas automáticas a un prompt específico. Las respuestas se almacenan en un archivo CSV, se procesan, y se analizan utilizando **Python**. Finalmente, se generan gráficos que muestran estadísticas descriptivas de las respuestas obtenidas.

## Requisitos

- **Cuenta en Groq**: Necesitas crear una cuenta en [Groq](https://www.groq.com).
- **API Key de Groq**: Debes generar una API Key para poder hacer solicitudes.
- **Python 3.x** instalado.
- **Librerías necesarias**:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `groq`

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```
### 2. Instalar las librerías requeridas

```bash
pip install pandas matplotlib seaborn groq
```
### 3. Obtener API Key de Groq
1. Visita Groq y crea una cuenta o inicia sesión.
2. Navega a la sección de configuración de tu cuenta para generar una API Key.
3. Copia tu API Key.

### 4. Configurar la API Key en el script

En el código, reemplaza "tu_api_key_aqui" con tu API Key:

```bash
os.environ["GROQ_API_KEY"] = "tu_api_key_aqui"
```

## Ejecución

Para ejecutar el script, sigue estos pasos:

```bash
python main.py
```
## El script realizará las siguientes acciones:
1. Obtener respuestas automáticas: Envía un prompt a Groq y guarda 100 respuestas en un archivo CSV.
2. Procesar los datos: Realiza operaciones de limpieza y cálculo de estadísticas.
3. Visualizar gráficos: Muestra gráficos sobre la longitud de las respuestas y las palabras más comunes.



