#!/usr/bin/python
#-*- coding:utf-8 -*-
#记忆体化的装饰函数
#调用经过装饰的函数，相当于调用一个新函数
#查看函数的参数，只能看到装饰器的相关信息，而wraps可以帮助保存原函数信息
#相关装饰器，请查看个人印象笔记
#https://app.yinxiang.com/shard/s68/nl/14655162/8fa33384-1ca7-468e-9007-007d187aaecc?title=%E8%A3%85%E9%A5%B0%E5%99%A8
from functools import wraps

def memo(func):
    cache={}
    #保存计算过的结果
    #wraps保存原函数属性，fib._name_不会变成wrap
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            #如果没有缓存该结果
            cache[args]=func(*args)
        return cache[args]
    return wrap
