__date__ = '2019/5/8 11:30'

def removeOuterParentheses(S:str):
    stack = []
    res = ''
    index = 0
    for i in range(len(S)):

        if S[i] == "(":
            stack.append("(")
        else:
            stack.pop()

        if not stack:
            res += S[index+1:i]
            index = i+ 1
    return res

def minAddToMakeValid(S: str) -> int:
        stack = []
        num = 0
        if S=="":
            return 0
        for i in range(len(S)):
            if S[i] == '(':
                stack.append('(')
            else:
                if not stack or stack.pop() !="(":
                    num += 1
        return len(stack)+num


def calPoints(ops):
        stack = []
        num = 0
        for i in range(len(ops)):
            if ops[i] == 'D':
                stack.append(2*stack[-1])
            elif ops[i] == 'C':
                stack.pop()
            elif ops [i] == '+':
                stack.append(stack[-1]+stack[-2])
            else :
                stack.append(int(ops[i]))

        for i in stack:
            num += i
        return num


if __name__ == '__main__':
    print(removeOuterParentheses("(()())(())(()(()))"))
    print(minAddToMakeValid("))"))
    print(calPoints(["5","-2","4","C","D","9","+","+"]))