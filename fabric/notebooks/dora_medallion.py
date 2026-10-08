# Fabric notebook code sketch (PySpark); adapt paths to a Fabric Lakehouse.
# Bronze: immutable source landing; Silver: normalized event tables; Gold: service-week metrics.
from pyspark.sql import functions as F
from pyspark.sql.window import Window
bronze_deployments = spark.read.option("header", True).csv("Files/bronze/deployments/*.csv")
bronze_incidents = spark.read.option("header", True).csv("Files/bronze/incidents/*.csv")
silver_d = (bronze_deployments.withColumn("deployed_at",F.to_timestamp("deployed_at"))
 .withColumn("lead_time_hours",F.col("lead_time_hours").cast("double"))
 .withColumn("change_failed",F.col("change_failed").cast("int"))
 .dropDuplicates(["deployment_id"]).filter(F.col("deployment_id").isNotNull()))
silver_i = (bronze_incidents.withColumn("started_at",F.to_timestamp("started_at"))
 .withColumn("resolved_at",F.to_timestamp("resolved_at"))
 .withColumn("caused_by_deployment",F.col("caused_by_deployment").cast("int"))
 .dropDuplicates(["incident_id"]).filter(F.col("incident_id").isNotNull()))
# Gold grain: service x ISO week x production environment.
daily=(silver_d.filter(F.col("environment")=="prod").withColumn("week",F.date_trunc("week","deployed_at"))
 .groupBy("service","week").agg(F.countDistinct("deployment_id").alias("deployments"),F.avg("lead_time_hours").alias("avg_lead_time_hours"),F.sum("change_failed").alias("failed_changes")))
incident_week=(silver_i.filter(F.col("caused_by_deployment")==1).withColumn("week",F.date_trunc("week","started_at"))
 .withColumn("restore_hours",(F.col("resolved_at").cast("long")-F.col("started_at").cast("long"))/3600)
 .groupBy("service","week").agg(F.countDistinct("incident_id").alias("deployment_incidents"),F.avg("restore_hours").alias("mttr_hours")))
gold=(daily.join(incident_week,["service","week"],"left").fillna({"deployment_incidents":0})
 .withColumn("change_failure_rate",F.when(F.col("deployments")>0,F.col("failed_changes")/F.col("deployments"))))
gold.write.mode("overwrite").format("delta").saveAsTable("gold_dora_service_week")
