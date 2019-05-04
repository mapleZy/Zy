from flask import Blueprint, jsonify, abort, request
from app import models
from app.models import db

#创建蓝本对象
bp_three = Blueprint('bp_three', __name__)

#处理数据的函数，将其转换为字典形式，以便处理数据
def convert_list(tasks):
    return dict(id = tasks.id,
                name_for_pay = tasks.name_for_pay,
                operator = tasks.operator,
                approver = tasks.approver,
                use = tasks.use,
                cost = tasks.cost,
                name_collections = tasks.name_collections,
                petty_cash = tasks.petty_cash,
                methods = tasks.methods,
                remarks = tasks.remarks,
                accountnum = tasks.accountnum,
                date=tasks.date,
                cost_of_edu = tasks.cost_of_edu,
                )

#添加路由

#添加数据
@bp_three.route('/posts_three_post/', methods = ['POST'])
def add_three_posts():
    if not request.json or "name_for_pay" not in request.json or "operator" not in request.json or "approver" not in request.json or "use" not in request.json or "cost" not in request.json or "name_collections" not in request.json or "petty_cash" not in request.json or "methods" not in request.json or "remarks" not in request.json or "accountnum" not in request.json or "date" not in request.json or "cost_of_edu" not in request.json:
        abort(400)
    task = models.Three(request.json["name_for_pay"], request.json["operator"], request.json["approver"], request.json["use"], request.json["cost"], request.json["name_collections"], request.json["petty_cash"], request.json["methods"], request.json["remarks"], request.json["accountnum"], request.json["date"], request.json["cost_of_edu"])
    db.session.add(task)
    db.session.commit()
    return jsonify({"tasks": convert_list(task)}), 201

#查询全部数据
@bp_three.route('/get_three_all/')
def get_three_all():
    tasks = models.Three.query.all()
    if tasks is None:
        abort(404)
    return jsonify({"数据": list(map(convert_list, tasks))})

#查询单个数据
#通过手机号查询
# @bp.route('/get_three_num/<int:task_phone>/')
# def get_three_num(task_phone):
#     task = models.Three.query.filter_by(phone = task_phone).first()
#     if task is None:
#         abort(404)
#     return jsonify({"task": convert_list(task)})

#通过姓名查询
@bp_three.route('/get_three_name/<task_name_for_pay>/')
def get_three_name(task_name_for_pay):
    task = models.Three.query.filter_by(
        name_for_pay = task_name_for_pay).first()
    if task is None:
        abort(404)
    return jsonify({"task": convert_list(task)})

#修改数据(更新)
@bp_three.route('/update_three_by_name/<task_name_for_pay>/', methods = ['PUT'])
def update_two_by_name(task_name_for_pay):
    task = models.Three.query.filter_by(
        name_for_pay = task_name_for_pay).first()
    if task is None:
        abort(404)
    if not request.json or "name_for_pay" not in request.json or "operator" not in request.json or "approver" not in request.json or "use" not in request.json or "cost" not in request.json or "name_collections" not in request.json or "petty_cash" not in request.json or "methods" not in request.json or "remarks" not in request.json or "accountnum" not in request.json or "date" not in request.json or "cost_of_edu" not in request.json:
        abort(400)
    task["name_for_pay"] = request.json.get("name_for_pay", task["name_for_pay"])
    task["operator"] = request.json.get("operator", task["operator"])
    task["approver"] = request.json.get("approver", task["approver"])
    task["use"] = request.json.get("use", task["use"])
    task["cost"] = request.json.get("cost", task["cost"])
    task["name_collections"] = request.json.get("name_collections", task["name_collections"])
    task["petty_cash"] = request.json.get("petty_cash", task["petty_cash"])
    task["methods"] = request.json.get("methods", task["methods"])
    task["remarks"] = request.json.get("remarks", task["remarks"])
    task["accountnum"] = request.json.get("accountnum", task["accountnum"])
    task["date"] = request.json.get("date", task["date"])
    task["cost_of_edu"] = request.json.get("cost_of_edu", task["cost_of_edu"])
    db.session.commit()
    return jsonify({"task": convert_list(task)})


#删除数据(逻辑删除)

