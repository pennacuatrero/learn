import math
class xComplex:
    def __init__(self,x,y,is_exp:bool) -> None:
        if is_exp:
            r,theta = x,y
            self.r=r*math.cos(theta)
            self.i=r*math.sin(theta)
        else:
            self.r=x
            self.i=y


    #计算模
    def getMod(self):
        return math.sqrt(self.r*self.r+self.i*self.i)

    #计算辐角主值
    def getArg(self):
        return math.atan2(self.i, self.r)

    #相加
    def add(self,other):
        new_r=self.r+other.r
        new_i=self.i+other.i
        return xComplex(new_r,new_i,False)

    #相减
    def minus(self,other):
        new_r=self.r-other.r
        new_i=self.i-other.i
        return xComplex(new_r,new_i,False)

    #相乘
    def multi(self,other):
        new_r=self.r*other.r - self.i*other.i
        new_i=self.r*other.i + self.i*other.r
        return xComplex(new_r,new_i,False)

    #相除
    def div(self,other):
        if other.r*other.r+other.i*other.i == 0:
            raise ValueError
        new_r=(self.r*other.r+self.i*other.i)/(other.r*other.r+other.i*other.i)
        new_i=(self.i*other.r-self.r*other.i)/(other.r*other.r+other.i*other.i)
        return xComplex(new_r,new_i,False)

    #n次幂
    def Mi(self,n):
        r=self.getMod()
        theta=self.getArg()
        new_r=r**n
        new_theta=theta*n
        return xComplex(new_r,new_theta,True)


    def __str__(self) -> str:
        if self.i>=0:
            return f'{self.r:.2f}+{self.i:.2f}i'
        else:
            return f'{self.r:.2f}-{abs(self.i):.2f}i'




def test_all():
    z1 = xComplex(3,4,False)
    z2 = xComplex(5,math.pi/2,True)

    eps = 1e-12

    assert abs(z1.getMod() - 5.0) < eps
    assert abs(z1.getArg() - math.atan2(4, 3)) < eps

    z_add = z1.add(z2)
    assert abs(z_add.r - 3.0) < eps and abs(z_add.i - 9.0) < eps

    z_minus = z1.minus(z2)
    assert abs(z_minus.r - 3.0) < eps and abs(z_minus.i - (-1.0)) < eps

    z_mul = z1.multi(z2)
    assert abs(z_mul.r - (-20.0)) < eps and abs(z_mul.i - 15.0) < eps

    z_div = z1.div(z2)
    assert abs(z_div.r - 0.8) < eps and abs(z_div.i - (-0.6)) < eps

    z3 = xComplex(1, 1, False)
    z_pow = z3.Mi(3)
    assert abs(z_pow.r - (-2.0)) < eps and abs(z_pow.i - 2.0) < eps

    print('所有测试通过')

if __name__ == '__main__':
    test_all()
