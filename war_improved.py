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
    def __init__(self, cls, amount):
        self.units = []
        for i in range(amount):
            self.units.append(cls())
            
    def has_units(self):
        while self.units: 
            return True
        
    def get_first(self, war1, war2):
        self.war1 = self.unit1[0]
        self.war2 = self.unit2[0]
        
    
    def remove_units():
        pass
    
class Battle(Army):
    def __init__(self, army1, army2):
        self.army1 = army1
        self.army2 = army2
        
    def face_to_face_fight(self, war1, war2):
        kicker = war1
        receiver = war2
        while war1.is_alive() and war2.is_alive():
            kicker.kick(receiver)
            kicker, raceiver = receiver, kicker
            war1.show_health()
            war2.show_health()
            print ('battle')
        return war1.is_alive()
        
    def battle_fight (self):
        army1 = self.army1
        army2 = self.army2
        while army1.has_units() and army2.has_units():
            kicker = army1.get_first()
            receiver = army2.get_first()
        
        result = self.face_to_face_fight(kicker, receiver)
        
        if result:
            army2.remove_units()
        else:
            army1.remove_units()









    
#fight(Warrior(), Warrior())
my_army = Army(Warrior, 10)
my_army.has_units()