from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import time

driver = webdriver.Chrome()
driver.get("https://omerta.com.tr/#/jail.php")
login_link = driver.find_element(By.XPATH, "//a[@data-bs-target='#loginModal']")
login_link.click()
time.sleep(1)
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys("fmbslayer@gmail.com").perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys("yo123Aa!*").perform()
ActionChains(driver).send_keys(Keys.RETURN).perform()

time.sleep(1)
target_text = "Polislerin"
while(True):
    try:
        driver.get("https://omerta.com.tr/index.php#/?module=Crimes")
        time.sleep(1)
        jail = driver.find_elements(By.XPATH, f"//*[contains(text(), '{target_text}')]")
        if jail:
            time.sleep(10)
            continue

        buttons = driver.find_elements(By.CSS_SELECTOR, '.btn.btn-red.btn-bold.btn-big')
        driver.execute_script("arguments[0].click();", buttons[4])
        time.sleep(1)
            
        driver.get("https://omerta.com.tr/index.php#/?module=Cars")
        time.sleep(1)
        jail = driver.find_elements(By.XPATH, f"//*[contains(text(), '{target_text}')]")
        if jail:
            continue
        
        buttons = driver.find_elements(By.CSS_SELECTOR, '.btn.btn-red.btn-bold.btn-big')
        driver.execute_script("arguments[0].click();", buttons[3])

        time.sleep(28)
    except Exception as ex:
        print("exception occured", ex)
        time.sleep(30)

#time.sleep(200)

# Locate the email and password input elements
# Locate the email input element
#email_value = 'fmbslayer@gmail.com
#password = 'uYgWfSH8'
#driver.execute_script(f'var element = document.getElementById("input-mail"); element.value = "fmbslayer@gmail.com";')
#driver.execute_script(f'var element = document.getElementById("input-mailc"); element.value = "W1nSdg80";')
#button_class = "w-100 btn btn-action"  # Replace with the actual class name of the button

# Close the WebDriver
driver.quit()
