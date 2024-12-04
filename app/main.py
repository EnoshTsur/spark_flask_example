from flask import Flask
from app.repository.sales_repository import load_sales
from app.sprk.client import spark_client
from app.routes.sales_route import sales_blueprint


app = Flask(__name__)


if __name__ == "__main__":
    app.register_blueprint(sales_blueprint, url_prefix="/api/sales")
    app.run()