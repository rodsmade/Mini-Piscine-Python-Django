

class Intern:
    class WorkException(Exception):
        def __init__(self, message, cause=None):
            super().__init__(message)
            self.cause = cause

    class Coffee:
        def __str__(self):
            return ("This is the worst coffee you ever tasted.")

    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return self.name

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def work_hard(self):
        raise Intern.WorkException(
            "I'm just an intern, I cannot do that much work", "I am not experienced enough")

    def make_coffee(self):
        return (Intern.Coffee())


if __name__ == "__main__":
    noFace = Intern()
    print(noFace)
    junin = Intern("Junin")
    print(junin)
    aCoffee = junin.make_coffee()
    print(aCoffee)

    try:
        junin.work()
    except Exception as e:
        print(e)

    try:
        junin.work_hard()
    except WorkException as e:
        print(e)
        print("Cause:", e.cause)
