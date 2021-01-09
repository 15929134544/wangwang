"""
编写简单的工资管理程序，系统可以管理以下四类人：工人（worker）， 销售员（salesman），
经理（manager），销售经理（salemanager）
所有的员工都有员工号，姓名，工资等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法。
    1）：工人：工人具有工作小时数和时薪的属性，工资计算法方法为工作小时数*时薪
    2）：销售员：具有销售额和提成比例的属性，工资计算方法为销售额*提成比例。
    3）：经理：具有固定月薪属性，工资计算方法为固定月薪
    4）：销售经理：工资计算方法为销售额  *提成比例+固定月薪

请根据以上要求设计合理的类，完成以下功能：
    1）：添加所有类型的人员
    2）：计算月薪
    3）：显示所有人员工资情况

"""


class Person:
    def __init__(self, no, name, salary):
        self.name = name
        self.no = no
        self.salary = salary

    def __str__(self):
        msg = '工号：{}，姓名：{}，本月工资：{}'.format(self.no, self.name, self.salary)
        return msg

    def getSalary(self):
        return self.salary


class Worker(Person):
    def __init__(self, no, name, salary, hours, per_hour):
        super(Worker, self).__init__(no, name, salary)
        self.hours = hours
        self.per_hour = per_hour

    def getSalary(self):

        money = self.hours * self.per_hour
        self.salary += money
        return self.salary


class Salesman(Person):
    def __init__(self, no, name, salary, salemoney, percent):
        super().__init__(no, name, salary)
        self.salemoney = salemoney
        self.percent = percent

    def getSalary(self):
        money = self.salemoney * self.percent
        self.salary += money
        return self.salary


# 创建子类对象
w = Worker('001', 'king', 2000, 160, 100)
s = w.getSalary()
print('月薪：', s)
print(w)

print('-----------------------------------')
saler = Salesman('002', 'lucy', 5000, 5000000, 0.003)
s = saler.getSalary()
print('月薪：', s)
print(saler)