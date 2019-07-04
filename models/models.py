
from datetime import datetime
from mongoengine import (Document,EmbeddedDocument)
from mongoengine.fields import (
    DateTimeField,IntField, ReferenceField, StringField,
    EmbeddedDocumentListField,ListField
)

class Ganhadores_Por_Uf(EmbeddedDocument):
    cidade = StringField()
    uf = StringField()

class Resultado_Quina(Document):
    meta = {'collection':'resultado_quina' }
    concurso = IntField()
    data_sorteio =      DateTimeField()
    dezena_1     =      StringField()	
    dezena_2 	 =      StringField()	
    dezena_3	 =      StringField()	
    dezena_4	 =      StringField()	
    dezena_5	 =      StringField()	
    arrecadacao_total = StringField()
    ganhadores_quina =  IntField()
    ganhadores_por_uf = EmbeddedDocumentListField(Ganhadores_Por_Uf)
    rateio_quina = StringField()
    ganhadores_quadra = IntField()
    rateio_quadra = StringField()
    ganhadores_terno = StringField()
    rateio_terno = StringField()
    ganhadores_duque = IntField()
    rateio_duque = StringField()
    acumulado = StringField()
    valor_acumulado = StringField()
    estimativa_premio = StringField()
    valor_acumulado_sorteio_especial_sao_joao = StringField() 



