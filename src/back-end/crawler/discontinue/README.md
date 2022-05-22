# Back-end crawler : discontinue

## Outline

### setting_dynamic_crawl.py
Code with variables and methods for checking the operating system for dynamic crawling.


### NF_discontinue_data.py
Save Netflix discontinue video information as a json file.

### WC_discontinue_data.py
Save Watcha discontinue video information as a json file.

## folder : chromewebdrive
Folder containing chromewebdrive to use sellenium. <br>
**warning** : Depending on the **version of Chrome**, you may need to **update** the Chrome Driver folder.

## HOW TO USE?
### 1. Go to the discontinue Folder
- **In Linux**
`cd src/back-end/crawler/discontinue`

- **In Window**
`cd src\back-end\crawler\discontinue`

### 2. Check your Chrome Version and Compare Chromewebdrive Version in chromewebdrive
if you want, download the chromewebdrive in this [site](https://chromedriver.chromium.org/downloads) and change the chromewebdrive file.

### 3. Run the file named Crawling in the OTT you want.
- NF_discontinue_data.py
- WC_discontinue_data.py

### 4. If you want to save the data saved as a json file in the DB, Run saving_DB.py
it's Done!

## WARNING!
- YOU MUST **CHECK** Chrome web driver Version!!!
- First, the DB must be **set**.
