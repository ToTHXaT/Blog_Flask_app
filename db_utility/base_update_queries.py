from datetime import date


def update_user(columns:dict,userid:int):
    res = "update User set "
    for col in columns:
        res += "{} = {},".format(col,columns[col])
    res = res[0 : len(res) - 1] + " "
    res += "where Id = {}".format(userid)
    return res

def update_password(passwrd:str,userid:int):
    return (
        "update User_password set "
        "Passwrd = '{}'"
        "where UserId = {}"
        .format(passwrd,userid)
    )
    
def update_article_title(title:str,articleid:int):
    return (
        "update Article set "
        "set Title = '{}'"
        "where Id = {}"
        .format(title,articleid)
    )

def update_article_body(body:str,articleid:int):
    return (
        "update Article set "
        "set Body = '{}'"
        "where Id = {}"
        .format(body,articleid)
    )

def update_article(title:str,body:str,articleid:int):
    return (
        "update Article set "
        "Tile = '{}',"
        "Body = '{}'"
        "where Id = {}"
        .format(title,body,articleid)
    )

def update_comment(body:str,commentid:int):
    return (
        "update Comment set "
        "Body = '{}'"
        "where Id = {}"
        .format(body,commentid)
    )

def update_tag(name:str,tagid:int):
    return (
        "update Tag set "
        "Name = '{}'"
        "where Id = {}"
        .format(name,tagid)
    )
