import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# import unittest
driver = webdriver.Edge(service=Service(executable_path="C:\\py\\msedgedriver.exe"))  # 找到msedgedriver
wait = WebDriverWait(driver, 20)
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
switchover = wait.until(ec.presence_of_element_located
                        ((By.XPATH, "/html/body/div/div/section/div/section/header/div")))
driver.execute_script("arguments[0].click();", switchover)
# switchover.click()    # 登录与切换菜单！！！！！

deal_subscript = wait.until(ec.presence_of_element_located
                            ((By.XPATH, "/html/body/div/div/section/div/section/main/div[1]/ul/li["
                                        "2]/div/span/span[1]")))
deal_subscript.click()
time.sleep(1)
deal_my = wait.until(ec.presence_of_element_located(
    (By.XPATH, "/html/body/div/div/section/div/section/main/div[1]/ul/"
               "li[2]/ul/li[2]/span[1]")))
deal_my.click()

create_deal = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div/div[1]/"
                                            "div[1]/div[2]/button")
create_deal.click()
time.sleep(5)
deal_name = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]/div"
                                          "/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/input") \
    .send_keys("A级别-017")
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
    .send_keys("A级别-017")
manager_list = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                             "2]/div/div[1]/div[6]/div[2]/div[1]/div[1]/div/div[2]/div/div["
                                             "2]/div/div/div")
manager_list.click()
#   Select(manager_list).select_by_visible_text("投资经理2")    #  selenium.common.exceptions.UnexpectedTagName
#   Exception: Message: Select only works on <select> elements, not on <div>
time.sleep(2)
manager_list.send_keys(Keys.DOWN)
manager_list.send_keys(Keys.DOWN)
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
Create_Conference1 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                   "3]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div")
Create_Conference1.click()  # 点击新建会议
time.sleep(1)
Create_Conference2 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                   "3]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div["
                                                   "2]/div/div/div/div/div[1]/div/div[1]")
Create_Conference2.click()  # 点击新建会议下一步  ”项目全图/会议纪要“
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是项目全图
time.sleep(1)
Conference_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div/div[1]/div["
                                                "3]/span")
Conference_Time.click()
time.sleep(1)
Conference_Time1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[2]/div[3]/span/a")
Conference_Time1.click()  # 会议时间默认都为“今天”
time.sleep(1)
Conference_Modality = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div["
                                                    "3]/div/div[2]/div[3]/div/div")
Conference_Modality.click()
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.DOWN)
Conference_Modality.send_keys(Keys.ENTER)  # 会议形式为“电话会”
time.sleep(1)
Click_Create_Conference = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div"
                                                        "/div/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[3]/button[2]")
Click_Create_Conference.click()
time.sleep(6)
create_success_info = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[1]/span")
print("创建成功提示文案：{}".format(create_success_info.text))
Ok_Button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
Ok_Button.click()  # 创建会议完毕点击OK弹框
time.sleep(6)
Memo_Garde = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                           "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div["
                                           "2]/div[2]/div")
Memo_Garde.click()
time.sleep(1)
Memo_Garde.send_keys(Keys.DOWN)
Memo_Garde.send_keys(Keys.ENTER)  # 默认主导人一人参会，并且评级为A
time.sleep(1)
Garde_Ok_Button = wait.until(
    ec.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]")))
Garde_Ok_Button.click()
time.sleep(2)
driver.refresh()
time.sleep(6)
driver.switch_to.window(windows[-1])
Memo_Edit_Button = wait.until(
    ec.presence_of_element_located((By.XPATH, "//html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                              "/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div["
                                              "2]/div/div/div/div[1]/button")))
Memo_Edit_Button.click()
time.sleep(5)  # 点击编辑按钮
Product_Core_Business = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                      "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div["
                                                      "3]/div[3]/div/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div["
                                                      "1]")
