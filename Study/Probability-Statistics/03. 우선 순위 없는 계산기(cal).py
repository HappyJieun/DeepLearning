import cal

def calculate(expression):
    operators = "+-*/"
    current_num = ""
    current_operator = "+"
    result = 0

    for char in expression:
        if char in operators:
            if current_num:
                if current_operator == "+":
                    result = add(result, float(current_num))
                elif current_operator == "-":
                    result = minus(result, float(current_num))
                elif current_operator == "*":
                    result = multi(result, float(current_num))
                elif current_operator == "/":
                    result = dev(result, float(current_num))
            current_num = ""
            current_operator = char
        else:
            current_num += char

    if current_num:
        if current_operator == "+":
            result = add(result, float(current_num))
        elif current_operator == "-":
            result = minus(result, float(current_num))
        elif current_operator == "*":
            result = multi(result, float(current_num))
        elif current_operator == "/":
            result = dev(result, float(current_num))

    return result

expression = input("수식을 입력하세요: ")
result = calculate(expression)
print("결과:", result)
