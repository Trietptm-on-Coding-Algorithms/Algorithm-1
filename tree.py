#!/usr/bin/python
#-*- coding:utf-8 -*-
#����������

#�����ڵ���
class Node:
    lft=None
    rgt=None
    def __init__(self,key,val):
        self.key=key
        self.val=val

#�������
def insert(node,key,val):
    #����ڵ㣬key��val����������ڽڵ㣬�򴴽�
    if node is None:return Node(key,val)
    if node.key==key:node.val=val
    #����и��ڵ㣬�Ǿ���Ѱ����λ��
    elif key<node.key:
        #С�ڵ�ǰ�ڵ㣬��������߽ڵ㣬ֱ�����û�нڵ㣬�½��ڵ�
        node.lft=insert(node.lft,key,val)
    else:
        node.rgt=insert(node,rgt,key,val)
    return node

#��������
def search(node,key):
    if node is None:raise KeyError
    if node.key==key:return node.val
    #������ڵ�ǰ�ڵ��key�����������˽ڵ㣬�򷵻ؽڵ�ֵ
    elif:
        return search(node.lft,key)
        #���������
    else:
        return search(node,rgt,key)

#����������
class Tree:
    root=None
    #���ڵ�S
    def __setitem__(self,key,val):
        self.root=insert(self.root,key,val)
        #�½��ڵ�����������һ�ε������½����ڵ㣬֮���ٴε���
        #��Ϊ���ڸ��ڵ㣬���Ի�Ƚϴ�С�������ǲ�����߻����ұ�
    def __getitem__(self,key):
        return search(self.root,key)
        #�Ӹ��ڵ㿪ʼ����
    #����Ƿ����ĳ�ڵ�
    def __contains__(self,key):
        try:
            search(self.root,key)
        except KeyError:
            return False
        return True
