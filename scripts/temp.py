from databricks.connect import DatabricksSession

##spark = DatabricksSession.builder.getOrCreate()
spark = DatabricksSession.builder.remote(cluster_id="0428-095718-7sb3zcfi").getOrCreate()
spark.sql("SELECT 1").show()