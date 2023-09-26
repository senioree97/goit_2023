from collections import deque, UserList
from datetime import datetime

class Person():
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

class NoRight(Exception):
    pass

class Doctor(Person):
    def __init__(self, name, surname, position) -> None:
        super().__init__(name, surname)
        self.position = position

    def add(self, patient, disease_name):
        des = Disease(disease_name, " ".join((self.name, self.surname)))
        patient.story._Story__add(des)

    def treat(self, patient, disease_name, treatment):
        patient.story[disease_name].treat(treatment)
        

class Patient(Person):
    def __init__(self, name, surname, polis) -> None:
        super().__init__(name, surname)
        self.polis = polis
        self.story = None # TODO class story

    @property
    def healthy(self):
        return self.story.healthy
    
class Story(UserList):
    story_size = 10

    def __init__(self):
        self.__data = deque([], self.story_size)
        self.__data_dict = dict()
        self.data = list

    def __getitem__(self, key=None):
        if key is None:
            return list(self.__data)
        if isinstance(key, int):
            return self.__data[key]
        elif isinstance(key, str):
            return self.__data_dict.get(key)
        
    def __len__(self) -> int:
        return len(self.__data)
    
    def add(self, *_):
        raise NoRight # TODO class NoRight
    
    def __add(self, disease):
        self.__data.append(disease)
        self.__data_dict = {des.name: des for des in self.__data}
        self.data = [des for des in self.__data]

    def healthy(self):
        return all([disease.cured for disease in self.__data])



class Disease:
    def __init__(self, name, doctor) -> None:
        self.name = name
        self.doctor = doctor
        self.treatment = list()
        self.time = datetime.now()
        self.cured = False
        self.cure_time = None

    def cure(self):
        self.cured = True
        self.cure_time = datetime.now()

    def treat(self, treatment):
        self.treatment.append(treatment)




doctor_surgeon = Doctor("Bill", "Klinton", "Head")
doctor_tera = Doctor("Anton", "Jerry", "Therapist")

patient_one = Patient("Patient1", "super", 8293467892)
patient_two = Patient("Batak", "Obama", 2135235235)

doctor_tera.add(patient_one, "flu")
doctor_surgeon.add(patient_two, "appendix")

print(patient_one.story["flu"].time)
print(patient_two.story["appendix"].time)

doctor_tera.treat(patient_one, "medicine")
doctor_surgeon.treat(patient_two, "operation")

print(patient_one.story["flu"].treatment)
print(patient_two.story["appendix"].treatment)

print(patient_one.healthy)

print(patient_one.story["flue"].cure())

print(patient_one.healthy)


