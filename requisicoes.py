from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

i = 2;

idAnuncios = []
data = []
diasAtivo = []
visitasTotais = []
visitasDiarias = []
taxaConversao = []
titulos = []
valor = []
url = []

pyautogui.scroll(-10000)
sleep(2)
pyautogui.scroll(-10000)
sleep(2)
pyautogui.scroll(-10000)
sleep(2)
pyautogui.scroll(-10000)
sleep(2)
pyautogui.scroll(-10000)
sleep(2)
pyautogui.scroll(-10000)
sleep(2)
pyautogui.scroll(-10000)

pyautogui.scroll(+10000)
sleep(2)
pyautogui.scroll(+10000)
sleep(2)
pyautogui.scroll(+10000)
sleep(2)
pyautogui.scroll(+10000)
sleep(2)
pyautogui.scroll(+10000)
sleep(2)
pyautogui.scroll(+10000)
sleep(2)
pyautogui.scroll(+10000)



while(i < 50):
    print("teste", i)
    xpath = f'//*[@id="analiticoFindPosAdViewRetorno"]/table/tbody/tr[{i}]/td[5]/small'
    vendas = navegador.find_element(By.XPATH, xpath).text
    if vendas == 'De 51 a 100' or vendas == 'De 26 a 50' or vendas == 'De 101 a 150' or vendas == 'De 151 a 250' or vendas == 'De 251 a 500':
        print("encontrou")
        xpathImg = f'//*[@id="analiticoFindPosAdViewRetorno"]/table/tbody/tr[{i}]/td[9]/small[2]/img'
        xpathUrl = f'//*[@id="analiticoFindPosAdViewRetorno"]/table/tbody/tr[{i}]/td[9]/small[4]/a'
        xpathTitulo = f'//*[@id="analiticoFindPosAdViewRetorno"]/table/tbody/tr[{i}]/td[2]/small'
        xpathId = f'//*[@id="analiticoFindPosAdViewRetorno"]/table/tbody/tr[{i}]/td[1]/small'
        
        titulo = navegador.find_element(By.XPATH, xpathTitulo)
        idAnuncio = navegador.find_element(By.XPATH, xpathId)

        elementoUrl = navegador.find_element(By.XPATH, xpathUrl).get_attribute('href')
        elemento_img = navegador.find_element(By.XPATH, xpathImg)
        elemento_img.click()
        print("clicou")
        sleep(4)
        elemento_info = navegador.find_element(By.XPATH, '//*[@id="btnResumo"]');
        elemento_info.click()
        sleep(2)


        page_content = navegador.page_source
        site = BeautifulSoup(page_content, 'html.parser')
       

        paragrafoDescricao = site.find('p' ,attrs={'style' :'font-size: 13px;'})

        infosImportantes = paragrafoDescricao.find_all('strong')


        idAnuncios.append(idAnuncio.text)
        titulos.append(titulo.text);
        valor.append(site.find('span', attrs={'style': 'color:white;'}))
        data.append(infosImportantes[0])
        diasAtivo.append(infosImportantes[1])
        visitasTotais.append(infosImportantes[2])
        visitasDiarias.append(infosImportantes[3])
        taxaConversao.append(infosImportantes[4].find('span', attrs={"color" :"green"}))
        url.append(elementoUrl)

        pyautogui.press('esc')
          # scroll down 10 "clicks"

        i = i + 1;
    else:
        sleep(2)
        pyautogui.scroll(-80)
        print("nao encontro")
        i = i+ 1;
print("fim")

j = 1;
m = 3
i = 1
while(i < 2):
    k = m;
    while(k < 52):
        print("teste", i)
        xpath = f'//*[@id="lazyloading"]/table[{j}]/tbody/tr[{k}]/td[5]/small'
        vendas = navegador.find_element(By.XPATH, xpath).text
        print(vendas)
        if vendas == 'De 51 a 100' or vendas == 'De 26 a 50' or vendas == 'De 101 a 150' or vendas == 'De 151 a 250' or vendas == 'De 251 a 500':
            print("encontrou")
            xpathImg = f'//*[@id="lazyloading"]/table[{j}]/tbody/tr[{k}]/td[9]/small[2]/img'
            xpathUrl = f'//*[@id="lazyloading"]/table[{j}]/tbody/tr[{k}]/td[9]/small[4]/a'
            xpathTitulo = f'//*[@id="analiticoFindPosAdViewRetorno"]/table/tbody/tr[{i}]/td[2]/small'
            xpathId = f'//*[@id="analiticoFindPosAdViewRetorno"]/table[{j}]/tbody/tr[{i}]/td[1]/small'
        
            titulo = navegador.find_element(By.XPATH, xpathTitulo) 
            idAnuncio = navegador.find_element(By.XPATH, xpathId)
            
            elementoUrl = navegador.find_element(By.XPATH, xpathUrl).get_attribute('href')
            elemento_img = navegador.find_element(By.XPATH, xpathImg)
            elemento_img.click()
            print("clicou")
            sleep(4)
            elemento_info = navegador.find_element(By.XPATH, '//*[@id="btnResumo"]');
            elemento_info.click()
            sleep(2)

            
            page_content = navegador.page_source
            site = BeautifulSoup(page_content, 'html.parser')


            paragrafoDescricao = site.find('p' ,attrs={'style' :'font-size: 13px;'})

            infosImportantes = paragrafoDescricao.find_all('strong')
            
            print("----------")
            print(elementoUrl)
            print("----------")

            titulos.append(titulo.text);
            valor.append(site.find('span', attrs={'style': 'color:white;'}))
            data.append(infosImportantes[0])
            diasAtivo.append(infosImportantes[1])
            visitasTotais.append(infosImportantes[2])
            visitasDiarias.append(infosImportantes[3])
            taxaConversao.append(infosImportantes[4].find('span', attrs={"color" :"green"}))
            url.append(elementoUrl)

            pyautogui.press('esc')
            # scroll down 10 "clicks"

            i = i + 1;
            k = k + 1
        else:
            sleep(2)
            pyautogui.scroll(-80)
            print("nao encontro")
            i = i+ 1;
            k = k + 1;
    j = j + 1
    m = m + 1
print("fim")


sleep(3)



i = 0;

while(i < 150):
    print("")
    print("---------------------------------------------")
    print("id : ", idAnuncios[i])
    print("titulo : ",titulos[i])
    print("preço : ", valor[i].decode_contents())
    print("data : ", data[i].decode_contents())
    print("dias ativos: ", diasAtivo[i].decode_contents())
    print("total de visitas : ", visitasTotais[i].decode_contents())
    print("visitas diarias : ", visitasDiarias[i].decode_contents())
    print("taxa de conversão : ", taxaConversao[i].decode_contents() + '% ')
    print("url : ", url[i])
    print("---------------------------------------------")
    i = i+1


input("aa")