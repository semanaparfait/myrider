logo = ''' 
░██████╗░░█████╗░  ██████╗░██╗██████╗░███████╗██████╗░
██╔════╝░██╔══██╗  ██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
██║░░██╗░██║░░██║  ██████╔╝██║██║░░██║█████╗░░██████╔╝
██║░░╚██╗██║░░██║  ██╔══██╗██║██║░░██║██╔══╝░░██╔══██╗
╚██████╔╝╚█████╔╝  ██║░░██║██║██████╔╝███████╗██║░░██║
░╚═════╝░░╚════╝░  ╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝'''

print(logo)
driver_records=[]
passenger_record=[]

def add_driver():
    print("Ok Enter your cridentioals to register")
    driver_data={}
    driverregname = input("Enter your name: ")
    driverregpho = int(input("Enter your phone number: "))
    drivercarsits = int(input("Enter your sits of car: "))
    driverregpass = input("Enter your password: ")
    driver_data["name"] = driverregname
    driver_data["phone"] = driverregpho
    driver_data["car_sits"] =drivercarsits
    driver_data["password"] = driverregpass
            
    driver_records.append(driver_data)
    # print(driver_data)
    print("Driver Registered Successfully")
    


def get_passenger_info():
    while True:
        question1 = input("Do you want to continue as driver or passenger or owner: ") 
        if question1 == "passenger":
            print("Passenger Registration")
            passname = input("Enter your name: ")
            passphonenumber = int(input("Enter your phone number: "))
            passcurrentloc = input("Enter your current location: ")
            passdestination = input("Enter your destination: ")
            passenger_data = {}
            passenger_data["name"] = passname
            passenger_data["phone"] = passphonenumber
            passenger_data["current_location"] = passcurrentloc
            passenger_data["destination"] = passdestination
            passenger_record.append(passenger_data)

        elif question1 == "driver":
            driverreg=input("Are you registaded as driver yes / no: ").lower()
            if driverreg == 'yes':
                print("Ok Enter your cridentioals to log in")
                driverlogname=input("Enter you name: ")
                driverlogpass=input("Enter your password: ")
                    
                for driver in driver_records:
                    if driver["name"] == driverlogname and driver["password"] == driverlogpass:
                        print(f"\nWelcome, {driverlogname}! You have successfully logged in.")
                        for passenger_data in passenger_record:
                            for key, value in passenger_data.items():
                            # passengers_details=print(f"{key}: {value}")
                                passenger_details = f"{key}: {value}"
                            print(passenger_details)
                    #     return True
                    # elif driver["name"] != driverlogname and driver["password"] != driverlogpass :
                    #     print("OOH nigga try to check your password and name ! to continue")
                        
            elif driverreg == 'no':
                    add_driver()
        elif question1 == "owner":
            print("Enter the key word to acces the owner dashboard:")
            ownerkeyword= input("Enter the keyword to continue: ")
            if ownerkeyword == "gorider":
                print("Welcome to the owner dashboard")
                accessdriverorpass= input("Which data do you want to access for drivers or passengers: ").lower()
                if accessdriverorpass == "drivers":
                    if driver_records:
                        for data in driver_records:
                            for key, value in data.items():
                                print(f"{key}: {value}")
                elif accessdriverorpass == "passengers":
                    for passenger_data in passenger_record:
                        for key, value in passenger_data.items():
                            # passengers_details=print(f"{key}: {value}")
                            passenger_details = f"{key}: {value}"
                            print(passenger_details)
                else:
                    print("Invalid keyword! Please try again.")
                 
    

yesOrno = input("OOOOOOh welcome to go ride wanna take ride with us yes/no: ").lower()

if yesOrno == 'yes':
    # while True:
    get_passenger_info()  
elif yesOrno == 'no':
     print("Ok no problem, if you want, let me know.")
    #  break
else:
    print("Invalid choice! Please enter 'yes' or 'no'.")
    yesOrno
