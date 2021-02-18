class Utente:
    privilege = 0

    def __init__(self, privilege):
        self.privilege = privilege

    def get_privilege(self):
        return self.privilege


class Professore(Utente):
    seniority = 0

    def __init__(self, seniority):
        self.seniority = seniority
        super.__init__(1)

    def get_salary(self):
        return 2000 * self.seniority

    def get_privilege(self):
        return 1


class Rettore(Utente):
    seniority = 0

    def __init__(self, seniority):
        self.seniority = seniority
        super.__init__(2)

    def get_salary(self):
        return 2000 * self.seniority * 1.5

    def get_privilege(self):
        return 2


class Studente(Utente):
    isee = 0

    def __init__(self, isee):
        self.isee = isee
        super.__init__(0)

    def get_tuition(self):
        return self.isee * 3000
