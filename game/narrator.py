import os
import time


class Narrator():


    def story_1(self):
        print("###########################")
        print("##### Welcom Game RPG #####")
        print("#   Copyright Mahya 2019  #")
        print("###########################")
        time.sleep(3)

    def clear(self):
        """method to clear the terminal"""
        os.system('cls' if os.name =='nt' else 'clear')
