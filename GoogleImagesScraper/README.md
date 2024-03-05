# Google Images Scraper
This python program scrapes Google Images. It also supports downloading images in bulk. This program is useful for large scale data collection. 

## Features
- Remembers previous image results to ensure unique results.
- Supports downloading images in bulk.

## Usage
**NOTE: ONLY WINDOWS AND CHROME ARE SUPPORTED. PLEASE MAKE SURE GOOGLE CHROME IS INSTALLED BEFORE RUNNING THE PROGRAM!**

**General Scraping:**
1. After running `main.py`, the program will ask you for the URL to scrape. This should be the URL of the Google Images result page itself.
2. The program will ask you for a delay. This will be the interval the program will wait before clicking on another image and scraping it. This should be long enough to give Google Chrome to respond. Anything around 1 second should be good on average hardware.
3. Enter the amount of images you wish to scrape. Keep in mind that program remembers previously scraped images and this will be the amount of _new images_ to scrape. Old outputs are not counted in this number. Furthermore, scraping too many might cause Google to intervene and block your IP. I have scraped entire search result pages in single sittings before. However, I recommend spacing these out to mitigate the risk of Google blocking your IP. Lastly, if the program runs out of images to scrape in the results page then it will automatically stop.
4. Enter whether you would like images to be immedietly downloaded or not.
5. If you entered yes in the previous step then the image URLs will be downloaded after the desired amount of URLs have been scraped. If you enter no then the URLs will be saved in a .bin file regardless of the previous answer. You will be asked to provide a name for a folder in which the downloaded images will be stored if you answered yes to the first prompt. The folder will be automatically created if it does not exist. Lastly, you will also be prompted to provide a name for the .bin file in which the scraped URLs will be stored. **Keep in mind that .bin files are how this program remembers previous outputs. Make sure that the name provided is the same for each URL you want to scrape. This will ensure that the program remembers previous URLs in this page.**

**Bulk Downloading:**
Repeat the same steps as stated in the previous section but with a few differences.
1. The amount of images to scrape must be 0. If this is not 0, then the program will scrape normally.
2. You must agree to outputs being saved into a folder. The name provided is the name of the directory to which the images will be downloaded to. If it does not exist, then it will be created. If you refuse and do not provide a name then the images will be downloaded to a folder called "NoNameProvided."
3. The delay value and input URL values will be ignored.
4. The name of the .bin file is the .bin file whose contents will be downloaded.

## Installation
Installation is a very simple. It consists of cloning the repo, installing dependencies, and then running the program (`main.py`). This assumes that you are already on Windows with Google Chrome installed.
```Bash
git clone https://github.com/AlyElsharkawy/GoogleImagesScraper
cd .\GoogleImagesScraper
pip install -r .\requirements.txt
python .\Main.py
```

## Issues
If you encounter any issues while using the program, then please open an issue in the issues tab.
