import module.data_synchronization as data_sync
from logging import config as logging_config
import os

def main() -> None:
    logging_config.fileConfig(os.path.join(os.path.dirname(__file__), "logging.ini"), 
                              disable_existing_loggers=False)   
    # data_sync.data_sync()
    print("OK")
    
    # Testing Secrets variable from Jenkins Credentials Plugin    
    print(os.environ['Usr_teste'] + " " + os.environ['Psw_Test'] )    
    
if __name__ == '__main__':
    main()