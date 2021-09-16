#code for Heimdall
#Heimdall is an interactive online tool that helps secure gated communities, while also being the residents’ best friend.
# Including features such as security alerts from the community gate, community notice board, and information about the
# closest important sites (hospitals, stores, etc.) and more, Heimdall makes sure every aspect of a community's security
# and comfort is taken care of.

#importing Libraries
import string
import random
import re
import time
import datetime
from datetime import date

#Community section starts-----------------------------------------------------------------------------------------------
#Register
def Register():
    choice = int(input("\nRegister as:\n\t1. Resident \n\t2. Security Guard \n\tEnter option: "))
    if (choice == 1):
        print("\nEnter Name: ")
        name = input()

        print("\nEnter Email ID: ")
        email_ID = input()
        Email_Validation(email_ID)

        print("\nEnter Community ID: ")
        community_ID = input()

        print("\nEnter Phone Number: ")
        phone_number = int(input())
        Phone_Validation(phone_number)

        print("\nCreate Password: ")
        create_password = input()
        password_check(create_password)

        print("Confirm Password: ")
        conf_create_password = input()
        password_check(conf_create_password)

        print(
            "\nChoose three security questions:\n\t1. What was the house number and street name you lived in as a child? \n\t2. What were the last four digits of your childhood telephone number?")
        print("\t3. What primary school did you attend?")
        print(
            "\t4. In what town or city did you meet your spouse or partner? \n\t5. What is your grandmother's (on your mother's side) maiden name?")
        print(
            "\t6. In what town or city did your parents meet? \n\t7. What is your spouse or partner's mother's maiden name?")
        print(
            "\t8. What was you first pet's name? \n\t9. What are the last five digits of your driver's license number?")
        print("\t10. What time of the day were you born? (hh:mm)")
        for i in range(3):
            option1 = int(input("\nOption: "))
            answer1 = input("Enter answer:\n")
            print("\n")

    if (choice == 2):
        print("\nEnter Name: ")
        name = input()

        print("\nEnter Email ID: ")
        email_ID = input()
        Email_Validation(email_ID)

        print("\nEnter Community ID: ")
        community_ID = input()

        print("\nEnter Phone Number: ")
        phone_number = int(input())
        Phone_Validation(phone_number)

        print("\nCreate Password: ")
        create_password = input()
        password_check(create_password)

        print("Confirm Password: ")
        conf_create_password = input()
        password_check(conf_create_password)

        print(
            "\nChoose three security questions:\n\t1. What was the house number and street name you lived in as a child? \n\t2. What were the last four digits of your childhood telephone number?")
        print("\t3. What primary school did you attend?")
        print(
            "\t4. In what town or city did you meet your spouse or partner? \n\t5. What is your grandmother's (on your mother's side) maiden name?")
        print(
            "\t6. In what town or city did your parents meet? \n\t7. What is your spouse or partner's mother's maiden name?")
        print(
            "\t8. What was you first pet's name? \n\t9. What are the last five digits of your driver's license number?")
        print("\t10. What time of the day were you born? (hh:mm)")
        for i in range(3):
            option1 = int(input("\nOption: "))
            answer1 = input("Enter answer:\n")
            print("\n")
        Login()


# ----------------------------------------------------------------------------------------------------------
#Login
def Login():
    print("\n--------------- LOGIN ---------------")

    choice = int(input("\nLogin as:\n\t1. Resident \n\t2. Security Guard \n\tEnter option: "))
    if (choice == 1 or choice == 2):
        print("\nEnter Username: ")
        Username = input()

        print("\nEnter Password: ")
        password = input()
        password_check(password)

        print("\nForgot Password (Y = 1 / N = 0): ")
        forgot_password = int(input())

        if (forgot_password == 1):
            print("\nEnter registered Email-ID:")
            reg_em_id = input()
            # Heimdall sends code to email ID.
            code_sent = string.ascii_letters
            SENT_CODE = ''.join(random.choice(code_sent) for i in range(9))

            print()
            print("Your Code is: ", SENT_CODE)

            print("\nEnter code: ")
            code = input()

            # print("\nCode: ", code)
            # print("Code Sent", SENT_CODE)

            if (SENT_CODE == code):
                print("\nEnter new password: ")
                password = input()
                password_check(password)

                print("\nConfirm new password: ")
                conf_password = input()
                password_check(conf_password)

                if (password == conf_password):
                    print("\nPassword Updated.")
                    Login()
                else:
                    print("Passwords don't match.")

            else:
                print("\nWrong code. Please go again.")
                Login()

        if(choice == 1):
            print("Login Successful..........\n")
            services()


