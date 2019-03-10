class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = float(balance)


all_customers = []
while True:
    line = input()
    if line == 'end':
        break

    bank, name, balance = line.split(' | ')
    all_customers.append(BankAccount(name,bank, balance))

sorted_acc = sorted(all_customers,key=lambda acc : (-acc.balance,len(acc.bank)))

for acc in sorted_acc:
    print(f'{acc.name} -> {acc.balance:.2f} ({acc.bank})')