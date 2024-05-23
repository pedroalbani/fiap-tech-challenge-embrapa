from fastapi import APIRouter, Depends
from app.services.baixar_dados_service import BaixarDadosService
from bson import json_util
import json

importar_route = APIRouter(
    prefix="/importar",
    tags=["importar"],
)

def criar_instancia_de_servico():
    return BaixarDadosService()

@importar_route.get("", summary="Importar dados Embrapa")
def importar(tipo_operacao, sub_categoria = None, atualizar_base = True, service: BaixarDadosService = Depends(criar_instancia_de_servico)):    
    """
    Utilize esse serviço para importar os dados 
    diretamente do [site da Embrapa](http://vitibrasil.cnpuv.embrapa.br/).

    Para saber quais tipos de importações possíveis, consulte as
    <a href="/docs/#/configuracao/listar_configuracoes_configuracao_get" target="_self">
    configurações
    </a> existentes.
    """
    response = service.importar(tipo_operacao, sub_categoria, atualizar_base)

    return json.loads(json_util.dumps(response))