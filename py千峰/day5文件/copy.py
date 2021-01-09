
import os

# 文件复制（文件夹里面都是文件，没有目录）
# 源路径
src_path = r'D:\pythonhello\py千峰\day5文件'
# 目标路径
target_path = r'D:\pythonhello\py千峰\day6文件'


# 封装成函数
def copy(src, target):
    # 判断是否是一个文件夹
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)

        for file in filelist:
            path1 = os.path.join(src, file)
            with open(path1, 'rb') as rstream:
                container = rstream.read()
                path2 = os.path.join(target, file)
                with open(path2, 'wb') as wstream:
                    wstream.write(container)

        else:
            print('复制完毕')


# 调用函数
copy(src_path, target_path)