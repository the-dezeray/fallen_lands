def set_turn(current_player_turn)->bool:
    if current_player_turn == True: 
        return False
    else:
        return True
def fight(entity = None,player = None,player_turn = True):
    print(f"you are have enter a fight  with a {entity.name}")
    while (entity.hp >= 0  or player.hp >= 0):
        if player_turn == True:
            array =player.inv.list("weapon")
            for index , item in enumerate( array):
                print(f"\n {index}. {item.name} | DMG = {item.dmg} | effect = {item.effect}")
            a = get_user_input(len(array))
            deal_damage(array[a],entity=entity)
    
        elif player_turn == False:
            deal_damage_entity(entity,player)


        player_turn = set_turn(player_turn)
class Fight():
    def __init__ (self,entity = None,player = None,player_turn = True,reward = None):
        self.entity = entity
        self.player = player
        self.player_turn = player_turn
        self.reward = reward
        self._event_loop()
    def _game_over():
        print("you have lost")
    def _player_reward():
        print("you gained xp")
    def _is_fight_over(self):
        if self.player.hp <= 0 :
            # check if resurrect is there
            self._game_over()
        if self.entity.hp <= 0 :
            self._player_reward()

                
    def _event_loop(self)->None:
        print(f"you are have enter a fight  with a {self.entity.name}")
        while (self.entity.hp >= 0  or self.player.hp >= 0):
            if self.player_turn == True:
                array =self.player.inv.list("weapon")
                for index , item in enumerate( array):
                    print(f"\n {index}. {item.name} | DMG = {item.dmg} | effect = {item.effect}")
                a = get_user_input(len(array))
                deal_damage(array[a],entity=self.entity)
        
            elif self.player_turn == False:
                deal_damage_entity(self.entity,self.player)

            self._is_fight_over()
            self.player_turn = set_turn(self.player_turn)


def deal_damage(weapon,entity)-> None:
    entity.hp -= weapon.dmg
    print(f"\n You have done {weapon.dmg} damgae  their current health ENEMY HP = {entity.hp}")
def deal_damage_entity(entity,player):
        player.hp -= entity.dmg
        print(f"\n {entity.dmg} damgae  as afflicted on you your current HP = {player.hp}")
def get_user_input(available_choices):
    
    ass = input("enter an option ")
    print(f"this is {ass}")
    user_input = int(ass)
    if user_input > available_choices -1:
        print(f"value not in the list of given options enter a number from 0 to {available_choices}")
        return get_user_input(available_choices)
    return user_input
