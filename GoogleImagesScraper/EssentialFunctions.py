import requests
import io
from PIL import Image
from selenium.webdriver.common.by import By
from MiscFunctions import *
import time
from colorama import Fore, Back, Style
import os
TIME_OUT=5

#Helper function to download image
def downloadImage(url, fileName, downloadPath=getFilePath("ImagesOutput")):
    if os.path.exists(getFilePath(downloadPath, fileName)) == True:
        print(f"{Fore.YELLOW}The image {fileName} already exists")
        return
    if fileName == None:
        print(Fore.RED + "ERROR: filename cannot be empty")
        return
    try:
        #HTTP request to URL
        imageContent = requests.get(url,timeout=TIME_OUT).content

        #I know nested try and excepts look ugly but Pillow doesn't support SVG images
        #The solution is to write it out to a file using wb mode directly
        #This is because SVGs are internally just XML and not Bitmaps
        try:
            #Saving the image bytes in memory
            imageFile = io.BytesIO(imageContent)
            #Converting the bytes to a image object in memory
            finalImage = Image.open(imageFile)
            #Getting path of final image
            if finalImage.mode != "RGB":
                finalImage = finalImage.convert("RGB")
        except:
            print(f"{Fore.RED}Failed to fetch and/or convert {url}.\n")
            return
        imagePath = None
        if url.find(".jpg") != -1:
            imagePath = getFilePath(downloadPath,fileName + ".jpg")
        elif url.find(".png") != -1:
            imagePath = getFilePath(downloadPath, fileName + ".png")
        elif url.find(".jpeg") != -1:
            imagePath = getFilePath(downloadPath, fileName + ".jpg")
        elif url.find(".gif") != -1:
            imagePath = getFilePath(downloadPath, fileName + ".gif")
        elif url.find(".webp") != -1:
            imagePath = getFilePath(downloadPath, fileName + ".webp")
        elif url.find(".svg") != -1:
            #SVGs are not supported in pillow, so we will download it directly here
            imagePath = getFilePath(downloadPath, fileName + ".svg")
            with open(imagePath, "wb") as file:
                file.write(imageContent)
                print(f"{Fore.GREEN}Image URL: {url}")
                print(f"{Fore.GREEN}Image succesfully downloaded at {imagePath}\n")
                file.close()
                return
        else:
            imagePath = getFilePath(downloadPath,fileName + ".png")
        
        #saving the image to disk
        with open(imagePath, "wb") as f:
            finalImage.save(f)
            finalImage.close()
        print(f"{Fore.GREEN}Image URL: {url}")
        print(f"{Fore.GREEN}Image succesfully downloaded at {imagePath}\n")
    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED}Image URL: {url}")
        print(f"{Fore.RED}Failed to download {fileName}. Failed to connect.\n")
    except requests.exceptions.Timeout:
        print(f"{Fore.RED}Image URL: {url}")
        print(f"{Fore.RED}Failed to download {fileName}. Timed out after {TIME_OUT} seconds.\n")
    except Exception as e:
        print(f"{Fore.RED}Image URL: {url}")
        print(f"{Fore.RED}Failed to download the image {fileName}")
        print(f"{Fore.RED}Exception: \n{e}\n")

def scrapGoogleImagesURLs(SCRAPE_URL,WEB_DRIVER, timeDelay, imageCount, scrapeFolder, scrapeFileName):
    global CURRENT_TRIALS
    global MAX_RETRIES    
    #attempt connection to the target URL
    try:
        #Try loading the URL
        WEB_DRIVER.get(SCRAPE_URL)
    except:
        print(f"{Fore.RED}Failed to print the target URL of {SCRAPE_URL}")
        print(f"{Fore.RED}Please make sure you are connected to the internet and that the URL is valid!")
        print(f"{Fore.RED}Retrying...")
        time.sleep(2)
        if CURRENT_TRIALS < MAX_RETRIES:
            CURRENT_TRIALS += 1
            scrapGoogleImagesURLs(SCRAPE_URL,WEB_DRIVER,timeDelay,imageCount, scrapeFolder, scrapeFileName)
    #set to prevent duplicates
    imageURLs = set()
    previousURLs = set()
    if scrapeFileName != None:
        previousURLs = loadPickledFile(getFilePath("Bin Files", scrapeFileName)) 
    print(f"{Fore.GREEN} Amount of previously stored urls {len(previousURLs)}")
    Fore.RESET
    skippedURLs = 0
    totalLoops = 0
    reachBottomOfPage(WEB_DRIVER)
    currentImageNumber = 1
    maxThumbnails = len(WEB_DRIVER.find_elements(By.CLASS_NAME, "Q4LuWd"))
    print(f"{Fore.BLUE}Total number of thumbails: {maxThumbnails}")
    while len(imageURLs) + skippedURLs < imageCount:
        #The basic idea is to load the page (already done in previous step), to find all thumbnails by searching for a common class
        #and then to get the src attribute of the thumbnail and then download it with the acquired src

        #The class name Q4LuWd is always present in all thumbnail images
        thumbnails = WEB_DRIVER.find_elements(By.CLASS_NAME, "Q4LuWd")
        if totalLoops >= maxThumbnails - 1:
            print(f"{Fore.BLUE}Bottom of page reached...saving results.")
            break

        for thumbnailImage in thumbnails[len(imageURLs) + skippedURLs: imageCount]:
            #Edge case: the image might not be laoded and clicking it will produce an error
            #In such cases, simply skip the image
            try:
                WEB_DRIVER.execute_script("arguments[0].scrollIntoView();", thumbnailImage)
                thumbnailImage.click()
                time.sleep(timeDelay)
            except:
                continue
        
            #This can occaisonally return multiple images
            returnedImages = WEB_DRIVER.find_elements(By.CLASS_NAME,"iPVvYb")
            #occaisonally, there are no high resolution images
            #If that is the case, then we must download the low resolution image
            if len(returnedImages) == 0:
                WEB_DRIVER.find_elements(By.CLASS_NAME,"pT0Scc")
            #If there are still no downloaded images...then skip
            if len(returnedImages) == 0:
                continue
            for image in returnedImages:
                #if the same image is found again then skip it
                if image.get_attribute("src") in imageURLs or image.get_attribute("src") in previousURLs:
                    imageCount += 1
                    skippedURLs += 1
                    break
                if image.get_attribute("src") and 'http' in image.get_attribute("src"):
                    imageURLs.add(image.get_attribute("src"))
                    currentImageNumber += 1
                    print(f"{Fore.GREEN}Found image number {currentImageNumber}!")
            totalLoops += 1

    #Save the output
    mergsedSet = imageURLs.union(previousURLs)
    savePickleFile(getFilePath("Bin Files", scrapeFileName),mergsedSet)
    if scrapeFolder == None:
        print(f"{Fore.GREEN}A total of {len(imageURLs) + 1} URLs have been succesfully scraped and saved to {scrapeFileName}.bin")
    
    elif scrapeFolder != None:
        print(f"{Fore.GREEN}A total of {len(imageURLs) + 1} URLs have been succesfully scraped and saved to {scrapeFileName}.bin, and they will now be downloaded")
        for url in mergsedSet:
            downloadImage(url, shortenString(url,16), scrapeFolder)

def BulkDownload(binFileName, folderName):
    URLSet = loadPickledFile(getFilePath("Bin Files", binFileName))
    if len(URLSet) == 0:
        print(f"{Fore.RED} Bin file is empty or does not exist!")
        return
    for url in URLSet:
        downloadImage(url, shortenString(url,16), folderName)
    
