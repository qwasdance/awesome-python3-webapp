#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user,blog,comment.
'''

import time,uuid
from orm import Model,StringField,BooleanField,FloatField,TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

def User(Model):
    __table__='user'

    id=StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    email=StringField(ddl='varchart(50)')
    passwd=StringField(ddl='varchart(50)')
    admin=BooleanField()
    name=StringField(ddl='varchart(50)')
    image=StringField(ddl='varchart(50)')
    created_at=FloatField(default=time.time)

class Blog(Model):
    __table__='blogs'

    id=StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    blog_id=StringField(ddl='varchar(50)')
    user_id=StringField(ddl='varchart(50)')
    user_name=StringField(ddl='varchart(50)')
    user_image=StringField(ddl='varchart(50)')
    content=TextField()
    created_at=FloatField(default=time.time)

class Comment(Model):
    __table__='comments'

    id=StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    blog_id=StringField(ddl='varchar(50)')
    user_id=blog_id=StringField(ddl='varchar(50)')
    user_name=blog_id=StringField(ddl='varchar(50)')
    user_image=blog_id=StringField(ddl='varchar(50)')
    content=TextField()
    created_at=FloatField(default=time.time)