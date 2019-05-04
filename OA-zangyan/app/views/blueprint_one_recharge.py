from flask import Blueprint, jsonify, abort, request, json
from app import models
from app.models import db

#创建蓝本对象
bp = Blueprint('bp', __name__)

# posts = [
#     {
#         "id": 6,
#         "name_for_recharge": "赵八",
#         "operator": "李一",
#         "approver": "李二",
#         "phonenum": 19932451234 ,
#         "cost": 100,
#         "methods": "微信",
#         "accountnum": 6228480031585959777,
#         "date": "1"
#     }
# ]

#处理数据的函数，将其转换为字典形式，以便处理数据
def convert_list(tasks):
    return dict(id = tasks.id,
                name_for_recharge = tasks.name_for_recharge,
                operator = tasks.operator,
                approver = tasks.approver,
                phonenum = tasks.phonenum,
                cost = tasks.cost,
                methods = tasks.methods,
                accountnum = tasks.accountnum,
                date = tasks.date)

#添加路由

#添加数据
@bp.route('/posts_one_post/', methods = ['POST'])
def add_one_posts():
    # if not request.json or "name_for_recharge" not in request.json or "operator" not in request.json or "approver" not in request.json or "phonenum" not in request.json or "cost" not in request.json or "methods" not in request.json or "accountnum" not in request.json or "date" not in request.json:
    #     abort(400)
    if not request.json or not "name_for_recharge" in request.json:
        abort(400)
    task = models.One(request.json.get("name_for_recharge", " "),
                      request.json.get("operator", " "),
                      request.json.get("approver", " "),
                      request.json.get("phonenum", " "),
                      request.json.get("cost", " "),
                      request.json.get("methods"," "),
                      request.json.get("accountnum", ""),
                      request.json.get("date", " "))

    db.session.add(task)
    db.session.commit()
    return jsonify({"tasks": convert_list(task)}), 201

#查询全部数据
@bp.route('/get_one_all/')
def get_one_all():
    tasks = models.One.query.all()
    if tasks is None:
        abort(404)
    return jsonify({"数据": list(map(convert_list, tasks))})

#查询单个数据
#通过手机号查询
@bp.route('/get_one_num/<int:task_phonenum>/')
def get_one_num(task_phonenum):
    task = models.One.query.filter_by(phonenum = task_phonenum).first()
    if task is None:
        abort(404)
    return jsonify({"task": convert_list(task)})

#通过姓名查询
@bp.route('/get_one_name/<task_name_for_recharge>/')
def get_one_name(task_name_for_recharge):
    task = models.One.query.filter_by(
        name_for_recharge = task_name_for_recharge).first()
    if task is None:
        abort(404)
    return jsonify({"task": convert_list(task)})

#修改数据(更新)
@bp.route('/update_one_by_name/<string:task_name_for_recharge>/', methods = ['PUT'])
def update_one_by_name(task_name_for_recharge):
    task = models.One.query.filter_by(
        name_for_recharge = task_name_for_recharge).first()
    if task is None:
        abort(404)
    if not request.json or "name_for_recharge" not in request.json or "operator" not in request.json or "approver" not in request.json or "phonenum" not in request.json or "cost" not in request.json or "methods" not in request.json or "accountnum" not in request.json or "date" not in request.json:
        abort(400)
    task.name_for_recharge = request.json.get("name_for_recharge")
    task.operator = request.json.get("operator")
    task.approver = request.json.get("approver")
    task.phonenum = request.json.get("phonenum")
    task.cost = request.json.get("cost")
    task.methods= request.json.get("methods")
    task.accountnum = request.json.get("accountnum")
    task.date = request.json.get("date")
    db.session.commit()
    return jsonify({"task": convert_list(task)})


#删除数据(逻辑删除)

