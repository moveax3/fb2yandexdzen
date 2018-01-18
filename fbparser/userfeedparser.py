import ipdb
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pickle

COOKIE_STORE_FILE = 'facebook.pkl'
SELENIUM_TIMEOUT = 5
SELENOUM_SCROLL_TIMEOUT = 3
SELENIUM_DEFAULT_LOCALE = "en-us"

class FacebookUserFeedParser():

    def __init__(self, user, password, profile_link):
        self.user = user
        self.password = password
        self.profile_link = profile_link
        self.init_selenium()
        if not self.is_login():
            self.login()
        self.open_profile()
        self.parse()
        self.selenium.close()

    def init_selenium(self):
        print('init_selenium')
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", SELENIUM_DEFAULT_LOCALE)
        firefox_profile.update_preferences()
        self.selenium = webdriver.Firefox(firefox_profile=firefox_profile)
        self.selenium.get("http://www.facebook.org")
        self.load_cookies()
        self.selenium.wait = WebDriverWait(self.selenium, SELENIUM_TIMEOUT)


    def login(self):
        print('login')
        elem = self.selenium.find_element_by_id("email")
        elem.click()
        elem.send_keys(self.user)
        elem = self.selenium.find_element_by_id("pass")
        elem.click()
        elem.send_keys(self.password)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.save_cookies()

    def save_cookies(self):
        print('save_cookies')
        pickle.dump(self.selenium.get_cookies(), open(COOKIE_STORE_FILE, "wb"))


    def load_cookies(self):
        print('load_cookies...')
        try:
            cookies = pickle.load(open(COOKIE_STORE_FILE, "rb"))
            print('cookie load successfull')
        except:
            print('no find cookie file')
            return
        print('    cookies:')
        for cookie in cookies:
            print('        '+str(cookie))
            self.selenium.add_cookie(cookie)
        print('end load cookies')

    def is_login(self):
        print('is_login...')
        self.selenium.get('https://www.facebook.com')
        time.sleep(SELENIUM_TIMEOUT)
        if self.selenium.title == "Facebook – log in or sign up":
            print('   NO')
            return False
        else:
            print('   YES')
            return True

    def open_profile(self):
        print("open profile")
        self.selenium.get(self.profile_link)
        time.sleep(SELENIUM_TIMEOUT)

    def parse(self):
        self.scroll_page()
        print("parse")
        self.result = []
        for element in self.selenium.find_elements_by_class_name('fbUserContent'):
            soup = BeautifulSoup(element.get_attribute('innerHTML'), 'html.parser')
            try:
                post_id = soup.find('input', {'name': 'ft_ent_identifier'}).get('value')
            except:
                continue
            #post_date = soup.find('span', {'class': 'timestampContent'}).text
            post_content = soup.find_all('p')
            #final_post_content = self.clean_content(str(post_content))
            final_post_id = int(post_id)
            #self.result.append({'fbid': str(final_post_id), 'fbpost': final_post_content, 'timestamp': post_date})
            self.result.append({'fbid': str(final_post_id), 'fbpost': str(post_content)})
            # '<a href="https://www.facebook.com/gornal/posts/'+str(post_id)+'">MAIN</a>'

    def clean_content(self, page_content):
        page_content = page_content.replace('</p>, <p>', '</p><p>')
        return page_content.replace('[', '').replace(']', '')

    def scroll_page(self):
        print('scroll page')
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
        self.selenium.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SELENOUM_SCROLL_TIMEOUT)
