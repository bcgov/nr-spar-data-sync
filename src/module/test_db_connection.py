import oracledb
from sqlalchemy import create_engine, text

class test_db_connection:
    """ Class used to test database connections. """
    def do_test(database_config):
        """ Test Connection """
        connection_string = test_db_connection.format_connection_string(database_config)
        engine = create_engine(connection_string)
        conn = engine.connect().execution_options(autocommit=False)
        result = conn.execute(database_config["test_query"])
        return result
        
    def format_connection_string(database_config: str):
        """ Formats the connection string based on the database type and the connection configuration. """
        if database_config['type'] == 'ORACLE':
            connection_string = (f'oracle+oracledb://:@',
                thick_mode=False,
                connect_args={
                    "user": database_config['username'],
                    "password": database_config['password'],
                    "host": database_config['host'],
                    "port": database_config['port'],
                    "service_name": database_config['service_name']
                }
            )

        if database_config['type'] == 'POSTGRES':
            connection_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
                database_config['username'], 
                database_config['password'], 
                database_config['host'], 
                database_config['port'],
                database_config['database'])

        return connection_string