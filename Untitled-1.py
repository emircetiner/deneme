import random

liste = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

şifre = int(input("şifren ne kadar uzun olsun?"))
                      
password = ""


for i in range(şifre):
    number = random.choice(liste)
    password = password + number




print("senin şifren", password)
