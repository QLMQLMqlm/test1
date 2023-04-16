password = 1234456
key = 7
print("原密码是：", password, "。")
password = password << key
print("加密之后的密码：", password, "。")
password = password >> key
print("解密之后的密码是：", password, "。")
