import random

class Skill:
	def __init__(self, name, atk = 0, cost = 1):
		self.name = name
		
		self.cost = cost
		self.atk = atk
		
		#handle buffs
		self.effect = {
			"atr": "atk",
			"val": "1",
			"cdw": "3", #cooldown
			"IsEnemy": True
		}

#--------------------------------------	

class Monster:
	def __init__(self, name):
		self.name = name
		
		#basic stats
		self.hp = 100
		self.atk = 1
		self.defe = 1
		self.ap = 50
		
		#powers?
		self.skills = []
		
		self.active_skills = []
		
	def applySkill(self, skill):
		
		#check if effect is still active
		for active_skill in self.active_skills:
			if active_skill.name == skill.name:
				active_skill.effect["cdw"] = skill.effect["cdw"]
				return
				
		#if here, then it is a new skill

#--------------------------------------	

class Pokemon(Monster):
	def __init__(self, name, type):
		super().__init__(name)
		
		self.type = type
		
#--------------------------------------	
		
class PokeContainer:
	def __init__(self, name, type):
		self.pokemons = []
		self.name = name
		self.type = type
		
	def randomPick(self, IsAlive = False):
		rndIndex = random.randrange(len(self.pokemons))
		return self.pokemons[rndIndex]


#belt = n pokemons
#how to: encounter system?
#how to: areas? Map?

#concept of a pikemon container
#that way, both the belt of thr uset
#and thr enguronment can contain
#pokemons and set a owner of 
#the container
####################
pokemon = Pokemon("Pikachu", "Electrical")

print(pokemon.type)

myBelt = PokeContainer("Arturs Belt", "Belt")

myBelt.pokemons.append(Pokemon("Geodude", "Earth"))

myBelt.pokemons.append(pokemon)

rndPokemon = myBelt.randomPick()

print("name = " + rndPokemon.name)
print(rndPokemon.__dict__)

rndPokemon.__dict__['atk'] = 2
rndPokemon.skills.append(Skill("Push", 10, 5))

rndPokemon.skills.append(Skill("Taunt", cost = 7))

rndPokemon.skills[1].effect = {
			"atr": "def",
			"val": "-2",
			"cdw": "3", #cooldown
			"IsEnemy": True
		}

print(rndPokemon.__dict__)

print(rndPokemon.skills[1].effect)