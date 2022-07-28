from my_package.datetime_convertor import Conver
from my_package.modeles import *
from flask import request, jsonify
from datetime import date
import json


def create_vies():
    @app.route("/users", methods=["GET", "POST"])
    def get_users():
        if request.method == "GET":
            users = User.query.all()
            users_list = []
            for i in users:
                users_list.append({
                    "id": i.id,
                    "first_name": i.first_name,
                    "last_name": i.last_name,
                    "age": i.age,
                    "email": i.email,
                    "role": i.role,
                    "phone": i.phone
                })
        elif request.method == "POST":
            with db.session.begin():
                user2 = json.loads(request.data)
                user = User(first_name=user2["first_name"],
                            last_name=user2["last_name"],
                            age=user2["age"],
                            email=user2["email"],
                            role=user2["role"],
                            phone=user2["phone"],)
                db.session.add(user)
                return jsonify({"user": "added"})
        return jsonify(users_list)

    @app.route("/users/<int:id>", methods=["GET", "DELETE", "PUT"])
    def make_users(id):
        with db.session.begin():
            i = User.query.get(id)
            if request.method == "DELETE":
                db.session.delete(i)
                return jsonify({"user is deleted": id})
            elif request.method == "PUT":
                user2 = json.loads(request.data)
                i.first_name = user2["first_name"]
                i.last_name = user2["last_name"]
                i.age = user2["age"]
                i.email = user2["email"]
                i.role = user2["role"]
                i.phone = user2["phone"]
                db.session.add(i)
        return jsonify({
            "id": i.id,
            "first_name": i.first_name,
            "last_name": i.last_name,
            "age": i.age,
            "email": i.email,
            "role": i.role,
            "phone": i.phone})

    @app.route("/orders", methods=["GET", "POST"])
    def get_orders():
        order = Order.query.all()
        ord = []
        if request.method == "GET":
            for i in order:
                ord.append({
                    "id": i.id,
                    "name": i.name,
                    "description": i.description,
                    "start_date": i.start_date,
                    "end_date": i.end_date,
                    "address": i.address,
                    "price": i.price,
                    "customer_id": i.customer_id,
                    "executor_id": i.executor_id
                })
            return jsonify(ord)
        elif request.method == "POST":
            user2 = json.loads(request.data)
            start_date = Conver(user2["start_date"])
            end_date = Conver(user2["end_date"])
            o = Order(name=user2["name"],
                      description=user2["description"],
                      start_date=date(start_date.yy, start_date.mm, start_date.dd),
                      end_date=date(end_date.yy, end_date.mm, end_date.dd),
                      address=user2["address"],
                      price=user2["price"],
                      customer_id=user2["customer_id"],
                      executor_id=user2["executor_id"])
            db.session.add(o)
            db.session.commit()
            return jsonify({"дело": "добавлено"})

    @app.route("/orders/<int:id>", methods=["GET", "DELETE", "PUT"])
    def make_orders(id):
        with db.session.begin():
            i = Order.query.get(id)
            if request.method == "DELETE":
                db.session.delete(i)
                return jsonify({"удалён": id})
            elif request.method == "PUT":
                user2 = json.loads(request.data)
                start_date = Conver(user2["start_date"])
                end_date = Conver(user2["end_date"])
                i.name = user2["name"]
                i.description = user2["description"]
                i.start_date = date(start_date.yy, start_date.mm, start_date.dd)
                i.end_date = date(end_date.yy, end_date.mm, end_date.dd)
                i.address = user2["address"]
                i.price = user2["price"]
                i.customer_id = user2["customer_id"]
                i.executor_id = user2["executor_id"]
                db.session.add(i)
        return jsonify({
                "id": i.id,
                "name": i.name,
                "description": i.description,
                "start_date": i.start_date,
                "end_date": i.end_date,
                "address": i.address,
                "price": i.price,
                "customer_id": i.customer_id,
                "executor_id": i.executor_id
            })

    @app.route("/offers", methods=["GET", "POST"])
    def get_offers():
        offer = Offer.query.all()
        offr = []
        if request.method == "GET":
            for i in offer:
                offr.append({
                    "id": i.id,
                    "order_id": i.order_id,
                    "executor_id": i.executor_id,
                })
            return jsonify(offr)
        elif request.method == "POST":
            user2 = json.loads(request.data)
            i = Offer(order_id=user2["order_id"],
                      executor_id=user2["executor_id"])
            db.session.add(i)
            db.session.commit()
            return jsonify({
                    "id": i.id,
                    "order_id": i.order_id,
                    "executor_id": i.executor_id,
                })

    @app.route("/offers/<int:id>", methods=["GET", "DELETE", "PUT"])
    def get_offers_id(id):
        with db.session.begin():
            i = Offer.query.get(id)
            if request.method == "DELETE":
                db.session.delete(i)
                return jsonify({"удален": id})
            elif request.method == "PUT":
                user2 = json.loads(request.data)
                i.order_id = user2["order_id"]
                i.executor_id = user2["executor_id"]
                db.session.add(i)
        return jsonify({
                "id": i.id,
                "order_id": i.order_id,
                "executor_id": i.executor_id})


create_vies()


if __name__ == "__main__":
    app.run()
