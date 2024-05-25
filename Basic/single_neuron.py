# i nuron with 4 input , input layer

inputs = [1,2,3,2.5]
weights = [0.2,0.8,-0.5,1.0]
bias = 3

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + inputs[3] * weights[3]+ bias
# we can use numpy for calculate this but let it be as in initial level


print(output)

output = 0

for index, item in enumerate(inputs):
   nodeSum =+ item * weights[index]
   output = output + nodeSum
   print(output)
output = output+ bias;
print(output);


