#This code was created by Aly Mohamed Elsharkawy
#Development began on February 5, 2024 and ended on February 10, 2024 with final edits done on 3/1/2024

import MiscFunctions
import EssentialFunctions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import InputFunctions as IF
from colorama import init, Fore, Back, Style
from time import sleep
if __name__ == "__main__":
    SCRAPE_DIR = None
    SCRAPE_FILE = None
    MiscFunctions.createFolder("Bin Files", False)
    #initialize colorama for colors
    init()
    print("NOTE:")
    print("BEFORE RUNNING MAKE SURE THAT YOU HAVE THE LATEST VERSION OF GOOGLE CHROME INSTALLED")

    print("This should be the URL of a Google Images search on Google Chrome")
    SCRAPE_URL = IF.takeInput("Enter URL to scrape")

    #To Check and verify
    print("Recommended time is around 1 or 2 seconds on an average computer")
    print("This is so that the browser can have enough time to respond.")
    SCRAPE_TIME_DELAY = IF.takeInputFloat("Enter Time Delay")

    print("\nPlease note setting this value to high can cause google to block your IP.")
    SCRAPE_AMOUNT = IF.takeInputInt("Enter Amount of Images to Scrape")

    print("If the images aren't saved to a directory, then their URLs will be stored in a file for later use.")
    SAVE_IMAGES_TO_DIRECTORY = IF.takeInputYesNo("Save Images to Directory?")
    if SAVE_IMAGES_TO_DIRECTORY == True:
        SCRAPE_DIR = IF.takeInput("Enter Folder Name for Output")
        MiscFunctions.createFolder(SCRAPE_DIR)
   
    SCRAPE_FILE = IF.takeInput("Enter file name for scraped URLs .bin file(do not add .bin in the name).")
    print(f"{Fore.BLUE}\nKeep in mind that the program will slow down near the end of the search results page. This is not a problem in the program itself. Rather, it is because there are lots of duplicate results in the end that must be skipped.")
    sleep(2)
    Fore.RESET
    if SCRAPE_AMOUNT != 0:
        WEB_DRIVER = webdriver.Chrome()
        EssentialFunctions.scrapGoogleImagesURLs(SCRAPE_URL, WEB_DRIVER, SCRAPE_TIME_DELAY, SCRAPE_AMOUNT, SCRAPE_DIR, SCRAPE_FILE)
        #close web driver after succesful scraping
        WEB_DRIVER.quit()
    elif SCRAPE_AMOUNT == 0:
        if SCRAPE_DIR == None:
            SCRAPE_DIR = "NoNameProvided"
        print(f"{Fore.BLUE} Bulk downloading all URLs in {SCRAPE_FILE}.bin!")
        EssentialFunctions.BulkDownload(SCRAPE_FILE, SCRAPE_DIR)
