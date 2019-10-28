from datetime import date

def delete_user(userid:int):
    return (
        "delete from User "
        "where "
        "Id = {}"
        .format(userid)
    )

def delete_article(articleid:int):
    return (
        "delete from Article "
        "where "
        "Id = {}"
        .format(articleid)
    )

def delete_comment(commentid:int):
    return (
        "delete from Comment "
        "where "
        "Id = {}"
        .format(commentid)
    )

def unbind_article_tag(tagid:int,articleid:int):
    return (
        "delete from Article_Tag "
        "where "
        "ArticleId = {} and TagId = {}"
        .format(articleid,tagid)
    )

