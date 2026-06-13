class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == '.':
                    continue
                
                # Determine the index of the 3x3 box (0 to 8)
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Check if the value already exists in the row, column, or box
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                # Document the seen value
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True
    


