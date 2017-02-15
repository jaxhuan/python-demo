# 摘要算法.通过一个函数，把任意长度的数据转换为一个长度固定的字符串(通常以16进制表示),
# 目的是为了发现原始数据是否被人改动过md5 sha1


import hashlib

md5 = hashlib.md5()
md5.update('what\'s your name?'.encode('utf-8'))
print('md5=>', md5.hexdigest())

md5_flit = hashlib.md5()
md5_flit.update('what\'s your '.encode('utf-8'))
md5_flit.update('name?'.encode('utf-8'))
print('md5_flit=>', md5_flit.hexdigest())


# 应用:sql中存储密码,防止数据库被人盗用或管理员查看

def generate_md5(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()


db_user = {
    'jax': generate_md5('jax'),
    'yinsi': generate_md5('yinsi')
}


def login(user, pwd):
    try:
        if db_user[user] == generate_md5(pwd):
            print('sucessful')
        else:
            print('failed')
    except:
        print('no user name')


login('jax', '123456')
login('yinsi', 'yinsi')
login('wangsan', '123')

# 摘要算法并不是加密算法，因为摘要算法不能通过结果推算出原文，只能明文=》密文，所以只能用于防篡改，可以在不存储明文口令的情况下验证口令
