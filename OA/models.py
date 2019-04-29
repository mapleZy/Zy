from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#建库
db = SQLAlchemy()

#建立第一张表，手机号充值表
class One(db.Model):
    # 设置表名
    __tablename__ = 'recharge_for_phone'

    #设置字段
    id = db.Column(db.Integer, primary_key = True)
    name_for_recharge = db.Column(db.String(20))
    operator = db.Column(db.String(20))     #经办人
    approver = db.Column(db.String(20))     #审批人
    phonenum = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    methods = db.Column(db.String(20))
    accountnum = db.Column(db.Integer)
    date = db.Column(db.String(20))

class Two(db.Model):
    __tablename__ = 'cost_of_edu'

    id = db.Column(db.Integer, primary_key = True)
    name_for_pay = db.Column(db.String(20))    #支出对象
    operator = db.Column(db.String(20))
    approver = db.Column(db.String(20))
    use = db.Column(db.String(50))
    cost = db.Column(db.Float)
    methods = db.Column(db.String(20))
    name_collections = db.Column(db.String(20))     #收款对象
    accountnum = db.Column(db.Integer)
    remarks = db.Column(db.String(50))
    date = db.Column(db.String(20))

class Three(db.Model):
    __tablename__ = 'income_of_edu'

    id = db.Column(db.Integer, primary_key = True)
    name_payment = db.Column(db.String(20))
    name_collections = db.Column(db.String(20))
    use = db.Column(db.String(50))
    payable_cost = db.Column(db.Integer)
    paid_cost = db.Column(db.Integer)
    preferential = db.Column(db.Integer)    #优惠
    methods = db.Column(db.String(20))
    remarks = db.Column(db.String(50))
    date = db.Column(db.String(20))

class Four(db.Model):
    __tablename__ = 'income_of_school'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    phone = db.Column(db.Integer)
    wechat = db.Column(db.Integer)
    use = db.Column(db.String(50))
    total_cost = db.Column(db.Integer)
    payable_cost = db.Column(db.Integer)
    paid_cost = db.Column(db.Integer)
    supply_cost = db.Column(db.Integer)
    travelling_expenses = db.Column(db.Integer)
    preferential = db.Column(db.Integer)
    methods = db.Column(db.String(20))
    remarks = db.Column(db.String(50))
    source = db.Column(db.String(20))
    neibuwaiban = db.Column(db.String(50))
    date = db.Column(db.String(20))

class Five(db.Model):
    __tablename__ = 'cost_of_school'

    id = db.Column(db.Integer, primary_key = True)
    name_for_pay = db.Column(db.String(20))
    operator = db.Column(db.String(20))
    approver = db.Column(db.String(20))
    use = db.Column(db.String(50))
    cost = db.Column(db.Integer)
    name_collections = db.Column(db.String(20))
    petty_cash = db.Column(db.Integer)    #备用金
    methods = db.Column(db.String(20))
    remarks = db.Column(db.String(50))
    accountnum = db.Column(db.Integer)
    date = db.Column(db.String(20))
