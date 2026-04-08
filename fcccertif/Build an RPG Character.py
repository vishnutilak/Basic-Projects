def create_character(char_name, strength, intelligence, charisma):
    if not isinstance(char_name, str):
        return 'The character name should be a string'
    if char_name =='':
        return 'The character should have a name'
    if len(char_name)>10:
        return 'The character name is too long'
    if " " in char_name:
        return 'The character name should not contain spaces'
    #stats check
    if not all(isinstance(x,int) for x in (strength,intelligence, charisma)):
        return 'All stats should be integers'
    if not all(x>=1 for x in (strength, intelligence,charisma)):
        return 'All stats should be no less than 1'
    if not all(x<=4 for x in (strength, intelligence,charisma)):
        return 'All stats should be no more than 4'

    if (strength+ intelligence+ charisma)!=7:
        return 'The character should start with 7 points'
    #return statement
    full_dot = '●'
    empty_dot = '○'

    result = (
        f"{char_name}\n"
        f"STR {full_dot*strength}{empty_dot*(10-strength)}\n"
        f"INT {full_dot*intelligence}{empty_dot*(10-intelligence)}\n"
        f"CHA {full_dot*charisma}{empty_dot*(10-charisma)}"
    )
    return result
