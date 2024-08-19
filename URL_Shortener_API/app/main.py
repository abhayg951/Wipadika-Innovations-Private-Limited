from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import config, models, schema, db

import random, string

app = FastAPI()

db.Base.metadata.create_all(bind=db.engine)

def generate_short_code():
    """this function will generate a random alphanumeric string of six character"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.post("/shorten", response_model=schema.URLInfo)
def shorten_url(url: schema.URLCreate, db: Session = Depends(db.get_db)):
    """This will take url as parameter and return the short url code that will used to access the original url in the database"""
    short_code = generate_short_code()
    create_url = models.URL(original_url = url.original_url, short_code=short_code)
    db.add(create_url)
    db.commit()
    db.refresh(create_url)
    return create_url

@app.get("/{short_code}", response_model=schema.URLInfo)
def redirect_url(short_code: str, db: Session = Depends(db.get_db)):
    """this will search for the original url in the database"""
    get_url = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if not get_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return get_url
