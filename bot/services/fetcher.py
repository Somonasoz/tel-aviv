from math import fabs
import requests

from bot.core import URL_GET_PHONE
from bot.models.models import UserTarif, Package, store


class Fetcher:
    
    def get_phone(self, value):
        res = requests.post(url=URL_GET_PHONE, data={"msisdn":int(value)})
        if res.status_code == 200:
            try:
                data = res.json()
                print("here1",data)
                packages = Package(
                    code=data["Packages"]["Code"],
                    qanswers=data["Packages"]["Qanswers"],
                    tarif=data["Packages"]["Tarif"],
                    cached=data["Packages"]["Cached"],
                    balance=data["Packages"]["Balance"])
                print("here2")
                tarif = UserTarif(
                    userMsisdn=data["UserMsisdn"],
                    userBalance=data["UserBalance"],
                    loadDate=data["LoadDate"],
                    userTariff=data["UserTariff"],
                    packages=packages
                )
                print("here3")
                store.tarif = tarif
                return True
            except Exception as error:
                print("error: ", error)
                return False
        return False
        # return True if res.status_code == 200