Product_Core_Business.click()
time.sleep(1)
Product_Core_Business.send_keys("核心业务")
time.sleep(1)  # 在核心业务中输入
Product_Core_Business.send_keys(Keys.CONTROL, "a")
time.sleep(1)
Size = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                     "3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[3]/div[3]/div/div[1]/div/div["
                                     "2]/div[3]/div/div/div/div[1]/span[4]/span/span[1]")
time.sleep(1)
Size.click()
time.sleep(1)
Size01 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                       "3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[3]/div[3]/div/div[1]/div/div["
                                       "2]/div[3]/div/div/div/div[1]/span[4]/span/span[2]/span[1]")
Size01.click()
time.sleep(1)  # 设置字体
Background_color = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                 "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[3]/div["
                                                 "3]/div/div[1]/div/div[2]/div[3]/div/div/div/div[1]/span[8]/span["
                                                 "2]/span[1]")
time.sleep(1)
Background_color.click()
time.sleep(1)
Background_color01 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                   "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div["
                                                   "3]/div[3]/div/div[1]/div/div[2]/div[3]/div/div/div/div[1]/span["
                                                   "8]/span[2]/span[2]/span[2]")
time.sleep(1)
Background_color01.click()
time.sleep(1)  # 选中文字添加背景颜色和字体
Product_Similar_to = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                   "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div["
                                                   "3]/div[3]/div/div[2]/div/div/div[3]/div/div/div/textarea")
Product_Similar_to.click()
time.sleep(1)
Product_Similar_to.send_keys("类似于的")
time.sleep(1)  # 在类似于中输入
Product = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                        "3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[3]/div[3]/div/div[3]/div/div["
                                        "2]/div[3]/div/div/div/div[2]/div[1]")
time.sleep(1)
Product.click()
time.sleep(1)
Product.send_keys("未知的产品")  # 在产品中输入
time.sleep(2)
Current_Market_Overview = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div"
                                                        "/div/div[2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div["
                                                        "3]/div[4]/div[3]/div/div[3]/div/div[2]/div["
                                                        "3]/div/div/div/div[2]/div[1]")
time.sleep(1)
Current_Market_Overview.click()
time.sleep(1)
Current_Market_Overview.send_keys("未知的当前市场概述")  # 在当前市场概述中输入
time.sleep(2)
Client = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                       "3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[7]/div/div["
                                       "2]/div[3]/div/div/div/div[2]/div[1]")
time.sleep(1)
Client.click()
time.sleep(1)
Client.send_keys("未知的用户和客户")
time.sleep(2)
Market_Size01 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div["
                                              "3]/div/div[10]/div[3]/div/div[1]/div[1]/div[1]/div/div["
                                              "2]/div/div/input")
Market_Size01.send_keys("未知的当前规模定义")
time.sleep(1)
Market_Size02 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div["
                                              "3]/div/div[10]/div[3]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div["
                                              "2]/input")
Market_Size02.send_keys("666")
time.sleep(1)
Market_Size03 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div["
                                              "3]/div/div[10]/div[3]/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div["
                                              "2]/input")
Market_Size03.send_keys("667")
time.sleep(1)  # 在市场规模中输入当前规模定义、当前年GMV规模、当前年收入规模
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[10]/div[3]/div/div[2]/div["
                              "1]/div[1]/div/div[2]/div/div/input").send_keys("未知的潜在规模")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[10]/div[3]/div/div[2]/div["
                              "1]/div[2]/div/div[2]/div/div/div[2]/input").send_keys("668")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[10]/div[3]/div/div[2]/div["
                              "1]/div[4]/div/div[2]/div/div/div[2]/input").send_keys("669")
time.sleep(2)  # 在市场规模中输入潜在规模、潜在年GMV规模、潜在年收入规模
Computing_Method = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                 "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div["
                                                 "3]/div/div[10]/div[3]/div/div[3]/div/div[2]/div[2]/div/div/div/div["
                                                 "2]/div[1]")
