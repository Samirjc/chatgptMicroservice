import requests

def main():
    token = ''
    thread_id = 'thread_AO9tGt1hZuN4K4YO7AQpBUfZ'
    run_id = 'run_z83hfN2JDRz6ZI5JnKeoL8Aa'
    call_id = 'call_NjDwMI8uvHxXQ0g1Goyzgh2g'

    # URL do endpoint que você deseja chamar
    url = f'https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/submit_tool_outputs'
    
    # Headers personalizados que você deseja enviar
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'OpenAI-Beta': 'assistants=v2'
    }

    # Dados que você deseja enviar no corpo da requisição (opcional)
    data = {
        'tool_outputs': [
            {
                'tool_call_id': call_id,
                'output': 'R$100,00'
            }
        ]
    }

    try:
        # Fazendo a requisição POST ao endpoint com os headers e os dados
        response = requests.post(url, headers=headers, json=data)

        # Verificando se a requisição foi bem sucedida (código 200)
        if response.status_code == 200:
            # Extraindo e imprimindo os dados da resposta
            data = response.json()  # se a resposta for JSON
            print(data)
        else:
            print(f'Erro ao chamar o endpoint: {response.status_code}')

    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')

if __name__ == '__main__':
    main()
