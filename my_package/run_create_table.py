from my_package.modeles import *
from my_package.jsoner import load_json
from my_package.datetime_convertor import Conver
import datetime

my_users = load_json("users.json")
my_orders = load_json("orders.json")
my_offers = load_json("offers.json")

db.drop_all()
db.create_all()
for i in my_users:
    with db.session.begin():
        elmt = User(id=i["id"],
                    first_name=i["first_name"],
                    last_name=i["last_name"],
                    age=i["age"],
                    email=i["email"],
                    role=i["role"],
                    phone=i["phone"])
        db.session.add(elmt)

for i in my_offers:
    with db.session.begin():
        elmt = Offer(id=i['id'],
                     order_id=i['order_id'],
                     executor_id=i['executor_id'])
        db.session.add(elmt)

for i in my_orders:
    with db.session.begin():
        start_date = Conver(i["start_date"])
        end_date = Conver(i["end_date"])
        elmt = Order(id=i["id"],
                     name=i["name"],
                     description=i["description"],
                     start_date=datetime.date(start_date.yy, start_date.mm, start_date.dd),
                     end_date=datetime.date(end_date.yy, end_date.mm, end_date.dd),
                     address=i["address"],
                     price=i["price"],
                     customer_id=i["customer_id"],
                     executor_id=i["executor_id"])
        db.session.add(elmt)