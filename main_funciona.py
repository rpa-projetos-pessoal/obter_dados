
resultado = []
referencias = []
resultado_numeros = []

def obter_dados(typeId) -> [None, list]:
    selected_config = config_jogo.get(typeId)
    if not selected_config:
        raise ValueError(f"Configuração não encontrada para typeId: {typeId}")
    global resultado
    global referencias
    global resultado_numeros

    ultimos_resultados = []
    codigo_jogada = []
  
    if typeId == 22:
        url = 'https://lotteryapi.brgames.cc/api/webapi/GetNoaverageEmerdList'
        authority = 'lotteryapi.brgames.cc'
        origin = 'https://brloteria.com'
        referer = 'https://brloteria.com/'
    elif typeId == 1:
        url = 'https://22885.club/api/webapi/GetNoaverageEmerdList'
        authority = '22885.club'
        origin = 'https://www.poplottery.com'
        referer = 'https://www.poplottery.com/'

    headers = {
        'authority': authority,
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'pt-BR,pt;q=0.9',
        # 'content-type': 'application/x-www-form-urlencoded',
        'content-type': 'application/json; charset=utf-8',  # NOVO Content-Type
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

    payload = {
        "pageSize": 10,
        "pageNo": 1,
        "typeId": 2,
        "language": 0,
        "random": "a980db4ee3854d5ca3266866767cded3",
        "signature": "6597DA3044315FE987B85D17FDDD4DD9",
        "timestamp": 1694286702
    }

    response = None
    while True:
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=(7, 30))

            if response.status_code == 200:
                results = response.json()
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
           
            print(f"O parâmetro {key_error} não existe ou foi alterado nos dados retornados pela API! typeId: {typeId}")
            print("Dados retornados:")
            pprint(response.json(), indent=2)
            time.sleep(2)
        except Exception as e:
            print(f"Erro ao acessar a API: {e}")
typeId = 1
obter_dados(typeId)

"""
DEVERIA DEVOLVER ALGO ASSIM:
"""
