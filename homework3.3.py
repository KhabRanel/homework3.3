def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = ["str", 4, False]
values_dict = {"a": 26, "b": True, "c": "python"}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [14.5, "qwerty"]
print_params(*values_list_2, 42)
