# 2)	Write a new function with same functionality from Question 1, but it should be able to handle
# a Python object in addition to a dictionary from Question 1.


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person('User','1', None)
person_b = Person('User', '2', person_a)
# person_c = Person('User', '3', person_b)
# person_d = Person('User', '4', person_c)

a = {
    'key1': 1,
        'key2': {
            'key3': 1,
                'key4': {
                    'key5': 4,
                    'user': person_b,
    }
}
}

def myDict(d):
    for k,v in d.items():
        if isinstance(v,Person):
            myDict(v.__dict__)
            # v = v.__dict__
            # d[k] = v
        else:
            d[k] = v

    return d



def print_depth(data):
    new_list = [(data, list(data.keys()))]
    while len(new_list):
        dic, keys_list = new_list.pop()
        while len(keys_list):
            key, keys_list = keys_list[0], keys_list[1:]
            print(key, len(new_list) + 1)
            value = dic[key]
            if type(value) == dict:
                new_list.append((dic, keys_list))
                new_list.append((value, list(value.keys())))
                break
            elif type(value) is Person:
                all_dict = myDict(value.__dict__)
                new_list.append((dic, keys_list))
                new_list.append((all_dict, list(all_dict.keys())))

print_depth(a)