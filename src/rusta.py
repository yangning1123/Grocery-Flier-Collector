import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_rusta_flier(pdf_name: str):
    # The following options are required to make headless Chrome
    # work in a Docker container
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_argument("--no-sandbox")

    # Initialize a new browser
    browser = webdriver.Chrome(options=chrome_options)

    flier_url = 'https://view.publitas.com/rusta-bladet?publitas_embed=maximized'
    browser.get(flier_url)
    element = browser.find_element(By.ID, "downloadAsPdf")

    pdf_url = element.get_attribute('href')

    response = requests.get(pdf_url)
    with open(pdf_name, "wb") as f:
        f.write(response.content)


if __name__ == '__main__':
    get_rusta_flier('/tmp/fliers/Rusta/202450.pdf')

