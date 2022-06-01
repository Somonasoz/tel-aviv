class UserTarif:
    def __init__(
        self,
        userMsisdn=None, 
        loadDate=None,
        userBalance=None,
        userTariff=None,
        packages=[]):
        self.userMsisdn = userMsisdn
        self.loadDate = loadDate
        self.userBalance = userBalance
        self.userTariff = userTariff
        self.packages = packages

class Package:
    def __init__(
        self, code=None, 
        qanswers=None, 
        comments=None,
        tarif=None, 
        cached=None,
        balance=None):
        self.code = code
        self.qanswers = qanswers
        self.comments = comments
        self.tarif = tarif
        self.cached = cached
        self.balance = balance



class LocalStorage:
    __phone = None
    __tarif = UserTarif()
    __lang = "ru"

    @property
    def phone(self):
        return self.__phone

    @property
    def tarif(self):
        return self.__tarif
    
    @property
    def lang(self):
        return self.__lang

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @tarif.setter
    def tarif(self, value):
        self.__tarif = value

    @lang.setter
    def lang(self, value):
        self.__lang = value

store = LocalStorage()