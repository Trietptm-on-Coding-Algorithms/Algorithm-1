#!/usr/bin/python
#-*- coding:utf-8 -*-
#用AA树结构实现再平衡的二分搜索树

#基本节点类
class Node:
    lft=None
    rgt=None
    lvl=1
    def __init__(self,key,val):
        self.key=key
        self.val=val

#偏斜处理，让所有同级边都向右，一边调用split函数进行分割处理
def skew(node):
    if None in [node,node.lft]:return node
    #如果节点为None，或者节点左边为None，则不需要进行偏斜处理
    if node.lft.lvl !=node.lvl:return node
    #如果节点左边不与其平级，也不需要进行偏斜处理
    lft=node.lft
    #左边节点
    node.lft=lft.rgt
    #节点左边变成左边节点的右节点，而左边节点的左节点，随着左节点一起上移
    lft.rgt=node
    #将node节点变为左边节点的右节点
    return lft

#分割处理
def split(node):
    if None in [node,node.rgt,node,rgt.rgt]:return node
    if node.rgt.rgt.lvl !=node.lvl:return node
    #如果右节点与其右节点的级数不同，不需要进行分割处理
    rgt=node.rgt
    node.rgt=rgt.lft
    rgt.lft=node
    rgt.lvl+=1
    #分割完，右节点级数增加
    return rgt

#插入操作函数
def insert(node,key,val):
    if node is None:return Node(key,val)
    if node.key == key:node.val=val
    elif key<node.key:
        node.lft=insert(node.lft,key,val)
    else:
        node.rgt=insert(node.rgt,key,val)
    node=skew(node)
    node=split(node)
    return node
