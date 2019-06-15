from mongoengine import connect
import config as c
from models import Resultado_Quina , Cidades, Users




connect('appLoteria',host=c.QUINA_CONFIG['url_database'])
