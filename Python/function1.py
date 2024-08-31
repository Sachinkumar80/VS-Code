# def tool():
#    print("Print my function")

# tool()

# def name(fname):
#    print(fname + " Kumar")
   
# name("Sachin")
# name("Rahul")
# name("Harsh")
# name("murari")


# def jobs(fname):
#    print(fname + " Company")

# jobs("HCL IT")


# def add(arg1 ,arg2):
#     total = arg1 + arg2
#     return total

# out = add(2, 4)
# print(out)
# print(add(10,30))

def adder(arg1 ,arg2):
    total = arg1 + arg2
    print(total)

adder(40, 70)
print(adder(40, 70))

###########################
def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x 
    
out = summ([10, 20, 30])
print(out)