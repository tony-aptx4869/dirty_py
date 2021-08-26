#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @ Tony Chang
# Copyright (c) 1994-2021 Tony Chang \
# https://github.com/tony-aptx4869 \
# https://aptx4869.tv \
# All Rights Reserved.

import time
startTime = time.time()

class position:
  def __init__(self, x, y):
    self.availableDigital = []
    self.digital = 0
    self.x = x
    self.y = y

def rowNum(p, sudoku):
  row = set(sudoku[p.y * 9 : (p.y + 1) * 9])
  row.remove(0)
  return row

def colNum(p, sudoku):
  col = []
  length = len(sudoku)
  for i in range(p.x, length, 9):
    col.append(sudoku[i])
  col = set(col)
  col.remove(0)
  return col

def blockNum(p, sudoku):
  block_x = p.x // 3
  block_y = p.y // 3
  block = []
  start = block_y * 3 * 9 + block_x * 3
  for i in range(start, start + 3):
    block.append(sudoku[i])
  for i in range(start + 9, start + 9 + 3):
    block.append(sudoku[i])
  for i in range(start + 9 + 9, start + 9 + 9 + 3):
    block.append(sudoku[i])
  block = set(block)
  block.remove(0)
  return block

def initPosition(sudoku):
  positionList = []
  length = len(sudoku)
  for i in range(length):
    if sudoku[i] == 0:
      p = position(i % 9, i // 9)
      for j in range(1, 10):
        if j not in rowNum(p, sudoku) and j not in colNum(p, sudoku) and j not in blockNum(p, sudoku):
          p.availableDigital.append(j)
      positionList.append(p)
  return positionList

def tryInsert(p, sudoku):
  availableDigital = p.availableDigital
  for digital in availableDigital:
    p.digital = digital
    if check(p, sudoku):
      sudoku[p.y * 9 + p.x] = p.digital
      if len(positionList) <= 0:
        endTime = time.time()
        usedTime = endTime - startTime
        showSudoku(sudoku)
        print('Time: %f s' %(usedTime))
        exit()
      p2 = positionList.pop()
      tryInsert(p2, sudoku)
      sudoku[p2.y * 9 + p2.x] = 0
      sudoku[p.y * 9 + p.x] = 0
      p2.digital = 0
      positionList.append(p2)
    else:
      pass

def check(p, sudoku):
  if p.digital == 0:
    print('The digital of position \'p\' has not been assigned.')
    return False
  if p.digital not in rowNum(p, sudoku) and p.digital not in colNum(p, sudoku) and p.digital not in blockNum(p, sudoku):
    return True
  else:
    return False

def showSudoku(sudoku):
  for j in range(9):
    for i in range(9):
      print('%d ' %(sudoku[j * 9 + i]), end = '')
    print('')
  print('')

def difficultySudoku(sudoku):
  difficultySudoku = 9 * 9
  for digital in sudoku:
    if digital:
      difficultySudoku -= 1
  print('Difficulty of this Sudoku: %d (Larger number, Greater difficulty).' %difficultySudoku)
  return difficultySudoku

if __name__=='__main__':
  sudoku = [
    # 芬兰数学家因卡拉，花费3个月时间设计出了世界上迄今难度最大的数独游戏
    # 8, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 3, 6, 0, 0, 0, 0, 0,
    # 0, 7, 0, 0, 9, 0, 2, 0, 0,
    # 0, 5, 0, 0, 0, 7, 0, 0, 0,
    # 0, 0, 0, 0, 4, 5, 7, 0, 0,
    # 0, 0, 0, 1, 0, 0, 0, 3, 0,
    # 0, 0, 1, 0, 0, 0, 0, 6, 8,
    # 0, 0, 8, 5, 0, 0, 0, 1, 0,
    # 0, 9, 0, 0, 0, 0, 4, 0, 0,

    # sudoku2
    # 0, 0, 2, 0, 0, 7, 0, 0, 3,
    # 0, 3, 0, 0, 0, 8, 0, 2, 0,
    # 4, 0, 0, 0, 9, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 8, 4,
    # 0, 0, 6, 0, 0, 0, 5, 0, 0,
    # 2, 9, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 4, 0, 0, 0, 5,
    # 0, 8, 0, 5, 0, 0, 0, 3, 0,
    # 3, 0, 0, 6, 0, 0, 9, 0, 0,

    # Another:
    # 3, 0, 0, 0, 1, 8, 2, 0, 0,
    # 0, 0, 6, 0, 4, 0, 0, 8, 9,
    # 0, 8, 0, 0, 5, 0, 0, 0, 4,
    # 0, 0, 0, 4, 6, 0, 0, 0, 8,
    # 0, 6, 0, 7, 0, 0, 0, 0, 2,
    # 8, 0, 0, 1, 2, 0, 0, 6, 5,
    # 0, 0, 0, 0, 0, 2, 8, 4, 7,
    # 0, 4, 0, 0, 0, 1, 0, 0, 0,
    # 9, 0, 8, 0, 3, 4, 6, 0, 0,

    # Designed by myself:
    1, 0, 0, 0, 0, 6, 0, 0, 0,
    0, 5, 0, 7, 8, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 5, 6, 7, 0, 9, 0,
    5, 6, 0, 0, 9, 0, 0, 0, 4,
    0, 0, 1, 0, 3, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 2,
    0, 7, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 8,

    # All Brand Damn New Sudoku:
    # 全新的数独，供你玩乐：
    # 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # 0, 0, 0, 0, 0, 0, 0, 0, 0,
  ]
  difficultySudoku(sudoku)
  positionList = initPosition(sudoku)
  # showSudoku(sudoku)
  p = positionList.pop()
  tryInsert(p, sudoku)

