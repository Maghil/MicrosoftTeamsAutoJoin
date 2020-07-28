import time
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



def wait_until_found(sel, timeout):
    try:
        element_present = EC.visibility_of_element_located((By.CSS_SELECTOR, sel))
        WebDriverWait(driver, timeout).until(element_present)

        return driver.find_element_by_css_selector(sel)
    except exceptions.TimeoutException:
        print("Timeout waiting for element.")
        return Nonene
    
def signin():
    #useremail
    login_email = wait_until_found("input[type='email']", 30)
    if login_email is not None:
        login_email.send_keys("2017pecit268@panimalarengg.onmicrosoft.com")
    # find the element again to avoid StaleElementReferenceException
    login_email = wait_until_found("input[type='email']", 5)
    if login_email is not None:
        login_email.send_keys(Keys.ENTER)

    #password
    login_pwd = wait_until_found("input[type='password']", 5)
    if login_pwd is not None:
        login_pwd.send_keys("Iamjust16")

    # find the element again to avoid StaleElementReferenceException
    login_pwd = wait_until_found("input[type='password']", 5)        
    if login_pwd is not None:
        login_pwd.send_keys(Keys.ENTER)

        keep_logged_in = wait_until_found("input[id='idBtn_Back']", 5)
        if keep_logged_in is not None:
                keep_logged_in.click()

        use_web_instead = wait_until_found(".use-app-lnk", 5)
        if use_web_instead is not None:
            use_web_instead.click()

def joinMeeting():

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    driver = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
    driver.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fpackage%2Fgo&state=fde2fa59-c3fc-463a-95b6-eaa16bbfc542&client-request-id=3b4a8dab-8203-46a6-909c-2176c5c6933b&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=11ea4c65-414a-4f32-9a25-4abc901a14b5&domain_hint=&sso_reload=true")
    signin()
    joinMeeting()


