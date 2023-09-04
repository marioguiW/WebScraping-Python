from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

options = Options();

options.add_argument('window-size=1280,768')

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

navegador.get("https://app.melibox.com.br/advProductPosition")

inputEmail = navegador.find_element(By.NAME, "email");
inputSenha = navegador.find_element(By.NAME, "password");

inputEmail.send_keys("Nelson.wilhelms@gmail.com");
inputSenha.send_keys("caraio123");
inputSenha.submit();

sleep(3)

inputTagProduto = navegador.find_element(By.NAME, "textoPesquisa");
inputTagProduto.send_keys("Retrovisor S10")
buttonEnviar = navegador.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div[1]/div/div/button[1]")
buttonEnviar.click();


sleep(4)


elemento_img = navegador.find_element(By.XPATH, '//*[@id="analiticoFindPosAdViewRetorno"]/table/tbody/tr[2]/td[9]/small[2]/img')
elemento_img1 = navegador.find_element(By.XPATH, '//*[@id="analiticoFindPosAdViewRetorno"]/table/tbody/tr[3]/td[9]/small[2]/img')



elemento_img1.click()

sleep(3)

elemento_info = navegador.find_element(By.XPATH, '//*[@id="btnResumo"]');

elemento_info.click()

sleep(2)

page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

titulo = site.find('div', attrs={'class': 'col col-10'})
valor = site.find('span', attrs={'style': 'color:white;'})

textoCompleto = titulo.get_text(strip=True)
parte_desejada = textoCompleto.split('(')[0].strip()
paragrafoDescricao = site.find('p' ,attrs={'style' :'font-size: 13px;'})
infosImportantes = paragrafoDescricao.find_all('strong')

data = infosImportantes[0]
diasAtivo = infosImportantes[1]
visitasTotais = infosImportantes[2]
visitasDiarias = infosImportantes[3]
taxaConversao = infosImportantes[4].find('span', attrs={"color" :"green"})

print("titulo : ",parte_desejada )
print("preço : ", valor.decode_contents())
print("data : ", data.decode_contents())
print("dias ativos: ", diasAtivo.decode_contents())
print("total de visitas : ", visitasTotais.decode_contents())
print("visitas diarias : ", visitasDiarias.decode_contents())
print("taxa de conversão : ", taxaConversao.decode_contents() + '% ')



input("aa")