# Write a program that creates a dictionary where the keys are subjects (e.g., 'Math', 'Science') and
#  the values are lists of marks. Add marks for 3 subjects, and print the average marks for each subject.

def avgofsubjectlist(subjectnumberlist,subj):
    totalnum = 0
    subjectavg = 0
    for x in range(len(subjectnumberlist)):
        totalnum = totalnum + subjectnumberlist[x]
    subjectavg = totalnum/len(subjectnumberlist)
    printavg(subjectavg,subj)
    return

def printavg(subjavg,subj):
    print(f"Average of {subj} subject = {subjavg}")

subjects= {
    "Math": [90,80,95,65],
    "Science" : [95,86,90,60],
    "English" : [96,60,92,70]
}

print(f"Subjects with numbers: {subjects}")

subjects["Math"].append(50)
subjects["Science"].append(75)
subjects["English"].append(60)

print(f"Subjects after update of numbers: {subjects}")

print("Averages:")
getavg = avgofsubjectlist(subjects["Math"],"Math")
getavg = avgofsubjectlist(subjects["Science"],"Science")
getavg = avgofsubjectlist(subjects["English"],"English")


print(subjects.get("Math")[0])