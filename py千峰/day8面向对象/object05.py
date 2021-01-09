class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print('{}正在吃{}！...'.format(self.name, food))

    def run(self):
        print('{}，今年{}岁，正在跑步'.format(self.name, self.age))


p = Person('lisi', 18)
p.eat('红烧肉')
p.run()


p1 = Person('王五', 20)
p1.eat('狮子头')
p1.run()
