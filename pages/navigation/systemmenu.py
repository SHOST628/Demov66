from selenium.webdriver.common.by import By

system_menu = (By.XPATH,"//div[@class='v-slot']/div/div[1]/div[1]/div/div")
system_configuration = (By.XPATH,"//div[@role='tree']/div[1]/div[1]/div/span")
backend_system_configuration = (By.XPATH,"//div[@role='tree']/div[1]/div[2]/div[2]/div[1]/div/span")
region_maintanence = (By.XPATH,"//div[@role='treeitem']/div[1]/div/span[contains(text(),'Region')]")
