import os


USER = os.path.expanduser("~")

CHROME = "chrome"
FIREFOX = "firefox"


SUPPORTED_BROWSERS = [CHROME, FIREFOX]
CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
FIREFOX_PATH = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

CHROME_SESSION_PATH = (
    f"{USER}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Sessions"
)
CHROME_CACHE_PATH = (
    f"{USER}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache\\Cache_Data"
)

FIREFOX_STORAGE_PATH = f"{USER}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\m9lmsbu9.default-release\\storage\\default"