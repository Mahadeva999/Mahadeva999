# storing a varibale using n as a input and number of iterations to be perfromed 
n = int(input("Enter how many numbers to be displayed"))
# assigning two more vairbales such as first and second because first and second number in the series is 0 and 1
first = 0
second = 1
# opening a for loop for iteration method to find out fibnocci numbers
for i in range(n):
    print(first)
    temp = first  # which means i am initating a temp varible whihc becomes the first so that i can say the first is second
    first = second  # which means if first is temp then first is second here because our second number is 1 in the fibnaci series
    second = first + second  # whihc means the next number in the series is a sumof the last and the number before.
