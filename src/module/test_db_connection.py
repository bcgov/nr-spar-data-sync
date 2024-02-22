import oracledb
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

class test_db_connection:
    """ Class used to test database connections. """
    def do_test(database_config):
        """ Test Connection """
        connection_string = test_db_connection.format_connection_string(database_config)
        print(connection_string)
        engine = create_engine(connection_string)
        conn = engine.connect().execution_options(autocommit=False)
        result = conn.execute(text(database_config["test_query"]))
        return result        
        
    def format_connection_string(database_config: str):
        """ Formats the connection string based on the database type and the connection configuration. """
        if database_config['type'] == 'ORACLE':
            cp = oracledb.ConnectParams(
                host=database_config['host'],
                port=database_config['port'],
                service_name=database_config['service_name'])
                
            connection_string = URL.create(
                "oracle+oracledb",
                host=cp.get_connect_string(),
                username=database_config['username'],
                password=database_config['password'],
            )

        if database_config['type'] == 'POSTGRES':
            connection_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
                database_config['username'], 
                database_config['password'], 
                database_config['host'], 
                database_config['port'],
                database_config['database'])

        return connection_string