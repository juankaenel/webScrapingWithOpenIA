import requests
import os

# export API_KEY=YOUR_API_KEY
api_key = os.environ.get("API_KEY")

# La URL de la página que quieres consultar
url = "https://url"

# Realizamos la consulta a la API de OpenAI
response = requests.post(
    "https://api.openai.com/v1/images/generations", 
    verify=False,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    },
    json={
        "model": "image-alpha-001",
        "prompt": f"Consultar precios de celulares en {url}",
        "num_images": 1,
        "size": "256x256",
        "response_format": "url"
    },
    proxies={
    "http": "http://127.0.0.1:8080","https": "http://127.0.0.1:8080"
    }
)

# Verificamos que la consulta haya sido exitosa
print(response.status_code)
if response.status_code == 200:
    # Obtenemos la URL de la imagen generada por la API
    image_url = response.json()["data"][0]["url"]
    # Descargamos la imagen
    image = requests.get(image_url).content
    # Guardamos la imagen en disco
    with open("precios_celulares.jpg", "wb") as f:
        f.write(image)
    print("Imagen descargada con éxito")
else:
    print("Error al realizar la consulta a la API")
