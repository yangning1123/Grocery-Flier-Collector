from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_ica_flier_url() -> str:
    # The following options are required to make headless Chrome
    # work in a Docker container
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_argument("--no-sandbox")

    # Initialize a new browser
    browser = webdriver.Chrome(options=chrome_options)

    flier_url = 'https://www.e-magin.se/latestpaper/pg99xpgh/paper/1#/paper/ff88hxh0/1'
    browser.get(flier_url)
    # browser.find_element(By.XPATH, '//*[@id="toolbarContainer"]/div[3]/div/button[3]/div[1]').click()
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="toolbarContainer"]/div[3]/div/button[3]/div[1]'))).click()

    pdf_url = browser.current_url
    return pdf_url


if __name__ == '__main__':
    print(get_ica_flier_url())

