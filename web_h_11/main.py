from fastapi import FastAPI
from api import database, models, crud, schemas
from datetime import datetime, timedelta



app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

@app.post("/contacts/", response_model=schemas.Contact)
def create_contact(contact: schemas.ContactCreate):
    return crud.create_contact(database.SessionLocal(), contact)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
