from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def bing_search(query):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    result_titles = []

    try:
        driver.get("https://www.bing.com")
        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
        search_box.send_keys(query)
        search_box.send_keys("\n")

        results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.b_algo h2"))
        )
        result_titles = [result.text for result in results]
    finally:
        driver.quit()

    return result_titles

if __name__ == "__main__":
    print(bing_search("planets"))
