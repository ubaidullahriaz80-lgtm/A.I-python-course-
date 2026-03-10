import bankcore
import accounts


def main():

    print("Welcome to ABC Bank")

    while True:

        print("\n1. Create an account")
        print("2. Login to account")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':

            name = input("Enter your name: ")
            password = input("Create password: ")

            bankcore.create_account(name, password)


        elif choice == '2':

            customer_id = input("Enter Customer ID: ")
            password = input("Enter Password: ")

            if bankcore.login(customer_id, password):

                while True:

                    print("\n--- Banking Menu ---")
                    print("1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Logout")

                    option = input("Enter option: ")

                    if option == '1':

                        balance = accounts.check_balance(customer_id)
                        print("Your balance is:", balance)

                    elif option == '2':

                        amount = float(input("Enter amount to deposit: "))
                        accounts.deposit(customer_id, amount)

                    elif option == '3':

                        amount = float(input("Enter amount to withdraw: "))
                        accounts.withdraw(customer_id, amount)

                    elif option == '4':

                        print("Logged out successfully")
                        break

                    else:
                        print("Invalid option")


        elif choice == '3':

            print("Thank you for using Ab Bank")
            break

        else:
            print("Invalid choice")


main()