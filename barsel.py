from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time

driver = webdriver.Chrome()
driver.get("https://barafranca.com/#/jail.php")
login_link = driver.find_element(By.XPATH, "//a[@data-bs-target='#loginModal']")
login_link.click()
time.sleep(1)
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys("fmbslayer@gmail.com").perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys("W1nSdg80").perform()
ActionChains(driver).send_keys(Keys.RETURN).perform()

popup_elements = driver.find_elements(By.CLASS_NAME, "popup-box-wrapper")
highest_probability = -1
selected_element = None

# Iterate through the elements and extract probabilities
for element in popup_elements:
    probability_element = element.find_element(By.CLASS_NAME, "head").find_element(By.TAG_NAME, "h4")
    probability = int(probability_element.text.strip('%'))
    if probability > highest_probability:
        highest_probability = probability
        selected_element = element
if selected_element is not None:
    button = selected_element.find_element(By.TAG_NAME, "button")
    button.click()


time.sleep(1)
target_text = "Cop"
while(True):
    try:
        driver.get("https://barafranca.com/index.php#/?module=Crimes")
        time.sleep(1)
        jail = driver.find_elements(By.XPATH, f"//*[contains(text(), '{target_text}')]")
        if jail:
            time.sleep(10)
            continue

        buttons = driver.find_elements(By.CSS_SELECTOR, '.btn.btn-red.btn-bold.btn-big')
        driver.execute_script("arguments[0].click();", buttons[4])
        time.sleep(1)
            
        driver.get("https://barafranca.com/index.php#/?module=Cars")
        time.sleep(1)
        jail = driver.find_elements(By.XPATH, f"//*[contains(text(), '{target_text}')]")
        if jail:
            continue
        
        popup_elements = driver.find_elements(By.CLASS_NAME, "popup-box-wrapper")
        highest_probability = -1
        selected_element = None

        # Iterate through the elements and extract probabilities
        for element in popup_elements:
            probability_element = element.find_element(By.CLASS_NAME, "head").find_element(By.TAG_NAME, "h4")
            probability = int(probability_element.text.strip('%'))
            print(f"%{probability}")
            if probability > highest_probability:
                highest_probability = probability
                selected_element = element
        if selected_element is not None:
            probability_element = selected_element.find_element(By.CLASS_NAME, "head").find_element(By.TAG_NAME, "h4")
            probability = int(probability_element.text.strip('%'))
            print(f"Selected: %{probability}")

            button = selected_element.find_element(By.CSS_SELECTOR, '.btn.btn-red.btn-bold.btn-big')
            driver.execute_script("arguments[0].click();", button)

        time.sleep(28)
    except Exception as ex:
        print("exception occured", ex)
        time.sleep(30)

driver.quit()
