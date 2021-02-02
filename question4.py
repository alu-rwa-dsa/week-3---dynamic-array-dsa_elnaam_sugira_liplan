
a_list = dict()

class our_list:
    def __init__(self):

        print("Hello")

    def add(self, name, age, major, country):
        a_list["name"] = name
        a_list["age"] = age
        a_list["Faculty"] = faculty
        a_list["country"] = country
        return a_list

    def a_remove(self, key):
        del a_list[key]
        return a_list

    def a_modify(self, name, major, country):
        a_list.update({"name":name})
        a_list.update({"Faculty": faculty})
        a_list.update({"country":country})
        return a_list

    def a_lookup(self, i):
        for key in a_list.keys():
            if key == i:
                return "found"
            else:
                return "not found"


if __name__ == "__main__":
    p = our_list()

    print(p.add("Umutoni", 20, "CS", "Rwanda"))

    print(p.a_remove("Faculty"))

    print(p.a_modify("Liplan", "CS", "GC"))

    print(p.a_lookup("name"))



