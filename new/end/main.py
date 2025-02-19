from flask import Flask
from log import log_and_submit  # 确保正确导入蓝图
from customer import  customer
from hotel_receptionist import  hotel_receptionist

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(log_and_submit, url_prefix='/')
app.register_blueprint(customer, url_prefix='/customer')
app.register_blueprint(hotel_receptionist, url_prefix='/receptionist')

if __name__ == '__main__':
    app.run(debug=True)
