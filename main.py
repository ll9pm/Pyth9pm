import requests
i#mport json
#import base64
from random import randint

TARGET_URL ="https://www.effectivegatecpm.com/uji4es8pqd?key=da098a0a0bd7ccec9dc42d9bbfcd0f40"#sca_esv=b9187f4daeb51a28&sxsrf=AE3TifPm9_qKH49AUTRmy8KUB3Zfi1pfKg%3A1752523657653&source=hp&ei=iWN1aPirJa_5i-gPnemUmQI&oq=myaiforyou.blogspot&gs_lp=EhFtb2JpbGUtZ3dzLXdpei1ocCITbXlhaWZvcnlvdS5ibG9nc3BvdEjUN1C0B1j6MnABeACQAQGYAZoMoAH3PaoBCTUtMy4xLjMuMbgBA8gBAPgBAvgBAZgCAaACbqgCD8ICBxAjGCcY6gKYA27xBXOEX6WXlLGzkgcDMC4xoAfdA7IHALgHAMIHAzYtMcgHZg&sclient=mobile-gws-wiz-hp"
API_KEY ="dGgBKIuM9fgLUbnmkNcGSCrvinGPyLWe"
SCRAPER_URL= 'https://api.webscrapingapi.com/v1'

PARAMS= {
"api_key":API_KEY,
"url":TARGET_URL,
"country":"us",
"render_js":1,
"device":"desktop",
"wait_for":randint(10000,25000),
"wait_until":"networkidle0",
#"screenshot":1,
#"screenshot_options":'{"full_page ":"1"}',
"js_instructions":'[{"action":"click","selector":"body","timeout":2000}]'

}
for i in range(1000):
	res=requests.get(SCRAPER_URL,params=PARAMS)
  email =rand_name+domain

  driver= web_driver()

  wait = WebDriverWait(driver, 30)
  #start sign up on hasdata
  url_s ="https://app.hasdata.com/sign-up"
  driver.get(url_s)
  sleep(2)
  driver.find_element(By.XPATH,'//*[@id="root"]/div/section/form/div[1]/input').send_keys(email)
  sleep(1)
  driver.find_element(By.XPATH,'//*[@id="root"]/div/section/form/div[2]/div/input').send_keys(password)
  wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/section/form/button'))).click()
  wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/main/div/div[1]/div[2]/div[2]/div[2]/a'))).click()

  wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/main/div/div/div[1]/div[2]/div/div/div/div/p/button'))).click()
  print(email)
  data =f"""
  email => {email}
  password => {password}
  """

  bot.send_message("1085837500",data)

  driver.get(url)
  el=driver.find_element(By.XPATH,'/html/body/header/div[4]/div/div/div')
  driver.execute_script("arguments[0].scrollIntoView(true);", el)
  wait.until(EC.element_to_be_clickable((By.ID,'change_email_btn'))).click()
  sleep(1)
  driver.find_element(By.ID,'random_code_input').send_keys(rand_name)
  sleep(1)
  driver.find_element(By.ID,'change_email').click()
  sleep(2)
  wait_mes=driver.find_element(By.XPATH,'/html/body/section[1]')
  driver.execute_script("arguments[0].scrollIntoView(true);", wait_mes)
  wait.until(EC.element_to_be_clickable((By.ID,'mailbox'))).click()

  sleep(2)
  iframe =driver.find_element(By.ID,'myContent')
  driver.switch_to.frame(iframe)
  url_con=driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/p[3]/a')
  url_act=url_con.get_attribute("href")
  driver.get(url_act)
  sleep(5)
  token=driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div[2]/div[1]/div[1]/p/span')
  


  apis.append(token.text)
  bot.send_message("1085837500",f"api {token.text}")

 except Exception as e:
    print(e)
bot.send_message("1085837500",f"{apis}")
filename = "apis.txt"
with open(filename, 'w') as f:
    for api in apis:
      f.writelines(f"{api}")
with open(filename,'r') as doc_file:
     bot.send_document("1085837500 ", doc_file, caption="Here is your document!")
