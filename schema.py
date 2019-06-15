import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Resultado_Quina as Resultado_Model
from models import Cidades as CidadesModel
from models import Users as UsersModel


class Users(MongoengineObjectType):
    class Meta:
        model = UsersModel
        interfaces = (Node,)



class Cidades(MongoengineObjectType):

    class Meta:
        model = CidadesModel
        interfaces = (Node,)



class Resultado_Quina(MongoengineObjectType):

    class Meta:
        model = Resultado_Model
        interfaces = (Node,)




class Query(graphene.ObjectType):
    node = Node.Field()
    results = MongoengineConnectionField(Resultado_Quina)
    



    
schema = graphene.Schema(query=Query, types=[Resultado_Quina,Cidades,Users])
