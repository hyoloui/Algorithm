def solution(s):
    stack = []  # 빈 스택 생성
    
    for char in s:
        if char == '(':
            # 여는 괄호를 만나면 스택에 push
            stack.append('(')
        elif char == ')':
            # 닫는 괄호를 만나면
            if not stack:  # 스택이 비어있으면 짝이 안 맞음
                return False
            stack.pop()  # 스택에서 pop (여는 괄호 제거)
    
    # 모든 문자를 처리한 후 스택이 비어있어야 올바른 괄호
    return len(stack) == 0