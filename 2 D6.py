def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text + "\n")

def main():
    filename = "user_input.txt"
    
    while True:
        user_input = input("Enter your text (type 'stop' to end): ")
        if user_input.lower() == "stop":
            break
        append_to_file(filename, user_input)

    print(f"Your input has been saved to {filename}")

if __name__ == "__main__":
    main()
