import os

# Set the environment variable
os.environ["GROQ_API_KEY"] = "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"

from groq import Groq

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
    stream=False,
)

print(chat_completion.choices[0].message.content)
