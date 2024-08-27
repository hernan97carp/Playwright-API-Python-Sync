from tests.testbase import sync_playwright, createNewUserDemoqa

def test_post(playwright: sync_playwright):
    # Genera los datos de usuario, asegurando que incluyen username y password
    data = createNewUserDemoqa()
    
    # Crea el contexto de solicitud
    context = playwright.request.new_context(base_url="https://demoqa.com")
    
    # Realiza la solicitud POST, asegurando que los datos se envían como JSON
    response = context.post(url="/Account/v1/User", data= data)
    
    # Imprime la respuesta
    print(response.status)
    print(response.text())
