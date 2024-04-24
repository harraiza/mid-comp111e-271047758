string="i like cocomelon"
def reversal(string):
    if len(string)==1:
        print(string[-1],end="")
    else:
        print(string[-1],end="")
        reversal(string[:len(string)-1])
reversal(string)