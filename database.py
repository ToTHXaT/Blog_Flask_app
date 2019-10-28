from datetime import date

from flask import jsonify
from db_utility.executor import DB
from db_utility.base_insert_queries import *
from db_utility.base_select_queries import *
from db_utility.base_update_queries import *
from db_utility.base_delete_queries import *


db = DB('Blog',dictionary=True)

def registrate_user(sname:str,fname:str, nick:str,email:str,birthdate:date,passwrd:str):
    try:
        (db
            .exe( add_user(sname,fname,nick,email,birthdate))
            .exe('select last_insert_id()')
            .exe( add_user_password(db.temp[0][0],passwrd))
        )
    except Exception as e:
        print(e)
        return False

    db.commit()
    return True

def update_user_info(columns:dict,userid:int):
    try:
        db.exe( update_user(columns,userid) )

    except Exception as e:
        print(e)
        return False
    
    db.commit()
    return True

def get_user_info(userid:int):
    response = None
    try:
        response = db.get_raw(get_user(userid),get_one=True)

    except Exception as e:
        print(e)
        return None
    
    return response

def post_article(title:str,body:str,userid:int,tags:list):

    tag_ids = []

    try:
        for tag in tags:
            db.exe(get_tag_id(tag))
            if(len(db.temp) > 0):
                tag_ids.append(db.temp[0][0])

        if len(tag_ids) > 0:
            db.exe(add_article(title,body,userid))
            db.exe('select last_insert_id()')
            article_id = db.temp[0][0]

            for tag_id in tag_ids:
                db.exe(bind_article_tag(tag_id,article_id))
        else:
            raise Exception('Tag list is invalid')
    
    except Exception as e:
        print(e)
        return False
        
    db.commit()
    return True

def change_article(title:str,body:str,tags:list,articleid:int):
    try:
        if(title == None):
            update_article_body(body,articleid)
        elif(body == None):
            update_article_title(title,articleid)
        elif title and body:
            update_article(title,body,articleid)

        if(len(tags) > 0):
            db.exe(get_tags_of_article(articleid))
            res = db.temp
            res_ = []
            for i in res:
                res_.append(i[0])

            tag_ids = []
            for tag in tags:
                db.exe(get_tag_id(tag))
                if(len(db.temp) > 0):
                    tag_ids.append(db.temp[0][0])

            for tag in tag_ids:
                if (tag in res_):
                    db.exe(unbind_article_tag(tag,articleid))
                else:
                    db.exe(bind_article_tag(tag,articleid))
                
    except Exception as e:
        print(e) 
        return False
    
    db.commit()
    return True

def get_article_info(articleid:int):
    response = None
    try:
        art = db.get_raw(get_article(articleid),get_one=True)
        
        tags = db.get_raw(get_tagnames_of_article(articleid))
        tag_list = []

        for tag in tags:
            tag_list.append(tag['Name'])

        art['TagList'] = tag_list

        response = art
    except Exception as e:
        print(e)
        return None

    return response

def get_user_articles(userid:int):
    response = None
    try:
        arts = db.get_raw(get_articles_of(userid))
        for art in arts:
            articleid = art['Id']
            tags = db.get_raw(get_tagnames_of_article(articleid))
            tag_list = []
            for tag in tags:
                tag_list.append(tag['Name'])

            art['TagList'] = tag_list
        
        response = arts
    except Exception as e:
        print(e)
        return None
    
    return response

def leave_comment(body:str,userid:int,articleid:int):
    try:
        db.exe(add_comment(body,userid,articleid))
        
    except Exception as e:
        print(e)
        return False

    db.commit()
    return True

def edit_comment(body:str,commentid:int):
    try:
        db.exe(update_comment(body,commentid))

    except Exception as e:
        print(e)
        return False
    
    db.commit()
    return True

def get_comments_of_article(articleid:int):
    response = None
    try:
        response = db.get_raw(get_comments_of(articleid))
    
    except Exception as e:
        print(e)
        return None

    return response