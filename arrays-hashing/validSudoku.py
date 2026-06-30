class Solution:
  def validSudoku(self, board: List[List[str]]) -> bool:
    seenr = defaultdict(set)
    seenc = defaultdict(set)
    square = defaultdict(set)

    for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] = ".":
          continue
        if (board[i] in seenr or board[j] in seenc or board[i][j] in square[(i//3, j//3)]):
          return False
        
        seenc[i].add(board[i])
        seenr[j].add(board[j])
        square[(i//3,j//3)].add(board[i][j])
      
    return True
