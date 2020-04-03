def say_hello(name):
    print(f'Hello {name}')

say_hello_2 = say_hello
say_hello_2('Johnny')

ENVIRONMENT = 'prod'

def fetch_data_real():
    print('Doing some very time intensive operations...')

def fetch_data_fake():
    print('Returning fake data')
    return {
        'name': 'Jane Doe',
        'age': 34
    }

fetch_data = fetch_data_real if ENVIRONMENT == 'prod' else fetch_data_fake

data = fetch_data()