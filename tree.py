#!/usr/bin/python
#-*- coding:utf-8 -*-
#二分搜索树

#基本节点类
class Node:
    lft=None
    rgt=None
    def __init__(self,key,val):
        self.key=key
        self.val=val

#插入操作
def insert(node,key,val):
    #传入节点，key，val，如果不存在节点，则创建
    if node is None:return Node(key,val)
    if node.key==key:node.val=val
    #如果有根节点，那就搜寻插入位置
    elif key<node.key:
        #小于当前节点，就搜索左边节点，直至左边没有节点，新建节点
        node.lft=insert(node.lft,key,val)
    else:
        node.rgt=insert(node,rgt,key,val)
    return node

#搜索操作
def search(node,key):
    if node is None:raise KeyError
    if node.key==key:return node.val
    #如果等于当前节点的key，即搜索到了节点，则返回节点值
    elif:
        return search(node.lft,key)
        #向左边搜索
    else:
        return search(node,rgt,key)

#二分搜索树
class Tree:
    root=None
    #根节点S
    def __setitem__(self,key,val):
        self.root=insert(self.root,key,val)
        #新建节点操作，如果第一次调用则新建根节点，之后再次调用
        #因为存在根节点，所以会比较大小，决定是插在左边还是右边
    def __getitem__(self,key):
        return search(self.root,key)
        #从根节点开始搜索
    #检查是否包含某节点
    def __contains__(self,key):
        try:
            search(self.root,key)
        except KeyError:
            return False
        return True
