
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for selecting dropdown options
from selenium.webdriver.support.select import Select

# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service impo rt Service
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# opto=webdriver.ChromeOptions()
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

#service = Service(executable_path = "")

# for opening browser after the action - leave the browser open
# options = Options()
# options.add_experimental_option("detach", True)

#########################      TYPES OF LOCATOTS  ######################################################

# LOCATORS SELENIUM
    # all locators should be in upperclass letter
# 1. Builtin Locator
    # id -> driver.find_element(By.ID,"name_of_id/locator")
    # name -> driver.find_element(By.NAME,"name_of_name_attribute/locator")
    # class name -> by.CLASS_NAME
    # linked text / partial linked text -> <a> link text </a> in partial link text small or partial part is linked . 
        # driver.find_element(By.LINK_TEXT,"text inside link")
        # driver.find_element(By.PARTIAL_LINK_TEXT,"pass partial / some text inside link")
    # tagname  By.TAG_NAME
# 2. Customize Locators
    # css selectors
    # tag_name is optional
        # tag and id -> driver.find_element(By.CSS_SELECTOR,"tagname#id_value")
        # tag and class -> tagname.valueofclass
        # tag and attribute ->  tagname[attribute = value] 
        # tag, class and attribute tag.valueofclass[attribute = value]

###########################  ALL ABOUT XPATH ###################################################################

    # XPATH  -> XPATH is defined as XML Path
        # used to defined the location of any element on webpage
        # used to navigate through elements and attributes in DOM 
        # XPATH is the address of element
    
    # Types of XPATH
        # Absolute / Full XPATH 
            # start from root html
            # start with single /
            # use only tags / nodes
        # Relative XPATH / Partial XPATH 
            # directly jump to the element on DOM
            # start with double //
            # use attributes

    # HOW TO WRITE XPATH MANUALLY
        # selectorshub

    # OTHER OPTIONS WITH XPATH
        # and 
        # or
        # contains()
        # starts-with()
        # text()


    # KEYWORDS WITH XPATH  --> XPATH ACCESS  ------->  used for tiverse through whole DOM
        # self -> every node itself a self node
        # parent -> immediate node top of self node is called parent node of that self node
        # child -> immediate node buttom of self node is called child node of that self node
        # ancestors -> parent of parent one level
        # desecendeant -> child of child
        # following -> left side of parent node
        # following-sibling -> left side of self node
        # preceding -> right side of parent node
        # preceding-sibling -> right side of self node


    #########################################################################################333333
    # METHODS AND FUNCTIONS
        # GET/APPLICATION COMMANDS
            # title
            # currunt_url
            # page_source
            # get()

        # CONDITIONAL COMMANDS  
            # is_displayed()
            # is_enabled()
            # is_selected()  --> for radio buttons and check boxes and selectors
     
        # BROWSER COMMANDS --> driver commands
            # close() --> close single brownser window (where driver focused)
            # quit() --> close multiple browser windows (this will kill the process)

        # NAVIGATIONAL COMMANDS  --> driver commands
            # back()
            # forward()
            # refresh()
    
        # WAIT COMMANDS
            # implicit wait  --> driver.implicity_wait() 
            # explicit wait  --> works based on condition -> 

            # declaration of explicit wait
                # mywait =  WebDriverWait(driver, 10, poll_frequency = 2, ignore_exceptions=[NoSuchElementException, ElementNotVisibleException,
                #  ElementNotSelectableException, Exception]) -> when we use explixit wait we can't use find_element method
            # condition
                # mywait.untill(EC.presence_of_element_located(add xpath or any other way to find the element))
            

    # remaining methods
        # clear()
    
    # difference between find elements and find element

    # defference between text vs get_attribute
        # text --> return inner text of element
        # get-attribute --> returns values of any attribute of web element
        


############################################## LECTURE 07 ##########################################################

    # Working with checkboxes   
        # Select Specific Checkbox from the list
        # Select multiple checkboxes by choice 
    
    # Working With Links
        # There are 3 kinds of links are available
            # internal -> 
            # external
            # broken link -> having no target pages for navigation
        # how to hangle broken links
            # 
    # Working with Dropdown Menus
        # selet the drop down by xpath, id, or ny locator
        # then using select method to that dropdown -> Select(dropdown_element)
        # then select the option which we want to select there are multiple methods for that -> dropdown.select-by_visible-text("text option")
        
        # we can capture all the options and print them -> dropdown_element.options will give lint of all options 

        # Selet option from dropdown without using built-in-method
            # by using options method

        # --> assignmwnt 
        # testautomationpractice.blogspot.com
        # itera-qa-.azurewebsites.net/home/automation


##################################  LECTURE  08 ######################################################################################

    # How to Handle Alerts/Popups

    

####################################################################################################################################

# creating and downloading webdriver tool for chrome 
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

driver.get("https://demo.nopcommerce.com/login")

driver.maximize_window()

driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").send_keys('admin')
driver.find_element(By.CLASS_NAME, "login-button").click()


# close only one browser at a time
#driver.close()

# close all browsers
#driver.quite() 