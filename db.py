import databases
from decouple import config
import sqlalchemy

DATABASE_URL = f"mysql+mysqlconnector://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost/{config('DB_DATABASE')}"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
