from urllib import request, parse

# 模拟get请求百度
# with request.urlopen('https://www.baidu.com') as page:
#     data = page.read()
#
#     print('Status:', page.status, page.reason)
#
#     for k, v in page.getheaders():
#         print('%s: %s' % (k, v))
#
#     print('Data:', data.decode('utf-8'))

# 可以在request中加入自己想要的参数
requests = request.Request('https://www.baidu.com')
requests.add_header('User-Agent', 'Android')

# post请求(模拟微博登陆)
print('Login to weibo.cn...')
username = input('input username:')
pwd = input('input password:')

login_data = parse.urlencode([
    ('username', username),
    ('password', pwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as page:
    data = page.read()

    print('Status:', page.status, page.reason)

    for k, v in page.getheaders():
        print('%s: %s' % (k, v))

    print('Data:', data.decode('utf-8'))
