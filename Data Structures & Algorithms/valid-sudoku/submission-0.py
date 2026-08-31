class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = []
        column_hash = []
        box_hash = []

        for _ in range(10):
            row_hash.append(set())
            box_hash.append(set())
            column_hash.append(set())

        for c in range(81):
            i = c // 9
            j = c % 9
            if board[i][j] != '.':
                box_id = i // 3 * 3 + j // 3
                if board[i][j] in row_hash[i]:
                    return False
                else:
                    row_hash[i].add(board[i][j])
                
                if board[i][j] in column_hash[j]:
                    return False
                else:
                    column_hash[j].add(board[i][j])
                
                if board[i][j] in box_hash[box_id]:
                    return False
                else:
                    box_hash[box_id].add(board[i][j])
                
        return True
'''
1 2 3 4 5 6 7, 8, 9
'''