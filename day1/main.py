import re


def main():
    total = 0
    pattern = r"(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))"
    num_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    with open("input.txt") as f:
        for line in f:
            line_nums = list(re.findall(pattern, line, re.IGNORECASE))

            for i, n in enumerate(line_nums):
                if n in num_dict:
                    line_nums[i] = num_dict[n]

            if len(line_nums) == 0:
                total += 0
            else:
                line_sum = (int(line_nums[0]) * 10) + int(line_nums[-1])
                total += line_sum

    print(total)


if __name__ == "__main__":
    main()
