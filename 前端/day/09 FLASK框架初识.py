from flask import Flask, request

app = Flask(__name__)


# 当前url既可以支持get请求，也可以支持post请求,如果不写默认只能支持get请求
@app.route('/index/', methods=['GET', 'POST'])
def index():
    print(request.form)  # 获取from表单提交过来的非文件数据
    print(request.files)  # 获取文件数据
    file_obj = request.files.get('myfile')
    print(file_obj.name)
    file_obj.save(file_obj.name)
    return 'OK'


app.run()
