from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

if __name__ == "__main__":
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome (options=options)
    driver.get("https://hertie-scraping-website.vercel.app/")

wait = WebDriverWait(driver, 10)

# Extracting the content
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

flag_level1 = []

# Get all text elements including "flag-"
flag_in_text = soup.find_all(text=lambda text: text and text.strip().startswith("flag-"))
# Extract the flags
for flag in flag_in_text:
    # Check if the flag is not already in the list
    if flag not in flag_level1:
        flag_level1.append(flag)

# Get the flag which are hidden in attributes
for tag in soup.find_all(True):  # True = all tags
    for attr_val in tag.attrs.values():
        # Handle string or list attributes (like class)
        values = attr_val if isinstance(attr_val, list) else [attr_val]

        for val in values:
            if isinstance(val, str) and "flag-" in val:
                flag_level1.append(val)

# Extract the flags
print("\nFlags Level 1:\n")
for flag in flag_level1:
    print(flag)

# Count the number of flags
print("Number of flags found:", len(flag_level1), "\n")


###### LEVEL 2 ######

if __name__ == "__main__":
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome (options=options)
    driver.get("https://hertie-scraping-website.vercel.app/level2")

wait = WebDriverWait(driver, 10)

# Extracting the content
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Get all text elements including "flag-"
flag_level2 = soup.find_all(text=lambda text: text and text.strip().startswith("flag-"))

# Extract the flags
print("Flags Level 2:\n")
for flag in flag_level2:
    print(flag)

# Count the number of flags
print("Number of flags found:", len(flag_level2))




# # Country dropdown
# dropdown1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "select2-selection__rendered")))
# dropdown1.click()

# # Selecting France
# france_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'France')]")))
# france_option.click()

# # Discipline dropdown
# dropdown2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-selectDiscipline")))
# dropdown2.click()

# # Selecting CWT
# CWT_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(), 'CWT')]")))
# CWT_option.click()

# # Clicking "Apply"
# apply_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply')]")))
# apply_button.click()


# # Wait for the table to load
# time.sleep(3)

# # Extracting the table and the athletes names
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# table_element = soup.find(id="js-table")
# if table_element is None:
#     raise ValueError("Table with id 'js-table' not found")
# # Extract the table rows
# rows = table_element.find_all("tr") # Table row

# # Extract the names from each row
# names = []
# for row in rows:
#     # Find the <strong> tag within the row and extract the text
#     strong_tag = row.find("strong")
#     if strong_tag:
#         # Extract the text from the <strong> tag
#         name = strong_tag.get_text(strip=True)
#         names.append(name)
    
# for name in names:
#     print(name)

driver.quit()