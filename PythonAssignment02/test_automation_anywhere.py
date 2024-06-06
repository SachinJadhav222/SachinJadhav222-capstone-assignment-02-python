import time
import pytest
import platform
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    # Determine if the platform is Windows
    is_windows_platform = 'Windows' in platform.system()

    # Set the path to your ChromeDriver
    if is_windows_platform:
        chromedriver_path = "drivers/chromedriver-win64/chromedriver.exe"
    else:
        chromedriver_path = "drivers/chromedriver-mac-arm64/chromedriver"

    # Initialize the Chrome driver
    service = Service('drivers/chromedriver-mac-arm64/chromedriver')  # Update with your ChromeDriver path
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_navigate_to_process_discovery(driver):
    # Open the Automation Anywhere website
    driver.get("https://www.automationanywhere.com/")
    # cookie
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='onetrust-accept-btn-handler']")))
    accept_cookie_button = driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    accept_cookie_button.click()

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Products']")))

    # Mouse over on 'Products'
    products_menu = driver.find_element(By.XPATH, "//a[normalize-space()='Products']")
    ActionChains(driver).move_to_element(products_menu).perform()

    # Wait for the dropdown to appear and click on 'Process Discovery'
    process_discovery_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Process Discovery']"))
    )
    process_discovery_link.click()

    # Wait for navigation to complete
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://www.automationanywhere.com/products/process-discovery")
    )

    # Verify the URL
    assert driver.current_url == "https://www.automationanywhere.com/products/process-discovery"

    # Optional: Add more assertions to verify page content
    header = driver.find_element(By.XPATH, "//h1[contains(text(), 'Process Discovery')]")
    assert header.is_displayed()


if __name__ == "__main__":
    pytest.main()