time.sleep(1)
Computing_Method.click()
time.sleep(1)
Computing_Method.send_keys("未知的计算方式")  # 是在当前规模中的计算方式中输入
time.sleep(2)
"----------------------------------------------------------------------------------------------------------------------"
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[11]/div[3]/div/div[1]/div["
                              "1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/textarea") \
    .send_keys("未知的上游一号")

time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[11]/div[3]/div/div[1]/div["
                              "1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/textarea") \
    .send_keys("未知的上游一号的承担职责")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[11]/div[3]/div/div[1]/div["
                              "1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/textarea") \
    .send_keys("未知的环节名称")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[11]/div[3]/div/div[1]/div["
                              "1]/div[2]/div[2]/div/div/div[2]/div/div/div/div/textarea") \
    .send_keys("未知的环节名称的承担职责")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[11]/div[3]/div/div[1]/div["
                              "1]/div[3]/div/div/div[2]/div/div/div[1]/div/div/div/div/textarea") \
    .send_keys("未知的下游一号")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[11]/div[3]/div/div[1]/div["
                              "1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div/textarea") \
    .send_keys("未知的下游一号的承担职责")
time.sleep(2)  # 在价值链条中输入上游下游
Income_Mode = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                            "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div["
                                            "12]/div[3]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]")
time.sleep(1)
Income_Mode.click()
time.sleep(1)
Income_Mode.send_keys("未知的收入模式")  # 在收入模式中输入
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/textarea") \
    .send_keys("竞品一号名称")
time.sleep(1)
Year_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                          "3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div["
                                          "3]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div["
                                          "2]/div/div/div/div/div/div/div[1]")
time.sleep(1)
Year_Time.click()
time.sleep(1)
Year_Time01 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                            "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div["
                                            "13]/div[3]/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div["
                                            "2]/div/div/div/div/div/div/div[2]/div/input")
time.sleep(1)
Year_Time01.send_keys("2023")
time.sleep(1)
Year_Time01.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div/div/div/textarea") \
    .send_keys("江苏省")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[1]/div[2]/div/div[2]/div/div/div[4]/div/div/div/div/textarea") \
    .send_keys("融资一块钱")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[1]/div[2]/div/div[2]/div/div/div[5]/div/div/div/div/textarea") \
    .send_keys("竞品未知的收入模式")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[1]/div[2]/div/div[2]/div/div/div[6]/div/div/div/div/textarea") \
    .send_keys("竞品未知的核心竞争力")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[1]/div[2]/div/div[2]/div/div/div[7]/div/div/div/div/textarea") \
    .send_keys("竞品未知的创始人信息")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/div/textarea") \
    .send_keys("未知的对标")
time.sleep(1)
Year_Time02 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                            "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div["
                                            "13]/div[3]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div["
                                            "2]/div/div/div/div/div/div/div[1]")
time.sleep(2)
Year_Time02.click()
time.sleep(1)
Year_Time05 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                            "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div["
                                            "13]/div[3]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div["
                                            "2]/div/div/div/div/div/div/div[2]/div/input")
time.sleep(1)
Year_Time05.send_keys("2022")
time.sleep(1)
Year_Time05.send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div/div/textarea") \
    .send_keys("上海市")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[2]/div/div/div[2]/div/div/div[4]/div/div/div/div/textarea") \
    .send_keys("融资一个亿")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div/textarea") \
    .send_keys("对标未知的收入模式")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[2]/div/div/div[2]/div/div/div[6]/div/div/div/div/textarea") \
    .send_keys("对标未知的核心竞争力")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[4]/div[3]/div/div[13]/div[3]/div/div[1]/div["
                              "1]/div[2]/div/div/div[2]/div/div/div[7]/div/div/div/div/textarea") \
    .send_keys("对标未知的创始人信息")
time.sleep(2)  # 输入竞品与对标
"---------------------------------------------------------------------------------------------------------------------"
# 运营情况
Company_Start_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                   "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div["
                                                   "5]/div[3]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div["
                                                   "2]/div/span")
