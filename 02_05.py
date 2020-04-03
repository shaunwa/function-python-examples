def create_printer():
    my_favorite_number = 42

    def printer():
        print(f'My favorite number is {my_favorite_number}')

    return printer

my_printer = create_printer()
my_printer()

def create_counter():
    count = 0

    def get_count():
        return count

    def increment():
        nonlocal count
        count += 1

    return (get_count, increment)

get_count, increment = create_counter()

print(get_count())
increment()
increment()
print(get_count())
increment()
increment()
increment()
print(get_count())