class Class:
    def __init__(self):
        self.students = []

    def add(self, firstName, lastName, number, gender):
        student_data = {
            "firstName": firstName.title(),
            "lastName": lastName.title(),
            "number": number,
            "gender": gender.lower()
        }
        return self.students.append(student_data)

    def __len__(self):
        print(self.students)
        return len(self.students)

    def __getitem__(self, number):
        [student] = [student for student in self.students if student["number"] == number ]
        result = student if student else 'There is no student'
        return result

    def __setitem__(self, number, data):
        [index] = [index for index, student in enumerate(self.students) if student["number"] == number]
        self.students[index] = data


    def __iter__(self):
        return iter(self.students)


class_A = Class()
print(class_A.students)
class_A.add("yUnus eMre", "seRt", 156, "M")

class_A.add("emRe", "sErt", 145, "F")

for student in class_A:
    print(student)

print(len(class_A))



class_A[156] = {"firstName": "yunus1", "lastName": "sert1", "number": 1516, "gender": "m1"} # set
print(class_A[1516]) # get
print(class_A.students)

# class_A.students[0] = {"firstName": "yunus1", "lastName": "sert1", "number": 1516, "gender": "m1"}
# print(len(class_A))

# ogrenci numarsını yazıp ogrenci ismi getiren method
# a_sinifi = Class()
# a_sinifi.add({
# })
# len(a_sinifi) ogrenci sayisini verecek
# a_sinifi.sayi("erkek") => erkek sayisini verecek
# a_sinifi[334] =>>>>>>>>     {  get
#         "first_name": "adsad",
#         "last_name": "asdasd",
#         "number": 334,
#         "gender": "m"
#     }
#
# a_sinifi[156] = {  // set
#         "first_name":"ccc",
#         "last_name":"ccc",
#         "number": 3333,
#         "gender": "f"
#     },

# for student in a_sinifi:
#  print(student)

sinif = [{'firstName': 'Yunus Emre', 'lastName': 'Sert', 'number': 156, 'gender': 'm'}, {'firstName': 'Emre', 'lastName': 'Sert', 'number': 145, 'gender': 'f'}]

