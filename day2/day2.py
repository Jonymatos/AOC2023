import sys
import re

pattern = re.compile(r'(\d+) (\w+)')

def validate(games):
    def can_play(game):
        colors_limit = {'red' : 12, 'green' : 13, 'blue' : 14}
        for set_game in game:
            matches = pattern.findall(set_game)

            for amount, color in matches:
                if int(amount) > colors_limit[color]:
                    return False
                
        return True

    sum_id = 0
    for id_game, game in enumerate(games):
        if can_play(game):
            sum_id += id_game + 1

    return sum_id

def power_of_minimums(games):
    def get_minimums(game):
        minimus = {'red': None, 'green': None, 'blue': None}
        for set_game in game:
            matches = pattern.findall(set_game)

            for amount, color in matches:
                if minimus[color] is None or int(amount) > minimus[color]:
                    minimus[color] = int(amount)

        return minimus
    
    sum_minimums = 0
    for game in games:
        minimums = get_minimums(game)
        sum_minimums += (minimums['red'] * minimums['green'] * minimums['blue'])

    return sum_minimums

            
            
def main(filename):
    with open(filename) as f:
        games = [x.strip().split(':')[1].split(';') for x in f.readlines()]
        print(f'Part 1: {validate(games)}')
        print(f'Part 2: {power_of_minimums(games)}')
        

if __name__ == "__main__":
    main(sys.argv[1])