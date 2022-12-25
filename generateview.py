#open a soundcloud link using selenium and press the play button and let the user enter the song link first

import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import Thread
from lxml.etree import XPathError as XPathEvalError
import random
from fake_useragent import UserAgent


#get soundcloud link from user input
soundcloud_link = input("Please enter the soundcloud link:")
proxylist = input("Please enter the name of the proxy list text file: ")
soundcloud_link = "https://soundcloud.com/iamt0nic/id-iamt0nic-second-release"
optionheadless = input("Do you want to run chrome headless? true/false: ")
#threadscount = input("How many threads do you want to run? ")

random_number = random.randint(25, 35)


#random user agent
#def generate_random_user_agent():
#    ua = UserAgent()
#    
#    return ua['google chrome']


#open the browser using selenium/proxy and press the play button using the soundcloud link URL
def open_browser(soundcloud_link, proxy_list, optionheadless):
    # Read the list of proxies from the text file
    with open(proxy_list, 'r') as f:
        proxies = f.readlines()

    while True:
        try:
            # Choose a random proxy from the list
            proxy = random.choice(proxies)

            # Set up the ChromeOptions object with the proxy
            options = webdriver.ChromeOptions()
            #options.add_argument('--proxy-server={}'.format(proxy))
            #options.add_argument("user-agent=" + generate_random_user_agent())
            options.headless = optionheadless
            options.add_experimental_option("excludeSwitches", ["enable-logging"])

            # Create the ChromeDriver instance with the specified options
            browser = webdriver.Chrome(chrome_options=options)
            browser.get(soundcloud_link)

            time.sleep(6)
            xpath_clickers(browser)
            
        except Exception as e:
            # If there was an exception, print the error message and try again with a new proxy
            #print(e)
            continue
        

def xpath_clickers (browser):
    #Cookie Notice click
    try:
        cookienotice = browser.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        cookienotice.click()
        time.sleep(2)
    except XPathEvalError:
        print("Cookie Notice not found, action skipped!") 
        pass

    #press play button using xpath @class='sc-button-play playButton sc-button m-stretch'
    play_button = browser.find_element(by=By.XPATH, value='//*[@class="sc-button-play playButton sc-button m-stretch"]')
    play_button.click()
    
    time.sleep(1)

    #mute button click 
    mutesong = browser.find_element(by=By.XPATH, value='//*[@class="volume__button volume__speakerIcon sc-ir"]')
    mutesong.click()


    #wait for the song to play 25 seconds 
    time.sleep(random_number)
    
    #close browser
    browser.close()



#Mulitthread open chromedriver with proxy calling open_browser function
def threaded_open_browser(url, num_threads, proxylist, optionheadless):
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=open_browser, args=(url, proxylist, optionheadless))
        t.start()
        threads.append(t)
        t.join()
        
    
    
#call multithread viewer def

threaded_open_browser(soundcloud_link, 3, proxylist, optionheadless)










