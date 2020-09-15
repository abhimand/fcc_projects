def arithmetic_arranger(problems, signal=False):

    # check base cases 
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # turns into 2d array split of each problem
    res = []
    for p in problems:
        split = p.split()
        res.append(split)

    # initialize our strings
    firstLine = ""
    secondLine = ""
    dashLine = ""
    resLine = ""
    fourSpaces = "    "

    for problem in res: 
        secNum = problem.pop()
        operator = problem.pop()
        firstNum = problem.pop()
        res = 0

        ######################### Base Cases ########################################
        # check if only digits
        if firstNum.isdigit() == False or secNum.isdigit() == False: 
            return 'Error: Numbers must only contain digits.'

        # check if more than 4 digits
        if len(firstNum) > 4 or len(secNum) > 4: 
            return 'Error: Numbers cannot be more than four digits.'

        # check if correct operator
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
        #################################################################

        # get the result
        if operator == '+': 
            res = int(firstNum) + int(secNum)
        else: 
            res = int(firstNum) - int(secNum)

        # build our strings
        if len(firstNum) > len(secNum):
            spaces = len(firstNum) - len(secNum)
            firstLine += "  " + firstNum + fourSpaces
            secondLine += operator+ " " + " "*spaces + secNum + fourSpaces
            dashLine += "-"*(len("  " + firstNum)) + fourSpaces

            resSpaces = len(firstNum) - len(str(res))
            # remove a space if negative in number
            if "-" in str(res): 
                resLine += " " + " "*resSpaces +  str(res) + fourSpaces
            else:
                resLine += "  " + " "*resSpaces + str(res) + fourSpaces

        elif len(firstNum) < len(secNum):
            spaces = len(secNum) - len(firstNum)
            firstLine += "  " + " "*spaces + firstNum + fourSpaces
            secondLine += operator + " " + secNum + fourSpaces
            dashLine += "-"*(len(operator + " " + secNum)) + fourSpaces

            resSpaces = len(secNum) - len(str(res))
            # remove a space if negative in number
            if "-" in str(res): 
                resLine += " " + " "*resSpaces +  str(res) + fourSpaces
            else:
                resLine += "  " + " "*resSpaces + str(res) + fourSpaces

        elif len(firstNum) == len(secNum):
            firstLine += "  " + firstNum + fourSpaces
            secondLine += operator + " " + secNum + fourSpaces
            dashLine += "-"*(len("  " + firstNum)) + fourSpaces

            resSpaces = len(firstNum) - len(str(res))
            # remove a space if negative in number
            if "-" in str(res): 
                resLine += " " + " "*resSpaces +  str(res) + fourSpaces
            else:
                resLine += "  " + " "*resSpaces + str(res) + fourSpaces


    # remove trailing space while combining our list
    if signal == True: 
        ansList = [firstLine.rstrip(), secondLine.rstrip(), dashLine.rstrip(), resLine.rstrip()]
    else: 
        ansList = [firstLine.rstrip(), secondLine.rstrip(), dashLine.rstrip()]

    # join different strings with a newline
    return "\n".join(ansList)
