from flask import render_template,request, redirect,url_for, session,flash
from Config.DataBaseConnection import getDBConnection, closeDBConnection
from controller.common.header import header
from model.student import StudentModel
import io

class Students:
    error={}
    formData = {}
    flagForEdit = False
    def getList(self):
        data = {'title' : "Students", 'menus': header()}
        totalStudent = StudentModel.totalStudent()
        length = 10
        data['pagination'] = self.paginate(totalStudent["total"], length)
        searchText = request.args.get('search',"")
        data['pageNumber'] = request.args.get('page',1,type=int)

        if searchText == "":
            DBdata = StudentModel.fetchAllStudentInfo(False,limit=length)
        else:
            DBdata = StudentModel.fetchAllStudentInfo(searchText,length)
        
        data['search'] = searchText
        return render_template("students.html", data=data, DBdata = DBdata)

    def paginate(self, total,lenght):
        numberOfPage = total // lenght + 1
        if (total%lenght!=0):
            numberOfPage+=1
        page_numbers = list(range(1,numberOfPage))
        offset = 0
        listPage = []
        for page_number in page_numbers:
            dicPage = {'page':page_number, 'offset':offset}
            offset+=lenght
            listPage.append(dicPage)
        return listPage

    def add(self):
        self.flagForEdit = False
        if request.method == "POST" and self.validation():
            self.formData = self.getFormData()
            StudentModel.addStudent(self.formData)
            # Redirect to the students page using the endpoint name
            return redirect(url_for('students'))

        return self.form()
    
    def edit(self):
        student_id =  request.args.get('student_id')
        studentData = StudentModel.fetchStudent(student_id)
        if studentData:
            self.formData = studentData
        else:
            return redirect(url_for("students"))
            
        if request.method == "POST" and self.validation():
            self.formData = self.getFormData()
            StudentModel.updateStudent(self.formData, student_id)
            return redirect(url_for('students'))
           
        return self.form()
    
    def getFormData(self):
        first_name = request.form.get("first_name","")
        last_name = request.form.get("last_name","")
        mobile_number = request.form.get("mobile_number","")
        standard = request.form.get("standard","")
        section = request.form.get("section","")
        age = request.form.get("age","")
        prn = request.form.get("prn","")
        
        self.formData = {"first_name" : first_name, "last_name" : last_name, "mobile_number" : mobile_number, "standard" : standard, "section" : section, "age" : age, "prn" : prn}
        return self.formData


    def form(self):
        error=self.error
        # print(self.formData)
        # if not self.flagForEdit:
        #     self.formData = self.getFormData()

        if not  request.args.get('student_id'):
            self.formData = self.getFormData()
        # print(self.formData)
        data = {'title' : "Add Students", 'menus': header()}
        
        return render_template("addstudent_krishna.html", error = error, formData = self.formData, data=data )

    def validation(self):
        self.error={}
        
        self.formData = self.getFormData()

        if self.formData["first_name"] == "":
            # print("yaha pe error ana chahiye")
            self.error["first_name_error"] = "First Name is required"

        if self.formData["last_name"] == "":
            self.error["last_name_error"] = "Last Name is required"

        if self.formData["mobile_number"] == "":
            self.error["mobile_number_error"] = "Mobile Number is required"

        if self.formData["standard"] == "":
            self.error["standard_error"] = "Standard is required"

        if self.formData["section"] == "":
            self.error["section_error"] = "Section is required"

        if self.formData["age"] == "":
            self.error["age_error"] = "Age is required"

        

        if self.formData["prn"] == "":
            self.error["prn_error"] = "PRN is required"
        elif not request.args.get('student_id'):
            if (StudentModel.validatePRN()):
                self.error["dub_prn_error"] = "PRN already exist"
        elif request.args.get('student_id'):
            if StudentModel.checkduplicatePrn(request.args.get('student_id'),self.formData["prn"]) is not None:
                self.error["dub_prn_error"] = "PRN already exist"
        

        if self.formData['mobile_number']=="":
            self.error['mobile_number_error'] = "Mobile Number is required"
        elif not request.args.get('student_id'):
            if(StudentModel.validateMobile()):
                self.error["dub_mobile_error"] = "Mobile Number already exist"
        elif request.args.get("student_id"):
            # print("edit elif\n")
            if self.checkDuplicateMobileNumber(student_id=request.args.get('student_id'), mobile_number= self.formData["mobile_number"]) is not None:
                self.error["dub_mobile_error"] = "Mobile Number already exist"
                # print("if condition true")



        if len(self.error) == 0:
            return True
        return False

    # def checkduplicatePrn(self,student_id,prn):
    #     db = getDBConnection()
    #     with db.cursor() as query:
    #         sql = f"SELECT id FROM students WHERE id != '{student_id}' and prn='{prn}'"
    #         query.execute(sql)
    #         db.commit()
    #         return query.fetchone()
    
    def checkDuplicateMobileNumber(self, student_id, mobile_number):
        db = getDBConnection()
        with db.cursor() as query:
            sql = f"SELECT id FROM students WHERE id != '{student_id}' and mobile_number = '{mobile_number}'"
            query.execute(sql)
            db.commit()
            return query.fetchone()

    def delete(self):
        student_id =  request.args.get('student_id')
        StudentModel.deleteStudent(student_id)
        return redirect(url_for('students'))

    def studentDetails(self):
        data = {'title' : "Student Details", 'menus': header()} 
        student_id =  request.args.get('student_id')
        self.formData = StudentModel.studentDetails(student_id)
        return render_template("studentdetails.html", data=data , formdata = self.formData)

    def importStudents(self):
        data = {'title' : "Student Details", 'menus': header()} 
        error = {}
        if request.method=="POST":
            uploaded_file = request.files['csv_file']
            # print(uploaded_file)
            if not uploaded_file.filename.endswith('.csv'):
                error['csv_file_error'] = 'please select valid file'
            else:
                content = uploaded_file.read().decode('utf-8')
                listInfo = []
                for line in content.split("\r\n")[1:]:
                    info = line.split(",")
                    StudentInfo = {}
                    # ['Abhas', 'Sakhare', '7744936139', '8', 'a', '13', '1101']
                    StudentInfo["first_name"] = info[0]
                    StudentInfo["last_name"] = info[1]
                    StudentInfo["mobile_number"] = info[2]
                    StudentInfo["standard"] = info[3]
                    StudentInfo["section"] = info[4]
                    StudentInfo["age"] = info[5]
                    StudentInfo["prn"] = info[6]

                    if StudentModel.unique_PRN_Mobile(StudentInfo['prn'], StudentInfo['mobile_number']):
                        listInfo.append(StudentInfo)
                if len(listInfo) != 0:
                    StudentModel.importStudents(listInfo)
                # if StudentModel.importStudents(listInfo):
                return redirect("/students")
        return render_template("importStudents.html", data=data, error = error)
    
