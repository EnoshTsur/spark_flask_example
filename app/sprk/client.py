from pyspark.sql import SparkSession

HDFS_URL = 'hdfs://192.168.1.2:8020'

spark_client: SparkSession = (
    SparkSession.builder
        .appName("SalesApp")
        .master('local[3]')
        .config("spark.hadoop.fs.defaultFS", HDFS_URL) 
        .config("spark.sql.legacy.timeParserPolicy","LEGACY")
        .config("spark.hadoop.fs.hdfs.impl", "org.apache.hadoop.hdfs.DistributedFileSystem") 
        .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem")
        .getOrCreate()
)

