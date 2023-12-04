import re


def is_possible(reds, greens, blues):
    for r in reds:
        if r > 12:
            return False

    for g in greens:
        if g > 13:
            return False

    for b in blues:
        if b > 14:
            return False

    return True


def main():
    sum_possible_games = 0
    sum_powers = 0

    with open("input.txt") as f:
        current_game = 0

        for game in f:
            print("*********************************")
            print(f"TESTING GAME: {game}")
            current_game += 1

            pattern = (
                "(?<=[;:]\s)(\d+\s(?:red|green|blue)(?:,\s\d+\s(?:red|green|blue))*)"
            )

            subsets = re.findall(pattern, game)
            red_subsets = [re.findall("\d+ red", x) for x in subsets]
            blue_subsets = [re.findall("\d+ blue", x) for x in subsets]
            green_subsets = [re.findall("\d+ green", x) for x in subsets]

            reds = []
            for red_subset in red_subsets:
                if red_subset:
                    reds.append(int(red_subset[0].split()[0]))
            print(f"REDS: {reds}")

            greens = []
            for green_subset in green_subsets:
                if green_subset:
                    greens.append(int(green_subset[0].split()[0]))
            print(f"GREENS: {greens}")

            blues = []
            for blue_subset in blue_subsets:
                if blue_subset:
                    blues.append(int(blue_subset[0].split()[0]))
            print(f"BLUES: {blues}")

            if is_possible(reds, greens, blues):
                print("GAME IS POSSIBLE")
                sum_possible_games += current_game
                print(f"CURRENT GAMES SUM: {sum_possible_games}")
            else:
                print("GAME IS NOT POSSIBLE")

            lowest = {"reds": max(reds), "greens": max(greens), "blues": max(blues)}
            print(f"MIN # OF CUBES REQUIRED: {lowest}")
            power = lowest["reds"] * lowest["greens"] * lowest["blues"]
            sum_powers += power
            print(f"CURRENT SUM OF POWERS: {sum_powers}")


if __name__ == "__main__":
    main()
