def print_many_times(text, times):
    for _ in range(times):
        print(text)

if __name__ == "__main__":
    print_many_times("hi", 5)
    print()

    text = "All Pythons, except one, grow up"
    times = 3
    print_many_times(text, times)