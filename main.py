import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)


def login(u_name, p_word):
    driver.get("https://test.salesforce.com/")
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "username").send_keys(u_name);
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "password").send_keys(p_word);
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "Login").click();


login("shubhang.vats@addeqa1.com.svqa", "Shubhang@123")

driver.implicitly_wait(40)
driver.find_element(By.XPATH,
                    "//a[contains(@class,'menuTriggerLink slds-button slds-button_icon slds-button_icon slds-button_icon-container slds-button_icon-small slds-global-actions__setup slds-global-actions__item-action')]//div[contains(@class,'tooltip-trigger uiTooltip')]").click();
driver.implicitly_wait(10)
driver.find_element(By.XPATH,
                    "//a[contains(@data-id,'related_setup_app_home')]//div[contains(@class,'slds-col slds-size_10-of-12')]").click()

# Handling new window
p = driver.current_window_handle
chwd = driver.window_handles
for w in chwd:
    # switch focus to child window
    if w != p:
        driver.switch_to.window(w)

driver.find_element(By.XPATH, "//input[@placeholder='Quick Find']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Quick Find']").send_keys("Data Export")

driver.find_element(By.XPATH, "//mark[@class='highlight']").click()
driver.implicitly_wait(30)

iframe = driver.find_element(By.XPATH, "//iframe[@title='Weekly Export Service ~ Salesforce - Enterprise Edition']")
driver.switch_to.frame(iframe)

driver.find_element(By.XPATH, "//input[@title='Export Now']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@title='Start Export']").click()
