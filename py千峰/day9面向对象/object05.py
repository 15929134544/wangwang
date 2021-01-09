# student   book    computer
"""
student空间包含book和computer
这叫包含关系

知识点：
1、理解has a的关系
    一个类中使用了另外一种自定义的类型

    student类里面使用了computer 和 book
2、类型：
    系统类型：
        int str float
        list dict tuple set
    自定义类型：
        算是自定义的类，都可以将其当成一种类型
        s = Student()
        s是Student类型的对象
"""


class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print('正在使用电脑上网...')

    def __str__(self):
        return self.brand + '------' + self.type + '--------' + self.color


class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + '------' + self.author + '----------' + str(self.number)


class Student:  # has a
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        # 多本书
        self.books = []
        self.books.append(book)

    def borrow_book(self, book):
        for book1 in self.books:
            if book1.bname == book.bname:
                print('已经借过此书！')
                break
            else:
                # 将参数book添加到列表中
                self.books.append(book)
                print('添加成功！')

    def show_book(self):
        for book in self.books: # book就是一个book对象
            print(book.bname)

    def __str__(self):
        return self.name + '------' + str(self.computer) + '---------' + str(self.books)

# 创建对象


computer = Computer('mac', 'mac pro', '深灰色')

book = Book('盗墓笔记', '南派三叔', 10)

student = Student('songsong', computer, book)

print(student)  # TypeError: can only concatenate str (not "Computer") to str
# 所以将computer对象和book对象进行字符串强转
"""
类型：
    系统提供的类型：int str list dict float
    自定义类型：类
    computer类型
    book类型
"""
# 看借了哪些书
student.show_book()

book1 = Book('鬼吹灯', '天下霸唱', 8)
student.borrow_book(book1)
print('------------')

student.show_book()