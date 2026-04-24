def main():
    try:
        #ask the user input
        username = input("Enter username: ").strip()
        if not username:
            raise ValueError("Enter age: ").strip()

        age_input = input('Enter age: ').strip()
        age = int(age_input)

        if age <= 0:
            raise ValueError("Age must be a positive number. ")

        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")

    except ValueError as ve:
        print(f"Input Error: {ve}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

    finally:      
        try:
            print("\nSaved Users: ")
            with open("users.txt", "r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No users found. ")

        print("\nSystem complete.")

main()  