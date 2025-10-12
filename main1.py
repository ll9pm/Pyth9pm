from selenium import webdriver
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import telebot
token_api="6517080417:AAHQx2gxkQ5Sxs2GilTyCaOI4-jJZfIGaho"
bot =telebot.TeleBot(token_api)
def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=2020,1680")
    options.add_argument("--kiosk")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string
apis =[]
for i in range(10):
try:
  url ="https://www.1secmail.cc/en"
  domain="@duckhunt.site"
  password ="7739122alIna77@@"
  rand_name = generate_random_string(15)
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
  filename = "apis1.txt"


  apis.append(token.text)
  bot.send_message("1085837500",f"api {token.text}")

except Exception as e:
   print(e)
bot.send_message("1085837500",f"{apis}")
with open(filename, 'w') as f:
    for api in apis:
      f.writelines(f"{api}")
with open(filename,'r') as doc_file:
     bot.send_document("1085837500 ", doc_file, caption="Here is your document!")
