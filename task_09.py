def output_vowels(word):
    vowels = "Vowels: "
    temp_string = word.lower()
    for i in "aeiou":
        if(temp_string.count(i) > 0):
            vowels += i+", "
    vowels = vowels[:-2]
    return vowels


print(output_vowels("Umuzi"))