time.sleep(1)
Company_Start_Time.click()
time.sleep(1)
Company_Start_Time01 = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div/div/div[2]/div/div["
                                                     "2]/table/tbody/tr[3]/td[3]")
time.sleep(1)
Company_Start_Time01.click()
time.sleep(2)  # 在公司启动时间中选中2022的当前月份
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[3]/div[3]/div/div[2]/div["
                              "1]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/input") \
    .send_keys("66666")  # 在4年营收情况中的收入输入今年字段
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[3]/div[3]/div/div[2]/div["
                              "1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/input") \
    .send_keys("66667")  # 在4年营收情况中的收入输入明年字段
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[3]/div[3]/div/div[2]/div["
                              "1]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div[2]/input") \
    .send_keys("66668")  # 在4年营收情况中的收入输入后年字段
time.sleep(1)  # 在4年营收情况中输入收入一栏
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[3]/div[3]/div/div[2]/div["
                              "1]/div/div[3]/div[2]/div/div[1]/div/div/div/div/div[2]/input") \
    .send_keys("66669")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[3]/div[3]/div/div[2]/div["
                              "1]/div/div[3]/div[2]/div/div[2]/div/div/div/div/div[2]/input") \
    .send_keys("66670")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[3]/div[3]/div/div[2]/div["
                              "1]/div/div[3]/div[2]/div/div[3]/div/div/div/div/div[2]/input") \
    .send_keys("6665")
time.sleep(2)  # 在4年营收情况中输入净利润一栏
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[4]/div[3]/div/div[1]/div["
                              "1]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/textarea") \
    .send_keys("线上-广告投入")  # 在获客方式的方式中输入
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[4]/div[3]/div/div[1]/div["
                              "1]/div/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/textarea") \
    .send_keys("未知的渠道")  # 在获客方式的渠道中输入
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[4]/div[3]/div/div[1]/div["
                              "1]/div/div[2]/div/div[1]/div/div/div[3]/div/div/div/div/textarea") \
    .send_keys("未知量化详情")  # 在获客方式的量化详情中输入
time.sleep(1)  # 输入获客方式
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[6]/div[3]/div/div["
                              "1]/div/div/div/div[2]/div/div[1]/div[2]/input") \
    .send_keys("66")  # 输入员工总数
time.sleep(3)
Department = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                           "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div["
                                           "6]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div/div["
                                           "1]/div/div/div/div")
time.sleep(1)
Department.click()
time.sleep(1)
Department01 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                             "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div["
                                             "3]/div/div[6]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div/div["
                                             "1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div/input")
time.sleep(1)
Department01.send_keys("产品")
Department01.send_keys(Keys.ENTER)
time.sleep(2)  # 选择部门为产品
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[6]/div[3]/div/div[2]/div["
                              "1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/input") \
    .send_keys("66")
time.sleep(1)  # 在年月的员工
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[6]/div[3]/div/div[2]/div["
                              "1]/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/div/div/div[2]/input") \
    .send_keys("66")
time.sleep(2)  # 在年月的员工
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[7]/div[3]/div/div[1]/div["
                              "1]/div[1]/div/div[2]/div/div/div[2]/input") \
    .send_keys("665")  # 输入账上现金余额
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[7]/div[3]/div/div[1]/div["
                              "1]/div[3]/div/div[2]/div/div/div[2]/input") \
    .send_keys("656")  # 输入账上现金余额
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[7]/div[3]/div/div[1]/div["
                              "1]/div[5]/div/div[2]/div/div/div[2]/input") \
    .send_keys("6565")  # 输入应付
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[7]/div[3]/div/div[2]/div["
                              "2]/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/input") \
    .send_keys("未知的支出类型")  # 输入支出类型
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[7]/div[3]/div/div[2]/div["
                              "2]/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/input") \
    .send_keys("6656")  # 输入支出金额
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[7]/div[3]/div/div[3]/div["
                              "2]/div[1]/div/div/div[1]/div/div[2]/div/div/input") \
    .send_keys("当前最大单一支出类型的未知的支出类型")  # 输入当前最大单一支出类型的支出类型
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[5]/div[3]/div/div[7]/div[3]/div/div[3]/div["
                              "2]/div[1]/div/div/div[2]/div/div[2]/div/div/div[2]/input") \
    .send_keys("765")  # 输入当前最大单一支出类型的支出金额
