import math


def do_turn(pw):
    num_ships = 0
    source = 0
    dest = 0
    if len(pw.my_planets()) == 0:
        return
    if len(pw.neutral_planets()) >= 1:
        num_ships = 10000
        for i in pw.neutral_planets():
            if(i.num_ships() < num_ships):
                dest = i
                num_ships = i.num_ships()

    if len(pw.enemy_planets()) >= 1:
        for i in pw.enemy_planets():
            if(i.num_ships() < num_ships):
                dest = i
                num_ships = i.num_ships()
    for i in pw.my_planets():
        if(dest.owner == 2):
            if(i.num_ships() > dest.num_ships() + dest.growth_rate()): 
                source = i
                num_ships = dest.num_ships() + dest.growth_rate()
        else:
            if(i.num_ships() > dest.num_ships()+1):
                source = i
                num_ships = dest.num_ships() + 1
    if source == 0:
        source = pw.my_planets()[0]
    if dest==0:
        dest = pw.neutral_planets()[0]
        num_ships = source.num_ships()-1
    pw.issue_order(source,dest,num_ships)
