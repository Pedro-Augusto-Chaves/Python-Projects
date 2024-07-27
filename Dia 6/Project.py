https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    else:
        turn_right()
        move()
    
# Não pode mover quando tiver um parade na frent
# se tiver parede na frente e a direta
# estiver livre, vire para direita
# se não parede tiver ele move

# se tiver parede na frente e a esquerda
# livre, mova para esquerda

#se o caminho não tiver parede na direita e o caminho
#estiver livre vire para esquerda

#se tiver parede na direita e na frente
#vire para esquerda

#se tiver pare na direita e a frente livre: mova


        

