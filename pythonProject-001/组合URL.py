def filterchar(string):
    """功能：过滤危险字符，并将规律后的结果输出
    about ：要规律的字符串
    没有的话直接返回值
    :param string:
    :return:
    """
    import re
    pattern = r'(黑客)|(抓包)'
    sub = re.sub(pattern, '@_@', string)
    print(sub)


about = '我是一名黑客'
filterchar(about)

A = 'hello world'
filterchar(A)


def function_tips():
    """

    :return:
    功能：每天输出一条励志文字
    """
    import datetime
    mot = ['坚持下去不是我很坚强，而是我别无选择',
           '播种的人一定可以笑着收获',
           '做对的事情比把事情做更重要',
           '命运给予我们是希望之杯',
           '明日永远是最好',
           '求知若渴',
           '成功的人从来不会说”不可能“'
           ]
    day = (datetime.datetime.now().weekday())
    print(day)
    print(mot[day])


function_tips()


def fun_bim(person, height, weight):
    """
    功能：根据身高和体重计算BIM数据
    person : 姓名
    height： 身高
    weight：体重
    """
    print(person + '的身高:' + str(height) + 'm\t体重:' + str(weight) + 'KG')
    bim = weight / (height * height)
    print(person + '的bim指数为:' + str(bim))
    # 判断体重是否合理
    if bim < 18.5:
        print('您的体重过轻')
    if 18.5 <= bim < 24.9:
        print('您的体重正常')
    if 24.9 <= bim < 29.9:
        print('您的体重过重')
    if bim >= 29.9:
        print('您的体重肥胖')


fun_bim('张三', 1.83, 60)
fun_bim('李四', 1.60, 50)








