class Warrior():
    attack = 15
    health = 50
    
    def real_attack(self, opp):
        return opp.attack
    
    def kick(self,war):
        war.health -= war.real_attack(self) 
    
    def is_alive(self):
        return not self.health <= 0
   
        
    def show_health(self):
        print('H: {}'.format(self.health))
    


class Konnica(Warrior):
    defence = 2
    def real_attack(self, war):
        real_attack = war.attack - self.defence
        if real_attack > 0:
            return real_attack
        return 0

class Mechnik(Warrior):
    attack = 20
    health = 40
    
class Healer (Warrior):
    attack = 3
    health = 100

def fight(war1, war2):
    kicker = war1
    receiver = war2
    while war1.is_alive() and war2.is_alive():
        kicker.kick(receiver)
        kicker, raceiver = receiver, kicker
        war1.show_health()
        war2.show_health()
        print ('battle')
    return war1.is_alive()

class Army():
    pass
    #def __init__(self, cls, amount):
        #self.units = []
        #for i in range(amount)
    
class Battle():
    pass
	
