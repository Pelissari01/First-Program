from hashlib import sha256
from time import sleep

class PassWord():


    def __init__(self):
        self._password = None
        self.__real_password = None
        self.real_one = '123'
        self.keep = False




    @property
    def check(self):
        return self._password

    @check.setter
    def check(self, word):
        if len(word) > 0 and isinstance(word, str):
             cod = word.encode('utf-8')
             hash = sha256(cod).hexdigest()
             self._password = hash
             print("\nValid password")
        else:
            print("\nInvalid password")
            self.keep = True


    def validation(self):


        cod = self.real_one.encode('utf-8')
        hash = sha256(cod).hexdigest()
        self.__real_password = hash

        if self._password == self.__real_password:
            print('\nChecking...')
            sleep(2)
            print('\nWelcome!')
            self.keep = True
        else:

            print('\nChecking...')
            sleep(2)
            print('\nPlease, write the right password')
