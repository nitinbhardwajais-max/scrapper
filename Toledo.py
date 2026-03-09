import time
from playwright.sync_api import sync_playwright
import pandas as pd


with sync_playwright()as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    url = "https://toledodiocese.org/find-a-school?page=1#find-a-results"
    page.goto(url)
    count=page.locator('//article[@class="result-item result-item__find-a"]').count()
    print(count)
    name=page.locator('//div[@class="top-row"]//h3').first
    print(name.inner_text())
    address=page.locator('//article[@class="result-item result-item__find-a"]/p[1]/a[1]').first
    print(address.inner_text())
    phone_no=page.locator('//article[@class="result-item result-item__find-a"]/p[2]/a[1]').first
    print(phone_no.inner_text())
    Website=page.locator('//article[@class="result-item result-item__find-a"]/a').first
    print(Website.get_attribute('href'))
    time.sleep(3)
    schoolss=[]

    next_page=page.locator('//i[@class="fas fa-angle-right"]')
    while True:
        if next_page.is_visible():
            no = 2

            for i in range(count):
                next_page=page.locator('//i[@class="fas fa-angle-right"]').last
                name = page.locator('//div[@class="top-row"]//h3').nth(i)
                Name=name.inner_text()
                address = page.locator('//article[@class="result-item result-item__find-a"]/p[1]/a[1]').nth(i)
                Address= address.inner_text()
                phone_no=page.locator('//article[@class="result-item result-item__find-a"]/p[2]/a[1]').nth(i)
                Phone_No=phone_no.inner_text()
                Website=page.locator('//article[@class="result-item result-item__find-a"]/a').nth(i)
                Websites=Website.get_attribute('href')
                schoolss.append({
                    "Name":Name,
                    "Address":Address,
                    "Phone":Phone_No,
                    "Website":Websites
                })
            df=pd.DataFrame(schoolss)
            df.to_csv("Toledo.csv",index=False)
            next_page.click()
        else:
            print("Done")

    browser.close()








