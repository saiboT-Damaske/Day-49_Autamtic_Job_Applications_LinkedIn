from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time


LINKEDIN_SIGN_IN_PAGE = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
JOB_SEARCH_URL = ""

LINKEDIN_MAIL = ""
LINKEDIN_PW = ""


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get(LINKEDIN_SIGN_IN_PAGE)
time.sleep(3)
reject_cookies_button = driver.find_element(
    By.XPATH,
    '//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]')

reject_cookies_button.click()

username = driver.find_element(By.ID, "username")
username.send_keys(LINKEDIN_MAIL)

pw = driver.find_element(By.ID, "password")
pw.send_keys(LINKEDIN_PW)
pw.send_keys(Keys.ENTER)

time.sleep(4)
driver.get(JOB_SEARCH_URL)
time.sleep(4)

# find the first job on the list
first_job = driver.find_element(By.CLASS_NAME, "job-card-list__title")
first_job.click()

# --------------- apply --------------- #
# time.sleep(3)
# driver.find_element(By.CLASS_NAME, "artdeco-button__icon--in-bug").click()
# time.sleep(4)
# # page 1 contact
# next_button = driver.find_element(By.XPATH, '//span[text()="Weiter"]')
# next_button.click()
# # time.sleep(1)
# # # page 1 cv
# # driver.find_element(By.CLASS_NAME, "artdeco-button__text").click()


# --------------- save the job --------------- #
# time.sleep(4)
# # save job
# save_button = driver.find_element(By.XPATH, '//span[text()="Speichern"]')
# save_button.click()

# -------------- Save the first five jobs on that page ------------ #

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
list_jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
for job in list_jobs:
    job.click()
    time.sleep(3)
    try:
        save_button = driver.find_element(By.XPATH, '//span[text()="Speichern"]')
        save_button.click()
        time.sleep(2)
    except NoSuchElementException:
        print("you already saved for this one.")
        time.sleep(2)