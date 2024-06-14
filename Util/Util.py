import random

c = "1234567890abcdefghijklmnopqrstuvwxyz"
def get_random_id():
    r = ""
    for i in range(30):
        r += c[random.randrange(0, len(c))]
    return r
