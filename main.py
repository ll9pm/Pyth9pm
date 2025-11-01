

from time import sleep
from random import randint
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
   playwright =  sync_playwright().start()
   browser =  playwright.chromium.connect_over_cdp("wss://browser.scrapeless.com/browser?token=sk_jRXfVrBSwsQ3SlpKTbXt1r6NWy2jvjj3a51BAwbrJZ09l8vp1Rzu1ohZEDNZIZNd&session_name=sdk_test&session_ttl=180&session_recording=True&proxy_country=US")
   page =  browser.contexts[0].new_page()
   page.goto("https://viikqoye.com/dc/?blockID=399132")
   sleep(randint(10,25))

   #await page.screenshot(path="screenshot.png", full_page=True)# end session
   browser.close()
   playwright.stop()
with sync_playwright() as playwright:
    run(playwright)
