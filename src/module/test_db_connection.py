import cx_Oracle
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
            dsn = cx_Oracle.makedsn(
                database_config['host'], 
                database_config['port'], 
                service_name=database_config['service_name']
            )

            connection_string = (
                'oracle+cx_oracle://{}:{}@'.format(
                    database_config['username'], 
                    database_config['password']
                ) + dsn
            )

        if database_config['type'] == 'POSTGRES':
            connection_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
                database_config['username'], 
                database_config['password'], 
                database_config['host'], 
                database_config['port'],
                database_config['database'])

        return connection_string