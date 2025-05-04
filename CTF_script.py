from bs4 import BeautifulSoup
import warnings
import re
import requests as req
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
warnings.filterwarnings("ignore", category=DeprecationWarning)


if __name__ == "__main__":
    content = req.get("https://hertie-scraping-website.vercel.app/").content
    soup = BeautifulSoup(content, 'html.parser')
    flag_level1 = []

    # Get all text elements including "flag-"
    flag_in_text = soup.find_all(text=lambda text: text and text.strip().startswith("flag-"))
    for flag in flag_in_text:
        if flag not in flag_level1:
            flag_level1.append(flag)

    # Get the flag which are hidden in attributes
    for tag in soup.find_all(True):  # True means "all tags"
        for attr_val in tag.attrs.values():
            # Handle string or list attributes (like class)
            values = attr_val if isinstance(attr_val, list) else [attr_val]

            for val in values:
                if isinstance(val, str) and "flag-" in val:
                    # Check if the flag is not already in the list
                    if val not in flag_level1:
                        flag_level1.append(val)

    # Extract the flags
    print("\nFlags Level 1:\n")
    for flag in flag_level1:
        print(flag)

    # Count the number of flags
    print("Number of flags found:", len(flag_level1), "\n")

    print("STARTING Level 2\n")
    content = req.get("https://hertie-scraping-website.vercel.app/level2").content
    soup = BeautifulSoup(content, 'html.parser')

    flag_level2 = []

    # Get all text elements including "flag-"
    flag_in_text = soup.find_all(text=lambda text: text and text.strip().startswith("flag-"))
    for flag in flag_in_text:
        if flag not in flag_level1:
            flag_level2.append(flag)

    # Get the flag which are hidden in attributes
    for tag in soup.find_all(True):  # True means "all tags"
        for attr_val in tag.attrs.values():
            # Handle string or list attributes (like class)
            values = attr_val if isinstance(attr_val, list) else [attr_val]

            for val in values:
                if isinstance(val, str) and "flag-" in val:
                    flag_level2.append(val)

    # Get the flag which are hidden in script
    script_chunks = soup.find_all("script")

    for script in script_chunks:
        if script.string and "flag-" in script.string:
            # Find all occurrences of 'flag-' followed by exactly two digits
            matches = re.findall(r'flag-\d{2}', script.string)
            for match in matches:
                if match not in flag_level2:
                    flag_level2.append(match)

    print("Flags Level 2:\n")
    for flag in flag_level2:
        print(flag)

    print("Number of flags found:", len(flag_level2))

    print("STARTING Level 3\n")

    content = req.get("https://hertie-scraping-website.vercel.app/level3").content
    soup = BeautifulSoup(content, 'html.parser')

    flag_level3 = []

    # Get the flag which are hidden in attributes
    for tag in soup.find_all(True):  # True = all tags
        for attr_val in tag.attrs.values():
            # Handle string or list attributes (like class)
            values = attr_val if isinstance(attr_val, list) else [attr_val]

            for val in values:
                if isinstance(val, str) and "flag-" in val:
                    flag_level3.append(val)

    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome (options=options)
    driver.get("https://hertie-scraping-website.vercel.app/level3")

    wait = WebDriverWait(driver, 10)

    # Click the three buttons to reveal the flags
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-blue-500.text-blue-700.border-blue-500.font-semibold.py-2.px-4.border.rounded.my-4")))
    button.click()

    button2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-yellow-500.text-yellow-700.border-yellow-500.font-semibold.py-2.px-4.border.rounded.my-4")))
    button2.click()

    button3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-red-500.text-red-700.border-red-500.font-semibold.py-2.px-4.border.rounded.my-4")))
    button3.click()

    # Get the new clicked page
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Get all text elements including "flag-"
    for tag in soup.find_all("button"):
        matches = tag.find_all(text=lambda t: t and t.strip().startswith("flag-"))
        for match in matches:
            flag_level3.append(match.strip())

    # Extract the flags
    print("Flags Level 3:\n")
    for flag in flag_level3:
        print(flag)

    # Count the number of flags
    print("Number of flags found:", len(flag_level3))

    # Total number of flags
    total_flags = len(flag_level1) + len(flag_level2) + len(flag_level3)
    print("\nTotal number of flags found:", total_flags, "\n")

    driver.quit()
