# __str__
"""
触发时机：打印对象名的时候，自动触发调用__str__里面的内容

注意：一定要在__str__中添加return，return后面的内容就是打印对象看到的内容部分

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名：'+ self.name + ',年龄：' + str(self.age)


p = Person('tom', 18)
print(p)  # <__main__.Person object at 0x018901D0>

# 单纯打印对象名称，出来的是一个地址。地址对于开发者来说没有太大的意义
# 如果想在打印对象名的时候，想给开发者更多的信息量

p1 = Person('jack', 20)
print(p1)

"""
总结：魔术方法

重点：
__init__ (构造方法：创建完空间之后调用的第一个方法)  __str__

了解：
__new__ 作用：开辟空间 

__del__：作用：没有指针引用的时候被触发,一般不需要重写

__call__:作用： 想不想将对象当成函数用。 想：重写


大总结：
方法：
    普通方法------>重点：
        定义：
            def 方法名(self, [参数...])：
                方法体
        
        调用：
        对象.方法（）
        
        方法之间的调用：
        class A:
            def a(self):
                pass
            
            def b(self):
                # 调用a方法
                self.a()
                
    类方法:
    定义：
        @classmethod
            def 方法名(cls, [参数...]):
                pass
            
    调用：对于类方法，对象和类都是可以调用的    
    类名.方法名()
    对象.方法名()
        
    静态方法:
    定义：
        @staticmethod
             def 方法名([参数...]):
                pass
            
    调用：
     类名.方法名()
     对象.方法名()
   
    魔术方法：
        自动执行的一些方法
        
        print(p)-----> __str__
         
         
"""