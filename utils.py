import webbrowser
from browserstack.constants import (
    CHROME,
    FIREFOX,
    CHROME_PATH,
    FIREFOX_PATH,
    SUPPORTED_BROWSERS,
    CHROME_SESSION_PATH,
    CHROME_CACHE_PATH,
    FIREFOX_STORAGE_PATH
)
import os
import psutil
from pywinauto import Application
import shutil


webbrowser.register(CHROME, None, webbrowser.BackgroundBrowser(CHROME_PATH))
webbrowser.register(FIREFOX, None, webbrowser.BackgroundBrowser(FIREFOX_PATH))


def _delete_chrome_browsing_data():

    # session
    shutil.rmtree(CHROME_SESSION_PATH)
    os.mkdir(CHROME_SESSION_PATH)

    # cache
    shutil.rmtree(CHROME_CACHE_PATH)
    os.mkdir(CHROME_CACHE_PATH)

def _delete_firefox_browsing_data():
    # browsing_data
    shutil.rmtree(FIREFOX_STORAGE_PATH)
    os.mkdir(FIREFOX_STORAGE_PATH)

def open_tab(browser_name, url):
    if browser_name in SUPPORTED_BROWSERS:
        browser = webbrowser.get(browser_name)
        browser.open_new_tab(url)
        return f"Opening {browser_name.capitalize()}....."

    return f"Browser not supported"


def close_browser(browser_name):
    if browser_name in SUPPORTED_BROWSERS:
        os.system(f"taskkill /im {browser_name}.exe /f")
        return f"Closed {browser_name.capitalize()} window."
    return f"Browser not supported."


def active_tab(browser_name: str):
    if browser_name in SUPPORTED_BROWSERS:
        if browser_name == CHROME:
            app = Application(backend="uia")
            app.connect(title_re=".*Chrome.*")
            element_name = "Address and search bar"
            dlg = app.top_window()
            url = dlg.child_window(title=element_name, control_type="Edit").get_value()
            return (
                f"The url for {browser_name.capitalize()}'s active tab is ->",
                f"https://www.{url}",
                f"https://www.{url}",
            )

        return f"Browser has no active tab!"
    return f"Browser not supported."


def browser_cleanup(browser_name: str):
    if browser_name in SUPPORTED_BROWSERS:
        if browser_name == CHROME:
            _delete_chrome_browsing_data()
            return f"{browser_name.capitalize()} cleanup done."
        if browser_name == FIREFOX:
            _delete_firefox_browsing_data()
            return f"{browser_name.capitalize()} cleanup done." 
        return f"Cleanup not possible."
    return f"Browser not supported."
