## LinkedIn Parser
The aim of this script is to scrape CVs from LinkedIn. This was an early approach taken by the team. However, it was proven not to be the best of approaches. Check the `Known Issues` section to understand more.

### Requirements:
- Python 3.8 or later
- Selenium 4.18.1 or later.
- [Firefox.](https://www.mozilla.org/en-US/firefox/new/) 
- [Gecko Driver](https://github.com/mozilla/geckodriver/releases) by Mozilla.

### How to use it:
1. Open `cookie_gatherer.py` and add your credentials to line 9 and 10.
2. Run `cookie_gather.py` and login into LinkedIn through the new window that opened up.
3. Return to the `cookie_gather.py` and press Enter.
4. Open `main.py`:
    1. Add your desired keywords to line 13.
    2. Add your desired download path to line 25.
5. Run `main.py`.

### Known Issues:
1. The account used to find and download CVs gets 
temporarily blocked by LinkedIn repeatedly.
2. Results returned from the script are hugely biased towards the account's interests and region.

