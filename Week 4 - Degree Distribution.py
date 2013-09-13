import csv

class Degree:
    def __init__(self, code, name, uni, places):
        self.code = int(code)
        self.name = name
        self.uni = uni
        self.places = int(places)
        self.cutoff = '-'
        self.accepted = []

class Student:
    def __init__(self, name, atar, preferences):
        self.name = name
        self.atarMark = float(atar)
        self.bonuses = {}
        self.prefs = []
        self.uni = '-'

        # put all preferences into a list and
        # make a dictionary for all the degrees that give them a bonus
        for pref in preferences.split(';'):
            if '+' in pref:
                code, bonus = pref.split('+')
                self.bonuses[int(code)] = float(bonus)
                self.prefs.append(int(code))
            else:
                self.prefs.append(int(pref))

        # create dictionary with all the degrees currented listed as undecided
        self.rejected = dict.fromkeys(self.prefs, 0)

    # returns the ATAR of the student, taking into account if the degree they're
    # applying for gives them any bonus points
    def atar(self, code):
        if code in self.bonuses:
            if self.bonuses[code] + self.atarMark > 99.95:
                return 99.95
            else:
                return self.bonuses[code] + self.atarMark
        else:
            return self.atarMark

    # 0 = undecided, 1 = rejected, 2 = accepted
    # reject the degree
    def reject(self, code):
        self.rejected[code] = 1
        # if the uni they just got rejected from was
        # previously their uni
        if self.uni == code:
            self.uni = '-'

    # accept the degree
    def accept(self, code):
        self.rejected[code] = 2
        self.uni = code

    # checks if the current code is the next best preference:
    def check(self, code):
        # if the degree isn't even one of their preferences
        if code not in self.prefs:
            return False

        # or they've already gotten rejected by this degree before
        if self.rejected[code] == 1:
            return False

        for x in self.prefs:
            # if we've reached the code we're checking up to and there
            # hasn't been any zeros yet
            if x == code:
                return True
            # if there are any degrees in higher preference that have not
            # been checked yet
            if self.rejected[x] == 0:
                return False

    # check if the student either has no degrees they can enter or they've
    # already gotten a degree.
    def toDo(self):
        # if the're already gotten into a degree
        if 2 in self.rejected.values():
            return False

        # at this point we know no one has accepted them yet
        # so if they're got any 0s in the dictionary they still need to be processed
        if 0 in self.rejected.values():
            return True

        # otherwise, they've tried all degrees and been rejected for every single one
        return False

# are there any people who still need a degree?
def zero():
        everyone = [student.toDo() for student in students]

        # even if only one person still has degree options open but has no degree
        # this will turn True, and we continue checking.
        return any(everyone)

students = []
degrees = []

for line in csv.DictReader(open('students.csv')):
    students.append(Student(line["name"], line["score"], line["preferences"]))

for line in csv.DictReader(open('degrees.csv')):
    degrees.append(Degree(line["code"], line["name"], line["institution"], line["places"]))

while zero():
    for degree in degrees:
        rejected = []

        # potential applicant list
        for student in students:
            # if the current degree we're checking is their next best preference
            # and they don't yet have a degree
            if student.check(degree.code) and student.toDo():
                degree.accepted.append(student)

        # if there's no potential applicants
        if not degree.accepted:
            continue

        # hacky way to sort by atar and break ties in alphabetical order
        final = []
        scores = set([x.atar(degree.code) for x in degree.accepted])
        scores = sorted(list(scores), reverse=True)

        for score in scores:
            temp = [x for x in degree.accepted if x.atar(degree.code) == score]
            temp.sort(key=lambda x: x.name)
            final.extend(temp)

        degree.accepted = final

        # if there are too many people, take first n people
        if len(degree.accepted) > degree.places:
            rejected = degree.accepted[degree.places:]
            degree.accepted = degree.accepted[:degree.places]

        # set their status as accepted
        for student in degree.accepted:
            student.accept(degree.code)

        # reject the rest
        for student in rejected:
            student.reject(degree.code)


# calculate the cutoff mark and number of places left for the degree
for degree in degrees:
    degree.places = degree.places - len(degree.accepted)
    scores = [x.atar(degree.code) for x in degree.accepted]
    # add a default cutoff mark (ATAR of 100.00) so
    # that using min(scores) won't break the computer
    # in the situation that scores is empty
    scores.append(100)
    degree.cutoff = min(scores)
    # if the cutoff mark is the default, there obviously is no cutoff
    if degree.cutoff == 100:
        degree.cutoff = '-'

# sort by the degree's code
degrees.sort(key=lambda x: x.code)

# print the degree information degree by degree
print("code,name,institution,cutoff,vacancies")

for degree in degrees:
    # determine if there are any places left or not
    if degree.places > 0:
        places = "Y"
    else:
        places = "N"

    # if there's no cutoff for the degree, don't try and format to 2 d.p
    # (that'll break the computer)
    if degree.cutoff == '-':
        cutoff = '-'
    else:
         cutoff = "{:.2f}".format(degree.cutoff)

    print(degree.code, degree.name, degree.uni, cutoff, places, sep=',')

# hacky way to resort the student list by atar, breaking ties by alphabetical ordering
final = []
scores = sorted(list(set([x.atarMark for x in students])), reverse=True)

for score in scores:
    temp = [x for x in students if x.atarMark == score]
    temp.sort(key=lambda x: x.name)
    final.extend(temp)

students = final

# print student information student by student
print("\nname,score,offer")
for student in students:
    print(student.name, "{:.2f}".format(student.atarMark), student.uni, sep=',')