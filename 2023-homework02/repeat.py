def main():
    print(custom_repeater("abc", [1, 2, 3]))
    print(custom_repeater("hello", [1, 2]))
    print(custom_repeater("xyz", [0, 3]))
    print(custom_repeater("osnabrueck", [1, 2, 3, 4]))


def custom_repeater(s, pattern):
    pattern = pattern * (len(s) // len(pattern) + 1)
    return "".join([s[i] * pattern[i] for i in range(len(s))])


if __name__ == "__main__":
    main()
