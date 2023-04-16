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
time.sleep(6)  # 点击菜单Candidate的MY列表
Create_Candidate_Button = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div"
                                                        "/div[1]/div[1]/div[2]/button")
driver.execute_script("arguments[0].click();", Create_Candidate_Button)
time.sleep(2)  # 点击candidate的创建按钮
Candidate_Name = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                               "2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div["
                                               "2]/div/div/input")
Candidate_Name.send_keys("优质候选人-015")  # 输入候选人姓名
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
Candidate_Location001.send_keys(Keys.ENTER)  # 在地址中输入上海市并且回车确认
# 先点击地址输入框将style="display: none;"触发为style="display:block;"变成可见再次找到input属性进行操作
time.sleep(2)
Candidate_Strength = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                   "/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[5]/div/div/div"
                                                   "/div[2]/div/div/div/div/ul/li/div/input")
Candidate_Strength.send_keys("无敌的我")
time.sleep(2)  # 输入职业亮点
Candidate_Position = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                   "/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[7]/div/div["
                                                   "1]/div/div[2]/div/div/div/div/div")
Candidate_Position.click()
time.sleep(1)
Candidate_Position001 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                      "/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[7]/div/div["
                                                      "1]/div/div[2]/div/div/div/div/ul/li/div/input")
Candidate_Position001.send_keys("行业专家")
time.sleep(1)
Candidate_Position001.send_keys(Keys.ENTER)
time.sleep(2)  # 选择候选人类别为“行业专家”
Candidate_Phone = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div/div[1]/div[1]/div[2]/div[1]/div[9]/div[2]/div/div["
                                                "1]/div/div/div/div[2]/div/div/input")
Candidate_Phone.send_keys("19956223513")
time.sleep(1)  # 输入候选人电话，号码与社交平台二选一，这里输入号码
Candidate_Company_Name = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div"
                                                       "/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[1]/div/div"
                                                       "/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div/div/input")
Candidate_Company_Name.send_keys("未知的公司")
time.sleep(1)  # 输入候选人公司名称
Candidate_Workplace = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[1]/div/div/div[1]"
                                                    "/div/div/div[1]/div/div[3]/div/div[2]/div/div/div")
Candidate_Workplace.click()
time.sleep(1)
Candidate_Workplace001 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div"
                                                       "/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[1]/div/div"
                                                       "/div[1]/div/div/div[1]/div/div[3]/div/div[2]/div/div/div/div"
                                                       "/div[2]/div/input")
Candidate_Workplace001.send_keys("北京市")
time.sleep(1)  # 输入候选人工作地点
Carrier_List = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                             "2]/div/div[1]/div[6]/div[2]/div[1]/div[1]/div/div[1]/div/div["
                                             "2]/div/div/div")
Carrier_List.click()
time.sleep(1)
Carrier_List.send_keys(Keys.DOWN)
Carrier_List.send_keys(Keys.DOWN)
Carrier_List.send_keys(Keys.DOWN)
Carrier_List.send_keys(Keys.DOWN)
Carrier_List.send_keys(Keys.DOWN)
Carrier_List.send_keys(Keys.DOWN)
Carrier_List.send_keys(Keys.DOWN)
Carrier_List.send_keys(Keys.DOWN)
Carrier_List.send_keys(Keys.ENTER)
time.sleep(1)  # 主导人为钱立民扫码
Create_Button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "2]/div/div[2]/div/div/button")
Create_Button.click()  # 点击创建按钮
time.sleep(2)
OK_Button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
OK_Button.click()
time.sleep(2)
Candidate_Info = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div"
                                               "/div/div[2]/span/span/a")
Candidate_Info.click()
time.sleep(2)
windows = driver.window_handles  # 打开所有窗口。   注意需要在新的窗口操作是需要切换窗口滴！！！
driver.switch_to.window(windows[-1])  # 切换到最新打开的窗口
time.sleep(5)
Candidate_Conference = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div"
                                                     "/div[2]/div/div[2]/div/div[2]/div[2]")
Candidate_Conference.click()
time.sleep(2)  # 点击会议创建按钮
Candidate_Conference001 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div"
                                                        "/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div/div")
Candidate_Conference001.click()
time.sleep(0.5)
Candidate_Conference001.send_keys(Keys.ENTER)
time.sleep(1)  # 选择会议类型为Memo-专，行业专家
Conference_Modality = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[2]/div/div[3]/div/div[2]/div[3]/div/div[2]/div[3]/div/div")
Conference_Modality.click()
time.sleep(0.5)
Conference_Modality.send_keys(Keys.ENTER)
time.sleep(1)  # 选择会议形式为面谈
Conference_Location = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[2]/div/div[3]/div/div[2]/div[3]/div/div[3]/div[3]/div/input")
Conference_Location.send_keys("未知的会议地点")
time.sleep(1)  # 输入会议地点
Create_Conference_Button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div"
                                                         "/div/div[2]/div/div[3]/div/div[3]/button[2]")
Create_Conference_Button.click()
time.sleep(1)  # 点击创建按钮
OK_Button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
time.sleep(1)
OK_Button.click()
time.sleep(1)
