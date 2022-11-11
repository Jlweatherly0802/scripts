import sqlite3

conn = sqlite3.connect('mydata.db')
c = conn.cursor()

class member():
    
    count = 0

    def __init__(self, id, first, last, relation, table) -> None:
        self.id = id
        self.first = first
        self.last = last
        self.relation = relation
        self.table = table

    def info(self, result):
        self.id = result[0]
        self.first = result[1]
        self.last = result[2]
        self.relation = result[3]

    def add(self):
        c.execute('INSERT INTO {} VALUES (?, ?, ?, ?)' .format(self.table),
            (self.id, self.first, self.last, self.relation))
        member.count += 1
        conn.commit()

    def remove(self):
        c.execute('DELETE FROM {} WHERE id = {}' .format(self.table, self.id))
        print('{} {} was removed from family' .format(self.first, self.last))
        member.count -= 1
        conn.commit()

    def print_count(self):
        print('Number of people in family: {}' .format(member.count))


class dish():

    dishes = {}
    
    def __init__(self, dish_id, id, dish, person) -> None:
        self.dish_id = dish_id
        self.id = id
        self.dish = dish 
        self.person = person

    def info(self, result):
        self.dish_id = result[0]
        self.id = result[1]
        self.dish = result[2]
        self.person = result[3]

    def add(self):
        c.execute('INSERT INTO dishes_for_thanksgiving VALUES (?, ?, ?, ?)', 
        (self.dish_id, self.id, self.dish, self.person))
        dish.dishes.update({self.person: self.dish})
        conn.commit()

    def remove(self):
        c.execute('DELETE FROM dishes_for_thanksgiving WHERE id={}' .format(self.dish_id))
        try:
            del dish.dishes[self.person]
            print('{} made by {} was removed' .format(self.dish, self.person))
        except KeyError:
            print('Person not found')
        conn.commit()

    def print_dishes(self):
        print('-----This is a list of dishes for Thanksgiving-----')
        for x, y in dish.dishes.items():
            print(x,':', y)
        print('---------------------------------------------------')