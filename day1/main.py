import re


def main():
    total = 0
    pattern = r"(?:\d)"

    with open("input.txt") as f:
        for line in f:
            line_nums = list(re.findall(pattern, line, re.IGNORECASE))

            if len(line_nums) == 0:
                total += 0
            else:
                line_sum = (int(line_nums[0]) * 10) + int(line_nums[-1])
                total += line_sum

    print(total)


if __name__ == "__main__":
    main()
