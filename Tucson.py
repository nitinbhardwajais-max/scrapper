import time
from playwright.sync_api import sync_playwright
import pandas as pd
import random
random=random.randint(0,5)
with sync_playwright()as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    url = "https://diocesetucson.org/schoolfinder"

    page.goto(url)
    time.sleep(random)
    page.wait_for_selector('//div[@class="categoryName ui-accordion-header ui-corner-top ui-accordion-header-collapsed ui-corner-all ui-state-default ui-accordion-icons"]')
    main=page.locator('//div[@role="tab"]//span')
    count=main.count()
    time.sleep(random)

    data=[]
    for i in range(count):
        print(i)
        main.nth(i).click()
        print("z")
        inner=page.locator('//li[@class="site"]')
        count_inner=inner.count()
        for j in range(count_inner):
            print(j)
            inner.nth(j).click()
            name=page.locator('//div[@class="title"]//div').nth(j)
            address=page.locator('//a[@class="address"]').nth(j)
            phone=page.locator('//a[@class="phoneLink"]').nth(j)
            website=page.locator('//div[@class="website"]//a').nth(j)
            Name=name.inner_text()
            Address=address.inner_text()
            Phone=phone.inner_text()
            Website=website.get_attribute('href')
            print("done")
        data.append({
            "Name":Name,
            "Address":Address,
            "Phone No":Phone,
            "Website":Website
        })
        df=pd.DataFrame(data)
        df.to_csv("Tucson.csv",index=False)








