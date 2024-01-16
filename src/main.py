import module.data_synchronization as data_sync
from logging import config as logging_config
import os, requests, json

def do_tests_in_jenkins():
    print("Starting Jenkins Tests")
    
    # Testing Secrets variable from Jenkins Credentials Plugin    
    print(os.environ['Usr_teste'] + " " + os.environ['Psw_Test'] ) 
    
    if os.environ['Usr_teste'] == "usuario_teste":
        print("Usr credential accepted")
    else:
        print("Usr credential incorrect")
        
    if os.environ['Psw_Test'] == "senha":
        print("Password credential accepted")
    else:
        print("Password credential incorrect")
        
def do_tests_in_vault():
    print("Starting Vault Tests") 
    vault_token = os.environ['VltToken'] #From Jenkins Credentials
    vault_url = os.environ['VltEndPoint'] #From Jenkins Credentials 
    headers = {'X-Vault-Token': vault_token}
    res = requests.get(vault_url, headers=headers)
    print(res.text)
    j = json.loads(res.text)
    print(j)



def main() -> None:
    logging_config.fileConfig(os.path.join(os.path.dirname(__file__), "logging.ini"), 
                              disable_existing_loggers=False)   
    #data_sync.data_sync() 
    do_tests_in_vault()
    
if __name__ == '__main__':
    main()