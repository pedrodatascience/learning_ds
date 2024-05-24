import timeit
from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio


url = "https://www.google.com/"
inicio = timeit.default_timer()

# configuração do webdriver do selenium
def create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless=new')
    return webdriver.Chrome(options=chrome_options)

driver = create_driver()

cotacao_euro = []
cotacao_dolar = []

#Pesquisa por "euro"
async def euro():    
    driver.get(url)
    try:
        digita_pesquisa = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
        digita_pesquisa.send_keys("euro")
        clica_pesquisa = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
        clica_pesquisa.click()
        extrai_euro= driver.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
        texto = extrai_euro.text
        cotacao_euro.append(texto)
        await asyncio.sleep(1) 
              
    except:
        print("Falha ao fazer a raspagem")

#Pesquisa por "dolar"
async def dolar():
    driver.get(url)
    try:        
        digita_pesquisa = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
        digita_pesquisa.send_keys("dolar")
        clica_pesquisa = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
        clica_pesquisa.click()
        extrai_dolar= driver.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
        texto = extrai_dolar.text
        cotacao_dolar.append(texto)
        await asyncio.sleep(2)               
    except:
        print("Falha ao fazer a raspagem")

#configuração para utilizar o asyncio
async def main():
    await asyncio.gather(euro(), dolar())

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
finally:
    driver.quit()
    loop.close()

           
print(f'valor do euro: {cotacao_euro} | valor do dolar: {cotacao_dolar}') #printa os valores da cotação
fim = timeit.default_timer()
print('duracao: %f'  %(fim - inicio)) #calcula o tempo gasto do início ao fim do script

