def query_articles(string:str,fr:int=0,num:int=10):
    return (
        "select * from "
        "Article "
        "where "
        r"Title like '%" + string + r"%' "
        "order by Article.PubDate desc "
        "limit {},{}"
        .format(fr,num)
    )
print(query_articles('Hello'))
