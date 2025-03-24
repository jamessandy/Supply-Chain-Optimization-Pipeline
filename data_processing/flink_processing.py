from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
tenv = StreamTableEnvironment.create(env)

tenv.execute_sql("""
    CREATE TABLE kafka_source (
        shipment_id INT,
        location STRING,
        status STRING,
        timestamp DOUBLE
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'supply_chain',
        'properties.bootstrap.servers' = 'localhost:9092',
        'format' = 'json'
    )
""")

tenv.execute_sql("""
    CREATE TABLE bigquery_sink (
        shipment_id INT,
        location STRING,
        status STRING,
        timestamp DOUBLE
    ) WITH (
        'connector' = 'bigquery',
        'project' = 'my-gcp-project',
        'dataset' = 'supply_chain',
        'table' = 'shipments'
    )
""")

tenv.execute_sql("INSERT INTO bigquery_sink SELECT * FROM kafka_source")

env.execute("Supply Chain Processing")
