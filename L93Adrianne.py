#Adrianne
string='SPAM!HelloSPAM! WorldSPAM!'
def replace_substring(string, sub, replace):
    output=[]
    index=0
    while index<len(string):
        if string[index:index+len(sub)]==sub:
            index+=len(sub)
        else:
            output.append(string[index])
            index+=1
    print("".join(output))

replace_substring(string, "SPAM", "")
