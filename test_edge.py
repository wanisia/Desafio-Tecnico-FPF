from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Importa o módulo para adicionar delays

# Configurando o WebDriver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

def preencher_campos(driver, v1, v2, v3):
    # Localiza os campos pelo atributo "name" e preenche os valores com um delay de 10 segundos entre cada campo
    driver.find_element(By.NAME, "V1").clear()
    driver.find_element(By.NAME, "V1").send_keys(v1)
    time.sleep(2)  # Delay de 2 segundos

    driver.find_element(By.NAME, "V2").clear()
    driver.find_element(By.NAME, "V2").send_keys(v2)
    time.sleep(2)  # Delay de 2 segundos

    driver.find_element(By.NAME, "V3").clear()
    driver.find_element(By.NAME, "V3").send_keys(v3)
    time.sleep(2)  # Delay de 2 segundos

    # Clica no botão "Identificar"
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

try:
    # Abre o site
    driver.get("http://www.vanilton.net/triangulo/")
    print("Site carregado com sucesso!")

    # Aguarda os elementos estarem disponíveis
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "V1")))

    # Cenário 1: Triângulo Equilátero
    print("Testando triângulo Equilátero...")
    preencher_campos(driver, "10", "10", "10")

    # Aguarda e verifica a mensagem exibida
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Equilátero")
    )
    print("Resultado: Triângulo Equilátero identificado corretamente!")

    # Cenário 2: Triângulo Isósceles
    print("Testando triângulo Isósceles...")
    preencher_campos(driver, "15", "7", "7")

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Isósceles")
    )
    print("Resultado: Triângulo Isósceles identificado corretamente!")

    # Cenário 3: Triângulo Escaleno
    print("Testando triângulo Escaleno...")
    preencher_campos(driver, "5", "10", "15")

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Escaleno")
    )
    print("Resultado: Triângulo Escaleno identificado corretamente!")

# Cenário FE 01: Soma dos lados 1 e 2 é menor que o lado 3
    print("Testando soma dos lados 1 e 2 menor que o lado 3...")
    preencher_campos(driver, "4", "6", "12")
    try:
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "os valores digitados não formam um triângulo")
        )
        print("Resultado: Soma dos lados menor que o lado 3 identificada corretamente!")
    except Exception:
        print("Teste falhou: O sistema não retornou a mensagem esperada para soma dos lados 1 e 2 menor que o lado 3.")

    # Cenário FE 02: Soma dos lados 1 e 2 é igual ao lado 3
    print("Testando soma dos lados 1 e 2 igual ao lado 3...")
    preencher_campos(driver, "3", "4", "7")
    try:
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "os valores digitados não formam um triângulo")
        )
        print("Resultado: Soma dos lados igual ao lado 3 identificada corretamente!")
    except Exception:
        print("Teste falhou: O sistema não retornou a mensagem esperada para soma dos lados 1 e 2 igual ao lado 3.")

    # Cenário FE 03: Campos obrigatórios não preenchidos
    print("Testando campos obrigatórios não preenchidos...")
    preencher_campos(driver, "", "", "")
    try:
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Digite os valores dos vértices")
        )
        print("Resultado: Mensagem de erro exibida para campos obrigatórios não preenchidos!")
    except Exception:
        print("Teste falhou: O sistema não retornou a mensagem esperada para campos obrigatórios não preenchidos.")

except Exception as e:
    print(f"Erro durante o teste: {e}")
finally:
    # Aguardando 3 segundos antes de fechar o navegador
    time.sleep(3)
    driver.quit()
