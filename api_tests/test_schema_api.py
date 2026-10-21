import requests
from jsonschema import validate

BASE_URL = "https://jsonplaceholder.typicode.com/posts/1"

# Definição do Schema esperado para o recurso Post
post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

def test_post_schema_validation():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    
    # Lança exceção se a estrutura do JSON não corresponder ao schema definido
    validate(instance=response.json(), schema=post_schema)