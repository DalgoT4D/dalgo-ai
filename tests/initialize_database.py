import mindsdb_sdk

server = mindsdb_sdk.connect()
try:
    server.query("DROP MODEL [IF EXISTS] mindsdb.test_regression_model;")
    server.create_database(
        engine="postgres",
        name="example_db",
        connection_args={
            "user": "demo_user",
            "password": "demo_password",
            "host": "3.220.66.106",
            "port": "5432",
            "database": "demo"
        }
    )
except Exception as e:
    print(e)