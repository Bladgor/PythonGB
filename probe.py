import json

dict_1 = "{'full_name': 'London'}"

print(dict(dict_1))


class MyClass:

    @classmethod
    def func(cls, processed):
        for elem in processed:
            return elem


print(MyClass.func(dict_1))
