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
driver.get("https://release.skyviewfund.com/login2")
normal_login_username = driver.find_element(By.ID, "normal_login_username")
normal_login_password = driver.find_element(By.ID, "normal_login_password")
normal_login_username.clear()
normal_login_username.send_keys("八水")
normal_login_password.clear()
normal_login_password.send_keys("yanhuang2021jizhi")
login_btn = driver.find_element(By.XPATH,
                                "//*[@id='root']/div/section/section/main/div/div/div[2]/form/div[""3]/"
                                "div/div/span/button/span")
driver.execute_script("arguments[0].click();", login_btn)
time.sleep(3)
switchover = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/header/div")
switchover.click()  # 登录与切换菜单！！！！！
deal_subscript = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/main/div[1]/ul/li["
                                               "2]/div/span/span[1]")
deal_subscript.click()
time.sleep(2)
deal_my = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/main/div[1]/ul/li[2]/ul/li[2]/span[1]")
deal_my.click()
time.sleep(3)
create_deal = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div/div[1]/"
                                            "div[1]/div[2]/button")
create_deal.click()
time.sleep(2)
deal_name = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]/div"
                                          "/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/input") \
    .send_keys("memoV4-008")
time.sleep(1)
Deal_Tag1 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]/div/div["
                                          "1]/div[1]/div[2]/div[1]/div[3]/div/div/div["
                                          "2]/div/div/div/div/ul/li/div/input")
Deal_Tag1.send_keys("标签1")
time.sleep(1)
Deal_Tag1.send_keys(Keys.ENTER)
time.sleep(1)
Deal_Tag2 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]/div/div["
                                          "1]/div[1]/div[2]/div[1]/div[3]/div/div/div["
                                          "2]/div/div/div/div/ul/li/div/input")
Deal_Tag2.send_keys("标签2")
time.sleep(1)
Deal_Tag2.send_keys(Keys.ENTER)
time.sleep(1)
Deal_Tag3 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]/div/div["
                                          "1]/div[1]/div[2]/div[1]/div[3]/div/div/div["
                                          "2]/div/div/div/div/ul/li/div/input")
Deal_Tag3.send_keys("标签3")
time.sleep(1)
Deal_Tag3.send_keys(Keys.ENTER)
time.sleep(2)
founder = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]"
                                        "/div/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/input") \
    .send_keys("memoV4-008")
manager_list = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                             "2]/div/div[1]/div[6]/div[2]/div[1]/div[1]/div/div[2]/div/div["
                                             "2]/div/div/div")
manager_list.click()
#   Select(manager_list).select_by_visible_text("投资经理2")    #  selenium.common.exceptions.UnexpectedTagName
#   Exception: Message: Select only works on <select> elements, not on <div>
time.sleep(1)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
time.sleep(1)
manager_list.send_keys(Keys.ENTER)
time.sleep(1)
submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "2]/div/div[2]/div/div/div/button")
submit_button.click()
time.sleep(3)
ok_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
ok_button.click()  # 创建deal完毕
time.sleep(2)
Deal_Info = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                          "2]/span/span/a")
driver.execute_script("arguments[0].click();", Deal_Info)  # 创建deal之后直接进入deal基本信息
time.sleep(6)
windows = driver.window_handles  # 打开所有窗口。   注意需要在新的窗口操作是需要切换窗口滴！！！
driver.switch_to.window(windows[-1])  # 切换到最新打开的窗口
time.sleep(2)
Create_Conference001 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                     "2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]")
Create_Conference001.click()  # 点击新建会议
time.sleep(1)
Create_Conference_type = driver.find_element(By.XPATH,
                                             "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]"
                                             "/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div"
                                             "/div/div/div/div[1]/div")
Create_Conference_type.click()  # 点击新建会议下一步  ”项目全图/会议纪要“
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是项目全图
time.sleep(1)
Conference_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div/div[1]/div["
                                                "3]/span/div/input")
Conference_Time.click()
time.sleep(1)
Conference_Time1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[2]/div[3]/span/a")
Conference_Time1.click()  # 会议时间默认都为“今天”
time.sleep(1)
Conference_Modality = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div["
                                                    "3]/div/div[2]/div[3]/div/div")
Conference_Modality.click()
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.ENTER)  # 会议形式为“电话会”
time.sleep(1)
Click_Create_Conference = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                        "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[3]/button[2]")
Click_Create_Conference.click()
time.sleep(5)
Ok_Button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
Ok_Button.click()  # 创建会议完毕点击OK弹框
time.sleep(6)
"""
------------------------------------------------------------------------------------------------------------------------
"""
Create_Conference002 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                     "2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]")
Create_Conference002.click()  # 点击新建会议
time.sleep(1)
Create_Conference_type = driver.find_element(By.XPATH,
                                             "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]"
                                             "/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div"
                                             "/div/div/div/div[1]/div")
Create_Conference_type.click()  # 点击新建会议下一步  ”项目全图/会议纪要“
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是会议纪要续
time.sleep(1)
Conference_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div/div[1]/div["
                                                "3]/span/div/input")
Conference_Time.click()
time.sleep(1)
Conference_Time1 = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a")
time.sleep(1)
Conference_Time1.click()  # 会议时间默认都为“今天”
time.sleep(1)
Conference_Modality = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div["
                                                    "3]/div/div[2]/div[3]/div/div")
