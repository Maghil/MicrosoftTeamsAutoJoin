import time

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class Driver:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        self.driver.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=f5a5fdce-c4ac-4d32-a953-22a007ba501d&client-request-id=b1ac9b9e-fb8f-40b4-87bb-4a478e7aecf1&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=d2d19ff5-7899-4d44-9019-e3be429e7d6c&domain_hint=&sso_reload=true")

    def wait_until_found(self,sel, timeout):
        try:
            element_present = EC.visibility_of_element_located((By.CSS_SELECTOR, sel))
            WebDriverWait(self.driver, timeout).until(element_present)
            return self.driver.find_element_by_css_selector(sel)

        except exceptions.TimeoutException:
            print("Timeout waiting for element.")
            return None
        
    def signIn(self,email,pwd):
        try:
            #useremail
            login_email = self.wait_until_found("input[type='email']", 30)
            if login_email is not None:
                login_email.send_keys(email)
            # find the element again to avoid StaleElementReferenceException
            login_email = self.wait_until_found("input[type='email']", 5)
            if login_email is not None:
                login_email.send_keys(Keys.ENTER)

            #password
            login_pwd = self.wait_until_found("input[type='password']", 5)
            if login_pwd is not None:
                login_pwd.send_keys(pwd)

            # find the element again to avoid StaleElementReferenceException
            login_pwd = self.wait_until_found("input[type='password']", 5)        
            if login_pwd is not None:
                login_pwd.send_keys(Keys.ENTER)

                keep_logged_in = self.wait_until_found("input[id='idBtn_Back']", 5)
                if keep_logged_in is not None:
                    keep_logged_in.click()

                use_web_instead = self.wait_until_found(".use-app-lnk", 5)
                if use_web_instead is not None:
                    use_web_instead.click()
            return(True)
        except Exception as e:
            print(e)
            return(False)

    def joinMeeting(self):
        try:
            #select calendar
            self.wait_until_found("button[id='app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c']",10).click()
            time.sleep(10)

            time.sleep(5)
            #clicking join on the recent meeting
            el=self.driver.find_elements_by_xpath("//button[contains(text(), 'Join')]")
            el[-1].click()

            time.sleep(3) 
            #selecting audio off
            self.driver.find_element_by_xpath("//span[contains(text(), 'Audio off')]").click()
            return(True)
        except Exception as e :
            print(e)
            return(False)

    def endMeeting(self):
        try:
            self.wait_until_found("svg[class='app-svg icons-call-end']", 10)  
            return(True)

        except Exception as e:
            print(e)
            return(False)