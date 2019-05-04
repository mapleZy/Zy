from flask import Blueprint, jsonify, abort, request
from app import models
from app.models import db

#创建蓝本对象
bp_PM = Blueprint('bp_PM', __name__)

#处理数据的函数，将其转换为字典形式，以便处理数据
def convert_list(tasks):
    return dict(id = tasks.id,
                name = tasks.name,
                date = tasks.date,
                company = tasks.company,
                link_person = tasks.link_person,
                phone = tasks.phone,
                should_pay = tasks.should_pay,
                react_pay = tasks.react_pay,
                )

#添加路由

#添加数据
@bp_PM.route('/posts_PM_post/', methods = ['POST'])
def add_PM_posts():
    # if not request.json or "name" not in request.json or "phone" not in request.json or "wechat" not in request.json or "use" not in request.json or "total_cost" not in request.json or "payable_cost" not in request.json or "paid_cost" not in request.json or "supply_cost" not in request.json or "travelling_expenses" not in request.json or "preferential" not in request.json or "methods" not in request.json or "remarks" not in request.json or "source" not in request.json or "neibuwaiban" not in request.json or "date" not in request.json:
    #     abort(400)
    task = models.PurchaseManagement(request.json.get("name"),
                      request.json("date"),
                      request.json("company"),
                      request.json("link_person"),
                      request.json("phone"),
                      request.json("should_pay"),
                      request.json("react_pay"),
                      )
    db.session.add(task)
    db.session.commit()
    return jsonify({"tasks": convert_list(task)}), 201

#查询全部数据
@bp_PM.route('/get_PM_all/')
def get_PM_all():
    tasks = models.PurchaseManagement.query.all()
    if tasks is None:
        abort(404)
    return jsonify({"数据": list(map(convert_list, tasks))})

#查询单个数据
#通过手机号查询
@bp_PM.route('/get_PM_num/<int:task_phone>/')
def get_PM_num(task_phone):
    task = models.PurchaseManagement.query.filter_by(phone = task_phone).first()
    if task is None:
        abort(404)
    return jsonify({"task": convert_list(task)})

#通过姓名查询
@bp_PM.route('/get_PM_name/<task_name>/')
def get_PM_name(task_name):
    task = models.PurchaseManagement.query.filter_by(
        name = task_name).first()
    if task is None:
        abort(404)
    return jsonify({"task": convert_list(task)})

#修改数据(更新)
@bp_PM.route('/update_PM_by_name/<task_name>/', methods = ['PUT'])
def update_PM_by_name(task_name):
    task = models.PurchaseManagement.query.filter_by(
        name = task_name).first()
    # if task is None:
    #     abort(404)
    # if not request.json or "name" not in request.json or "phone" not in request.json or "wechat" not in request.json or "use" not in request.json or "total_cost" not in request.json or "payable_cost" not in request.json or "paid_cost" not in request.json or "supply_cost" not in request.json or "travelling_expenses" not in request.json or "preferential" not in request.json or "methods" not in request.json or "remarks" not in request.json or "source" not in request.json or "neibuwaiban" not in request.json or "date" not in request.json:
    #     abort(400)
    task.name = request.json.get("name")
    task.date = request.json.get("date")
    task.company = request.json.get("company")
    task.link_person = request.json.get("link_person")
    task.phone = request.json.get("phone")
    task.should_pay = request.json.get("should_pay")
    task.react_pay = request.json.get("react_pay")
    db.session.commit()
    return jsonify({"task": convert_list(task)})


#删除数据(逻辑删除)

