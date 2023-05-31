firstNumber = int(input("Enter the First number = "));
function = str(input("Enter the sum (+, -, /, *) : "));
secondNumber = int(input("Enter the Second number = "));

if(function == '+'):
    output=firstNumber+secondNumber

elif(function == '-'):
    output=firstNumber-secondNumber

elif(function == '/'):
    output=firstNumber/secondNumber

elif(function == '*'):
    output=firstNumber*secondNumber

print("Answer is = ", output)