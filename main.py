
from random import randint
# start browser, not to use 'with' context
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    playwright = await async_playwright().start()
    browser = await playwright.chromium.connect_over_cdp("wss://browser.scrapeless.com/browser?token=sk_jRXfVrBSwsQ3SlpKTbXt1r6NWy2jvjj3a51BAwbrJZ09l8vp1Rzu1ohZEDNZIZNd&session_name=sdk_test&session_ttl=180&session_recording=True&proxy_country=US")
    page = await browser.contexts[0].new_page()
    await page.goto("https://viikqoye.com/dc/?blockID=399132",timeout=40)
    await asyncio.sleep(randint(10,25))

    #await page.screenshot(path="screenshot.png", full_page=True)# end session
    await browser.close()
    await playwright.stop()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
for i in range(100):
  asyncio.run(main())
