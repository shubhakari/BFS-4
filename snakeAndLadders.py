class Solution:
    # TC : O(n**2)
    # SC : O(n**2)
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        if board is None:
            return 0
        n = len(board)
        q = deque()
        moves = 0
        nums = [0]*(n*n) # flattened version of board array
        idx,row,col,even = 0,n-1,0,0
        while idx < n*n:
            if board[row][col] != -1:
                nums[idx] = board[row][col]-1
            else:
                
                nums[idx] = -1
            idx += 1
            if even % 2 == 0:
                col += 1
                if col == n:
                    row -= 1
                    even += 1
                    col = n-1
            else:
                col -= 1
                if col == -1:
                    row -= 1
                    even += 1
                    col = 0
        # now implement bfs 
        # check if cell is explored or not, if not explored change to -2 statingt it is visited
        # 3 states of cells -2: visited, -1: unvivited, any positive number: snake or ladder
        # die value ranges b/w 1 to 6 so we need to pick 1 num in b/w
        q.append(0)
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                
                if cur == n * n - 1:
                    return moves

                for i in range(1, 7):
                    child = cur + i
                    if child >= n * n:
                        continue
                    if nums[child] != -2:
                        next_cell = nums[child] if nums[child] != -1 else child
                        q.append(next_cell)
                        nums[child] = -2  # Mark as visited
            moves += 1
        return -1


        