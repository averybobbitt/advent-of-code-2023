def main():
    total = 0

    with open("input.txt") as f:
        for line in f:
            winning_nums = line.split()[2:12]
            card_nums = line.split()[13::]

            exp = -1
            for num in card_nums:
                if num in winning_nums:
                    exp += 1
            if exp > -1:
                total += pow(2, exp)

    return total


if __name__ == "__main__":
    print(main())
