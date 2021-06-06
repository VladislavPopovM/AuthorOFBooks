from typing import Optional
from fastapi import FastAPI
from db import DB

app = FastAPI()
db = DB()
@app.get("/")
def read_root():
    return "Hi, this test was done by Vlad Popov"


@app.get("/writers_non_json/{writer_id}/")
def read_item_non_json(writer_id: int, q: Optional[str] = None):
    res = db.get_author_with_books_non_json(writer_id)
    context = {}
    if res:
        context['id'] = res[0][0]
        context['name'] = res[0][1]
        context['books'] = []
        for i in res:
            context['books'].append({'id':i[2],"name":i[3]})

    return context

@app.get("/writers/{writer_id}/")
def read_item(writer_id: int, q: Optional[str] = None):
    res = db.get_author_with_books(writer_id)
    print(res)
    context = {}
    if res:
        context['id'] = res[0][0]
        context['name'] = res[0][1]
        context['books'] = []
        for i in res:
            context['books'].append(i[2])

    return context