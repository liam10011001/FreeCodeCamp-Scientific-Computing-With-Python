def isValidProblem(problem):
    if len(problem.split()) != 3:
        return (False, "Error: Invalid format.")
    
    (x, operator, y) = problem.split()
    if operator != '+' and operator != '-':
        return (False, "Error: Operator must be '+' or '-'.")
    if not x.isdigit() or not y.isdigit():
        return (False, "Error: Numbers must only contain digits.")
    if int(x) >= 10000 or int(y) >= 10000:
        return (False, "Error: Numbers cannot be more than four digits.")

    return (True, "Valid")

def display(problems, calculate=False):
    firstLine = ""
    secondLine = ""
    thirdLine = ""
    answerLine = ""
    seperator = "    " # 4 space to sperate between problems
    for problem in problems:
        if calculate:
            (x, y, operator, ans) = problem
        else:
            (x, y, operator) = problem
        width = 2 + max(len(x), len(y)) # 1 space for operator and another one to spearate between operator and operand
        
        for i in range(width - len(x)):
            firstLine += " "
        firstLine += x
        if problems.index(problem) < len(problems) - 1:
            firstLine += seperator 

        secondLine = secondLine + operator
        for i in range(width - 1 - len(y)):
            secondLine += " "
        secondLine += y
        if problems.index(problem) < len(problems) - 1:
            secondLine += seperator

        for i in range(width):
            thirdLine += "-"
        if problems.index(problem) < len(problems) - 1:
            thirdLine += seperator

        if calculate:
            for i in range(width - len(ans)):
                answerLine += " "
            answerLine += ans
            if problems.index(problem) < len(problems) - 1:
                answerLine += seperator
                
    if not calculate:
        return firstLine + "\n" + secondLine + "\n" + thirdLine
    else:
        return firstLine + "\n" + secondLine + "\n" + thirdLine + "\n" + answerLine
    
def arithmetic_arranger(problems, calculate=False):
    if len(problems) > 5 :
        return "Error: Too many problems."
    else:
        arranged_problems = ""
        transformedList = [] # [ (operandA, operandB, operator, (Answer)), ........]
        for problem in problems:
            (valid, message) = isValidProblem(problem)
            if not valid:
                return message
            
            (x, operator, y) = problem.split()
            if calculate:
                if operator == '+':
                    transformedList.append((x, y, operator, str(int(x) + int(y))))
                else:
                    transformedList.append((x, y, operator, str(int(x) - int(y))))
            else:
                transformedList.append((x, y, operator))
                
        arranged_problems = display(transformedList, calculate)  
        return arranged_problems

if __name__=="__main__":
    print(arithmetic_arranger(['2 + 3', '2 - 3', '234 + 23', '12 - 3', '9999 + 3', '1 + 1'])) # problems > 5
    print(arithmetic_arranger(['2 * 3'])) # Invalid operator
    print(arithmetic_arranger(['2a + 3'])) # Invalid operand
    print(arithmetic_arranger(['10000 + 3'])) # 5-digit operand
    print(arithmetic_arranger(['-2 + 3'])) # Negative operand
    print(arithmetic_arranger(['2 + 3', '2 - 3', '234 + 23', '12 - 3', '9999 + 3'])) # Accepted
    print(arithmetic_arranger(['2 + 3', '2 - 3', '234 + 23', '12 - 3', '9999 + 3'], True)) # Accepted
