import numpy as np
import random
import time

# 五连
FIVE = 5
# 活四
FOUR = 4
# 活三
THREE = 3
# 活二
TWO = 2
# 冲四
CFOUR = 14
# 眠三
CTHREE = 13
# 眠二
CTWO = 12
# 其他
DEFAULT = 0
# 隔子为二
ATWO = 22
# 隔子为三
ATHREE = 23
# 隔子为四
AFOUR = 24
# 分值表
SCORE_TABLE = {
    FIVE: 9999999,
    FOUR: 50000,
    THREE: 5000,
    TWO: 50,
    CFOUR: 5000,
    CTHREE: 500,
    CTWO: 20,
    DEFAULT: 0,
    ATWO: 30,
    ATHREE: 4500,  # 隔子为三
    AFOUR: 40000
}

COLOR_BLACK = -1
COLOR_WHITE = 1
COLOR_NONE = 0
random.seed(0)
# don't change the class name


class AI(object):
    # chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        # You are white or black
        self.color = color
        # You are white or black
        self.enemy = 0-color
        # the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need add your decision into your candidate_list. System will get the end of your candidate_list as your decision .
        self.candidate_list = []
        # The input is current chessboard.

    def go(self, chessboard):
        # Clear candidate_list
        # print(chessboard)
        print("before")
        self.printBoard(chessboard)
        self.candidate_list.clear()
        # ==================================================================
        # Write your algorithm here
        # Here is the simplest sample:Random decision
        new_pos = self.findNext(chessboard)
        # ==============Find new pos========================================
        # Make sure that the position of your decision in chess board is empty.
        # If not, return error.
        assert chessboard[new_pos[0], new_pos[1]] == COLOR_NONE

        chessboard[new_pos[0], new_pos[1]] = self.color
        # print("new pos")
        # print(new_pos)
        print("after")
        self.printBoard(chessboard)
        # Add your decision into candidate_list, Records the chess board
        self.candidate_list.append(new_pos)

    def findNext(self, chessboard):
        idx = np.where(chessboard == COLOR_NONE)
        idx = list(zip(idx[0], idx[1]))
        # deal with the firt one
        if(len(idx) == 15*15):
            return [7, 7]
        # print(idx)
        # pos_idx = random.randint(0, len(idx)-1)
        score = -1
        tmpScore = 0
        next = [7, 7]
        for i in idx:
            tmpScore = self.getPosScore(chessboard, i, self.color)
            tmpScore += self.getPosScore(chessboard, i, self.enemy)*0.8
            # print("tempScore")
            # print(tmpScore)
            if tmpScore > score:
                score = tmpScore
                next = i
        print("Next")
        print(next)
        return next

    def getMyShapeScore(self, shape):
        shape = [0, 1, 1, 0, -1, -1, -1, 1, 0]

        return 0

    def getEnemyShapeScore(self, shape):
        return 0

    def getPosScore(self, chessBoard, pos, color):
        line1 = list()
        line2 = list()
        line3 = list()
        line4 = list()
        row = pos[0]
        col = pos[1]

        for i in range(self.chessboard_size):
            line1.append(int(chessBoard[row][i]))
            line2.append(int(chessBoard[i][col]))
        score1 = self.getLineScore(line1, col, color)
        score2 = self.getLineScore(line2, row, color)

        index1 = min(row, col)
        tempRow1 = row - index1
        tempCol1 = col - index1
        while tempRow1 < self.chessboard_size and tempCol1 < self.chessboard_size:
            line3.append(int(chessBoard[tempRow1][tempCol1]))
            tempRow1 += 1
            tempCol1 += 1
        score3 = self.getLineScore(line3, index1, color)

        maxIndex = row + col
        minIndex = max(maxIndex-self.chessboard_size+1, 0)
        index2 = col-minIndex

        # print(pos)
        # print(minIndex)
        for i in range(minIndex, min(self.chessboard_size, maxIndex+1)):
            line4.append(int(chessBoard[maxIndex-i][i]))
        score4 = self.getLineScore(line4, index2, color)

        return score1+score2+score3+score4

    def getLineScore(self, line, stonePos, color):
        line1 = line
        line1[stonePos] = color
        lineType = self.AnalyseLineType(line1, stonePos)
        # print(line1)
        # print(stonePos)
        # print(lineType)
        return SCORE_TABLE[lineType]

    def AnalyseLineType(self, line, stonePos):

        if(len(line) < 5):
            return 0

        color = line[stonePos]
        enemy = 0-color
        left = stonePos
        right = stonePos
        length = len(line)

        while(left > 0):
            if(line[left-1] != color):
                break
            left -= 1

        while(right < length-1):
            if(line[right+1] != color):
                break
            right += 1

        leftRange = left
        rightRange = right

        # 计算可以下棋的范围
        while leftRange > 0:
            if line[leftRange-1] == enemy:
                break
            leftRange -= 1

        while rightRange < length-1:
            if line[rightRange+1] == enemy:
                break
            rightRange += 1

        # print("RIGHT:" + str(right))
        # print("LEFT:" + str(left))
        # print("RIGHTRANGE:" + str(rightRange))
        # print("LEFTRANGE:" + str(leftRange))

        # 排除范围小于4的情况
        if rightRange-leftRange < 4:
            return 0

        # 五连
        if right-left > 3:
            return FIVE
        leftNone = False
        rightNone = False

        # 四连
        if right-left == 3:
            if left > 0:
                if line[left-1] == COLOR_NONE:
                    leftNone = True
            if right < length-1:
                if line[right+1] == COLOR_NONE:
                    rightNone = True

            if leftNone and rightNone:
                return FOUR
            else:
                return CFOUR

        # 三连
        if right-left == 2:
            # 冲四
            if left > 1:
                if line[left-1] == COLOR_NONE:
                    if line[left-2] == color:
                        if left > 2 and right < length-1:
                            if line[left-3] != enemy and line[right+1] != enemy:
                                return AFOUR
                        return CFOUR

            if right < length-2:
                if line[right+1] == COLOR_NONE:
                    if line[right+2] == color:
                        if left > 0 and right < length-3:
                            if line[left-1] != enemy and line[right+3] != enemy:
                                return AFOUR
                        return CFOUR

            # 活三
            if left > 0 and right < length-1:
                if line[left-1] == COLOR_NONE and line[right+1] == COLOR_NONE:
                    return THREE

            # 眠三
            return CTHREE

        # 二连
        if right-left == 1:
            if left > 1:
                if line[left-1] == COLOR_NONE:  # 0(1)1
                    if line[left-2] == color:  # 至少三个子 1011
                        if left > 2 and line[left-3] == color:  # 至少四个子
                            if left > 3 and right < length-1:
                                if line[left-4] != enemy and line[right+1] != enemy:
                                    return AFOUR
                            return CFOUR
                        if left > 2 and right < length-1:
                            if line[left-3] != enemy and line[right+1] != enemy:
                                return ATHREE
                        return CTHREE

            if right < length-2:
                if line[right+1] == COLOR_NONE:  # 1(1)0
                    if line[right+2] == color:  # 至少三个子
                        if right < length-3 and line[right + 3] == color:  # 至少四个子
                            if right < length-4 and left > 0:
                                if line[right+4] != enemy and line[left-1] != enemy:
                                    return AFOUR
                            return CFOUR
                        if right < length-3 and left > 0:
                            if line[right+3] != enemy and line[left-1] != enemy:
                                return ATHREE
                        return CTHREE

            if left > 0 and right < length-1:
                if line[left-1] == COLOR_NONE and line[right+1] == COLOR_NONE:
                    return TWO

            return CTWO

        if right == left:
            if left > 1:
                if line[left-1] == COLOR_NONE:
                    if line[left-2] == color:
                        if left > 2 and line[left-3] == color:
                            if left > 3 and line[left-4] == color:
                                if left > 4 and right < length-1:
                                    if line[left-5] != enemy and line[right+1] != enemy:
                                        return AFOUR
                                return CFOUR
                            if left > 3 and right < length-1:
                                if line[left-4] != enemy and line[right+1] != enemy:
                                    return ATHREE
                            return CTHREE
                        if left > 2 and right < length-1:
                            if line[left-3] != enemy and line[right+1] != enemy:
                                return ATWO
                        return CTWO

            if right < length-2:
                if line[right+1] == COLOR_NONE:
                    if line[right+2] == color:
                        if right < length-3 and line[right+3] == color:
                            if right < length-4 and line[right+4] == color:
                                if left > 0 and right < length-5:
                                    if line[left-1] != enemy and line[right+5] != enemy:
                                        return AFOUR
                                return CFOUR
                            if left > 0 and right < length-4:
                                if line[left-1] != enemy and line[right+4] != enemy:
                                    return ATHREE
                            return CTHREE
                        if left > 0 and right < length-3:
                            if line[left-1] != enemy and line[right+3] != enemy:
                                return ATWO
                        return CTWO

        return 0

    def printBoard(self, chessboard):
        print()
        for row in chessboard:
            print("| ", end="")
            for pos in row:
                if pos == 0:
                    print(" ", end="")
                elif pos == COLOR_BLACK:
                    print("x", end="")
                elif pos == COLOR_WHITE:
                    print(0, end="")
                print(" | ", end="")
            print()
