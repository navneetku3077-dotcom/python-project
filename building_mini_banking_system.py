accounts = []


def find_account(name: str):  # created a function name find accounts
    for account in accounts:
        if account['name'].lower() == name.lower():
            return account
    return None


def create_account(name: str, intial_balance: float):
    if intial_balance < 0:
        raise ValueError('intial balance must be greater than zero')
    # check duplicate account name
    if find_account(name):
        raise ValueError('an account with this name already exists')
    # create a dic for the account
    account = {
        'name': name,
        'balance': intial_balance,
        'transactions': []
    }
    # add account to the list
    accounts.append(account)
    return account

# deposit


def deposit(name: str, amount: int):
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than 0.")

    account = find_account(name)

    if not account:
        raise ValueError("Account not found.")

    account["balance"] += amount

    account["transactions"].append({
        "type": "Deposit",
        "amount": amount
    })

    return account["balance"]


def withdraw(name: str, amount: float):
    if amount <= 0:
        raise ValueError('withraw amount must be greater than zero')
    account = find_account(name)
    if not account:
        raise ValueError('account not found')
    if amount > account['balance']:
        raise ValueError('insufficient fund')
    account['balance'] -= amount
    account['transactions'].append(
        {'type': 'withdrawal', 'amount': amount}
    )
    return account['balance']

# show account summary


def show_account(name: str):
    account = find_account(name)
    if not account:
        print('account not found')
        return
    print(f'account summary for {account['name']}')
    print(f'current balance:${account['balance']}')
    print('transactions:')
    if not account['transactions']:
        print('no transactions yet')
    else:
        for transaction in account['transactions']:
            print(f'-{transaction['type']}:${transaction['amount']}')

# testing section


def run_tests():
    try:
        create_account('Navneet', 1000)
        deposit('navneet', 100)
        withdraw("navneet", 150)
        withdraw("navneet", 2000)  # Overdraft test

    except ValueError as error:
        print("Error:", error)

    show_account("navneet")
run_tests()

