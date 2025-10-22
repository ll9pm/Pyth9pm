import requests
#import json
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
  print(i)
