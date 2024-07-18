import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rpc = [rock,paper,scissors]

person_choice = int( input("Type 0 for Rock, 1 for Paper or 2 for Scissors: ") )
rpc_person = rpc[person_choice]

computer_choice = random.randint(0,2)
rpc_computer = rpc[computer_choice]

if person_choice == computer_choice:
    print(f"Computer choose: \n {rpc_computer} \n Draw")

elif person_choice == 0 and computer_choice == 1:
    print(f"Computer choose: \n {rpc_computer} \n You lose")

elif person_choice == 0 and computer_choice == 2:
    print(f"Computer choose: \n {rpc_computer} \n You win")

elif person_choice == 1 and computer_choice == 2:
    print(f"Computer choose: \n {rpc_computer} \n You lose")

elif person_choice == 1 and computer_choice == 0:
    print(f"Computer choose: \n {rpc_computer} \n You win")

elif person_choice == 2 and computer_choice == 0:
    print(f"Computer choose: \n {rpc_computer} \n You lose")

elif person_choice == 2 and computer_choice == 1:
    print(f"Computer choose: \n {rpc_computer} \n You win")



#se for pedra x papel = papel
#se for tesoura x papel = tesoura
#se for pedra x tesoura = pedra
#se for igual = empate
