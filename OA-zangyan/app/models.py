from flask_sqlalchemy import SQLAlchemy


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

    def __init__(self, name_for_recharge, operator, approver, phonenum, cost, methods, accountnum, date ):
        self.name_for_recharge = name_for_recharge
        self.operator = operator
        self.approver = approver
        self.phonenum = phonenum
        self.cost = cost
        self.methods = methods
        self.accountnum = accountnum
        self.date = date

'''
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
'''
class Two(db.Model):
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
    income_of_edu = db.Column(db.Integer)

    def __init__(self, name, phone, wechat, use, total_cost,
                 payable_cost, paid_cost, supply_cost,
                 travelling_expenses, preferential, remarks, source,
                 neibuwaiban, date, income_of_edu):
        self.name = name
        self.phone = phone
        self.wechat = wechat
        self.use = use
        self.total_cost = total_cost
        self.payable_cost = payable_cost
        self.paid_cost = paid_cost
        self.supply_cost = supply_cost
        self.travelling_expenses = travelling_expenses
        self.preferential = preferential
        self.remarks = remarks
        self.source = source
        self.neibuwaiban = neibuwaiban
        self.date = date
        self.income_of_edu = income_of_edu

class Three(db.Model):
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
    cost_of_edu = db.Column(db.Integer)

    def __init__(self, name_for_pay, operator, approver, use, cost, name_collections,
                 petty_cash, methods, remarks, accountnum, date, cost_of_edu):
        self.name_for_pay = name_for_pay
        self.operator = operator
        self.approver = approver
        self.use = use
        self.cost = cost
        self.name_collections = name_collections
        self.petty_cash = petty_cash
        self.methods = methods
        self.remarks = remarks
        self.accountnum = accountnum
        self.date = date
        self.cost_of_edu = cost_of_edu

class Four(db.Model):
    __tablename__ = 'recharge_for_phone_trash'
    id = db.Column(db.Integer, primary_key = True)
    name_for_recharge = db.Column(db.String(20))
    operator = db.Column(db.String(20))     #经办人
    approver = db.Column(db.String(20))     #审批人
    phonenum = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    methods = db.Column(db.String(20))
    accountnum = db.Column(db.Integer)
    date = db.Column(db.String(20))

    def __init__(self, name_for_recharge, operator, approver, phonenum, cost, methods, accountnum, date ):
        self.name_for_recharge = name_for_recharge
        self.operator = operator
        self.approver = approver
        self.phonenum = phonenum
        self.cost = cost
        self.methods = methods
        self.accountnum = accountnum
        self.date = date

class Five(db.Model):
    __tablename__ = 'income_of_school_trash'

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
    income_of_edu = db.Column(db.Integer)

    def __init__(self, name, phone, wechat, use, total_cost,
                 payable_cost, paid_cost, supply_cost,
                 travelling_expenses, preferential, remarks, source,
                 neibuwaiban, date, income_of_edu):
        self.name = name
        self.phone = phone
        self.wechat = wechat
        self.use = use
        self.total_cost = total_cost
        self.payable_cost = payable_cost
        self.paid_cost = paid_cost
        self.supply_cost = supply_cost
        self.travelling_expenses = travelling_expenses
        self.preferential = preferential
        self.remarks = remarks
        self.source = source
        self.neibuwaiban = neibuwaiban
        self.date = date
        self.income_of_edu = income_of_edu

class Six(db.Model):
    __tablename__ = 'cost_of_school_trash'

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
    cost_of_edu = db.Column(db.Integer)

    def __init__(self, name_for_pay, operator, approver, use, cost, name_collections,
                 petty_cash, methods, remarks, accountnum, date, cost_of_edu):
        self.name_for_pay = name_for_pay
        self.operator = operator
        self.approver = approver
        self.use = use
        self.cost = cost
        self.name_collections = name_collections
        self.petty_cash = petty_cash
        self.methods = methods
        self.remarks = remarks
        self.accountnum = accountnum
        self.date = date
        self.cost_of_edu = cost_of_edu

class PurchaseManagement(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    date = db.Column(db.String(20))
    company = db.Column(db.String(50))
    link_person = db.Column(db.String(20))
    phone = db.Column(db.Integer)
    should_pay = db.Column(db.Integer)
    react_pay = db.Column(db.Integer)

    def __init__(self, name, date, company, link_person, phone, should_pay, react_pay):
        self.name = name
        self.date = date
        self.company = company
        self.link_person = link_person
        self.phone = phone
        self.should_pay = should_pay
        self.react_pay = react_pay