def roll_call_dwarves(dwarves_list):
    index = 1
    for dwarve in dwarves_list:
        print(f"{index}. {dwarve}")
        index += 1

def summon_captain_planet(planeteer_calls):
    return [call.capitalize()+"!" for call in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    # return [True if len(call)>4 else False for call in planeteer_calls]
    for call in planeteer_calls:
        if len(call)>4:
            return True
    return False

def find_the_cheese(ll):
    cheese_list = ["cheddar", "gouda", "thyme"]
    for l in ll:
        if l in cheese_list:
            return l
    return None 

# l = ["Doc", "Dopey", "Bashful", "Grumpy"]
# roll_call_dwarves(l)
# print(summon_captain_planet(l))
# print(long_planeteer_calls(l))
# snacks = ["crackers", "thymne"]
# print(find_the_cheese(snacks))