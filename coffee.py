class Coffee:
    def __init__(self,name):
        if not isinstance(name,str):
            print("Name should be a string")
        elif not len(name) >=3:
            print("Name should be at least 3 characters long")
        else:
            self._name=name
    @property
    def name(self):
        return self._name


Mocha = Coffee("Mocha")