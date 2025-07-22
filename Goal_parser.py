class Solution:
    def interpret(self, command: str) -> str:
        result=""
        i=0
        for i in range(len(command)):
            if command [i]=='G':
                result +='G'
            elif command[i]=='(':
                if command[i+1]=='a':
                    result +='al'
                else:
                    result +='o'
        return result

