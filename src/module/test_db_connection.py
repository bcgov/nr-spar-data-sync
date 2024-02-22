import oracledb
from sqlalchemy import create_engine, text

class test_db_connection:
    """ Class used to test database connections. """
    def do_test(database_config):
        """ Test Connection """
        #connection_string = test_db_connection.format_connection_string(database_config)
        engine = test_db_connection.create_engine_by_type(database_config)
        conn = engine.connect().execution_options(autocommit=False)
        result = conn.execute(database_config["test_query"])
        return result
        
    def create_engine_by_type(database_config: str):
        if database_config['type'] == 'ORACLE':
           return create_engine(
               f'oracle+oracledb://:@',
               thick_mode=False,
               connect_args={
                   "user": username,
                   "password": password,
                   "host": cp.host,
                   "port": cp.port,
                   "service_name": cp.service_name
            })

        if database_config['type'] == 'POSTGRES':
            connection_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
                database_config['username'], 
                database_config['password'], 
                database_config['host'], 
                database_config['port'],
                database_config['database'])
            return create_engine(connection_string)

        
"""    def format_connection_string(database_config: str):
        """ Formats the connection string based on the database type and the connection configuration. """
        if database_config['type'] == 'ORACLE':
            connection_string = ('oracle+oracledb://:@',
                thick_mode=False, #ERROR HERE. WHY?
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
"""