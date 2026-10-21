import pytest
import os
from playwright.sync_api import sync_playwright
from login_page import LoginPage

@pytest.fixture(scope="function")
def page(request):
    # Executa em modo Headless (segundo plano)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        yield page
        
        # Se o teste falhar, salva um print na pasta /screenshots
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{request.node.name}_falha.png")
            
        browser.close()

# Hook do Pytest para monitorar o status (sucesso/falha) de cada teste
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# Scenario 1: Login com sucesso
def test_login_sucesso(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in page.url

# Scenario 2: Login com credenciais inválidas
def test_login_usuario_invalido(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("usuario_inexistente", "senha_errada")
    assert login_page.error_message.is_visible()
    assert "Username and password do not match" in login_page.error_message.inner_text()