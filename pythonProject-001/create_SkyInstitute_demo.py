import time
import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys

#   from selenium.webdriver.support.ui import Select

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
switchover.click()
time.sleep(1)  # 登录与切换菜单！！！！！
SkyInstitute = driver.find_element(By.XPATH, "/html/body/div/div/section/div/section/main/div[1]/ul/li[3]/span[1]")
SkyInstitute.click()
time.sleep(3)
#   links = driver.find_elements(By.PARTIAL_LINK_TEXT, "查看研究院通知")
#   links[0].click()
create_SkyInstitute = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div["
                                                    "2]/div/div[3]/div[1]/div[2]/div[1]/button[2]")
create_SkyInstitute.click()
time.sleep(2)
SkyInstitute_Grade = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div[2]/div["
                                                   "2]/div[""1]/div/div[ ""1]/div[3]/div/div")
SkyInstitute_Grade.click()
time.sleep(1)
SkyInstitute_Grade.send_keys(Keys.ENTER)  # 默认为S级别
time.sleep(1)
SkyInstitute_name = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div[2]/div["
                                                  "2]/div[1]/div/div[2]/div[3]/div/textarea") \
    .send_keys("研究院之未知研究-0001")
time.sleep(1)
SkyInstitute_question = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div["
                                                      "2]/div[2]/div[1]/div/div[3]/div[3]/div/textarea") \
    .send_keys("研究未知问题")
time.sleep(1)
SkyInstitute_object = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div["
                                                    "2]/div[2]/div[1]/div/div[4]/div[3]/div/textarea") \
    .send_keys("研究未知目标")
time.sleep(1)
SkyInstitute_initiator = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div"
                                                       "/div[2]/div[2]/div[3]/div/div[1]/div[3]/div/div")
SkyInstitute_initiator.click()
SkyInstitute_initiator.send_keys(Keys.DOWN)
SkyInstitute_initiator.send_keys(Keys.ENTER)
time.sleep(1)
SkyInstitute_functionary = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div["
                                                         "2]/div[2]/div[3]/div/div[2]/div[3]/div/div")
SkyInstitute_functionary.send_keys(Keys.ENTER)
time.sleep(1)
SkyInstitute_functionary.send_keys(Keys.DOWN)
SkyInstitute_functionary.send_keys(Keys.DOWN)
SkyInstitute_functionary.send_keys(Keys.DOWN)
SkyInstitute_functionary.send_keys(Keys.DOWN)
SkyInstitute_functionary.send_keys(Keys.DOWN)
SkyInstitute_functionary.send_keys(Keys.DOWN)
SkyInstitute_functionary.send_keys(Keys.DOWN)
SkyInstitute_functionary.send_keys(Keys.DOWN)
SkyInstitute_functionary.send_keys(Keys.DOWN)
SkyInstitute_functionary.send_keys(Keys.ENTER)  # 主导人为钱立民扫码，模拟键盘上下健选择到的
time.sleep(1)
Date_time1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div"
                                           "/div[2]/div[2]/div[4]/div/div[1]/div[3]/span/div/input")
Date_time1.click()
time.sleep(1)
Start_Time = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div[1]/div/input")
ST1 = datetime.date.today()  # 获取当前时间
Start_Time.send_keys(str(ST1))  # 输入当前时间，是在选择日期框中输入时间
time.sleep(1)
Start_Time.send_keys(Keys.ENTER)
time.sleep(1)
Date_time2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div"
                                           "/div[2]/div[2]/div[4]/div/div[2]/div[3]/span/div/input")
Date_time2.click()
time.sleep(1)
End_time = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[1]/div/input")
time.sleep(1)
Next_Page = driver.find_element(By.CLASS_NAME, "ant-calendar-next-month-btn")
Next_Page.click()  # 选择下一个月再次输入时间
time.sleep(1)
End_time.send_keys(str(ST1 + datetime.timedelta(days=30)))  # 输入结束时间，默认周期为一个月 30天
time.sleep(1)
End_time.send_keys(Keys.ENTER)
# js = "document.getElementByXpath('/html/body/div[5]/div/div/div/div/div[2]/div[3]/span/a').removeAttribute(
# 'readonly')"
# driver.execute_script(js)           getElementByXXX使用需要ID属性定位最好
submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div[2]/div["
                                              "1]/div[2]/button")
submit_button.click()  # 主研究创建完毕
time.sleep(5)  # 界面加载慢，需要等待久一点，
Create_Institute_Sub = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div["
                                                     "2]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/button/span")
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView(true)", Create_Institute_Sub)  # 定位到元素与页面顶部对齐
# driver.execute_script("arguments[0].scrollIntoView(false)", Create_Institute_Sub) # 页面底部对齐
time.sleep(1)
driver.execute_script("arguments[0].click();", Create_Institute_Sub)  # element click intercepted解决方式
time.sleep(1)
Institute_Sub_Grade = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div["
                                                    "2]/div[2]/div[3]/div[1]/div[2]/div[2]/div["
                                                    "2]/div/div/div/div/div/div/table/tbody/tr[2]/td/div/div[2]/div["
                                                    "1]/div[2]/div[1]/div/div[1]/div[3]/div/div")
