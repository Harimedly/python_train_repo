number=7
user_input=input('would you like to play? (y/n) ')
while user_input!='n':
    user_number=int(input('guess the number: '))
    if user_number== number:
        print('you guessed correctly')
    else:
        print('Sorry, its wrong!')

    user_input = input('would you like to play? (y/n) ')

