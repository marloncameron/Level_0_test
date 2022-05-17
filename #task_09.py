vowels = ['a', 'e', 'i', 'o', 'u']
word ="Umuzi"
input_list = list(word.lower())
v_list = []

for x in input_list:
    if x.lower() in vowels:
        if x not in v_list:
            v_list.append(x)
            vowels_out = ', '.join(v_list)
print("Vowels: ",vowels_out)



