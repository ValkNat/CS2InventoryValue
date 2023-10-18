import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

    # Initialize the Chrome WebDriver with the correct executable path
options = Options()
options.add_experimental_option('detach', True)
service = Service(executable_path = r'C:\Users\Natalie\Documents\chromedriver\chromedriver.exe')
options.binary_location = "C:\\Users\\Natalie\\Documents\\chrome testing binary\\chrome.exe"

def on_enter():
    user_input = entry.get()
    result_label.config(text=f"You entered: {user_input}")

    driver = webdriver.Chrome(service = service, options = options)
    driver.get("https://steamid.co")

     # Use WebDriverWait to wait for the search bar to be visible
    wait = WebDriverWait(driver, 10)
    search_bar = wait.until(EC.presence_of_element_located((By.ID, 'search')))

    search_bar.clear()
    search_bar.send_keys(user_input)
    search_bar.send_keys(Keys.ENTER)

    steam64text = wait.until(EC.presence_of_element_located((By.ID, 'steam_id64')))
    steam64 = steam64text.get_attribute("value")
    result_label.config(text=steam64)

    driver.get("https://montuga.com/")
    input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Steam64Id..."]')))
    input_element.clear()
    input_element.send_keys(steam64)
    # Handle the custom dropdown (in this example, we assume you can click it)
    dropdown = wait.until(EC.presence_of_element_located((By.ID, 'select-input')))
    dropdown.click()
    
    # Locate and click the desired option
    option_to_select = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title="CS 2"]')))
    option_to_select.click()

    input_element.send_keys(Keys.ENTER)

    account_value = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'totalvalue')))
    result_label.config(text=account_value.text)




root = tk.Tk()
root.title("Steam Account Value Checker")

title_label = tk.Label(root, text="Please enter Steam profile URL: ")
title_label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=on_enter)
submit_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

value_label = tk.Label(root, text='')
value_label.pack()

root.mainloop()
