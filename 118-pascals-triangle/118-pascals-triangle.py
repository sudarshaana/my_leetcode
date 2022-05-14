def rowCal(row, col, memo):
    if col == 1:
        return 1
    elif row == col:
        return 1
    s = str(row)+","+str(col)
    if s in memo:
        return memo[s]

    return rowCal(row-1, col-1, memo)+ rowCal(row-1, col, memo)


class Solution:
    
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        memo={}

        for i in range(1, numRows+1):
            sub = []
            for j in range(1, i+1):
                x = rowCal(i, j, memo)
                # print(x, end=" ")
                s = str(i)+","+str(j)
                memo[s] = x
                sub.append(x)
            # print()
            ans.append(sub)
        #print("%s"%(time.time()-start))
        return ans
    
    