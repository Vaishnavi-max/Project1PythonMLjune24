def freq_str(input_str):
    freq_dict={}
    for char in input_str:
        if char in freq_dict:
            freq_dict[char]+=1
        else:
            freq_dict[char]=1
    return freq_dict
input_str=input("inter a string")
freq=freq_str(input_str)
for char,freq in freq.items():
    print(char,":",freq)
