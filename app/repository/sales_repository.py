from pyspark.sql import DataFrame
from app.sprk.client import spark_client
from pyspark.sql.types import (
    StructType, StructField,
    StringType, DateType,
    IntegerType, FloatType
)

data_schema = StructType(fields=[
    StructField("Region", StringType()),
    StructField("Country", StringType()),
    StructField("Item Type", StringType()),
    StructField("Sales Channel",StringType()),
    StructField("Order Priority", StringType()),
    StructField("Order Date", DateType()),
    StructField("Order ID", IntegerType()),
    StructField("Ship Date", DateType()),
    StructField("Units Sold", IntegerType()),
    StructField("Unit Price", FloatType()),
    StructField("Unit Cost", FloatType()),
    StructField("Total Revenue", FloatType()),
    StructField("Total Cost", FloatType()),
    StructField("Total Profit", FloatType())
])


def load_sales() -> DataFrame:
    return (
        spark_client.read
            .option("dateFormat", "MM/dd/yyyy")
            .option("header", True)
            .schema(data_schema)
            .csv("file:///home/enosh/ruvi_project/app/data/sales.csv")
    )