'''
http模块包含了一些关于cookie的模块
    - CookieJar
        - 管理存储cookie，向传出的http请求添加cookie
        - cookie存储在内存中，CookieJar实例回收后cookie将消失
    - FileCookieJar(filename, delayload=None, policy=None):
        - 使用文件管理cookie
        - filename是保存cookie的文件
    - MozillaCookieJar(filename, delayload=None, policy=None):
        - 创建mozilla浏览器cookie.txt兼容的FileCookieJar实例
    - LwpCookieJar
        - 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
    - 它们的关系是：CookieJar --> FileCookieJar --> MozillaCookieJar & LwpCookieJar

利用cookieJar登录，大致流程
    - 打开登录页面后自动通过用户名密码登录
    - 自动提取反馈回来的cookie
    - 利用提取的cookie登录隐私页面
'''

from urllib import request, parse
from http import cookiejar

# 创建cookeJar的实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''
    # url从form表单的action属性中提取
    url = "http://www.renren.com/PLogin.do"

    # 从登录form的两个对应的input中提取name属性
    data = {
        "email": "13119144223",
        "password": "123456"
    }

    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/965187997/profile"
    # 如果已经执行了login函数，则opener自动已经包含了相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("rsp.html", "w") as f:
        f.write(html)

if __name__ == '__main__':
    login()

    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)

    getHomePage()









