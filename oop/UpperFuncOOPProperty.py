# @property 将参数当做方法用，避免setter和getter方法过多，用法如下。注：这个好


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score is must be a number')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value


stu1 = Student()
stu1.score = 60  # 相当于调用了setter方法
print(stu1.score)


# practice

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


screen = Screen()
screen.width = 1024
screen.height = 768
print('1024*768=%d' % screen.resolution)
