import requests
import json
import module.data_synchronization as data_sync
from logging import config as logging_config
import os

def do_tests_in_jenkins():
    print("Starting tests")
    
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
        
def testVault():  
    vault_token = os.environ['vtoken']  # Copying my token from vault
    print(vault_token)
    vault_url = 'https://knox.io.nrs.gov.bc.ca/v1/groups/data/spar/test'
    headers = {'X-Vault-Token': vault_token}
    res = requests.get(vault_url, headers=headers)
    print(res.text)    
    j = json.loads(res.text)
    print(j)


def main() -> None:
    logging_config.fileConfig(os.path.join(os.path.dirname(__file__), "logging.ini"), 
                              disable_existing_loggers=False)   
    data_sync.data_sync()    
    
if __name__ == '__main__':
    print("I'm containerized now. So what?")
    testVault()
   
