from flask import Blueprint, jsonify
from app.repository.sales_repository import load_sales

sales_blueprint = Blueprint("sales", __name__)

@sales_blueprint.route("/first_five", methods=['GET'])
def get_first_five_sales():
    return jsonify([ 
        { 
            **x.asDict(), 
            'Order Date': str(x['Order Date']),
            'Ship Date': str(x['Ship Date'])
        } 
        for x in load_sales().limit(2).collect()
    ]), 200
