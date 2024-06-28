from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
EMAIL_ACCOUNT = "abc@gmail.com"
PASSWORD = "abc@123"
PHONE = 1234567890

def abort_application():
    
    #-----------------------click close button
    close_button = driver.find_element(By.CLASS_NAME, value="artdeco-button__text")
    close_button.click()
    
    
#---------------optional - Keep the browser open if the script crashes     
chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3896573105&distance=25&f_AL=true&f_WT=2&geoId=102713980&keywords=customer%20relationship%20manager&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")

# sign_in_page = driver.find_element(by=By.CLASS_NAME,value="authwall-join-form__form-toggle--bottom form-toggle")
# sign_in_click = sign_in_page.send_keys(Keys.ENTER)
# print(sign_in_page.text)

# ---------------click reject cookie button---------#
# time.sleep(3)
# reject_button = driver.find_element(by=By.CSS_SELECTOR,value='button[action-type="DENY"]')
# reject_button.click()

time.sleep(2)
sign_in = driver.find_element(By.LINK_TEXT,value="Sign in")
sign_in.click()
# sign_in.send_keys(Keys.ENTER)
# print(sign_in.text)

# ----Sign in--------#
time.sleep(2)
email_field = driver.find_element(By.ID,value="username")
email_field.send_keys(EMAIL_ACCOUNT)
password = driver.find_element(By.ID,value="password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
# sign_in_button = driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
# sign_in_button.send_keys(Keys.ENTER)
# driver.quit()

input("Press Enter when you have solved the Captcha")

#--------------Get listings

time.sleep(2)
all_listings = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

#-------------------applying to jobs-----------------#
for listing in all_listings:
    print("Opening listing")
    listing.click()
    time.sleep(2)
    try:
        #----------------easy apply
        easy_apply = driver.find_element(by=By.CLASS_NAME,value="jobs-apply-button--top-card")
        easy_apply.send_keys(Keys.ENTER)
        # easy_apply.click()
        
        #------Insert Phone number
        #------find an <input> element where id contains phonenumber
        time.sleep(2)
        phone = driver.find_element(By.CSS_SELECTOR,value="input[id*=phoneNumber]")
        if phone.text=="":
            phone.send_keys(PHONE)        
            

        #------------select next button
        # time.sleep(2)
        # select_next = driver.find_element(By.CSS_SELECTOR,value=".display-flex justify-flex-end ph5 pv4 button")
        # select_next.click()
        
        #-----------submit button
        submit_button = driver.find_element(By.CLASS_NAME,value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("complex application. Skipped")
            continue
        else:
            #-----------click submit button
            print("Submitting job application")
            submit_button.click()
            
        time.sleep(2)
        #Click close button
        close_button = driver.find_element(By.CSS_SELECTOR,value="artdeco-modal__dismiss")
        close_button.click()
        
    except NoSuchElementException:
        abort_application()
        print("No application button. Skipped.")
        continue
    
    time.sleep()
    driver.quit()
        
        
