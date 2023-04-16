import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

#   driver = webdriver.Edge(executable_path="E:\\study\\webdriver\\msedgedriver.exe")
s = Service(executable_path="C:\\py\\msedgedriver.exe")
driver = webdriver.Edge(service=s)  # 找到msedgedriver
wait = WebDriverWait(driver, 10)
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
time.sleep(5)
switchover = wait.until(ec.presence_of_element_located
                        ((By.XPATH, "/html/body/div/div/section/div/section/header/div")))
driver.execute_script("arguments[0].click();", switchover)  # 登录与切换菜单！！！！！
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
    .send_keys("流程-013")
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
    .send_keys("流程-013")
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
time.sleep(3)
Create_Conference1 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                   "3]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div")
Create_Conference1.click()  # 点击新建会议
time.sleep(1)
Create_Conference2 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                   "3]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div["
                                                   "2]/div/div/div/div/div[1]/div/div[1]")
Create_Conference2.click()  # 点击新建会议下一步  ”项目全图/会议纪要“
time.sleep(1)
Conference_Type = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div["
                                                "3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div["
                                                "3]/div/div")
Conference_Type.click()
time.sleep(1)
Conference_Type.send_keys(Keys.ENTER)  # 会议类型是项目全图
time.sleep(1)
Conference_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "3]/div[3]/div[1]/div[2]/div/div[3]/div[2]/div/div[3]/div/div[1]/div["
                                                "3]/span/div/input")
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
Ok_Button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
Ok_Button.click()  # 创建会议完毕点击OK弹框
time.sleep(6)
Edit_Memo = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[3]/div["
                                          "3]/div[1]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[1]/button")
time.sleep(2)
Edit_Memo.click()
time.sleep(5)  # 点击项目全图编辑按钮
Memo_Garde = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                           "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div["
                                           "2]/div[2]/div")
Memo_Garde.click()
time.sleep(1)
Memo_Garde.send_keys(Keys.ENTER)  # 默认主导人一人参会，并且评级为S
time.sleep(1)
Ok_Button2 = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]")
Ok_Button2.click()
time.sleep(6)  # 默认主导人一人参会，并且评级为S, 二次确认弹框
Founder_Grade_Button = driver.find_element(By.XPATH,
                                           "//html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                           "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div[3]/div/div["
                                           "3]/div/div[1]/div/div/button")
# driver.execute_script("arguments[0].scrollIntoView(true)", Founder_Grade_Button)
time.sleep(3)
# driver.execute_script("arguments[0].click();", Founder_Grade_Button)
Founder_Grade_Button.click()
time.sleep(3)
Founder_Grade = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                              "3]/div/div[3]/div/div[4]/div/div[2]/div/div/div[1]/div")
time.sleep(1)
driver.execute_script("arguments[0].click();", Founder_Grade)
time.sleep(1)
Founder_Grade.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde01 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[4]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde01)
time.sleep(1)
Founder_Garde01.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde02 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[4]/div[2]/div[1]/div[3]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde02)
time.sleep(1)
Founder_Garde02.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde03 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[4]/div[2]/div[1]/div[4]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde03)
time.sleep(1)
Founder_Garde03.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde04 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[4]/div[2]/div[1]/div[5]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde04)
time.sleep(1)
Founder_Garde04.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde05 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[4]/div[2]/div[1]/div[6]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde05)
time.sleep(1)
Founder_Garde05.send_keys(Keys.ENTER)
time.sleep(1)
Founder_Garde06 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                                "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[3]/div[8]/div["
                                                "3]/div/div[4]/div[2]/div[1]/div[7]/div/div[2]/div/div[1]/div/div/div")
driver.execute_script("arguments[0].click();", Founder_Garde06)
time.sleep(1)
Founder_Garde06.send_keys(Keys.ENTER)
time.sleep(3)  # 输入主导人的创始人维度评级（只填写六个）
Points = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[3]/div["
                                       "3]/div[1]/div[2]/div/div[3]/div/div/div[5]/div[3]/div/div[1]/div["
                                       "2]/div/div/div[1]/button")
