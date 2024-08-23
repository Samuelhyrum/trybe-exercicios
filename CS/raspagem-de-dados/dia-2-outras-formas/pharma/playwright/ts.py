import json
import re
from fuzzywuzzy import fuzz
from playwright.sync_api import sync_playwright
import pandas as pd

def normalizar_texto(texto):
    texto = texto.lower() 
    texto = re.sub(r'[^\w\s]', '', texto) 
    texto = re.sub(r'\s+', ' ', texto)     
    return texto.strip()

def comparar_textos(texto1, texto2):
    return fuzz.ratio(texto1, texto2)

def run_script(ean):
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=True)
        context = browser.new_context()

        # Aba para o primeiro site
        page1 = context.new_page()
        page1.goto('https://consultaremedios.com.br/')
        
        try:
            page1.wait_for_selector('input[type="search"]', timeout=60000)  # Aumenta o tempo de espera para 60 segundos
            page1.fill('input[type="search"]', ean)
            page1.click('button[type="submit"]')
            page1.wait_for_timeout(5000)  # Aumenta o tempo de espera após o clique para 5 segundos
        except Exception as e:
            print(f"Erro ao esperar pelo seletor no primeiro site: {e}")
            page1.screenshot(path='pagina_inicial_erro.png')
            return 'Título não encontrado', 'Título não encontrado'

        # Captura o texto do primeiro site
        try:
            title_1 = page1.locator('h1').text_content()
            if ean == title_1:
                title_1 = page1.locator('h2').nth(0).text_content()
        except Exception as e:
            title_1 = 'Título não encontrado'
            print(f"Erro ao processar o item '{ean}' no primeiro site: {e}")

        # Aba para o segundo site
        page2 = context.new_page()
        page2.goto(f'https://www.google.com/')
        
        try:
            page2.wait_for_selector('textarea[name="q"]', timeout=60000)
            page2.fill('textarea[name="q"]', ean)
            page2.click('input[name="btnK"]')
            page2.wait_for_timeout(5000)
        except Exception as e:
            print(f"Erro ao esperar pelo seletor no segundo site: {e}")
            page2.screenshot(path='pagina_google_erro.png')
            return 'Título não encontrado', 'Título não encontrado'

        # Captura o texto do segundo site
        try:
            title_2 = page2.locator('h3').nth(0).text_content()
        except Exception as e:
            title_2 = 'Título não encontrado'
            print(f"Erro ao processar o item '{ean}' no segundo site: {e}")

        browser.close()
        return title_1, title_2

def verificar_e_salvar_resultados(dados_json):
    resultados = []
    
    for index, item in enumerate(dados_json):
        if index >= 1:
            break
        
        ean = item['referencia']
        print(ean)
        descricao = item['descricao']
        print(descricao)
        
        # Obtém títulos dos sites
        title_1, title_2 = run_script(ean)
        
        # Normaliza os textos
        texto_normalizado1 = normalizar_texto(title_1)
        texto_normalizado2 = normalizar_texto(title_2)
        descricao_normalizada = normalizar_texto(descricao)
        
        # Compara os textos
        similaridade1 = comparar_textos(texto_normalizado1, descricao_normalizada)
        similaridade2 = comparar_textos(texto_normalizado2, descricao_normalizada)
        
        # Adiciona os resultados à lista
        resultados.append({
            'EAN': ean,
            'Título 1': title_1,
            'Título 2': title_2,
            'Descrição': descricao,
            'Similaridade 1': similaridade1,
            'Similaridade 2': similaridade2
        })
    
    # Cria um DataFrame e salva em uma planilha Excel
    df = pd.DataFrame(resultados)
    df.to_excel('resultados.xlsx', index=False)

def read_json():
    nome_arquivo = "duplicados.json"

    try:
        with open(nome_arquivo, "r") as arquivo:
            dados_json = json.load(arquivo)
        if dados_json:
            verificar_e_salvar_resultados(dados_json)
            print("acabou")
        else:
            print("Erro na coleta do EAN.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o JSON do arquivo '{nome_arquivo}'.")

def calcular_similaridade_entre_titulos(df):
    # Função para calcular similaridade entre dois textos
    def calcular_similaridade(row):
        titulo1 = row['Título 1'].lower()
        titulo2 = row['Título 2'].lower()
        return fuzz.ratio(titulo1, titulo2)
    
    # Adiciona uma nova coluna 'Similaridade Títulos' com a similaridade calculada
    df['Similaridade Títulos'] = df.apply(calcular_similaridade, axis=1)
    
    # Salva o DataFrame atualizado em um novo arquivo Excel
    df.to_excel('resultados_com_similaridade.xlsx', index=False)

def ler_e_calcular_similaridade():
    try:
        # Lê o arquivo Excel gerado anteriormente
        df = pd.read_excel('resultados.xlsx')
        calcular_similaridade_entre_titulos(df)
    except FileNotFoundError:
        print("Arquivo 'resultados.xlsx' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

if __name__ == '__main__':
    # Primeiro executa a verificação e salva os resultados
    read_json()
    
    # Em seguida, lê a planilha e calcula a similaridade entre os títulos
    # ler_e_calcular_similaridade()