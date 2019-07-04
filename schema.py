import graphene
import datetime
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models.models import Resultado_Quina as Resultado_Model

'''
class Ganhadores_Cidades(MongoengineObjectType):

    class Meta:
        model = CidadesModel
        interfaces = (Node,)
'''
class Resultado_Quina(MongoengineObjectType):

    class Meta:
        model = Resultado_Model
        interfaces = (Node,)



class Query(graphene.ObjectType):
    node = Node.Field()
    results = MongoengineConnectionField(Resultado_Quina)
    



    
schema = graphene.Schema(query=Query, types=[Resultado_Quina])
