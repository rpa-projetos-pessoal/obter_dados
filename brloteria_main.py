import requests
import time
import pprint

resultado = []
referencias = []
resultado_numeros = []


def obter_dados() -> [None, list]:
    #selected_config = config_jogo.get(typeId)
    #if not selected_config:
    #    raise ValueError(f"Configuração não encontrada para typeId: {typeId}")
    global resultado
    global referencias
    global resultado_numeros

    ultimos_resultados = []
    codigo_jogada = []
  
    
    url = 'https://lotteryapi.brgames.cc/api/webapi/GetNoaverageEmerdList'
    authority = 'lotteryapi.brgames.cc'
    origin = 'https://brloteria.com'
    referer = 'https://brloteria.com/'
    Accept_Encoding = 'gzip, deflate, br'
    content_type = 'application/problem+json; charset=UTF-8'
    random = "c1c6ecc1e57d4655a72d3d850fcfb1df"
    signature = "EF9B1338569284E4D5B849576BE22130"
    timestamp = 1695647123

    payload = {
        "pageSize": 10,
        "pageNo": 1,
        "typeId": 1,
        "language": 3,
        "random": random,
        "signature": signature,
        "timestamp": timestamp
    }

    headers = {
        'authority': authority,
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'pt-BR,pt;q=0.9',
        'accept-encoding': Accept_Encoding, # Coloquei para testar, ve se vem os dados
        'content-type': 'application/x-www-form-urlencoded',
        'content-type': content_type,  # NOVO Content-Type
        'origin': origin,
        'referer': referer,
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }


    response = None
    while True:
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=(7, 30))

            if response.status_code == 200:
                results = response.json()
                print(results)
                for result in results['data']['list']:
                    numero = int(result['number']) 
                    referencia = int(result['issueNumber'])
                    ultimos_resultados.append(numero)
                    codigo_jogada.append(referencia)

                referencias = codigo_jogada
                resultado = ultimos_resultados
                
                return resultado
            else:
                print(f"Erro na solicitação. Status code: {response.status_code}")
                print("Erro retornado: ", response.json())
                time.sleep(3)
        except KeyError as key_error:
           
            print(f"O parâmetro {key_error} não existe ou foi alterado nos dados retornados pela API! typeId")
            print("Dados retornados:")
            pprint(response.json(), indent=2)
            time.sleep(2)
        except Exception as e:
            print(f"Erro ao acessar a API: {e}")

# para conectar y obter as respostas tem que entrar e fazer o registro aqui-> https://brloteria.com/#/register?invitationCode=5838824772

obter_dados()

"""
DEVERIA DEVOLVER ALGO ASSIM:

{
    "data": {
        "list": [
            {
                "issueNumber": "20230924010341",
                "number": "4",
                "colour": "red",
                "premium": "19954"
            },
            {
                "issueNumber": "20230924010340",
                "number": "4",
                "colour": "red",
                "premium": "96614"
            },
            {
                "issueNumber": "20230924010339",
                "number": "2",
                "colour": "red",
                "premium": "17592"
            },
            {
                "issueNumber": "20230924010338",
                "number": "8",
                "colour": "red",
                "premium": "47038"
            },
            {
                "issueNumber": "20230924010337",
                "number": "8",
                "colour": "red",
                "premium": "82428"
            },
            {
                "issueNumber": "20230924010336",
                "number": "6",
                "colour": "red",
                "premium": "23266"
            },
            {
                "issueNumber": "20230924010335",
                "number": "2",
                "colour": "red",
                "premium": "74872"
            },
            {
                "issueNumber": "20230924010334",
                "number": "3",
                "colour": "green",
                "premium": "78943"
            },
            {
                "issueNumber": "20230924010333",
                "number": "2",
                "colour": "red",
                "premium": "04042"
            },
            {
                "issueNumber": "20230924010332",
                "number": "1",
                "colour": "green",
                "premium": "39671"
            }
        ],
        "pageNo": 1,
        "totalPage": 3059,
        "totalCount": 30581
    },
    "code": 0,
    "msg": "Succeed",
    "msgCode": 0
}

"""
