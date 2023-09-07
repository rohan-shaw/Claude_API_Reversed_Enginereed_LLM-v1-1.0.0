from selenium import webdriver
import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
service = ChromeService(executable_path="./chromedriver.exe")
# options.add_experimental_option("detach", True)
driver = uc.Chrome(service=service, options=options)

def Chat():
    driver.get("https://claude.ai/chats")
    driver.maximize_window
    print("[+] Opening Browser")

    time.sleep(15)

    driver.find_element(By.CSS_SELECTOR, 'button[data-testid=login-with-google]').click()

    print("[+] Opening Google SSO Popup")

    time.sleep(12)

    parent_handle = driver.current_window_handle
    # changing the handles to access login page
    for handle in driver.window_handles:
        if handle != parent_handle:
            login_page = handle

    print("[+] Switching to Login Handle")

    driver.switch_to.window(login_page)

    print("[+] Getting Login Token and URL", driver.current_url)

    time.sleep(2)

    print("[+] Sending Email Info")

    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys("nqueryofficial@gmail.com")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
    time.sleep(5)

    print("[+] Sending Password Info")

    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("@NQuery22")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()

    driver.switch_to.window(parent_handle)

    print("[+] Switching To Claude Handle")

    time.sleep(50)

    print("[+] Successfully Logged In")

    driver.find_element(By.CSS_SELECTOR, '#radix-\:rh\: > div > div > fieldset > div.flex.items-center.flex-grow.overflow-x-hidden > div > div > div').send_keys("Hey")

    time.sleep(.5)

    driver.find_element(By.CSS_SELECTOR, '#radix-\:rh\: > div > div > fieldset > div.sc-QdHZx.blyGAo.grid.grid-flow-col.items-center.gap-2.pb-3.place-self-end.-mr-3.sm\:pb-0.sm\:place-self-auto.sm\:mr-0 > div > button').click()

    time.sleep(1)

    response_display = driver.find_element(By.CSS_SELECTOR, 'body > div.sc-jgCDkn.ktjLWq.flex.relative.mx-auto.h-screen > div > div.sc-ioBKGh.jgPhPb.max-w-3xl.mx-auto.px-3.pt-16.pb-4.grid.gap-x-2.gap-y-3 > div:nth-child(4) > div > div.contents > p').is_displayed()

    if response_display:
        response = driver.find_element(By.CSS_SELECTOR, 'body > div.sc-jgCDkn.ktjLWq.flex.relative.mx-auto.h-screen > div > div.sc-ioBKGh.jgPhPb.max-w-3xl.mx-auto.px-3.pt-16.pb-4.grid.gap-x-2.gap-y-3 > div:nth-child(4) > div > div.contents > p').text

    print(response)

    while True:
        input = input("User: ")
        driver.find_element(By.CSS_SELECTOR, 'body > div.sc-jgCDkn.ktjLWq.flex.relative.mx-auto.h-screen > div > div.sc-fGZLLs.bGcCPt.max-w-3xl.w-full.fixed.bottom-0.mx-auto.left-1\/2.-translate-x-1\/2 > div > fieldset > div.flex.items-center.flex-grow.overflow-x-hidden > div > div > div').send_keys(input)

        time.sleep(.5)

        driver.find_element(By.CSS_SELECTOR, 'body > div.sc-jgCDkn.ktjLWq.flex.relative.mx-auto.h-screen > div > div.sc-fGZLLs.bGcCPt.max-w-3xl.w-full.fixed.bottom-0.mx-auto.left-1\/2.-translate-x-1\/2 > div > fieldset > div.sc-1d2d8c9e-4.jPGUnL.grid.grid-flow-col.gap-2.items-center > button').click()

        response_display = driver.find_element(By.CSS_SELECTOR, 'body > div.sc-jgCDkn.ktjLWq.flex.relative.mx-auto.h-screen > div > div.sc-ioBKGh.jgPhPb.max-w-3xl.mx-auto.px-3.pt-16.pb-4.grid.gap-x-2.gap-y-3 > div:nth-child(4) > div > div.contents > p').is_displayed()

        if response_display:
            response = driver.find_element(By.CSS_SELECTOR, 'body > div.sc-jgCDkn.ktjLWq.flex.relative.mx-auto.h-screen > div > div.sc-ioBKGh.jgPhPb.max-w-3xl.mx-auto.px-3.pt-16.pb-4.grid.gap-x-2.gap-y-3 > div:nth-child(4) > div > div.contents > p').text

        print(response)

        time.sleep(.5)

if __name__ == "__main__":
    Chat()
    driver.quit()
