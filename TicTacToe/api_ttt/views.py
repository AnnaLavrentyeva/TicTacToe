from django.shortcuts import render
from django.http import JsonResponse
import json
import random

from django.views.decorators.csrf import csrf_exempt

win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def index(request):
   return render(request,'index.html',{})

# @csrf_exempt
# def movement(request):
#     if request.method == 'POST':
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#
#         return JsonResponse({})

@csrf_exempt
def game(request):
    if request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        value = int(body['value'])
        cell = body['x']

        if (value >=9 or value < 0):
            return JsonResponse({'wrong_cell': 'true'})

        if cell[value] != 'X' and cell[value] != 'O':
            cell[value] = 'X'
        else:
            return JsonResponse({'wrong_cell': 'true'})

        if checkWinner(cell, 'X') == True:
            winner = 'X'
            return JsonResponse({'winner': winner})

        if checkWinner(cell, 'O') == True:
            winner = 'O'
            return JsonResponse({'winner': winner})

        if cell and all(elem == "X" or elem == 'O' for elem in cell):
            winner = 'Draw'
            return JsonResponse({'winner': winner})

        cell = pc_move(cell)

        winner = 0
        return JsonResponse({'cell': cell, 'winner': winner})

def pc_move(cell):
    while True:
        random.seed()
        move = random.randint(0, 8)

        if cell[move] != 'X' and cell[move] != 'O':
            cell[move] = 'O'
            return cell

def checkWinner(cell, sign):
    print(cell)
    for i in win_positions:
        score = 0
        for j in i:
            if cell[j] == sign:
                score += 1
            if score == 3:
                return True
            else:
                continue
