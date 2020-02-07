amount_input=int(input("Amount of Inputs:"))

def bubble(lis):
    for i in range(len(lis)):
        current=0
        nex=1
        while nex != len(lis):
            if len(lis[current])<len(lis[nex]):
                lis[current],lis[nex]=lis[nex],lis[current]
                current,nex=nex,nex+1
            elif len(lis[current])==len(lis[nex]):
                if lis[current]>lis[nex]:
                    lis[current],lis[nex]=lis[nex],lis[current]
                current,nex=nex,nex+1
            else:
                current,nex=nex,nex+1

def acronym(amount_input):
    temp_list=list()
    for _ in range(amount_input):
        temp_str=""
        names=input("Input:")
        split_names=names.split(" ")
        for i in split_names:
            if i[0].isupper():
                temp_str+=i[0]
        temp_list.append(temp_str)
    return temp_list


total_acronym=acronym(amount_input)
bubble(total_acronym)
for i in range(len(total_acronym)):
    print(total_acronym[i])