time.sleep(2)
Company_Development = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div"
                                                    "/div[2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div["
                                                    "5]/div[3]/div/div[8]/div/div[2]/div[3]/div/div/div/div[2]/div[1]")
time.sleep(1)
Company_Development.click()
time.sleep(1)
Company_Development.send_keys("未知的公司发展历程及八卦")  # 输入公司发展历程及八卦
time.sleep(2)
# 股东/董事
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div[3]/div/div[2]/div[1]/div[2]/div["
                              "2]/div/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/input") \
    .send_keys("未知的股东名称")  # 输入股东名称
time.sleep(1)
Shareholder = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                            "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div[3]/div/div["
                                            "2]/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div/div["
                                            "2]/div/div/div/div/div")
time.sleep(1)
Shareholder.click()
time.sleep(1)
Shareholder.send_keys(Keys.ENTER)  # 输入股东身份为创始人
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div[3]/div/div[2]/div[1]/div[2]/div["
                              "2]/div/div[1]/div/div/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/input") \
    .send_keys("100")  # 输入持股为100，
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div[3]/div/div[2]/div[1]/div[2]/div["
                              "2]/div/div[1]/div/div/div[1]/div/div/div[4]/div/div/div/div/div[2]/input") \
    .send_keys("88888")  # 输入融资金额
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div[3]/div/div[2]/div[1]/div["
                              "4]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/input") \
    .send_keys("未知的ESOP")  # 输入ESOP
time.sleep(1)
Shareholder01 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div["
                                              "3]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/div[1]/div/div/div["
                                              "2]/div/div/div/div/div")
time.sleep(1)
Shareholder01.click()
time.sleep(1)
Shareholder01.send_keys(Keys.ENTER)  # 输入股东身份为初创创始人
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div[3]/div/div[2]/div[1]/div["
                              "4]/div/div/div[1]/div/div/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/input") \
    .send_keys("0")  # 输入ESOP持股为0
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div[3]/div/div[2]/div[1]/div["
                              "4]/div/div/div[1]/div/div/div[1]/div/div/div[4]/div/div/div/div/div[2]/input") \
    .send_keys("88889")  # 输入融资金额
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div[3]/div/div[2]/div[1]/div[3]/div["
                              "1]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div/div[2]/input") \
    .send_keys("0")  # 在ESOP上方选择持股为0
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div[3]/div/div[2]/div[1]/div[3]/div["
                              "1]/div/div/div[1]/div/div/div[3]/div/div/div/div/div[2]/input") \
    .send_keys("88898")  # 输入融资金额
time.sleep(1)
Previous_Round = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                               "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div["
                                               "3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div["
                                               "2]/div/div/div/div/div[2]/div/div/div")
time.sleep(1)
Previous_Round.click()
time.sleep(1)
Previous_Round.send_keys(Keys.ENTER)  # 选择上一轮为尚不融资
time.sleep(2)
Share = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                      "3]/div[""1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div[3]/div/div[2]/div["
                                      "1]/div[5]/div[""1]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]")
print("持股：{}".format(Share.text))
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[6]/div[3]/div/div[3]/div[2]/div["
                              "1]/div/div/div[1]/div/div/div/div/div[2]/input") \
    .send_keys("666888")  # 输入累计融资
time.sleep(2)
# 融资情况
Previous_Round = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                               "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[7]/div["
                                               "3]/div/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div")
