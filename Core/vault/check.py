

from Core.vault.auth import vault



def get_auth():


    saved = vault.load()



    if saved:


        return saved



    return None




