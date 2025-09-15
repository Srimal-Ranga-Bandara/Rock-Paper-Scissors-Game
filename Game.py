import random

print("\n\n-----------------------  Welcome to Rock Paper Scissors  -----------------------")
print('''

██████████████████████████
█▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄███
██─▄─▄█─██─█─███▀██─▄▀████
▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
█████████████████████████████████
█▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀███
██─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
██████████████████████████████████████████████
█─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
█▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
''')

print(
"\n 1.ROCK \n 2.PAPER \n 3.SCISSORS \n  "
      )

Your_choice = int(input("Choose your option :( 1,2 or 3) "))
Computer_Choice=random.randint(1,3)
print(Computer_Choice)

#1=Rock
#2=PAPER
#3=SCISSOR
#
if Computer_Choice==1:
    if  Your_choice==1:
        print("Your Choice is : Rock ")
        print('''\n
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        ''')

        print("Computer Choice is : Rock ")
        print('''_______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            ''')

        print("GAME DROW")

    elif Your_choice == 2:
        print("Your Choice is : Paper")
        print('''\n
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
        ''')

        print("Computer Choice is : Rock ")
        print('''_______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            ''')
        print("Game Win")

    else:
        print("Your Choice is : SCISSOR ")
        print('''\n
               _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)

        ''')

        print("Computer Choice is : Rock ")
        print('''_______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            ''')

        print("Game Loss")

elif Computer_Choice==2:
    if  Your_choice==1:
        print("Your Choice is : Rock ")
        print('''\n
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        ''')

        print("Computer Choice is : Paper ")
        print('''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
            ''')

        print("GAME Loss")

    elif  Your_choice==2:
        print("Your Choice is : Paper ")
        print('''\n
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
        ''')

        print("Computer Choice is : Paper ")
        print('''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
            ''')

        print("GAME Drow")

    else:
        print("Your Choice is : SCISSOR ")
        print('''\n
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
        ''')

        print("Computer Choice is : Paper ")
        print('''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
            ''')

        print("GAME Win")
else:
    if Your_choice==1:
        print("Your Choice is : Rock ")
        print('''\n
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        ''')

        print("Computer Choice is : SCISSOR ")
        print('''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            ''')

        print("GAME Win")

    elif  Your_choice==2:
        print("Your Choice is : Paper ")
        print('''\n
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
        ''')

        print("Computer Choice is : SCISSOR ")
        print('''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            ''')

        print("GAME Loss")

    else:
        print("Your Choice is : SCISSOR ")
        print('''\n
               _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
        ''')

        print("Computer Choice is : SCISSOR ")
        print('''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            ''')

        print("GAME Drow")
















