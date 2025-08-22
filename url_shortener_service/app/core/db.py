import motor.motor_asyncio
from app.core.config import settings


client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URI)
db = client.get_database(settings.MONGODB_DB)
urls_collection = db.get_collection(settings.MONGODB_COLLECTION)
