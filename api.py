import random
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

promotions = [
  {
    "amount": random.randint(1,6),
    "daysToExpire": random.randint(1,6),
    "id": random.randint(1,6),
    "name": "rohlik",
    "price": random.randint(-1,100)
  }
]

orders = [
  {
    "address": "Brno, Hybesova",
    "canceled": random.choice([True,False]),
    "first_name": "Radim",
    "last_name": "Lipovcan",
    "goods_available": random.choice([True,False]),
    "is_payed": random.choice([True,False]),
    "id":  1,
    "order_price": random.randint(10,600),
    "phone_number": random.randint(1000000,6000000)
  }
]

suppliers = [
  {
    "supplier_name": "Rohlik.cz",
    "id": 1,
    "supplier_actual_amount": random.randint(10,120),
    "supplier_stats": random.randint(0,2)
  }
]

class Promotion(Resource):
    def get(self, name):
        for promotion in promotions:
            if(name == promotion["name"]):
                promotion["daysToExpire"] = random.randint(1,6)
                promotion["price"] = random.randint(-1,100)
                return promotion, 200
        return "Item not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("amount")
        parser.add_argument("daysToExpire")
        parser.add_argument("id")
        args = parser.parse_args()

        for promotion in promotions:
            if(name == promotion["name"]):
                return "Entry with name {} already exists".format(name), 400

        promotion = {
            "name": name,
            "amount": args["amount"],
            "amouidnt": args["id"],
            "daysToExpire": args["daysToExpire"],
        }
        promotions.append(promotion)
        return promotion, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("amount")
        parser.add_argument("daysToExpire")
        parser.add_argument("id")
        args = parser.parse_args()

        for promotion in promotions:
            if(name == promotion["name"]):
                promotion["amount"] = args["amount"]
                promotion["daysToExpire"] = args["daysToExpire"]
                promotion["id"] = args["id"]
                return user, 200

        promotion = {
            "name": name,
            "amount": args["amount"],
            "amouidnt": args["id"],
            "daysToExpire": args["daysToExpire"],
        }
        promotion.append(user)
        return promotion, 201

    def delete(self, name):
        global promotions
        promotions = [promotion for promotion in promotions if promotion["name"] != name]
        return "{} is deleted.".format(name), 200

class Order(Resource):
    def get(self, name):
        for order in orders:
            if(name == order["id"]):
                order["goods_available"] = random.choice([True,False])
                order["is_payed"] = random.choice([True,False])
                order["canceled"] = random.choice([True, False])
                order["order_price"] = random.randint(10,1500)
                return order, 200
        return "Item not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("address")
        parser.add_argument("canceled")
        parser.add_argument("first_name")
        parser.add_argument("last_name")
        parser.add_argument("goods_available")
        parser.add_argument("id")
        parser.add_argument("order_price")
        parser.add_argument("phone_number")
        args = parser.parse_args()

        for order in orders:
            if(name == order["id"]):
                return "Entry with name {} already exists".format(name), 400

        order = {
            "address": args["address"],
            "canceled": args["canceled"],
            "first_name": args["first_name"],
            "last_name": args["last_name"],
            "goods_available": args["goods_available"],
            "canceled": name,
            "canceled": args["order_price"],
            "amouidnt": args["phone_number"],
        }
        orders.append(order)
        return order, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("address")
        parser.add_argument("canceled")
        parser.add_argument("first_name")
        parser.add_argument("last_name")
        parser.add_argument("goods_available")
        parser.add_argument("id")
        parser.add_argument("order_price")
        parser.add_argument("phone_number")
        args = parser.parse_args()

        for order in orders:
            if(name == order["id"]):
                order["first_name"] = args["first_name"]
                order["last_name"] = args["last_name"]
                order["goods_available"] = args["goods_available"]
                return user, 200

        order = {
            "address": args["address"],
            "canceled": args["canceled"],
            "first_name": args["first_name"],
            "last_name": args["last_name"],
            "goods_available": args["goods_available"],
            "canceled": name,
            "canceled": args["order_price"],
            "amouidnt": args["phone_number"],
        }
        order.append(user)
        return order, 201

    def delete(self, name):
        global orders
        orders = [order for order in orders if order["id"] != name]
        return "{} is deleted.".format(name), 200

class Supplier(Resource):
    def get(self, name):
        for supplier in suppliers:
            if(name == supplier["id"]):
                supplier["supplier_stats"] = random.randint(0,2)
                return supplier, 200
        return "Item not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("supplier_name")
        parser.add_argument("supplier_actual_amount")
        parser.add_argument("supplier_stats")
        parser.add_argument("id")
        args = parser.parse_args()

        for supplier in suppliers:
            if(name == supplier["id"]):
                return "Entry with name {} already exists".format(name), 400

        supplier = {
            "id": name,
            "supplier_stats": args["supplier_stats"],
            "id": args["id"],
            "supplier_name": args["supplier_name"],
            "supplier_actual_amount": args["supplier_actual_amount"],
        }
        suppliers.append(supplier)
        return supplier, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("amount")
        parser.add_argument("daysToExpire")
        parser.add_argument("id")
        args = parser.parse_args()

        for supplier in suppliers:
            if(name == supplier["id"]):
                supplier["amount"] = args["amount"]
                supplier["daysToExpire"] = args["daysToExpire"]
                supplier["id"] = args["id"]
                return user, 200

        supplier = {
            "name": name,
            "amount": args["amount"],
            "amouidnt": args["id"],
            "daysToExpire": args["daysToExpire"],
        }
        supplier.append(user)
        return supplier, 201

    def delete(self, name):
        global suppliers
        suppliers = [supplier for supplier in suppliers if supplier["id"] != name]
        return "{} is deleted.".format(name), 200


api.add_resource(Promotion, "/promotions/<string:name>")
api.add_resource(Order, "/orders/<int:name>")
api.add_resource(Supplier, "/suppliers/<int:name>")
app.run(host='0.0.0.0',port=5000)
app.run(debug=True)
