from flask import Blueprint, jsonify, abort, request
from app import models
from app.models import db

#创建蓝本对象
bp_two = Blueprint('bp_two', __name__)

#处理数据的函数，将其转换为字典形式，以便处理数据
def convert_list(tasks):
    return dict(id = tasks.id,
                name = tasks.name,
                phone = tasks.phone,
                wechat = tasks.wechat,
                use = tasks.use,
                total_cost = tasks.total_cost,
                payable_cost = tasks.payable_cost,
                paid_cost = tasks.paid_cost,
                supply_cost = tasks.supply_cost,
                travelling_expenses = tasks.travelling_expenses,
                preferential = tasks.preferential,
                methods=tasks.methods,
                remarks = tasks.remarks,
                source = tasks.source,
                neibuwaiban = tasks.neibuwaiban,
                date=tasks.date,
                income_of_edu = tasks.income_of_edu
                )

#添加路由

#添加数据
@bp_two.route('/posts_two_post/', methods = ['POST'])
def add_two_posts():
    # if not request.json or "name" not in request.json or "phone" not in request.json or "wechat" not in request.json or "use" not in request.json or "total_cost" not in request.json or "payable_cost" not in request.json or "paid_cost" not in request.json or "supply_cost" not in request.json or "travelling_expenses" not in request.json or "preferential" not in request.json or "methods" not in request.json or "remarks" not in request.json or "source" not in request.json or "neibuwaiban" not in request.json or "date" not in request.json:
    #     abort(400)
    task = models.Two(request.json.get("name"),
                      request.json("phone"),
                      request.json("wechat"),
                      request.json("use"),
                      request.json("total_cost"),
                      request.json("payable_cost"),
                      request.json("paid_cost"),
                      request.json("supply_cost"),
                      request.json("travelling_expenses"),
                      request.json("preferential"),
                      request.json("methods"),
                      request.json("remarks"),
                      request.json("source"),
                      request.json("neibuwaiban"),
                      request.json("date"),
                      request.json("income_of_edu"),
                      )
    db.session.add(task)
    db.session.commit()
    return jsonify({"tasks": convert_list(task)}), 201

#查询全部数据
@bp_two.route('/get_two_all/')
def get_two_all():
    tasks = models.Two.query.all()
    if tasks is None:
        abort(404)
    return jsonify({"数据": list(map(convert_list, tasks))})

#查询单个数据
#通过手机号查询
@bp_two.route('/get_two_num/<int:task_phone>/')
def get_two_num(task_phone):
    task = models.Two.query.filter_by(phone = task_phone).first()
    if task is None:
        abort(404)
    return jsonify({"task": convert_list(task)})

#通过姓名查询
@bp_two.route('/get_two_name/<task_name>/')
def get_two_name(task_name):
    task = models.Two.query.filter_by(
        name = task_name).first()
    if task is None:
        abort(404)
    return jsonify({"task": convert_list(task)})

#修改数据(更新)
@bp_two.route('/update_two_by_name/<task_name>/', methods = ['PUT'])
def update_two_by_name(task_name):
    task = models.Two.query.filter_by(
        name = task_name).first()
    if task is None:
        abort(404)
    if not request.json or "name" not in request.json or "phone" not in request.json or "wechat" not in request.json or "use" not in request.json or "total_cost" not in request.json or "payable_cost" not in request.json or "paid_cost" not in request.json or "supply_cost" not in request.json or "travelling_expenses" not in request.json or "preferential" not in request.json or "methods" not in request.json or "remarks" not in request.json or "source" not in request.json or "neibuwaiban" not in request.json or "date" not in request.json:
        abort(400)
    task.name = request.json.get("name")
    task.phone = request.json.get("phone")
    task.wechat = request.json.get("wechat")
    task.use = request.json.get("use")
    task.total_cost = request.json.get("total_cost")
    task.payable_cost = request.json.get("payable_cost")
    task.paid_cost = request.json.get("paid_cost")
    task.supply_cost = request.json.get("supply_cost")
    task.travelling_expenses = request.json.get("travelling_expenses")
    task.preferential = request.json.get("preferential")
    task.methods = request.json.get("methods")
    task.remarks = request.json.get("remarks")
    task.source = request.json.get("source")
    task.neibuwaiban = request.json.get("neibuwaiban")
    task.date = request.json.get("date")
    task.income_of_edu = request.json.get("income_of_edu")
    db.session.commit()
    return jsonify({"task": convert_list(task)})


#删除数据(逻辑删除)

