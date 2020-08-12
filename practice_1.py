# 1)	Write the following function’s body. A nested dictionary is passed as parameter. You need to print all keys with their depth.
# Sample Input:


a = {
    'key1': 1,
        'key2': {
            'key3': 1,
                'key4': {
                    'key5': 4,
                    'key6':{
                        'key7':8,
                        'key8':0
                    },
                    'key10':7,
                    'key11':{
                        'key22':9
                    }
    }
}
}

# Sample Output:
# key1 1
# key2 1
# key3 2
# key4 2
# so on



def print_depth(data):
    new_list = [(data, list(data.keys()))]
    # print(new_list)
    while len(new_list):
        dic, keys_list = new_list.pop()
        # print('dic_values',dic)
        # print('key_list_values',keys_list)
        while len(keys_list):
            key, keys_list = keys_list[0], keys_list[1:]
            # print(len(new_list))
            print(key, len(new_list) + 1)
            value = dic[key]
            # print(value)
            if isinstance(value, dict):
                 new_list.append((dic, keys_list))
                 new_list.append((value, list(value.keys())))
                 break

print_depth(a)
