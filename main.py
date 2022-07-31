n = int(input(""))
correctAnswer = input("")
k = int(input())
temp = []
answerSheet = []
trues = [0] * k
falses = [0] * k
unanswered = [0] * k
for i in range(0,k):
    temp = []
    for j in range(0,n):
        temp.append(input())
    answerSheet.append(temp)
for i in range(0,k):
    for j in range(0,n):
        if answerSheet[i][j].count("#") == 1:
            if correctAnswer[j] == "A":
                if answerSheet[i][j][0] == "#":
                     trues[i] += 1
                else:
                     falses[i] += 1
            elif correctAnswer[j] == "B":
                if answerSheet[i][j][1] == "#":
                     trues[i] += 1
                else:
                     falses[i] += 1
            elif correctAnswer[j] == "C":
                if answerSheet[i][j][2] == "#":
                     trues[i] += 1
                else:
                     falses[i] += 1
            else:
                if answerSheet[i][j][3] == "#":
                     trues[i] += 1
                else:
                     falses[i] += 1
        elif answerSheet[i][j].count("#") > 1:
            falses[i] += 1
        else:
            unanswered[i] += 1
score = []
for i in range(0,k):
    score.append((3*trues[i])-falses[i])
    print(score[i])







