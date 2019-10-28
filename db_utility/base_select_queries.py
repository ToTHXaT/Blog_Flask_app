from datetime import date


def get_tags():
    return (
        "select * from Tag"
    )

def get_users():
    return (
        "select * from User"
    )

def get_articles():
    return (
        "select * from Article"
    )

def get_comments():
    return (
        "select * from Comment"
    )

def get_articles_tag():
    return (
        "select ArticleId, TagId from Article_Tag"
    )

def get_tags_of_article(articleid:int):
    return (
        "select TagId "
        "from Article_Tag "
        "where ArticleId = {}"
        .format(articleid)
    )

def get_tagnames_of_article(articleid:int):
    return (
        "select Tag.Name "
        "from Article "
        "left join "
        "Article_Tag "
        "on Article.Id = Article_Tag.ArticleId "
        "left join "
        "Tag "
        "on Article_Tag.TagId = Tag.Id "
        "where Article.Id = {}"
        .format(articleid)
    )

def get_tag_id(tag_name:str):
    return (
        "select t.Id "
        "from Tag t "
        "where t.Name = '{}'"
        .format(tag_name)
    )

def get_user(userid:int):
    return (
        "select * "
        "from User "
        "where "
        "User.Id = {}"
        .format(userid)
    )

def get_article(articleid:int):
    return (
        "select * "
        "from Article "
        "where "
        "Article.Id = {}"
        .format(articleid)
    )


def get_comments_of(articleid:int):
    return (
        "select * "
        "from Comment "
        "where Comment.ArticleId = {}"
        .format(articleid)
    )

def get_articles_of(userid:int):
    return (
        "select * "
        "from Article "
        "where Article.UserId = {}"
        .format(userid)
    )
