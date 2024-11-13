import os
import pandas as pd
import matplotlib.pyplot as plt
from groq import Groq
import time
from collections import Counter
import seaborn as sns

# Configurar la API key de Groq
os.environ["GROQ_API_KEY"] = "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"

# Inicializar el cliente de Groq
client = Groq()

# Diccionario para almacenar las respuestas
data = {"Response": []}

# Único prompt
prompt = "What is a dog?"
modelo = "llama3-groq-8b-8192-tool-use-preview"

# Función para obtener respuesta del LLM
def obtener_respuesta(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=modelo,
            max_tokens=50,  # Respuestas cortas
            stream=False,
            timeout=5
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Error al obtener respuesta: {e}")
        return "Error"

# Obtener 1000 respuestas
for i in range(100):
    response = obtener_respuesta(prompt)
    1
    # Guardar la respuesta en el diccionario
    data["Response"].append(response)
    
    # Mostrar progreso cada 100 respuestas
    if (i + 1) % 100 == 0:
        print(f"Progreso: {i + 1}/1000 respuestas obtenidas.")
    
    # Espera mínima para evitar saturar la API
    time.sleep(0.1)

# Crear un DataFrame con las respuestas
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
output_file = "basic_responses.csv"
df.to_csv(output_file, index=False)
print(f"Respuestas guardadas en el archivo {output_file}")

# Leer el CSV y mostrar las primeras 5 filas
df = pd.read_csv("basic_responses.csv")
print(df.head())


# Paso 2: Procesamiento de texto
# Convertir todas las respuestas a minúsculas
df['Response'] = df['Response'].str.lower()

# Contar la longitud de cada respuesta
df['Length'] = df['Response'].str.len()

# Contar la cantidad de palabras de cada respuesta
df['Word Count'] = df['Response'].str.split().apply(len)

# Paso 3: Generar estadísticas simples
# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df[['Length', 'Word Count']].describe())

# Análisis de las palabras más comunes en las respuestas
all_words = ' '.join(df['Response']).split()
word_freq = Counter(all_words)
most_common_words = word_freq.most_common(10)

print("\nPalabras más comunes:")
for word, freq in most_common_words:
    print(f"{word}: {freq}")

# Paso 4: Crear gráficos
# Gráfico de distribución de la longitud de las respuestas
plt.figure(figsize=(10, 6))
sns.histplot(df['Length'], kde=True, color='skyblue')
plt.title('Distribución de la longitud de las respuestas')
plt.xlabel('Longitud de la respuesta (caracteres)')
plt.ylabel('Frecuencia')
plt.grid()
plt.show()


# Gráfico de palabras más comunes
words, frequencies = zip(*most_common_words)
plt.figure(figsize=(10, 6))
sns.barplot(x=list(words), y=list(frequencies), palette="viridis")
plt.title('Top 10 palabras más comunes')
plt.xlabel('Palabra')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.grid()
plt.show()

