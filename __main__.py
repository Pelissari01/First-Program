from hash import *
from time import sleep
import os

def main():
    while True:
        p1 = PassWord()
        p1.check = str(input('\nWrite your pass word: ')).strip()

        while p1.keep == True:
            print('Write a valid password')
            p1.check = str(input('\nWrite your pass word: ')).strip()
            if isinstance(p1.check, str):
                p1.keep = False
            else:
                continue
        p1.validation()
        if p1.keep == True:
            return

        while True:
            Continue = input("\nDo you want to try again? [1]-Yes [2]-No: ").strip()
            if Continue == '2':
                print('\nClosing the program...')
                sleep(1.5)
                os.system('cls')
                return
            elif Continue == '1':
                os.system('cls')
                break
            else:
                os.system('cls')
                print('\n-Error Value!')
        os.system('cls')

if __name__ == '__main__':
    main()
