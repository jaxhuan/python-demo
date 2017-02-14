# 元类(python和java最大的不同:java的类在编译时就确定了，不能再改变，
# 而python中，某个变量的类型室通过运行时type()来创建的)

# 使用type()创建类
import logging


def fn(self, name='jax'):
    print('Hello,%s' % name)


# 三个参数，1.类名；2.父类；3.绑定方法
Hello = type('Hello', (object,), dict(hello=fn))  # 创建类Hello

h = Hello()

h.hello()

print(type(h))

print(type(Hello))


# metaclass(元类，用来写orm框架)

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


list = MyList()
list.add('jax')
print(list)


# practice(写一个orm框架)

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '%s:%s' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found Model:%s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mappings:%s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings:
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            logging.exception(e)
            raise AttributeError(r"'Model' object has no attr '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL:%s' % sql)
        print('ARGS:%s' % str(args))


# -------------------好了，用下试试
class User(Model):
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')


user = User(id=1, name='jax', email='jaxhuan.foxmail.com')
user.save()


# 总结：元类的作用：1.拦截类的创建;2.修改类；3.返回修改后的类
# 参考:http://blog.jobbole.com/21351/
# http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
