from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import python_functions

driver = webdriver.Chrome()

driver.get("https://www.google.com")
# to show output
time.sleep(1)

# maximize the browser-window
driver.maximize_window()

driver.find_element(By.NAME,"q").send_keys("dell")
# to show output
time.sleep(1)

driver.find_element(By.NAME,"btnK").send_keys(Keys.ENTER)
# to show output
time.sleep(1)

# find dell.com on google search results page
driver.find_element(By.XPATH,'//*[@id="tads"]/div/div/div/div/div[1]/a/div[1]/span').click()
# to show output
time.sleep(1)

# #console log after opening dell.com
# driver.execute_script('alert("Welcome to Dell, from Praveen")')

# sign-in --> hover it to show options
hover = ActionChains(driver)
sign_in = driver.find_element(By.ID,"um-si-label")
hover.move_to_element(sign_in).perform()
time.sleep(1)

# select sign-in options from the drop-down menu
driver.find_element(By.XPATH,'//*[@id="unified-masthead"]/div[1]/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/a[1]').click()
time.sleep(1)

#username
email = "kojapov301@breazeim.com"
#password
password = "TestingDell11@BDC"

# enter email
driver.find_element(By.NAME,"SignInModel.EmailAddress").send_keys(email)
time.sleep(1)

#enter password
driver.find_element(By.NAME,"userPwd_UserInputSecret").send_keys(password)
time.sleep(1)

#click to sign-in to your account
driver.find_element(By.ID,"btnSignIn").click()
time.sleep(1)

# search bar
driver.find_element(By.ID,"mh-search-input").send_keys("Allienware Laptops",Keys.ENTER)
time.sleep(1)

#press on search button,or enable press enter on previous step
# driver.find_element(By.XPATH,'//*[@id="unified-masthead"]/div[1]/div[1]/div[2]/button[2]/svg').click()  --- NOT ABLE TO DO

#filter the laptops --> precaution so NO other type of items show up
driver.find_element(By.XPATH,'//*[@id="refinement-36679"]').click()

# select the product
driver.find_element(By.XPATH,'//*[@id="d569946win9"]/section[1]/h3/a').click()
time.sleep(1)

# buy the product
driver.find_element(By.XPATH,'//*[@id="add-to-cart-stack"]/div[2]/a').click()
# driver.set_page_load_timeout(20)
time.sleep(20)

#checking availability
# # enter pin code
# driver.find_element(By.XPATH,'//*[@id="zipcode"]').send_keys("560048")
# time.sleep(1)

# # click check button
# driver.find_element(By.XPATH,'//*[@id="button-zipcode-check2"]').click()
# time.sleep(1)

# res = driver.find_element(By.XPATH,'//*[@id="form-product-zipcode2"]/div/div[3]')
# check if product can  be delivered to the pin code mentioned and if yes buy the product
# if isSubsequence("Delivery", res)==True:
#     driver.find_element(By.ID,"bundle-slide").click()

# else:
#     print("Product is currently not deliverable")

#click buy now to go to checkout
driver.find_element(By.XPATH,'//*[@id="bundle-slide"]').click()
time.sleep(1)

#enter details before pay now
#enter email
driver.find_element(By.XPATH,'//*[@id="customer-email"]').send_keys(email)

#enter personal details
firstName = "kojapov"
lastName = "breazeim"
phoneNo = "1234567890"
StreetAdd = "Mahadevapura"
pinCode = "560048"

driver.find_element(By.XPATH,'//*[@id="RRG9GMF"]').send_keys(firstName)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="XJ7CALD"]').send_keys(lastName)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="GTPIYVV"]').send_keys(phoneNo)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="E7DG1M1"]').send_keys(StreetAdd)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="PKACLMM"]').send_keys(pinCode)
time.sleep(1)

#check box of AGREE terms
driver.find_element(By.XPATH,'//*[@id="agreement__1"]').click()
time.sleep(1)

#enter pan number
panNumber = "ABCDE1234F"
driver.find_element(By.XPATH,'//*[@id="opc-sidebar"]/div[2]/div[2]/fieldset[2]/div/input').send_keys(panNumber)
time.sleep(1)

#checkout by clicking on PAY NOW
driver.find_element(By.XPATH,'//*[@id="opc-sidebar"]/div[2]/div[3]/div/div/button').click()
time.sleep(1)

print("Test successful!!")


driver.close()
driver.quit()