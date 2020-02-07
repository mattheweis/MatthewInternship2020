def hangman():
    answer_in=str(input("Enter 12 Digit Numbers:"))
    count=0
    count_score=0
    output=list()
    while len(answer_in)!=12:
        print("New Answer")
        answer_in=str(input("Enter 12 Digit Numbers:"))
    for _ in range(12):
        output.append("_")
    print(" ".join(output))
    while count<=5:
        storage=list()
        answer=str(input("Choice:"))
        if answer not in answer_in:
            output.append(answer)
        for i in range(len(answer_in)):
            if answer_in[i]==answer: 
                storage.append(i)
            
        for i in storage:
            output[i]=answer
        print(" ".join(output))
        count+=1

    for i in range(12):
        if output[i] is not "_":
            count_score+=1
    print(f"Score:{count_score}")

    
hangman()