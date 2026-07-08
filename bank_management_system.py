
def create_account(account,name,age,guardian_name=None):
    
   account_number=generate_account_number(account)
   account[ account_number]={
        "name":name,
        "age":age,
        "balance":0,
        "history":[]
   }
   if age >=18:
     
    print(f"your account no:{account_number}")
    print("------------------------------")
    print("      ACCOUNT CARD ")
    print("------------------------------")
    print(f"Name          :{name}")
    print(f"Age           :{age}")
    print(f"Account type  :Personal")
    print(f"Account Number:{account_number}")
    print("-------------------------------")
    
    return "Congratulations! Your account has been created successfully."
   else:
    print(f"your account no:{account_number}")
    print("------------------------------")
    print("      ACCOUNT CARD ")
    print("------------------------------")
    print(f"Name          :{name}")
    print(f"Age           :{age}")
    print(f"guardian      :{guardian_name}")
    print(f"Account type  :Joint")
    print(f"Account Number:{account_number}")
    print("-------------------------------")   
    return "Congratulations! Your account has been created successfully."    
     
 
    

def deposit(account,account_number,deposit_amount):
     
    deposit_amount=int(deposit_amount)
 
   
    account[account_number]["balance"]+=(deposit_amount)
    account[account_number]["history"].append(f"deposit ₹{deposit_amount}")
    return "amount deposited"
    
    

def withdraw(account,account_number,withdraw_amount):
    
 
    withdraw_amount=int(withdraw_amount)
    if account[account_number]["balance"]<=0 or withdraw_amount>account[account_number]["balance"]:
        return "Insufficient balance"
 
    account[account_number]["balance"]-=withdraw_amount
    account[account_number]["history"].append(f"withdraw ₹{withdraw_amount}")
    return "Amount withdrawn"
    
    

def transfer(account,from_account,to_account,amount):
    amount=int(amount)
    if account[from_account]["balance"]<=0 or amount>account[from_account]["balance"]:
        return "Insufficient balance"
    account[from_account]["balance"]-=amount
    account[to_account]["balance"]+=amount
    account[from_account]["history"].append(f"₹{amount} debited to {to_account}")
    account[to_account]["history"].append(f"₹{amount} credited from account:{from_account}")
                                          
    return "amount transferred"

def balance_enquiry(account,account_number):
 
    balance_in=f"""
    ================================================
                 BALANCE CHECK
    ================================================
    
    Account Holder  :{account[account_number]["name"]}
    Account Number  :{account_number} 
    
    --------------------------------------------------
    Balance        :₹{account[account_number]["balance"]}.00
    --------------------------------------------------
    """
    print(balance_in)
    return True
    

def transaction_history(account,account_number):
    
    print("="*35)
    print("     Transaction History       " )
    print("="*35)
    # print("Transaction          Amount")
    for transaction in account[account_number]["history"]:
        print(transaction)
    return True

def delete_account(account,account_number):
 
    if account[account_number]["balance"]>0:
        return f"""Cannot delete account......
    Please withdraw or transfer the remaining balance first........."""
    del account[account_number]
    return "Account deleted successfully."
    

def display_accounts(account):
    if len(account)==0:
        return  False
 
    print("----------------------------------------------------")
    print("Name               Account No      Balance")
    print("----------------------------------------------------")
    for account_number in account:
        print(f'{account[account_number]["name"]:<20}{account_number:<15}₹{account[account_number]["balance"]}')
    print("----------------------------------------------------")
    return True
    
    
    
    
 
def generate_account_number(account):
      global next_account
      while next_account in account:
          next_account=str(int(next_account)+1)
      return next_account
      
       
        

def is_valid_amount(amount):
    if  not amount.isdigit()  and (amount)!="0" :
        
        return  False
    return True 
 
     

def  is_account_exists(account,account_number):
   
    if account_number not in account:
        return False
    return  True
       
next_account="1001"

accounts={
          "1001":{"name":"MallikaErpula","age":20,"balance":50000,"history":["deposit ₹50000"]},
          "1003":{"name":"rebca","age":19,"balance":1000000000,"history":["deposited ₹1000000000"]}
    }
# accounts={}
menu=f"""
1.create account
2.deposit money
3.withdraw money
4.Transfer money
5.Check balance
6.Transaction History
7.Delete account
8.Display account
9.exit
"""

choice=''
while choice!="9":
    print(menu)
    choice=input("enter your choice:")
    if choice=="1":
        first_name=input("enter your first name:").capitalize()
        last_name=input("enter last name if exists:").capitalize()
        name=first_name+last_name
        age=input("enter your age:")
        if age.isdigit() and age!="0" :
            if int(age)>=18:
             print(create_account(accounts,name,int(age)))
            elif int(age)<18:
                guardian_name=input("enter your guardian name:")
                print(create_account(accounts,name,int(age),guardian_name))
        else:
            print("enter valid age")
  
    elif choice=="2":
      if len(accounts)>=1:
        while True:
            account_num=input("account number:")
             
            if  not is_account_exists(accounts, account_num,):
              print("account not found")
            else:   
                
               while True:
                amount=input("enter amount:")
                if not is_valid_amount(amount):
                    print("enter valid amount")
                else:
                    
                    break
 
               break
        print(deposit(accounts,account_num,amount))
      else:
              print("no account holders")
      
 
    elif choice=="3" :
      if len(accounts)>=1:   
        while True:
            account_num=input("account number:")
            if  not is_account_exists(accounts, account_num,):
               print("account not found")
            else:   
              
               while True:
                amount=input("enter amount:")
                if not is_valid_amount(amount):
                     print("enter valid amount")
                else:
                    break
 
               break
 
        print(withdraw(accounts,account_num,amount))
      else:
          print("no account holders")
    elif choice=="4":
      if len(accounts)>=2:
        while True:
            sender_num=input("enter sender account number:")
            if not is_account_exists(accounts,sender_num):
                print("sender not found")
            else:
                while True:
                    receiver_num=input("enter receiver number:")
                    if not is_account_exists(accounts,receiver_num) or  sender_num==receiver_num: 
 
                       
                         print("receiver not found")
                    else:
                        while True:
                           amount=input("enter amount:")
                           if not is_valid_amount(amount):
                             print("enter valid amount")
                           else:
                               break
                        break
                break
        print(transfer(accounts,sender_num,receiver_num,amount))
      else:
          print("not enough account holders")
    elif choice=="5":
      if  len(accounts)>=1:
        while True:
            account_num=input("enter account number:")
            if not is_account_exists(accounts,account_num):
                print("account not found")
            else:
                break
        if balance_enquiry(accounts,account_num):
          print()
      else:
           print("not enough account holders")
    elif choice=="6":
        if len(accounts)>=1:
          while True:
            account_num=input("enter account number:")
            if not is_account_exists(accounts,account_num):
                print("account not found")
            else:
                break
          if transaction_history(accounts,account_num):
                print()
        else:
            print("no account holders")
    elif choice=="7":
       if len(accounts)>=1:
          while True:
            account_num=input("enter account number:")
            if not is_account_exists(accounts,account_num):
                print("account not found")
            else:
                print(delete_account(accounts,account_num))
                break   
       else:
            print("no account holders")
    
    elif choice=="8":
         if display_accounts(accounts):
             print()
         else:
            print("no accounts........get customers")
    elif choice=="9":
        print("signing out")
    else:
        print("Invalid choice")                   
        
 
 
 
 
 