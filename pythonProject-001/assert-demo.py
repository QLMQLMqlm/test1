import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
# import unittest

#   driver = webdriver.Edge(executable_path="E:\\study\\webdriver\\msedgedriver.exe")
# s = Service(executable_path="E:\\study\\webdriver\\msedgedriver.exe")
driver = webdriver.Edge(service=Service(executable_path="E:\\study\\webdriver\\msedgedriver.exe"))  # 找到msedgedriver
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
time.sleep(3)
deal_name = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]/div"
                                          "/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/div/div/input") \
    .send_keys("填写A级别-015")
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
    .send_keys("填写A级别-015")
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
                                                   "2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]")
Create_Conference1.click()  # 点击新建会议
time.sleep(1)
Create_Conference2 = driver.find_element(By.XPATH, "/html/body/div/div/section/section/main/div/div/div/div/div/div[2]"
                                                   "/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div"
                                                   "/div/div/div/div[1]/div")
Create_Conference2.click()  # 点击新建会议下一步  ”项目全图/会议纪要“
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
time.sleep(6)
create_success_info = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[1]/span")
print("创建成功提示文案：{}".format(create_success_info.text))

"""
class TestWow(unittest.TestCase):
    def test01(self):
        self.assertEqual(create_success_info.text, "创建成功")


if __name__ == "__main__":
    unittest.main()

"""
Ok_Button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
Ok_Button.click()  # 创建会议完毕点击OK弹框
time.sleep(6)
Memo_Garde = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div[2]"
                                           "/div[3]/div[1]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]"
                                           "/div[2]/div")
Memo_Garde.click()
time.sleep(1)
Memo_Garde.send_keys(Keys.DOWN)
Memo_Garde.send_keys(Keys.ENTER)  # 默认主导人一人参会，并且评级为A
time.sleep(1)
Garde_Ok_Button = wait.until(
    ec.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]")))
Garde_Ok_Button.click()

time.sleep(6)
Memo_Edit_Button = wait.until(
    ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/section/main/div/div/div/div/div/div["
                                              "2]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div["
                                              "1]/button")))
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
