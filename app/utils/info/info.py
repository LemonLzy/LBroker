import random
import string
import time


def gen_email():
    """
    随机生成邮箱
    """
    email_name = random.choice(string.ascii_lowercase + string.digits)
    return email_name + str(int(round(time.time() * 1000000))) + '@qq.com'


def gen_8bit_phone() -> str:
    phone = int((random.randint(int(time.time()), int(time.time()) + int(time.time()))) / 100)
    return str(phone)


def gen_11bit_phone() -> str:
    phone = random.randint(int(time.time()), int(time.time()) + int(time.time()))
    return f"1{phone}"


if __name__ == '__main__':
    print(gen_email())
    print(gen_8bit_phone())
    print(gen_11bit_phone())
