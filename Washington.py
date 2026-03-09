from playwright.sync_api import sync_playwright
import pandas as pd
import time
import random


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    url="https://adwcatholicschools.org/find-a-school/?fwp_grade_level=preschool&fwp_region=montgomery-county#finder"
    page.goto(url)
    list_button=page.locator('//a[@data-show="listing"]')
    list_button.click()
    random=random.randint(0,5)

    time.sleep(random)



    no=page.locator('//h4[@class="school-listing__school-title"]//a').count()
    print(no)
    link=[]
    for i in range(no):
        links = page.locator('//h4[@class="school-listing__school-title"]//a').nth(i)
        Links=links.get_attribute('href')

        link.append(
            Links
        )
    print(link)
    data=[]
    for l in link:
        page.goto(l)
        time.sleep(random)
        try:
           Name=page.locator('//div[@class="hero__content"]//h1').inner_text()
        except:
            Name=page.locator('//div[@class="basic-content__wysiwyg-content wysiwyg-content"]//h1').inner_text()

        email=page.locator('//div[@class="school-detail__field-value"]//a').first
        Email=email.get_attribute('href')


        phone=page.locator('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div[3]/div[2]').inner_text()
        Website=page.locator('//div[@class="school-detail__field-value"]//a').last
        Address=page.locator('//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]').inner_text()
        Website_link=Website.get_attribute('href')
        data.append({
            "Name":Name,
            "Address":Address,
            "Phone No":phone,
            "Emails":Email,
            "Website":Website_link
        })

        df=pd.DataFrame(data)
        df.to_csv('Washington.csv',index=False)

        print("done")



