import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# 1. Teste simples de GET (Dia 1-2 da apostila)
def test_get_all_posts():
    response = requests.get(BASE_URL)
    
    # Validações / Asserções
    assert response.status_code == 200, f"Esperado 200, mas retornou {response.status_code}"
    assert len(response.json()) > 0, "A lista de posts veio vazia"

# 2. Teste no formato Pytest buscando por ID (Dia 3-4 da apostila)
def test_get_post_by_id():
    post_id = 1
    response = requests.get(f"{BASE_URL}/{post_id}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == post_id
    assert "userId" in data
    assert "title" in data

# 3. Teste Negativo (Cenário de Erro - Recurso não encontrado)
def test_get_non_existent_post():
    response = requests.get(f"{BASE_URL}/999999")
    
    # Espera-se um status code 404 (Not Found)
    assert response.status_code == 404