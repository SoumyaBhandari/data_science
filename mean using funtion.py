def mean(input_list):
    """4funtion for mean calculation."""
    sum=0
    for i in input_list:
        sum+=i
    output = sum / len(input_list)
    return output
p=mean([1,3,4,5,5])
o=mean([1,3,2,2,6,6])
print("output1 :",p)
print("output2 :",int(o))
print(mean.__doc__)

