import os
from selenium.webdriver.common.by import By
import pickle
import time
import hashlib
from colorama import Fore, Back, Style

MAX_RETRIES = 5
CURRENT_TRIALS = 0

#Creates folder without OS dependencies
def createFolder(folderName, showConfirmation=False):
    pwd = os.getcwd()
    folderDirectory = os.path.join(pwd, folderName)
    try:
        os.mkdir(folderDirectory)
        if showConfirmation == True:
            print(f"Created folder {folderName} at {folderDirectory}")
    except:
        if showConfirmation == True:
            print(f"{folderName} folder already exists or folder name contains illegal characters")

#Gets file path without OS dependencies
# UNIX like systems use '/' and windows uses '\' for some weird reason
def getFilePath(*filesAndFolders):
    pwd = os.getcwd()
    return os.path.join(pwd, *filesAndFolders)

#LZ4I  --> See more results button
#XfJHbe ---> SHow more results anyway
def scrollDown(WEB_DRIVER):
    #Executing a javascript command to scroll the entire page
    #6 times should be enough to load the entire page even with popular search terms
    #the wait 3 seconds is to give time for the web page to load 
    #Note: it might need to be longer for the ejust workstation
    for i in range(6):
        WEB_DRIVER.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)

def clickWebElement(WEB_DRIVER, webElement):
    WEB_DRIVER.execute_script("arguments[0].scrollIntoView();", webElement)
    WEB_DRIVER.execute_script("arguments[0].click();", webElement)

def getWebElementsToClick(WEB_DRIVER):
    showMoreResults = WEB_DRIVER.find_elements(By.CLASS_NAME, "LZ4I")
    showMoreAnyway = WEB_DRIVER.find_elements(By.CLASS_NAME, "XfJHbe")
    mergedList = showMoreAnyway + showMoreResults
    return mergedList

def reachBottomOfPage(WEB_DRIVER):
    #Scroll down and click on the buttons "See more anyway" and "Show more results" if they appear
    #then keep scrolling and see if they appear again...if so repeat the clicks
    #Then scroll again and your at the bottom of the page and all is loaded :)))
    scrollDown(WEB_DRIVER)
    print(f"{Fore.BLUE}Prepatory pass done")
    firstPass = getWebElementsToClick(WEB_DRIVER)
    for elm in firstPass:
        clickWebElement(WEB_DRIVER, elm)
    print(f"{Fore.BLUE}First pass done")
    scrollDown(WEB_DRIVER)
    secondPass = getWebElementsToClick(WEB_DRIVER)
    for elm in secondPass:
        clickWebElement(WEB_DRIVER, elm)
    print(f"{Fore.BLUE}Second pass done")
    scrollDown(WEB_DRIVER)
    print(f"{Fore.BLUE}Final pass done")
    #Scroll up again
    WEB_DRIVER.execute_script("window.scrollTo(0,0);")


#INPUT AND OUTPUT RELATED FUNCTIONS
#This will always return a python set
def loadPickledFile(fileName):
    try:
        with open(fileName + ".bin", "rb") as openedFile:
            toReturn = pickle.load(openedFile)
            return toReturn
    except:
        print(f"File name {fileName}.bin does not exist or could not be read")
        return set()

def savePickleFile(fileName, toPickle):
    if toPickle:
        try:
            with open(fileName + ".bin", "wb") as openedFile:
                pickle.dump(toPickle, openedFile)
        except:
            print(f"Couldn't save {fileName}.bin. Please make sure that the filename is allowed!")
    else:
        print(f"The data provided was empty and thus {fileName}.bin won't be saved.")
    

def shortenString(inputString, finalLength):
    hashedString = hashlib.sha256(str(inputString).encode())
    hexString = hashedString.hexdigest()
    return hexString[:finalLength]
 

