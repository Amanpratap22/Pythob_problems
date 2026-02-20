def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_kwargs(name="Aman", age=20, course="BTech")