# ----------------------------------------------------------------------------------------

#Registration for community
def Community_Registration():
    Country = ['Afghanistan', 'Albania', 'Argentina', 'Australia', 'Austria', 'Bahrain', 'Bavaria', 'Belgium',
               'Bolivia', 'Brazil', 'Bulgaria', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Denmark',
               'Egypt', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'India', 'Ireland', 'Israel',
               'Italy', 'Japan', 'Mexico', 'Nepal', 'Netherlands', 'New Zealand', 'Norway', 'Peru', 'Poland',
               'Portugal', 'Russia', 'Saudi Arabia', 'Singapore', 'South Africa', 'Spain', 'Sri Lanka', 'Sweden',
               'Switzerland', 'Thailand', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Venezuela', 'Vietnam']

    print("\nWelcome to Heimdall!\n")

    print("Please enter your name:")
    community_head_name = input()

    print("\nEnter Email ID: ")
    email_ID = input()
    Email_Validation(email_ID)

    print("\nEnter Phone Number: ")
    phone_number = int(input())
    Phone_Validation(phone_number)

    print(
        "\nBy registering, you agree that:\n1. You are registering your Community on Heimdall\n2. You are the Head of your Community.\n")

    print("\nPlease enter the Country where your Community is located:")
    Community_Country = input()
    if not any(char in Country for char in Community_Country):
        print("\nWe do not provide our services in {0}, sorry.".format(Community_Country))
        exit()

    print("\nPlease enter the State where your Community is located:")
    Community_State = input()

    print("\nPlease enter the City where your Community is located:")
    Community_City = input()

    print("\nPlease enter the Region where your Community is located:")
    Community_Region = input()

    print("\nPlease enter the name of your Community:")
    Community_Name = input()

    print("\nThank you!")

    Comm_Uq_ID = string.digits
    SENT_UQ_ID = ''.join(random.choice(Comm_Uq_ID) for i in range(7))
    print("\nYour Community Unique ID is: ", SENT_UQ_ID)

    print("\nResidents of {0} must register into your community using this Community Unique ID.".format(Community_Name))

    print("\n\nThank You for Registering at Heimdall!")


# ------------------------------------------------------------------------------------------------------------------------------------------

#miscellaneous
def password_check(password):
    SpecialSym = ['$', '@', '#', '%', '!', '^', '&', '*', '(', ')']
    val = True

    if len(password) < 8:
        print('Length of password must be at least 8.')
        val = False

    if len(password) > 20:
        print('Length of password must not be greater than 20.')
        val = False

    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral.')
        val = False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter.')
        val = False

    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#%!^&*()')
        val = False

    if val:
        print("Password Accepted.")

    if val == False:
        password = input("\nEnter valid password: \n")
        password_check(password)


# ----------------------------------------------------------------------------------------

def Email_Validation(email_ID):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    Is_it_valid = True

    if (re.search(regex, email_ID)):
        print("Email is valid.")

    else:
        Is_it_valid = False
        print("\nInvalid Email. Try again:")
        email_ID = input()
        Email_Validation(email_ID)


# ----------------------------------------------------------------------------------------

def Phone_Validation(phone_number):
    string_phone = str(phone_number)

    Ph_Valid = True

    if len(string_phone) != 10:
        Ph_Valid = False
        print("\nInvalid Phone Number. Try again:")
        phone_number = int(input())
        string_phone = str(phone_number)
        Phone_Validation(string_phone)


#Community Section ends----------------------------------------------------------------------------------------




#Service Section Starts----------------------------------------------------------------------------------------
#global varaible
id = {}

#logging out
def Logout():
    print("Thank you for you time")
    print("Logging out.............")

# ----------------------------------------------------------------------------------------

#generate unique id
def GenerateID():
    global id
    resinum = input("Enter your residence number")
    genid = random.randint(0,1000)
    print("Your Id is", genid)
    id.update({genid : resinum})

# ----------------------------------------------------------------------------------------

#delete the id
def DeleteID():
    global id
    delid = int(input("Enter your ID number"))

    if delid in id:
        id.pop(delid)
    else:
        print("Incorrect Id number, Try generating first!")
        self.GenerateID()

# ----------------------------------------------------------------------------------------

#display the notice board
def NoticeBoard():
    print("                                       Heimdall Notice\n")
    print("Stay safe Stay Home!")
    time.sleep(3)
    print("A444 reported a corona +ve case")
    time.sleep(3)
    print("No issuing services allowed after 9pm as per government guidlines")

# ----------------------------------------------------------------------------------------

#services main function
def services():
    print('\n\t\t\t\t\t\t\t\t\tWelcome to the HeimDall Service Page')
    print('-------------------------------------------------------------------------------------------------------------------\n')

    ans = 1
    while(ans == 1):

        print('What do you wish to access ?')
        print("1. Logout")
        print("2. Generate ID")
        print("3. Delete ID")
        print("4. Security")
        print("5. Community Map")
        print("6. Payment")
        print("7. Community Chat")
        print("8. Notice Board")
        print("9. Online essentials")
        choice = int(input("Enter your choice of Service: "))

        print('-------------------------------------------------------------------------------------------------------------------\n')
        try:
            if choice == 1:
                Logout()
            elif choice == 2:
                GenerateID()
            elif choice == 3:
                DeleteID()
            elif choice == 4:
                security()
            elif choice == 5:
                print('-------------------------------------------------------------------------------------------------------------------\n')
                print("Community Map is under maintenance, Thank you for you Patience")
                print('-------------------------------------------------------------------------------------------------------------------\n')
            elif choice == 6:
                PaymentCommunityFunds()
            elif choice == 7:
                print("Community Chat showing both the user sides")
            elif choice == 8:
                NoticeBoard()
            elif choice == 9:
                print("This service is under making, will be there on the site soon\n")
            else:
                print("Oops this service is not mentioned here, you may post your feedback by going to choice number 4")
        except Exception:
            print("Exception occured")


        print('-------------------------------------------------------------------------------------------------------------------\n')
        if choice != 1:
            print("Do you wish to explore more into the system?")
            ans = int(input())
        else:
            ans = 0
        print('-------------------------------------------------------------------------------------------------------------------\n')

#Service section ends----------------------------------------------------------------------------



#Security Section Starts-------------------------------------------------------------------------

#for issuing complaint
def IssueComplaint():
    complaint=str(input("COMPLAINTS BEING ISSUED:"))
    print("The complaint is:",complaint)
    print("COMPLAINT IS BEING CHECKED! COMPLAINT WILL BE TAKEN CARE OF!")

# ----------------------------------------------------------------------------------------

#for posting feedback
def PostFeedback():
    feedback=str(input("Enter feedback:"))
    print("FEEDBACK IS TAKEN CARE OF:",feedback)
    print("Thank You")

# ----------------------------------------------------------------------------------------

#for approving the entry
def ApproveEntry():
    print("Entry is APPROVED!")

# ----------------------------------------------------------------------------------------

#for disapproving the entry
def DisapproveEntry():
    print("NO ENTRY!")

# ----------------------------------------------------------------------------------------

#to verify the visitor
def Visitor_verification():
    Visitor_name= str(input("Enter first name of the visitor:"))
    print("Name of visitor:", Visitor_name)
    Resident_visitorisvisting=str(input("Enter ID of the resident the visitor is going to visit:"))
    print("Resident's confirmation is waiting for entry for visitor named:", Visitor_name)
    allowing = int(input("1.Visitor is allowed. Enter '1' \n2. Visitor is NOT allowed. Enter '2' "))
    print(allowing)

    if(allowing == 1):
        ApproveEntry()

    if(allowing == 2):
        DisapproveEntry()

# ----------------------------------------------------------------------------------------

#to verify the delivery
def delivery_verification():
    Delivery_item_name= str(input("Enter name of the delivery item:"))
    print("Name of delivery item is:", Delivery_item_name)
    Resident_delivery=str(input("Enter ID of the resident the delivery is going to:"))
    print("Resident's confirmation is waiting for entry for delivery :", Delivery_item_name)
    Delivery = int(input("1.Delivery is allowed. Enter '1' \n2. Delivery is NOT allowed. Enter '2' "))
    print(Delivery)

    if(Delivery == 1):
        ApproveEntry()

    if(Delivery == 2):
        DisapproveEntry()

# ----------------------------------------------------------------------------------------

#for child safety
def child_safety():
    print("CHILD SAFETY IS VERY IMPORTANT.")
    question = int(input("1. Is the kid above 12 years of age? Enter '1' \n2. Is the kid 12 years or younger? Enter '2' "))
    print(question)

    if(question == 1):
        print("Permission to leave the gate is GRANTED!")

    if(question == 2):
        print("Have to ask parents for permission\n")
        Child_name=str(input("Enter name of child:"))
        Resident_name=str(input("Enter name of the child's parent (resident):"))
        print("ASKING FOR PERMISSION FROM PARENTS WHETHER THEIR CHILD CAN GO OUTSIDE THE GATE?\n")
        answer = int(input("1. Yes my child can go outside. Enter '1' \n2. No my child cannot go outside. Enter '2' "))
    print(answer)

    if(answer == 1):
        print("Permission to leave the gate is GRANTED!")

    if(answer == 2):
        print("Sorry Permission to leave gate is NOT granted")

# ----------------------------------------------------------------------------------------

#to print resident details
def Resident_details():
    Resident_name= str(input("Enter first name of the resident:"))
    print("Resident_name is:", Resident_name)
    Resident_id=str(input("Enter resident id:"))
    print("Resident_id is:", Resident_id)
    Resident_Phone_Number=int(input("Enter 10 digit phone number:"))
    print("Resident_Phone_Number is:", Resident_Phone_Number)
    Community_name=str(input("Enter the name of the community:"))
    print("Community_name is:", Community_name)
    Residence_number=str(input("Enter residence number:"))
    print("Residence_number is:", Residence_number)
    Resident_Login_ID=str(input("Enter the login ID:"))
    print("Resident_Login_ID is:", Resident_Login_ID)
    Resident_payment=bool(input("Enter payment:"))
    print("Resident_payment is:", Resident_payment)
    Resident_password=str(input("Enter your password:"))
    print("Resident_password is: *******")
    Resident_Email_ID=str(input("Enter your email id:"))
    print("Resident_Email_ID is:", Resident_Email_ID)

# ----------------------------------------------------------------------------------------

#security main function
def security():
    print('\n\t\t\t\t\t\t\t\t\tWelcome to the HeimDall Security Page')
    print('-------------------------------------------------------------------------------------------------------------------\n')
    option = int(input("1. Child Safety \n2. Visitor Verification \n3. Resident Details \n4. Delivery Verification \n5.Issue Complaint \n6.Post Feedback Enter option: "))
    print(option)

    if(option == 1):
        child_safety()

    if(option == 2):
        Visitor_verification()

    if(option == 3):
        Resident_details()

    if(option == 4):
        delivery_verification()

    if(option == 5):
        IssueComplaint()

    if(option == 5):
        PostFeedback()

#Security Section ends---------------------------------------------------------------------------


#Payment Section starts-------------------------------------------------------------------------

#payment main function
def PaymentCommunityFunds():
  print("\n\n\t\t-------------Welcome to Payment Menu ------------\n\n1.Make Payment\n2.Show Past Payments\n3.Post feedback\n4.Report complaint\n5.Logout")
  pchoice=int(input("\nEnter the Option : "))
  if(pchoice==1):
    print("\n\t\t   The Payment Gateway\n\t\t__________________________")
    payer=input("\nEnter the Name of payer: ")
    validate_payer(payer)
    #user can pay for Rent,Emi's,Donations,or stores nearby
    pdetails=input("Enter the Details of Payment:")
    validate_pdetails(pdetails)
    payamount=float(input("Enter the Payment amount: "))
    if(payamount<=0 ):
      print("\t\t@@Payment amount Can't be Null@@\n-----transferring to Payment Menu")
      PaymentCommunityFunds()
    pmethod=int(input("\nThe Payment Method:\n1.Net banking\n2.Debit card/Credit card\nChoose the Payment method: "))
    if(pmethod==1):
      netbanking(payamount,payer,pdetails)
    elif(pmethod==2):
      debitcreditcard(payamount,payer,pdetails)
    else:
      print("\t\t@@Invalid Method@@\n-----Transferring you to home page")
      PaymentCommunityFunds()
  elif(pchoice==2):
    print("\n\n-------------The Payment Log --------")
    fr=open("Paymentlog.txt","r")
    contents=fr.read()
    print(contents)
    fr.close()
    print("--------------------------------------------")
    PaymentCommunityFunds()
  #try to print paymentlog
  elif(pchoice==3):
    PostFeedback()
    PaymentCommunityFunds()
  elif(pchoice==4):
    IssueComplaint()
    PaymentCommunityFunds()
  elif(pchoice==5):
    #Logout()
    exit()
  else:
    print("\t\t@@Invalide Choice@@\n----Transferring you to Payment Menu")
    PaymentCommunityFunds()

# ----------------------------------------------------------------------------------------

#validation
def validate_payer(payer):
  if(payer!='' and all(char.isalpha() for char in payer)):
    return
  else:
    print("\t\t@@Invalid Entry@@\n---Transferring to Payment Menu")
    PaymentCommunityFunds()

def validate_pdetails(pdetails):
  details=['Rent','RENT','EMI','Emi','Other','Donations']
  if(pdetails!=''):
    if pdetails not in details:
      print("\t\t@@Invalid Entry@@\n----Transferring to Payment Menu")
      PaymentCommunityFunds()
    else:
      return
  else:
    print("\t\t@@Invalid Entry@@\n----Transferring to Payment Menu")
    PaymentCommunityFunds()


def validate_banklogin(username,password):
  SpecialSym =['$', '@', '#', '!']
  if all (char.isdigit() for char in username) and len(username)>=10 and len(username)<=13:
    if len(password) > 6:
      if any(char.isdigit() for char in password):
        if any(char.isupper() for char in password):
          if any(char.islower() for char in password):
            if any(char in SpecialSym for char in password):
              return True


def validate_cdetails(cardnum,edate,cvcode):
  pattern = '^[973][0-9]{15}|[973][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
  result=re.match(pattern,cardnum)
  if result:
    mm,yy=edate.split('/')
    mm=int(mm)
    yy=int(yy)
    if(mm!=0 and mm<=12):
      y=datetime.datetime.today().strftime("%y")
      m=datetime.datetime.today().strftime("%m")
      m=int(m)
      y=int(y)
      if(yy>y):
        regex = "^[0-9]{3,4}$"
        cvv = re.compile(regex)
        if(re.search(cvv, cvcode)):
          return True
      else:
        if(yy<=y and mm>m):
          regex = "^[0-9]{3,4}$"
          cvv = re.compile(regex)
          if(re.search(cvv, cvcode)):
            return True
    else:
      return False
  else:
    return False

def validate_bname(bname):
  blist=['ACB','ALB','ANB','APN','AXB','BOB','BOI','BOM','BMB'
    ,'CNB','CRB','DCB','DNB','FBL','GSC','HDFC','ICIC','HCB','HDF','ICI','IDB','INB','IOB','IIB','ING','JSB','KTB','KMB','MUC','NTB',
         'NGB','OBC','PMC','PSB','PNB','RBL','SRC','SBJ','SBH','SBI','SBM','SBP','SBT','SYB','TMB','SIB','YBL']
  if bname.isalpha():
    if bname in blist:
      return True
  else:
    print("\t\t@@Invalid Bank name@@\n------Transferring you to netbanking")
    #netbanking(payamount,payer,pdetails)

# ----------------------------------------------------------------------------------------

#to check the funds
def enoughfunds(payamount):
  bankbalance=100000
  if(bankbalance>=payamount):
    return True
  else:
    return False

# ----------------------------------------------------------------------------------------

#netbanking
def netbanking(payamount,payer,pdetails):
  print("\n\n\t----------Welcome the Net banking----------------")
  bname=input("\nEnter the Bank name :")
  if(validate_bname(bname)==True):
    loginbank(payamount,payer,pdetails,0)
    PaymentCommunityFunds()
  else:
    print("\n@@Invalid Bank name@@")
    b=int(input("To Enter the bank again Press 1- "))
    if(b==1):
      netbanking(payamount,payer,pdetails)
    else:
      PaymentCommunityFunds()

# ----------------------------------------------------------------------------------------

#login to the bank
def loginbank(payamount,payer,pdetails,c_invalidlogin):
  print("\n-----------Welcome Login Page--------------\n")
  if(c_invalidlogin>=0 and c_invalidlogin<3):
    username=input("Enter the Username: ")
    password=input("Enter the Password: ")
    if(validate_banklogin(username,password)==True):
      print("##Successfully Logged in##")
      print("\nThe payment amount is: {}".format(payamount))
      p=int(input("\nPress 1 to pay and press 0 to cancel- "))
      if(p==1 and enoughfunds(payamount)==True):
        print("\t\t@@The Payment is Successfully done@@")
        fwp=open("Paymentlog.txt","a+")
        fwp.write("\n{} - {} - {}- {} - Netbanking".format(date.today(),payer,pdetails,payamount))
        fwp.close()
        fwr=open("Reciept.txt","w")
        fwr.write("\n\t-----------------------{} Reciept-----------------------\n".format(pdetails))
        fwr.write("\n\t\tTransaction date-{}".format(date.today()))
        fwr.write("\n\t{} successfully paid the amount - {}\n\t-----------------------------------------------".format(payer,payamount))
        fwr.close()
        fw=open("Reciept.txt","r")
        cr=fw.read()
        print(cr)
        fw.close()
        c_invalidlogin=-1
        return c_invalidlogin
      elif(p==0):
        print("\t\t@@Transcation canceled@@\n------Transferring you to the home page\n")
        PaymentCommunityFunds()

      else:
        print("\t\t@@The Transaction Failed(Not Suffiecient funds or something else went wrong)@@")
        print("\nTo Try again Press 1 else 0 to exit")
        ch=int(input("\n\tPress: "))
        if(ch==1):
          netbanking(payamount,payer,pdetails)
        else:
          PaymentCommunityFunds()

    else:
      print("\t\t@@Invalid Login credentials@@")
      c_invalidlogin+=1
      loginbank(payamount,payer,pdetails,c_invalidlogin)
  else:
    print("\t\t@@Out of Tries..Please try again later after sometime@@ ")
    PaymentCommunityFunds()

# ----------------------------------------------------------------------------------------

#debit and credit card
def debitcreditcard(payamount,payer,pdetails):
  print("\n\n\t\tDebit/credit card Payment window")
  cardnum=input("\nEnter The card number(separate with (-)): ")
  edate=input("Enter the Expiry date of the card : ")
  cvcode=input("Enter the Cv code: ")
  p=int(input("Enter 1 to pay and 0 to cancel= "))
  if(p==1 and enoughfunds(payamount)==True and validate_cdetails(cardnum,edate,cvcode)==True):
    print("\t\t@@The Payment is Successfully done@@")
    fw=open("Paymentlog.txt","a+")
    fw.write("\n%s - %s - %s - %s - Debit/Credit card"%(date.today(),payer,pdetails,payamount))
    fw.close()
    fwr=open("Reciept.txt","w")
    fwr.write("\n\t-------------------{} Reciept------------------\n\t\tTansaction date-{}\n\t{} successfully paid the amount - {}\n\t---------------------------------------------- ".format(pdetails,date.today(),payer,payamount))
    fwr.close()
    fw1=open("Reciept.txt","r")
    cr=fw1.read()
    fw1.close()
    print(cr)
    PaymentCommunityFunds()

  elif(p==0):
    print("@@Transaction canceled@@\n------Transferring you to the home page\n")
    PaymentCommunityFunds()
  else:
    print("@@The Transaction Failed(Entered wrong number/Not sufficient funds/Wrong credetials)@@")
    print("\nTo Try again Press 1 else 0 to exit")
    ch=int(input("\n\tPress: "))
    if(ch==1):
      debitcreditcard(payamount,payer,pdetails)
    else:
      PaymentCommunityFunds()

#Payment section ends ----------------------------------------------------------------------------------------


#Heimdall main
print("                                                 WELCOME TO HEIMDALL!                    ")
print("#Heimdall is an interactive online tool that helps secure gated communities, while also being the residents’ best friend."
      "\nIncluding features such as security alerts from the community gate, community notice board, and information about the"
      "\nclosest important sites (hospitals, stores, etc.) and more, Heimdall makes sure every aspect of a community's security"
      "\nand comfort is taken care of.")

print("\nWhat would you like to opt?\n")
option = int(input("1. Register \n2. Login \n3. Register Community\nEnter option: "))
print(option)

if(option == 1):
    Register()

if(option == 2):
    Login()

if(option == 3):
    Community_Registration()
