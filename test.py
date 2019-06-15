from mongoengine import *
import config as c
from models import Users

# You can connect to a real mongo server instance by your own.


try:
    
    '''
    client = pymongo.MongoClient(c.QUINA_CONFIG['url_database'])
    db = client.appLoteria
    col = db.resultado_quina
    result = col.find_one()
    '''
    
    url_database = 'mongodb+srv://ekdespe:%3Fjkyu%3F55@cluster0-icnup.mongodb.net/appLoteria?retryWrites=true&w=majority',     
    result = connect('appLoteria',host=url_database)
    result = (Users.objects.first())
except Exception as error:
    print("Error",error)
else:
    print("Sucess to connect to database")
    print(result.name)