Conference_Modality.click()
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.ENTER)  # 会议形式为“电话会”
time.sleep(1)
Click_Create_Conference = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                        "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[3]/button[2]")
Click_Create_Conference.click()
time.sleep(3)
Ok_Button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button")
Ok_Button.click()  # 创建会议完毕点击OK弹框
time.sleep(6)
"""
------------------------------------------------------------------------------------------------------------------------
"""
Create_Conference003 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                     "2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]")
Create_Conference003.click()  # 点击新建会议
time.sleep(1)
Create_Conference_type = driver.find_element(By.XPATH,
                                             "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]"
                                             "/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div"
                                             "/div/div/div/div[1]/div")
Create_Conference_type.click()  # 点击新建会议下一步  ”项目全图/会议纪要“
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是行业专家note
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是行业专家note
time.sleep(1)
Conference_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div/div[1]/div["
                                                "3]/span/div/input")
Conference_Time.click()
time.sleep(1)
Conference_Time1 = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a")
time.sleep(1)
Conference_Time1.click()  # 会议时间默认都为“今天”
time.sleep(1)
Conference_Modality = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div["
                                                    "3]/div/div[2]/div[3]/div/div")
Conference_Modality.click()
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.ENTER)  # 会议形式为“电话会”
time.sleep(1)
Click_Create_Conference = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                        "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[3]/button[2]")
Click_Create_Conference.click()
time.sleep(3)
Ok_Button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button")
time.sleep(1)
Ok_Button.click()  # 创建会议完毕点击OK弹框
time.sleep(3)
"""
------------------------------------------------------------------------------------------------------------------------
"""
Create_Conference003 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                     "2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]")
Create_Conference003.click()  # 点击新建会议
time.sleep(1)
Create_Conference_type = driver.find_element(By.XPATH,
                                             "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]"
                                             "/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div"
                                             "/div/div/div/div[1]/div")
Create_Conference_type.click()  # 点击新建会议下一步  ”项目全图/会议纪要“
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是关键人士note
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是行业专家note
time.sleep(1)
Conference_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div/div[1]/div["
                                                "3]/span/div/input")
Conference_Time.click()
time.sleep(1)
Conference_Time1 = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a")
time.sleep(1)
Conference_Time1.click()  # 会议时间默认都为“今天”
time.sleep(1)
Conference_Modality = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div["
                                                    "3]/div/div[2]/div[3]/div/div")
Conference_Modality.click()
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.ENTER)  # 会议形式为“电话会”
time.sleep(1)
Click_Create_Conference = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                        "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[3]/button[2]")
Click_Create_Conference.click()
time.sleep(3)
Ok_Button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button")
Ok_Button.click()  # 创建会议完毕点击OK弹框
time.sleep(3)
"""
------------------------------------------------------------------------------------------------------------------------
"""
Create_Conference003 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                     "2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]")
Create_Conference003.click()  # 点击新建会议
time.sleep(1)
Create_Conference_type = driver.find_element(By.XPATH,
                                             "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]"
                                             "/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div"
                                             "/div/div/div/div[1]/div")
Create_Conference_type.click()  # 点击新建会议下一步  ”项目全图/会议纪要“
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是非关键人士note
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是行业专家note
time.sleep(1)
Conference_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div/div[1]/div["
                                                "3]/span/div/input")
Conference_Time.click()
time.sleep(1)
Conference_Time1 = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a")
time.sleep(1)
Conference_Time1.click()  # 会议时间默认都为“今天”
time.sleep(1)
Conference_Modality = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div["
                                                    "3]/div/div[2]/div[3]/div/div")
Conference_Modality.click()
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.ENTER)  # 会议形式为“电话会”
time.sleep(1)
Click_Create_Conference = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                        "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[3]/button[2]")
Click_Create_Conference.click()
time.sleep(3)
Ok_Button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button")
Ok_Button.click()  # 创建会议完毕点击OK弹框
time.sleep(3)
"""
------------------------------------------------------------------------------------------------------------------------
"""
Create_Conference003 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                     "2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]")
Create_Conference003.click()  # 点击新建会议
time.sleep(1)
Create_Conference_type = driver.find_element(By.XPATH,
                                             "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]"
                                             "/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div"
                                             "/div/div/div/div[1]/div")
Create_Conference_type.click()  # 点击新建会议下一步  ”项目全图/会议纪要“
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是非关键人士note
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.DOWN)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是复盘会
time.sleep(1)
Conference_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div/div[1]/div["
                                                "3]/span/div/input")
Conference_Time.click()
time.sleep(1)
Conference_Time1 = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/div[3]/span/a")
time.sleep(1)
Conference_Time1.click()  # 会议时间默认都为“今天”
time.sleep(1)
Conference_Modality = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div["
                                                    "3]/div/div[2]/div[3]/div/div")
Conference_Modality.click()
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.ENTER)  # 会议形式为“电话会”
time.sleep(1)
Click_Create_Conference = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                        "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div[3]/button[2]")
Click_Create_Conference.click()
time.sleep(3)
Ok_Button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button")
Ok_Button.click()  # 创建会议完毕点击OK弹框
time.sleep(3)
