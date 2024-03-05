from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import queue
import pickle, time, threading
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions


#input the words you want the bot to search for here.
keywords = ["Software Engineer"]
tracker = [1] * len(keywords)



def gatherer(keyword, pos):
    
    #setting up firefox
    
    profile = FirefoxOptions()
    profile.set_preference("pdfjs.disabled", True)
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.dir", "Full/Path/to/Desired/Download/Folder")
   
    #helper
    q = queue.Queue(0)

    def ElementExists(parent, class_name, m = 0):
        try: 
            parent.find_element(By.CLASS_NAME if m == 0 else By.XPATH, class_name)
            return True
        except:
            return False
        
    #Load Cookies
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)

    #Open LinkedIn
    login_url = 'https://www.linkedin.com/' 
    driver = webdriver.Firefox(options=profile)
    driver.get(login_url)
    
    #Add Cookies to driver
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()

    try:
        # Wait for the element with the ID of wrapper
        wrapper = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="global-nav-typeahead"]/input'))
        )
    except:
        driver.quit()
        return

    srch_box = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
    srch_box.send_keys(keyword)
    srch_box.send_keys(Keys.ENTER)
    
    try:
        # Wait for the element with the ID of wrapper
        wrapper = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="People"]'))
        )
    except:
        driver.quit()
        return

    ppl_button = driver.find_element(By.XPATH, '//button[text()="People"]')
    ppl_button.click()

    try:
        # Wait for the element with the ID of wrapper
        wrapper = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li.reusable-search__result-container"))
        )
    except :
        driver.quit()
        return

    driver.get(driver.current_url + "&page=" + str(pos))    
    
    for i in range(1):

        try:
            # Wait for the element with the ID of wrapper
            wrapper = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "reusable-search__result-container"))
            )
        except :
            driver.quit()
            return
        
        time.sleep(5)
        ppl = driver.find_elements(By.CLASS_NAME, "reusable-search__result-container")
        
        unallowed_ppl = []

        #Remove People that appear as "LinkedIn Members"
        for i in ppl:
            if ElementExists(i, "entity-result__actions--empty"):
                unallowed_ppl.append(i)
        
        for i in unallowed_ppl:
            print("R")
            ppl.remove(i)

        for r in ppl:
            print("A")
            href = r.find_element(By.TAG_NAME, "a")
            q.put(str(href.get_attribute("href")))

        #Downloading CVs
        while not q.empty():
            driver.get(q.get())
            try:
                try:
                    # Wait for the element with the ID of wrapper
                    wrapper = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "button"))
                    )
                except :
                    continue
                
                time.sleep(5)
                
                more_btn = driver.find_elements(By.TAG_NAME, "button")
                for i in more_btn:
                    if str(i.get_attribute("innerText")) == "More":
                        i.click()
                        break

                dwld_btn = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[2]")
                dwld_btn.click()

                time.sleep(5)
            except:
                continue

    driver.quit()
    return

curr = 0

while True:
    
    thread = threading.Thread(target=gatherer, args=(keywords[curr], tracker[curr],))
    
    thread.start()
    thread.join()
    
    tracker[curr] += 1

    curr += 1
    curr %= int(len(keywords))

