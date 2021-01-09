import os

# 文件复制
# 源路径
src_path = r'D:\pythonhello\py千峰\day5文件'
# 目标路径
target_path = r'D:\pythonhello\py千峰\day06'


# 文件夹里面还有目录
def copy(src_path, target_path):
    # 获取文件夹里面的内容
    filelist = os.listdir(src_path)
    print(filelist)
    # 遍历列表
    for file in filelist:
        # 将列表名和源路径拼接成完整的绝对路径
        path = os.path.join(src_path, file)
        # 判断是文件夹还是文件
        if os.path.isdir(path):
            # 递归调用copy（如果是文件夹）
            # 新建文件夹
            target_path1 = os.path.join(target_path, file)
            os.mkdir(target_path1)
            copy(path, target_path1)
        else:
            # 不是文件夹，则直接进行复制
            with open(path, 'rb') as rstream:
                container = rstream.read()
                path2 = os.path.join(target_path, file)
                with open(path2, 'wb') as wstream:
                    wstream.write(container)
    else:
        print('复制完成')


# 调用函数
copy(src_path, target_path)