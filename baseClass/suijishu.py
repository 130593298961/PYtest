#获取固定长度的随机字符串
import random


def get_random_str(randomlength):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str
# print(get_random_str(randomlength=15))
def get_random_china(randomlength):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = '圆包火住调满县局照参红细引听该铁价严龙飞'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str
# print(get_random_china(5))