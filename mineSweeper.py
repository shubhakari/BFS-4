class Solution:
    # TC: O(m*n)
    # SC : O(m*n)
    def countMines(self, board: List[List[str]], click: List[int]) -> int:
        ct = 0
        for dx,dy in self.dirs:
            nr,nc = dx+click[0], dy+click[1]
            if 0<=nr<self.m and 0<=nc<self.n and board[nr][nc] == "M":
                ct += 1
        return ct


    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board is None or len(board) == 0:
            return 0
        self.m,self.n = len(board),len(board[0])
        self.dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(-1,-1),(1,1),(1,-1)] # U D L R UR UL LR LL
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        q = deque()
        q.append(click)
        board[click[0]][click[1]] = "B"
        while q:
            pos = q.popleft()
            ct = self.countMines(board,pos)
            if ct == 0:
                for dx,dy in self.dirs:
                    nr,nc = pos[0]+dx,pos[1]+dy
                    if nr >= 0 and nr < self.m and nc >=0 and nc < self.n and board[nr][nc] == "E":
                        board[nr][nc] = "B"
                        q.append([nr,nc])
            else:
                board[pos[0]][pos[1]] = str(ct)
        return board