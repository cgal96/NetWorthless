from db.database import engine, Base
from models.asset import Asset
from models.balance import Balance
from models.price import Price

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
