import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#   driver = webdriver.Edge(executable_path="E:\\study\\webdriver\\msedgedriver.exe")
s = Service(executable_path="E:\\study\\webdriver\\msedgedriver.exe")
driver = webdriver.Edge(service=s)  # 找到msedgedriver
driver.maximize_window()
driver.get("https://test-www.skyviewfund.com/login2")
normal_login_username = driver.find_element(By.ID, "normal_login_username")
normal_login_password = driver.find_element(By.ID, "normal_login_password")
normal_login_username.clear()
normal_login_username.send_keys("钱立民扫码")
normal_login_password.clear()
normal_login_password.send_keys("test2022jizhi")
login_btn = driver.find_element(By.XPATH,
                                "//*[@id='root']/div/section/section/main/div/div/div[2]/form/div[""3]/"
                                "div/div/span/button/span")
driver.execute_script("arguments[0].click();", login_btn)
time.sleep(3)
switchover = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/header/div")
switchover.click()  # 登录与切换菜单！！！！！
time.sleep(1)
Candidate = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/main/div[1]/ul/li[4]"
                                          "/div/span/span[1]")
Candidate.click()
time.sleep(1)
Candidate_My = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/main/div[1]/ul/li[4]/ul/li")
Candidate_My.click()
time.sleep(6)   # 点击菜单Candidate的MY列表
Create_Candidate_Button = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div"
                                                        "/div[1]/div[1]/div[2]/button")
driver.execute_script("arguments[0].click();", Create_Candidate_Button)
time.sleep(2)     # 点击candidate的创建按钮
Candidate_Name = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                               "2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div["
                                               "2]/div/div/input")
Candidate_Name.send_keys("优质候选人-001")    # 输入候选人姓名
time.sleep(1)
Candidate_Sex = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[3]/div/div["
                                              "2]/div/div/div")
Candidate_Sex.click()
time.sleep(1)
Candidate_Sex.send_keys(Keys.DOWN)
Candidate_Sex.send_keys(Keys.ENTER)  # 性别为女
time.sleep(2)
Candidate_Location = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                   "/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div["
                                                   "4]/div/div[2]/div/div")
# driver.execute_script("arguments[0].removeAttribute(\"style\")", Candidate_Location)
# driver.execute_script("arguments[0].style.display = 'inline')", Candidate_Location)  # input元素被隐藏掉需要特殊处理
Candidate_Location.click()
time.sleep(1)
Candidate_Location001 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                      "/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[4]/div"
                                                      "/div[2]/div/div/div/div/div[2]/div/input")
Candidate_Location001.send_keys("上海市")
time.sleep(2)
Candidate_Location001.send_keys(Keys.ENTER)     # 先点击地址输入框将
