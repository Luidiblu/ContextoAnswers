from unittest import result
import requests
import json


def _get_ten_tips(game_id):
    _result = {}
    for i in range(1, 9):
        r = requests.get(f"https://www.contexto.me/machado/pt-br/tip/{game_id}/{i}").json()
        _result[str(r.get("distance", "Error"))+"º"] = str(r.get("word", "Error")) 
    print(json.dumps(_result, indent=1, ensure_ascii=False))
    return _result


def _get_answer(game_id):
    _result = {}
    r = requests.get(f"https://contexto.me/machado/pt-br/giveup/{game_id}").json()
    _result['resposta'] = str(r.get("word", "Error"))
    print(json.dumps(_result, indent=1, ensure_ascii=False))
    return _result


if __name__ == "__main__":
    print('Bem vindo ao Menu! \n\n')
    print('O que você quer fazer? \n')
    print('[1] - Pegar as 10 dicas')
    print('[2] - Pegar a resposta \n')
    number = input('> ')
    print('\nQual o id da Challenge?')
    game_id = input('> ')
    if str(number) == "1":
        _get_ten_tips(game_id)
    elif str(number) == "2":
        _get_answer(game_id)
    else:
        print('Deu ruim')