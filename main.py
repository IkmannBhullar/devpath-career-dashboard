def add_application(applications):
    company = input("Enter Company Name: ")
    position = input("Enter Position: ")
    status = input("Enter Status: ")

    application = {"company": company, "position": position, "status": status}

    applications.append(application)

    print("Application added successfully!")


def view_applications(applications):

    if len(applications) == 0:
        print("No applications found")
        return

    for index, application in enumerate(applications, start=1):
        print(f"{index}. {application['company']}")
        print(f"   Position: {application['position']}")
        print(f"   Status: {application['status']}")
        print()


def main():

    applications = []

    while True:
        print("Welcome to DevPath!")

        print("1. Add Application")
        print("2. View Applications")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_application(applications)
        elif choice == "2":
            view_applications(applications)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice")


main()
