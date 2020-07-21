max_stack = [float("-inf")]
stack = []

def max_stack_operations(op,element=0):
    if op == "push":
        stack.append(element)
        if element >= max_stack[-1]:
            max_stack.append(element)
    elif op == "pop":
        y = stack.pop()
        if max_stack[-1] == y:
            max_stack.pop()
    else:
        return max_stack[-1]

# max_stack_operations("push",3)
# max_stack_operations("push",7)
# print(max_stack_operations("max"))
# max_stack_operations("push",9)
# print(max_stack_operations("max"))
# max_stack_operations("push",7)
# print(max_stack_operations("max"))

max_stack_operations("push",3)
print(max_stack_operations("max"))
max_stack_operations("push",7)
print(max_stack_operations("max"))
max_stack_operations("pop")
print(max_stack_operations("max"))




