class FileMaker():
    def WriteFile(self, listok):
        with open('extended_student_list.txt', 'w') as fp:
            for i in listok:
                fp.write(str(i.Name)+' '+str(i.LastName)+' '+str(i.Birth)+' '+str(i.Gender)+' '+str(i.Mark)+' '+str(i.Spec)+' '+str(i.Number)[0]+' '+str(i.Login)+' '+i.Password+'\n')