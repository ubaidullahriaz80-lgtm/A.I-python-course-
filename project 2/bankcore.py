branch_id = 2057
user_info = []

def gen_customer_id():
    user_number = len(user_info) + 1
    return f"{branch_id}-{user_number}"

def create_account(name,password):
    customer_id = gen_customer_id()
    user = [customer_id,name,password]
    user_info.append(user)
    print("account created")
    print("your customer id is",customer_id)
    return customer_id

def login(customer_id,password):
    for user in user_info:
        if user[0] == customer_id and user[2] == password:
           print("Login success")
        return True
    
    
    print("Invalid")
    return False