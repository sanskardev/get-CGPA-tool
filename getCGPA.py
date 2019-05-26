from selenium import webdriver
import time
import pandas
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://dms.jaipur.manipal.edu/loginForm.aspx')


def findCGPA(username, password, num = 1):
    username_box = browser.find_element_by_id('txtUserid')
    username_box.send_keys(Keys.CONTROL + 'a')
    username_box.send_keys(username)

    print ("username entered")

    password_box = browser.find_element_by_id('txtpassword')
    password_box.send_keys(password)

    print ("password entered")

    login = browser.find_element_by_id('hprlnkStduent')
    login.click()

    time.sleep(0.6)

    try:
        academic_records = browser.find_element_by_id('reptrMainManu1_lnkbtn_3')
        academic_records.click()
    except NoSuchElementException:
        return
    

    cgpa_page = browser.find_element_by_link_text('CGPA & GPA')
    time.sleep(0.6)
    cgpa_page.click()

    cgpa = browser.find_elements_by_xpath("//table[@id='ContentPlaceHolder1_GrdExamResults2']/tbody/tr[2]/td[1]")[0].text
    print (str(num) + ") " + cgpa)
    
    menu = browser.find_element_by_id('pnlImgBlank')
    menu.click()

    sign_out = browser.find_element_by_id('lnkSignout')
    sign_out.click()

    return cgpa

# matrix = pandas.read_excel('username_and_password.xlsx', sheet_name = 'Sheet1')
# print (matrix)

# header_list = ['username', 'dob', 'password', 'cgpa']
# matrix = matrix.reindex(columns = header_list)

# for i in range (0, 43):
#     usr = matrix.at[i, 'username']
#     pas = matrix.at[i, 'password']
#     matrix.ix[i, 'cgpa'] = findCGPA(usr, pas, i+1)

ans = findCGPA('189301179', '11mar1999')
print ('answer = ')
print (ans)

browser.quit()


# print (matrix)
# matrix.to_excel('result1.xlsx')
# print ("Exported.")