time.sleep(1)
Institute_Sub_Grade.click()
time.sleep(1)
Institute_Sub_Grade.send_keys(Keys.DOWN)
Institute_Sub_Grade.send_keys(Keys.ENTER)
time.sleep(1)
Institute_Sub_Name = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div["
                                                   "2]/div[2]/div[3]/div[1]/div[2]/div[2]/div["
                                                   "2]/div/div/div/div/div/div/table/tbody/tr[2]/td/div/div[2]/div["
                                                   "1]/div[2]/div[2]/div/div[1]/div[3]/div/textarea") \
    .send_keys("未知的子研究")
time.sleep(1)
Institute_Sub_Initiator = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div["
                                                        "2]/div[2]/div[3]/div[1]/div[2]/div[2]/div["
                                                        "2]/div/div/div/div/div/div/table/tbody/tr[2]/td/div/div["
                                                        "2]/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/div")
Institute_Sub_Initiator.click()
time.sleep(1)
Institute_Sub_Initiator.send_keys(Keys.ENTER)
time.sleep(1)  # 选择子研究的主导人
Institute_Sub_Date_Time1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div["
                                                         "2]/div[2]/div[3]/div[1]/div[2]/div[2]/div["
                                                         "2]/div/div/div/div/div/div/table/tbody/tr[2]/td/div/div["
                                                         "2]/div[1]/div[2]/div[3]/div/div[1]/div[3]/span/div/input")
Institute_Sub_Date_Time1.click()
time.sleep(1)
Institute_Sub_Start_Time = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[1]/div/input")
Institute_Sub_Start_Time.click()
time.sleep(1)
Institute_Sub_Start_Time.send_keys(str(ST1))
time.sleep(1)
Institute_Sub_Start_Time.send_keys(Keys.ENTER)  # 选择子研究开始时间与主研究一致
time.sleep(1)
Institute_Sub_Date_Time2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div["
                                                         "2]/div[2]/div[3]/div[1]/div[2]/div[2]/div["
                                                         "2]/div/div/div/div/div/div/table/tbody/tr[2]/td/div/div["
                                                         "2]/div[1]/div[2]/div[3]/div/div[2]/div[3]/span/div/input")
Institute_Sub_Date_Time2.click()
time.sleep(1)
Institute_Sub_End_Time = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div[1]/div/input")
time.sleep(1)
Institute_Sub_End_Time_Next_Page = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div[2]/div["
                                                                 "1]/div/a[3]")
time.sleep(1)
Institute_Sub_End_Time_Next_Page.click()
time.sleep(1)
Institute_Sub_End_Time.send_keys(str(ST1 + datetime.timedelta(days=30)))
time.sleep(1)
Institute_Sub_End_Time.send_keys(Keys.ENTER)
time.sleep(1)   # 子研究开始时间与截止时间
Milestone_Name = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div[2]/div["
                                               "2]/div[3]/div[1]/div[2]/div[2]/div["
                                               "2]/div/div/div/div/div/div/table/tbody/tr[2]/td/div/div[2]/div["
                                               "2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div[1]/div["
                                               "3]/input")
driver.execute_script("arguments[0].scrollIntoView(true)", Milestone_Name)  # 定位到元素与页面顶部对齐
time.sleep(2)
Milestone_Name.send_keys("未知的里程碑")
time.sleep(1)
Milestone_Name_Date_Time = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div["
                                                         "2]/div[2]/div[3]/div[1]/div[2]/div[2]/div["
                                                         "2]/div/div/div/div/div/div/table/tbody/tr[2]/td/div/div["
                                                         "2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div["
                                                         "2]/div/div[2]/div[3]/span/div/input")
Milestone_Name_Date_Time.click()
time.sleep(1)
Milestone_End_Time_Next_Page = driver.find_element(By.CLASS_NAME, "ant-calendar-next-month-btn")
Milestone_End_Time_Next_Page.click()
time.sleep(1)
Milestone_End_Time = driver.find_element(By.CLASS_NAME, "ant-calendar-input ")
Milestone_End_Time.click()
time.sleep(1)
Milestone_End_Time.send_keys(str(ST1 + datetime.timedelta(days=30)))
time.sleep(1)
Milestone_End_Time.send_keys(Keys.ENTER)
Institute_Sub_Submit = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div["
                                                     "2]/div[2]/div[3]/div[1]/div[2]/div[2]/div["
                                                     "2]/div/div/div/div/div/div/table/tbody/tr[2]/td/div/div["
                                                     "1]/div/button/span")
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView(true)", Institute_Sub_Submit)
time.sleep(1)
driver.execute_script("arguments[0].click();", Institute_Sub_Submit)
time.sleep(3)  # 子研究与里程碑创建完毕

SkyInstitute_tab = driver .find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div"
                                                  "/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div[2]")
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView(true)", SkyInstitute_tab)
time.sleep(2)
SkyInstitute_tab.click()    # 切换到研究院note的tab上
time.sleep(3)
Create_SkyInstitute_note = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div["
                                                         "2]/div[2]/div[3]/div[2]/div[2]/div/div[3]/div/div["
                                                         "1]/div/div/div/div[1]/button[2]")
Create_SkyInstitute_note.click()
time.sleep(2)
Ok_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
Ok_button.click()   # 创建研究院note完毕
time.sleep(1)
SkyInstitute_info = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div[2]/div[2]"
                                                  "/div[1]/div/div/div/div/div[1]/div[1]")
SkyInstitute_info.click()
time.sleep(6)
driver.close()
