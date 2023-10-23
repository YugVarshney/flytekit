from datetime import datetime, timedelta
i=1
while(i==1):
    now = datetime.now()
    print("Enter your date of birth (YYYY-MM-DD):")
    dob_input = input()
    birthday = datetime.strptime(dob_input, "%Y-%m-%d")
    difference = now - birthday
    age_in_years = difference.days // 365
    print(f"You are {age_in_years} years old.")
    a=int(input("Enter your choice : \n1: To Find AGE\n2: To exit\n"))
    if (a==1):
       i=1
    else : 
        i+=1
