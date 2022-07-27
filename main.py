from my_package.modeles import *
from flask import request, jsonify
from datetime import date

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
                user = User(first_name="Ron",
                            last_name="Rico",
                            age=34,
                            email="rrico@mail.ru",
                            role="executor",
                            phone="89990004477")
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
                i.age = 35
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
            o = Order(name="ddddddddd",
                      description="ffffffffffffff",
                      start_date=date(2000, 3, 6),
                      end_date=date(2000, 3, 8),
                      address="221b, Baker street",
                      price=3000,
                      customer_id=6,
                      executor_id=11)
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
                i.price = 5000
                db.session.add(i)
                return jsonify({"подорожал": "на 2000"})
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
            o = Offer(order_id=1,
                      executor_id=2)
            db.session.add(o)
            db.session.commit()
            return jsonify({"что-то": "добавили"})

    @app.route("/offers/<int:id>", methods=["GET", "DELETE", "PUT"])
    def get_offers_id(id):
        with db.session.begin():
            i = Offer.query.get(id)
            if request.method == "DELETE":
                db.session.delete(i)
                return jsonify({"удален": id})
            elif request.method == "PUT":
                i.order_id = 5
                db.session.add(i)
                return jsonify({"изменен": id})
        return jsonify({
                "id": i.id,
                "order_id": i.order_id,
                "executor_id": i.executor_id,
            })


create_vies()


if __name__ == "__main__":
    app.run()
