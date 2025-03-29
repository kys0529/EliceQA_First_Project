from src.utils import mainLocators
from selenium.webdriver.support import expected_conditions as EC
import time

def autoLogin(driver, wait, userInfo):
    driver.get("https://kdt-pt-1-pj-2-team03.elicecoding.com/signin")
    
    wait.until(EC.presence_of_element_located(mainLocators.MAINP_LOGIN_BTN)).click()
    wait.until(EC.presence_of_element_located(mainLocators.LOGINP_EMAIL_INPUT)).send_keys(userInfo["id"])
    wait.until(EC.presence_of_element_located(mainLocators.LOGINP_PW_INPUT)).send_keys(userInfo["pw"])
    wait.until(EC.presence_of_element_located(mainLocators.LOGINP_GOING_BTN)).click()

    time.sleep(2)