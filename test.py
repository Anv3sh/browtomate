import browser_cookie3

def delete_firefox_cookies():
    firefox_cookies = browser_cookie3.firefox()

    # Specify the cookie name you want to delete
    cookie_name = "your_cookie_name"

    # Delete the cookie
    for cookie in firefox_cookies:
        if cookie.name == cookie_name:
            cookie.expires = 0  # Set the expiry to the past
            print(f"Cookie '{cookie_name}' deleted successfully.")
            break
    else:
        print(f"Cookie '{cookie_name}' not found.")

delete_firefox_cookies()
