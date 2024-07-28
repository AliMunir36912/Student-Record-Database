import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Title")
mainWindow.geometry("1024x720")


class LabeledEntry:
    def __init__(self, Frame, text):
        self.Label = tkinter.Label(Frame, text=text)
        self.Entry = tkinter.Entry(Frame)

    def customGrid(self, row, column):
        self.Label.grid(row=row, column=column)
        self.Entry.grid(row=row, column=column+1)


class DisplayStudentData:

    currentRow = 2

    def __init__(self, Framtwo, name, age, gender, classNo, fees):
        self.name = name
        self.age = age
        self.gender = gender
        self.classNo = classNo
        self.fees = fees
        self.displayTable()
        self.displayData()

        # print(self.name, self.age, self.gender, self.classNo, self.fees)



    def displayTable(self):
        self.studentLabel = tkinter.Label(Frametwo, text="Student Name").grid(row=1, column=0, padx=30, pady=5)
        self.ageLabel = tkinter.Label(Frametwo, text="Student Age").grid(row=1, column=1, padx=30, pady=5)
        self.genderLabel = tkinter.Label(Frametwo, text="Gender").grid(row=1, column=2, padx=30, pady=5)
        self.classLabel = tkinter.Label(Frametwo, text="Student Class").grid(row=1, column=3, padx=30, pady=5)
        self.feesLabel = tkinter.Label(Frametwo, text="Fees").grid(row=1, column=4, padx=30, pady=5)

    def displayData(self):
        if self.name == "" and self.age == "" and self.gender == "" and self.classNo == "" and self.fees == "":
            print("Not Adding!")
        else:
            tkinter.Label(Frametwo, text=self.name).grid(row= DisplayStudentData.currentRow, column=0, padx=30, pady=5)
            tkinter.Label(Frametwo, text=self.age).grid(row= DisplayStudentData.currentRow, column=1, padx=30, pady=5)
            tkinter.Label(Frametwo, text=self.gender).grid(row= DisplayStudentData.currentRow, column=2, padx=30, pady=5)
            tkinter.Label(Frametwo, text=self.classNo).grid(row= DisplayStudentData.currentRow, column=3, padx=30, pady=5)
            tkinter.Label(Frametwo, text=self.fees).grid(row= DisplayStudentData.currentRow, column=4, padx=30, pady=5)
            DisplayStudentData.currentRow += 1


Frame = tkinter.Frame(mainWindow)
Frame.grid(row=0, column=0)

Frametwo = tkinter.Frame(mainWindow)
Frametwo.grid(row=1, column=0)

StudentName = LabeledEntry(Frame, "Student Name: ")
StudentName.customGrid(0,0)

StudentAge = LabeledEntry(Frame, "Student Age: ")
StudentAge.customGrid(row=0, column=2)

StudentGender = LabeledEntry(Frame, "Gender: ")
StudentGender.customGrid(row=1, column=0)

StudentClass = LabeledEntry(Frame, "Class: ")
StudentClass.customGrid(row=1, column=2)

MonthlyFees = LabeledEntry(Frame, "Fees: ")
MonthlyFees.customGrid(row=0, column=4)


def getValue():
    (studentName, studentAge, studentGender,
     studentClass, monthlyFees) = (StudentName.Entry.get(),StudentAge.Entry.get(),
                                    StudentGender.Entry.get(), StudentClass.Entry.get(),MonthlyFees.Entry.get())

    # print(studentName, studentAge, studentGender, studentClass, monthlyFees)
    DisplayStudentData(Frametwo, studentName, studentAge, studentGender, studentClass, monthlyFees)


button = tkinter.Button(Frame, text="Submit", command=getValue)
button.grid(row=3, column=0)





mainWindow.mainloop()