
def characters(common_letter1,common_letter2):
    str1=common_letter1.lower()
    str2=common_letter2.lower()
    common_str = list(set(str1)&set(str2))
    for letters in common_str:
        letters = ' , '.join(common_str)
    print("Common characters: ",letters)


characters("housE", "computers")
