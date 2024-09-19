class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stk = []
        for op in operations: 
            if op == 'D':
                stk.append(stk[-1]*2)
            elif op == 'C':
                stk.pop()
            elif op == '+':
                stk.append(stk[-1]+ stk[-2])
            else: 
                stk.append(int(op)) # dont understand this else statment lol
        return sum(stk)
