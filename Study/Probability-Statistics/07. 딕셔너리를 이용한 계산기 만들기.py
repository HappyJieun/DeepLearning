def switch_cals(x,op,y):
    return {
        '+': lambda x,y: x+y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y,
        '/': lambda x,y: x/y
        }.get(op)(x,y)

def switch_cals_v2(x,op,y):
    return {
        '+': lambda x,y: x+y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y,
        '/': lambda x,y: x/y
        }[op](x,y)

x = float(input("x:"))
op = input("operation:")
y = float(input("y:"))
print("result:", switch_cals(x,op,y))
print("result:", switch_cals_v2(x,op,y))
        
