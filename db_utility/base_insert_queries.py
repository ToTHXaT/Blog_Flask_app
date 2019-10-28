from datetime import date

def add_user(sname:str,fname:str, nick:str,email:str,birthdate:date):
    return (
        "insert into User " 
        "(SName, FName, Nick, Email, BirthDate) " 
        "values " 
        "('{}','{}','{}','{}','{}')"
        .format(sname,fname,nick,email,birthdate)
    )

def add_user_password(userid:int,passwrd:str):
    return (
        "insert into User_password "
        "(UserId, Passwrd) "
        "values "
        "({},'{}')"
        .format(userid,passwrd)
    )

def add_article(title:str,body:str,userid:int):
    return (
        "insert into Article " 
        "(Title, Body, UserId) " 
        "values " 
        "('{}','{}',{})"
        .format(title,body,userid)
    )

def add_comment(body:str,userid:int,articleid:int):
    return (
        "insert into Comment " 
        "(Body, UserId, ArticleId) " 
        "values " 
        "('{}',{},{})"
        .format(body,userid,articleid)
    )

def add_tag(name:str):
    return (
        "insert into Tag " 
        "(Name) " 
        "values "
        "('{}')"
        .format(name)
    )

def bind_article_tag(tagid:int,articleid:int):
    return (
        "insert into Article_Tag "
        "(TagId,ArticleId) "
        "values "
        "({},{})"
        .format(tagid,articleid)
    )


    
