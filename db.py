from pony.orm import *
import os
from urllib import parse


db_params = {}
try:
    url = parse.urlparse(os.environ["DATABASE_URL"])
    db_params = {"database": url.path[1:],
        "user": url.username,
        "password": url.password,
        "host": url.hostname,
        "port": url.port
    }
except KeyError:
    # Hardcode local defaults if not on Heroku
    db_params = {"database": "postgres",
        "user": "postgres",
        "password": "Postgres1234",
        "host": "127.0.0.1",
        "port": "5432"
    }

db = Database(provider="postgres", 
    user=db_params["user"], 
    password=db_params["password"], 
    host=db_params["host"],
    database=db_params["database"],
    port=db_params["port"]
)


class Query(db.Entity):
    text = Required(str)
    used = Required(bool)
    responses = Set("Response")


class Response(db.Entity):
    text = Required(str)
    query = Required(Query)


parse.uses_netloc.append("postgres")


db.generate_mapping(create_tables=True)

# TODO exception handling or better knowledge of what I might raise
@db_session
def load_tweet():
    r = select(r for r in Response)[:1][0]
    txt = r.text
    r.delete()
    return r.text[0:140]


@db_session
def store_responses(l, q):
    query = select(qu for qu in Query if qu.text == q)[:1][0]
    for r in l:
        Response(text=r, query=query)
    query.used = True

@db_session
def store_queries(q):
    for e in q:
        Query(text=e, used=False)

@db_session
def get_query():
    query = select(q for q in Query if not q.used)[:1][0]
    return query

@db_session
def reset_queries():
    delete(q for q in Query)
    Query(text="who",used=False)
    Query(text="what",used=False)
    Query(text="when",used=False)
    Query(text="where",used=False)
    Query(text="why",used=False)
    Query(text="how",used=False)