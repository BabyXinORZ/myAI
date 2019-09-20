

# class AI():

#     static total = 0


# def min(board, deep, alpha, beta):
#     v = evaluate()
#     total += 1
#     if deep < 0 or win(board):
#         pass
#     return 0


# def max():
#     return 0


# def evaluate():
#     return 0

# var min = function(board, deep, alpha, beta) {
#     var v = evaluate(board)
#     total + +
#     if(deep <= 0 | | win(board)) {
#         return v
#     }

#     var best = MAX
#     var points = gen(board, deep)

#     for(var i=0
#         i < points.length
#         i++) {
#         var p = points[i]
#         board[p[0]][p[1]] = R.hum
#         var v = max(board, deep-1, best < alpha ? best: alpha, beta)
#         board[p[0]][p[1]] = R.empty
#         if(v < best) {
#             best = v
#         }
#     if(v < beta) { // AB剪枝
#                   ABcut + +
#                   break
#                   }
#     }
#     return best
# }

# var max = function(board, deep, alpha, beta) {
#     var v = evaluate(board)
#     total + +
#     if(deep <= 0 | | win(board)) {
#         return v
#     }

#     var best = MIN
#     var points = gen(board, deep)

#     for(var i=0
#         i < points.length
#         i++) {
#         var p = points[i]
#         board[p[0]][p[1]] = R.com
#         var v = min(board, deep-1, alpha, best > beta ? best: beta)
#         board[p[0]][p[1]] = R.empty
#         if(v > best) {
#             best = v
#         }
#     if(v > alpha) { // AB 剪枝
#                    ABcut + +
#                    break
#                    }
#     }
#      return best
# }
