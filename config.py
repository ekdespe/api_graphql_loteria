
layout_documents ="""{
    "concurso" : $_concurso,
    "data_sorteio" : "$_data",
    "dezena_1" : "$_dezena1",
    "dezena_2" : "$_dezena2",
    "dezena_3" : "$_dezena3",
    "dezena_4" : "$_dezena4",
    "dezena_5" : "$_dezena5",
    "arrecadacao_total" : "$_arrecadacao",
    "ganhadores_quina" : $_ganhadores,
    "ganhadores_por_uf":$_cidades,
    "rateio_quina" : "$_rateio_quina",
    "ganhadores_quadra" : $_ganhadores_quadra,
    "rateio_quadra" : "$_rateio_quadra",
    "ganhadores_terno" : $_ganhadores_terno,
    "rateio_terno" : "$_rateio_terno",
    "ganhadores_duque" : $_ganhadores_duque,
    "rateio_duque" : "$_rateio_duque",
    "acumulado" : "$_acumulado",
    "valor_acumulado" : "$_valor_acumulador",
    "estimativa_premio" : "$_estimativa_premio",
    "valor_acumulado_sorteio_especial_sao_joao" : "$_acumulado_sao_joao"}"""


QUINA_CONFIG = {
        'url_database':'mongodb+srv://ekdespe:%3Fjkyu%3F55@cluster0-icnup.mongodb.net/appLoteria?retryWrites=true&w=majority',     
        'url_request_init' : 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_quina.zip',
        'name_database':'appLoteria',     
        'name_collection':'resultado_quina',     
        'layout_documents':layout_documents,     
        
        'url_request_update' : "http://loterias.caixa.gov.br/wps/portal/loterias/landing/quina/",
        'url_request_final' :"http://loterias.caixa.gov.br/wps/portal/loterias/landing/quina/!ut/p/a1/jc69DoIwAATgZ_EJepS2wFgoaUswsojYxXQyTfgbjM9vNS4Oordd8l1yxJGBuNnfw9XfwjL78dmduIikhYFGA0tzSFZ3tG_6FCmP4BxBpaVhWQuA5RRWlUZlxR6w4r89vkTi1_5E3CfRXcUhD6osEAHA32Dr4gtsfFin44Bgdw9WWSwj/"
        
        }



