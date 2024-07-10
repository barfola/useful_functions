def is_number_in_range(number, start, stop):
    return start <= number <= stop


def get_number_from_user(message_to_user):
    while True:
        try:
            number = int(input(message_to_user))
            break

        except ValueError:
            print(f'Input must be a number!!!')

    return number


def get_number_in_range(massage_to_user, start_of_range, end_of_range):
    while True:
        number = get_number_from_user(message_to_user=f'{massage_to_user} (range is {start_of_range}-{end_of_range}) : ')

        if is_number_in_range(start_of_range, end_of_range, number) is True:
            break

        print(f'Price must be in range of {start_of_range}-{end_of_range} !!!')

    return number