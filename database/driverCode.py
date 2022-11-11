import Database

conn = Database.conn
c = Database.c

# creating first table
c.execute('''CREATE TABLE family (
    id INT NOT NULL PRIMARY KEY,
    firstName VARCHAR(30),
    lastName VARCHAR(30),
    relation VARCHAR(30))
    ''')
conn.commit()

# adding members
darla = Database.member(2, 'Darla', 'Weatherly', 'mother','family')
darla.add()
rich = Database.member(3, 'Richard', 'Barnhart', 'father','family')
rich.add()
wyatt = Database.member(1, 'Wyatt', 'Weatherly', 'son','family')
wyatt.add()
kelly = Database.member(4, 'Kelly', 'Weatherly', 'sister','family')
kelly.add()
jolie = Database.member(5, 'Jolie', 'Estrada', 'sons mother','family')
jolie.add()

print('')  # added for better output 
wyatt.print_count()
print('')

# removing member 
jolie.remove()

print('')
wyatt.print_count()
print('')

c.execute('''
            CREATE TABLE dishes_for_thanksgiving(
            dish_id INT NOT NULL PRIMARY KEY,
            id INT NOT NULL REFERENCES family(id),
            dish VARCHAR(255),
            person VARCHAR(30))
            ''')
conn.commit()

# adding dishes
id2 = Database.dish(1, 2, 'turkey', 'Darla')
id2.add()
id3 = Database.dish(2, 3,'apple_pie', 'Rich')
id3.add()
id4 = Database.dish(3, 4,'ham','Kelly')
id4.add()
id5 = Database.dish(4, 5, 'potoato salad', 'Jolie')
id5.add()

print('') # added for better output
id2.print_dishes()
print('')

# remove dish from list
id5.remove()

print('')
id2.print_dishes()
print('')


conn.close()