driver.execute_script("arguments[0].click();", Points)
time.sleep(2)
Points1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[3]/div["
                                        "3]/div[1]/div[2]/div/div[3]/div/div/div[5]/div[3]/div/div[1]/div[1]/div["
                                        "2]/div/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]")
driver.execute_script("arguments[0].click();", Points1)
time.sleep(1)
Points1.send_keys("未知事的亮点")
time.sleep(1)
Points2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[3]/div["
                                        "3]/div[1]/div[2]/div/div[3]/div/div/div[5]/div[3]/div/div[1]/div[1]/div["
                                        "2]/div/div/div[1]/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div[1]")

driver.execute_script("arguments[0].click();", Points2)
time.sleep(1)
Points2.send_keys("未知事的风险")
time.sleep(1)
Points3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[3]/div["
                                        "3]/div[1]/div[2]/div/div[3]/div/div/div[5]/div[3]/div/div[1]/div[1]/div["
                                        "2]/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]")
driver.execute_script("arguments[0].click();", Points3)
time.sleep(1)
Points3.send_keys("未知人的亮点")
time.sleep(2)
Points4 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[3]/div["
                                        "3]/div[1]/div[2]/div/div[3]/div/div/div[5]/div[3]/div/div[1]/div[1]/div["
                                        "2]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div[1]")
driver.execute_script("arguments[0].click();", Points4)
time.sleep(1)
Points4.send_keys("未知人的风险")     # 输入主导人的天善观点
time.sleep(3)
Memo_OK_Button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                               "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[5]/div[3]/div/div["
                                               "1]/div[2]/div/div/div[1]/button[2]")
driver.execute_script("arguments[0].click();", Memo_OK_Button)
time.sleep(6)
Memo_Finish_Button = driver.find_element(By.XPATH, "/html/body/div[12]/div/div[2]/div/div[2]/div/div/div[2]/button")
time.sleep(1)
Memo_Finish_Button.click()
time.sleep(3)
Edit_Memo2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                           "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[2]/div/div/div["
                                           "1]/button")
time.sleep(1)
driver.execute_script("arguments[0].click();", Edit_Memo2)
time.sleep(8)
Ok_Button2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                           "3]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div[1]/div["
                                           "2]/button[2]")
time.sleep(1)
driver.execute_script("arguments[0].click();", Ok_Button2)
time.sleep(6)           # 重新点击项目全图编辑并保存，触发完成逻辑
hint = driver.find_element(By.XPATH, "/html/body/div[12]/div/div[2]/div/div[2]/div/div/div[1]/span/div")
time.sleep(1)
print("项目全图完成成功提示：{}。".format(hint.text))
Ok_Button3 = driver.find_element(By.XPATH, "/html/body/div[12]/div/div[2]/div/div[2]/div/div/div[2]/button")
time.sleep(1)
driver.execute_script("arguments[0].click();", Ok_Button3)
time.sleep(3)
""""
Wait_Application = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]"
                                                 "/div[3]/div[1]/div[2]/div/div[3]/div/div/div[5]/div[3]/div[2]"
                                                 "/label[3]/span[2]")
driver.execute_script("arguments[0].scrollIntoView(false)", Wait_Application)  # 定位到元素与页面底部对齐
time.sleep(1)
driver.execute_script("arguments[0].click();", Wait_Application)
time.sleep(1)
Confirm_Submit_Button = driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]"
                                            "/div[3]/div[1]/div[2]/div/div[3]/div/div/div[5]/div[3]/div[3]/button")
time.sleep(1)
driver.execute_script("arguments[0].click();", Confirm_Submit_Button)
time.sleep(2)
Wait_Application_Button = driver.find_element(By.XPATH,
                                              "/html/body/div[12]/div/div[2]/div/div[2]/div/div/div[2]/button[2]")
time.sleep(1)
driver.execute_script("arguments[0].click();", Wait_Application_Button)
time.sleep(3)
Ok_Button2 = driver.find_element(By.XPATH, "/html/body/div[12]/div/div[2]/div/div[2]/div/div/div[2]/button")
time.sleep(1)
driver.execute_script("arguments[0].click();", Ok_Button2)
time.sleep(1)           # 待申请点击并且确定

"""
