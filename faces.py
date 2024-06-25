def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    x = input()
    c = convert(x)
    print(c)

if __name__ == "__main__":
    main()
