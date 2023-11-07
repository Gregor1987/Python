def guessing_game(number):
    def attempts(attempts_number):
        for _ in range(attempts_number):
            guess = int(input('input number'))
            if guess == number:
                print('correct')
                return
            elif guess > number:
                print('lower')
            else:
                print('greater')
    return attempts


guessing_game(100)(10)