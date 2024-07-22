import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def index(request):
    return render(request, 'game/index.html')

def two_player(request):
    return render(request, 'game/two_player.html')

def ai(request):
    return render(request, 'game/ai.html')

@csrf_exempt
def get_ai_move(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        board = data['board']
        move = find_best_move(board)
        return JsonResponse({'move': move})

def is_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

def is_moves_left(board):
    return any(cell is None for cell in board)

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 10 - depth
    if is_winner(board, 'X'):
        return depth - 10
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] is None:
                board[i] = 'O'
                best = max(best, minimax(board, depth + 1, False))
                board[i] = None
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] is None:
                board[i] = 'X'
                best = min(best, minimax(board, depth + 1, True))
                board[i] = None
        return best

def find_best_move(board):
    best_val = -float('inf')
    best_move = -1
    for i in range(9):
        if board[i] is None:
            board[i] = 'O'
            move_val = minimax(board, 0, False)
            board[i] = None
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move
