class Player:
    def __init__(self,name,health,attack,defense):
        # 初始化
        # self:創自屬於自己的變數(只存在玩家內，不用傳入值)
        self.name=name
        self.health=health
        self.attack=attack
        self.defense=defense
    def take_damage(self,damage):
        if damage>self.defense:
            self.health-=damage-self.defense
            return f'{self.name}受到{damage}點傷害'
        else:
            return f'免疫'
class Mage(Player):
    def __init__(self,name,health,attack,defense,magic_power):
        super().__init__(name,health,attack,defense)
        self.magic_power=magic_power
    def cast_spell(self):
        self.magic_power-=10
        return self.attack*1.25
class Warrior(Player):
    def __init__(self,name,health,attack,defense,armor):
        super().__init__(name,health,attack,defense)
        self.armor=armor
    def use_armor(self):
        self.health+=self.armor
        return f'{self.name}回復{self.armor}點'


# player1=Player('1',100,27,9)
# print(f'name:{player1.name}')
# print(f'health:{player1.health}')
# print(f'attack:{player1.attack}')
# print(f'defense:{player1.defense}')
# player2=Player('2',150,16,5)
# print(f'name:{player2.name}')
# print(f'health:{player2.health}')
# print(f'attack:{player2.attack}')
# print(f'defense:{player2.defense}')
# print(player2.take_damage(player1.attack))
# print(f'player2_health:{player2.health}')
player1 = Warrior("戰士小明", 100, 15, 10, 5)  # 裡面包含了Player的物件，所以可以使用Player的方法
player2 = Mage("法師小華", 80, 10, 5, 20)

print(f"{player1.name}血量剩餘: {player1.health}")
print(player1.use_armor())
print(f"{player1.name}血量剩餘: {player1.health}")

print(f"{player2.name}目前魔力: {player2.magic_power}")
player1.take_damage(player2.cast_spell())
print(f"{player2.name}對{player1.name}施放魔法攻擊！")
print(f"{player2.name}目前魔力: {player2.magic_power}")
print(f"{player1.name}血量剩餘: {player1.health}")
