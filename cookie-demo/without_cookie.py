'''
cookie & session 区别
    - 存放位置不同
    - cookie不安全
    - session会保存在服务器(内存或数据库)上一定时间，会过期
    - 单个cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个
'''

from urllib import request

if __name__ == '__main__':

    url = "http://www.renren.com/965187997/profile"

    rsp = request.urlopen(url)

    html = rsp.read().decode()

    with open("rsp.html", "w") as f:
        f.write(html)