import math
class Point2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f'({self.x},{self.y})'


class Line2D:
    def __init__(self,a,b,c):
        if a==0 and b == 0:
            raise ValueError('参数a和参数b不能同时为0')
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        return f'{self.a}x+{self.b}y+{self.c}=0'


def distance(point:Point2D,line:Line2D):
    fenzi = abs(line.a*point.x+line.b*point.y+line.c)
    fenmu = math.sqrt(line.a*line.a+line.b*line.b)
    return fenzi/fenmu


def test():
    p1 = Point2D(0,0)
    l1 = Line2D(3,4,-5)

    d1 = distance(p1,l1)
    print(f'点{p1}到直线{l1}的距离是：{d1}')
    assert abs(d1-1.0)<1e-12,'测试失败'
    print('测试通过')

if __name__ == '__main__':
    test()


