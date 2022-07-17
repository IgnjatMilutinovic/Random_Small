from prettytable import PrettyTable
table=PrettyTable()
inputs=[]
outputs=[]
inputs_values=[]
outputs_values=[]
is_it_okay=0

while is_it_okay!=1:
    number_of_inputs = int(input('Enter number of inputs that you want : '))
    number_of_outputs = int(input('Enter number of outputs that you want : '))
    if type(number_of_inputs) != int or type(number_of_outputs) != int:
        print('Please enter numbers, try again.')
    elif number_of_outputs>number_of_inputs:
        print(number_of_inputs)
        print(2**number_of_outputs)
        print(number_of_inputs>(2**number_of_outputs))
        print('Number of inputs needs to be bigger than number of outputs, try again.')
    elif number_of_inputs<((2**(number_of_outputs-1))+1):
        print('Number of inputs needs to be bigger than ' + str((2**(number_of_outputs-1))) + " try again.")
    elif number_of_inputs>(2**number_of_outputs):
        print('Number of inputs needs to be less than or ' + str(2**number_of_outputs) + " try again.")
    else:
        is_it_okay=1

#making list of values for inputs
k =0
i = number_of_inputs
while k!=number_of_inputs:
    u=1
    while u!=number_of_inputs+1:
       if u==i:
           inputs_values.append(1)
       else:
           inputs_values.append(0)
       u+=1
    i-= 1
    k+=1
inputs_values=[inputs_values[i:i+number_of_inputs] for i in range(0, len(inputs_values), number_of_inputs)]


#making list of values for outputs
u=0
i=1
while u!=number_of_outputs:
    k=0
    while k!= 2**number_of_outputs:
        outputs_values.append([0]*i)
        k+=i
        outputs_values.append([1]*i)
        k+=i
    u+=1
    i*=2
outputs_values = [j for i in outputs_values for j in i]
outputs_values=[outputs_values[i:i+2**number_of_outputs] for i in range(0, len(outputs_values), 2**number_of_outputs)]
outputs_values.reverse()



for j in range(1, number_of_inputs + 1):
    inputs.append('Y' + str(number_of_inputs - j))
    table.add_column(inputs[j-1],inputs_values[j-1])
for j in range(1, number_of_outputs + 1):
    outputs.append('A' + str(number_of_outputs - j))
    table.add_column(outputs[j-1],outputs_values[j-1][:number_of_inputs])




print(table)
input()