time.sleep(1)
Previous_Round.click()
time.sleep(1)
Previous_Round.send_keys(Keys.ENTER)  # 在融资情况中的上一轮选择为“尚未融资”
time.sleep(1)
Round = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                      "3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[7]/div[3]/div/div[2]/div["
                                      "1]/div[1]/div/div[3]/div/div[2]/div/div/div")
time.sleep(1)
Round.click()
time.sleep(1)
Round.send_keys(Keys.ENTER)  # 在融资情况中的本轮选择为“尚未融资”
time.sleep(1)
Next_Round = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                           "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[7]/div[3]/div/div["
                                           "2]/div[1]/div[1]/div/div[4]/div/div[2]/div/div/div")
time.sleep(1)
Next_Round.click()
time.sleep(1)
Next_Round.send_keys(Keys.ENTER)  # 在融资情况中的下一轮选择为“尚未融资”
time.sleep(2)
# 核心团队
Sex = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                    "3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/div[1]/div[3]/div["
                                    "1]/div[1]/div[2]/div/div[1]/div/div[3]/div/div[2]/div/div/div")
time.sleep(1)
Sex.click()
time.sleep(1)
Sex.send_keys(Keys.ENTER)  # 性别选择男
time.sleep(1)
Location = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                         "3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/div[1]/div["
                                         "3]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div[2]/div/div/div")
time.sleep(1)
Location.click()
time.sleep(1)
Location01 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                           "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/div["
                                           "1]/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div[4]/div/div["
                                           "2]/div/div/div/div/div[2]/div/input")
time.sleep(1)
Location01.send_keys("上海市")
time.sleep(1)
Location01.send_keys(Keys.ENTER)  # 在常住地中输入上海市
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/div[1]/div[3]/div[1]/div[1]/div["
                              "2]/div/div[7]/div[2]/div/div[1]/div/div/div/div[2]/div/div/input") \
    .send_keys("19988886666")  # 在手机号码中输入
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/div[1]/div[3]/div[1]/div[1]/div["
                              "2]/div/div[5]/div/div/div/div[2]/div/div/div/div/ul/li/div/input") \
    .send_keys("未知的职业亮点")  # 在职业亮点中输入
time.sleep(1)
Work_Location = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                              "3]/div/div[1]/div[3]/div[1]/div[3]/div[2]/div/div[1]/div/div/div["
                                              "1]/div/div/div[1]/div/div[3]/div/div[2]/div/div/div")
time.sleep(1)
Work_Location.click()
time.sleep(1)
Work_Location01 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[1]/div[3]/div[1]/div[3]/div[2]/div/div[1]/div/div/div["
                                                "1]/div/div/div[1]/div/div[3]/div/div[2]/div/div/div/div/div["
                                                "2]/div/input")
time.sleep(1)
Work_Location01.send_keys("上海市")
time.sleep(1)
Work_Location01.send_keys(Keys.ENTER)  # Z工作地点输入上海市
time.sleep(2)
"--------------------------------------------------------------------------------------------------------------------"
# 主导人的创始人十个维度评级
Founder_Grade_Button = driver.find_element(By.XPATH,
                                           "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]"
                                           "/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/div[3]"
                                           "/div/div[1]/div/div/button")
# driver.execute_script("arguments[0].scrollIntoView(true)", Founder_Grade_Button)
time.sleep(3)
# driver.execute_script("arguments[0].click();", Founder_Grade_Button)
Founder_Grade_Button.click()
time.sleep(3)
Founder_Grade = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]"
                                              "/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/"
                                              "div[3]/div/div[4]/div/div[2]/div/div/div[1]/div")
time.sleep(1)
driver.execute_script("arguments[0].click();", Founder_Grade)
time.sleep(1)
Founder_Grade.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde01 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[4]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde01)
time.sleep(1)
Founder_Garde01.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde02 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[4]/div[2]/div[1]/div[3]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde02)
time.sleep(1)
Founder_Garde02.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde03 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]"
                                                "/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/"
                                                "div[4]/div[2]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde03)
