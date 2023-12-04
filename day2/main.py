import re


def is_possible(game):
    pattern = "(?<=[;:]\s)(\d+\s(?:red|green|blue)(?:,\s\d+\s(?:red|green|blue))*)"

    subsets = re.findall(pattern, game)
    red_subsets = [re.findall("\d+ red", x) for x in subsets]
    blue_subsets = [re.findall("\d+ blue", x) for x in subsets]
    green_subsets = [re.findall("\d+ green", x) for x in subsets]

    reds = []
    for red_subset in red_subsets:
        if red_subset:
            reds.append(int(red_subset[0].split()[0]))
    print(f"REDS: {reds}")

    for r in reds:
        if r > 12:
            return False

    greens = []
    for green_subset in green_subsets:
        if green_subset:
            greens.append(int(green_subset[0].split()[0]))
    print(f"GREENS: {greens}")

    for g in greens:
        if g > 13:
            return False

    blues = []
    for blue_subset in blue_subsets:
        if blue_subset:
            blues.append(int(blue_subset[0].split()[0]))
    print(f"BLUES: {blues}")

    for b in blues:
        if b > 14:
            return False

    return True


def main():
    result = 0

    with open("input.txt") as f:
        current_game = 0

        for game in f:
            print("*********************************")
            print(f"TESTING GAME: {game}")
            current_game += 1

            if is_possible(game):
                print("GAME IS POSSIBLE")
                result += current_game
                print(f"CURRENT TOTAL: {result}")
            else:
                print("GAME IS NOT POSSIBLE")

    print(result)


if __name__ == "__main__":
    main()
