stringnumber = input()  # "1 2"
number = stringnumber.split()  # number = [ "1" , "2" ]
numberA = int(number[0])  # "1" => 1
numberB = int(number[1])  # "2" => 2
print(numberA + numberB)