time.sleep(1)
Founder_Garde03.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde04 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[4]/div[2]/div[1]/div[5]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde04)
time.sleep(1)
Founder_Garde04.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde05 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[4]/div[2]/div[1]/div[6]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde05)
time.sleep(1)
Founder_Garde05.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde06 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[4]/div[2]/div[1]/div[7]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde06)
time.sleep(1)
Founder_Garde06.send_keys(Keys.ENTER)
time.sleep(3)  # 输入主导人的创始人维度评级（只填写六个）
# 其他核心团队成员背景资料
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/div[5]/div[3]/div[1]/div["
                              "2]/div/div/div[1]/div/div/div[1]/div/div/div/div/input") \
    .send_keys("张三")  # 姓名
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/div[5]/div[3]/div[1]/div["
                              "2]/div/div/div[1]/div/div/div[2]/div/div/div/div/input") \
    .send_keys("未知的职位")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/div[5]/div[3]/div[1]/div["
                              "2]/div/div/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/input") \
    .send_keys("100")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div[3]/div["
                              "1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/div[5]/div[3]/div[1]/div["
                              "2]/div/div/div[1]/div/div/div[4]/div/div/div/div/textarea") \
    .send_keys("一号  二号  十分优秀")
time.sleep(2)
"---------------------------------------------------------------------------------------------------------------"
# 天善观点
Points = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                       "3]/div[1]/div[2]/div/div[3]/div/div/div[6]/div[3]/div/div[1]/div["
                                       "2]/div/div/div[1]/button")
driver.execute_script("arguments[0].click();", Points)
time.sleep(2)
Points1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                        "3]/div[1]/div[2]/div/div[3]/div/div/div[6]/div[3]/div/div[1]/div[1]/div["
                                        "2]/div/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]")
driver.execute_script("arguments[0].click();", Points1)
time.sleep(1)
Points1.send_keys("未知事的亮点")
time.sleep(1)
Points2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                        "3]/div[1]/div[2]/div/div[3]/div/div/div[6]/div[3]/div/div[1]/div[1]/div["
                                        "2]/div/div/div[1]/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div[1]")

driver.execute_script("arguments[0].click();", Points2)
time.sleep(1)
Points2.send_keys("未知事的风险")
time.sleep(1)
Points3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                        "3]/div[1]/div[2]/div/div[3]/div/div/div[6]/div[3]/div/div[1]/div[1]/div["
                                        "2]/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]")
driver.execute_script("arguments[0].click();", Points3)
time.sleep(1)
Points3.send_keys("未知人的亮点")
time.sleep(2)
Points4 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]/div["
                                        "3]/div[1]/div[2]/div/div[3]/div/div/div[6]/div[3]/div/div[1]/div[1]/div["
                                        "2]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div[1]")
driver.execute_script("arguments[0].click();", Points4)
time.sleep(1)
Points4.send_keys("未知人的风险")  # 输入主导人的天善观点
time.sleep(3)
Memo_Save_Button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                 "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div["
                                                 "1]/div[2]/button[2]")
Memo_Save_Button.click()  # 项目全图保存按钮
time.sleep(6)
Memo_Save_Success_Button = driver.find_element(By.XPATH, "/html/body/div[26]/div/div[2]/div/div[2]/div/div/div["
                                                         "2]/button")
Success = driver.find_element(By.XPATH, "/html/body/div[26]/div/div[2]/div/div[2]/div/div/div[1]/span")
print("保存成功提示：{}".format(Success.text))
time.sleep(1)
Memo_Save_Success_Button.click()

"""
class TestWow(unittest.TestCase):
    def test01(self):
        self.assertEqual(create_success_info.text, "创建成功")


if __name__ == "__main__":
    unittest.main()

"""
