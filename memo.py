#!/usr/bin/python
#-*- coding:utf-8 -*-
#�����廯��װ�κ���
#���þ���װ�εĺ������൱�ڵ���һ���º���
#�鿴�����Ĳ�����ֻ�ܿ���װ�����������Ϣ����wraps���԰�������ԭ������Ϣ
#���װ��������鿴����ӡ��ʼ�
#https://app.yinxiang.com/shard/s68/nl/14655162/8fa33384-1ca7-468e-9007-007d187aaecc?title=%E8%A3%85%E9%A5%B0%E5%99%A8
from functools import wraps

def memo(func):
    cache={}
    #���������Ľ��
    #wraps����ԭ�������ԣ�fib._name_������wrap
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            #���û�л���ý��
            cache[args]=func(*args)
        return cache[args]
    return wrap
