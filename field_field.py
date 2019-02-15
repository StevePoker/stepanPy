"""Дано:
    Есть больница в которой есть Врачи и Пациенты.
    У каждого Пациента есть Истотрия_болезней
    В Истории_болезней хранится 10 последних Болезней.
    Болезнь содержит ионформацию когда поцинет заболел,
    кто его лечил, когда выздоровел (если выздоровел),
    процедуры и лечение, которые назначил врач.
Врач может назначать процедуры (например диагностические) и лечение
(напрмер курс лекарств).
У врачей и пациентов есть Имя и Фамилия. У пациентов есть номер полиса
социального страхования. У врачей есть должность.
Пациент не может изменять свою Истотрию_болезней.
Задача: реализовать в классах привдённые выше условия.
"""
from datetime import datetime
from collections import deque

class NoRights(BaseException):
    pass

class Disease():
    def __init__(self, name, treatment = ''):
        self.treatment = treatment
        self.time = datetime.now()
        self.name = name

class Story:
    def __init__(self):
        self.pac_story = []

    def add(self, disease):
        raise NoRights

    def __len__(self):
        if len(self.pac_story) <= 10:
            return len(self.pac_story)
        else:
            l = range(10)
            self.pac_story = deque(l)
            return len(self.pac_story)

    def __getitem__(self, key):
        if type(key) == int:
            return self.pac_story[key]
        else:
            desease = []
            count = 0
            while count <= len(self.pac_story) - 1:
                if self.pac_story[count].name == key:
                    desease.append(self.pac_story[count])
                count += 1
            return desease[0]
    def set_treat(self, name, treat):
        desease = []
        count = 0
        while count <= len(self.pac_story) - 1:
            if self.pac_story[count].name == name:
                desease.append(self.pac_story[count])
            count += 1
        index = self.pac_story.index(desease[0])
        self.pac_story[index].treatment = treat

    def __eq__(self, other):
        return self.pac_story == other



class Pacient:
    def __init__(self, name, surname, policy):
        self.name = name
        self.surname = surname
        self.policy = policy
        self.story = Story()
        self.healthy = True
    def doctor_add(self, disease):
        self.story.pac_story.append(Disease(disease))

class Doctor:
    def __init__(self, name, surname, title):
        self.name = name
        self.surname = surname
        self.title = title

    def add(self, pac, disease):
        pac.doctor_add(disease)
        pac.healthy = False

    def treat(self, pac, disease, treatment):
        pac.story.set_treat(disease, treatment)


doctor_surg = Doctor('Bill', 'Klinton', 'Head of surgery dep.')
doctor_tera = Doctor('Monika', 'Levinsky', 'Therapist')

pac1 = Pacient('Geoge', 'Bush', 128712678213)
pac2 = Pacient('Barak', 'Obama', 598624093862)

assert pac1.story == []
assert pac2.story == []

try:
    pac1.story.add('flue')
except NoRights:
    pass

try:
    pac1.story.add('flue')
except NoRights:
    pass

doctor_tera.add(pac1, 'flue')
doctor_surg.add(pac2, 'appendicitis')

assert len(pac1.story) == 1
assert len(pac2.story) == 1

assert pac1.story['flue'].time is not None
assert pac2.story['appendicitis'].time is not None

assert pac1.story['flue'].time < pac2.story['appendicitis'].time

doctor_surg.treat(pac1, 'flue', 'medicine')
doctor_tera.treat(pac2, 'appendicitis', 'operation')

assert 'medicine' in pac1.story['flue'].treatment
assert 'operation' in pac2.story['appendicitis'].treatment

assert 'medicine' in pac1.story[-1].treatment
assert 'operation' in pac2.story[-1].treatment

assert pac1.healthy == False
assert pac2.healthy == False

for _ in range(11):
    doctor_tera.add(pac1, 'flue')

assert len(pac1.story) == 10