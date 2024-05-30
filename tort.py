class MyClass:
    id_counter = 0

    def __init__(self):
        self.id = MyClass.id_counter
        MyClass.id_counter += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.id < MyClass.id_counter:
            self.id += 1
            return self.id - 1
        else:
            raise StopIteration

id1 = MyClass()
id2 = MyClass()
id3 = MyClass()

for obj_id in id1:
    print(obj_id)
