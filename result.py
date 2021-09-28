from StudentSet import *

class InvalidInput(Exception):
    def __init__(self,msg):
        self.msg=msg

def len_pincode(pincode):
    count=0
    while pincode>0:
        count+=1
        pincode=pincode//10
    return count

def check_avalability(pin):
    for i in Addresslist:
        if i.get_pincode()==pin:
            raise InvalidInput("this pincode is available already")
    else:
        return pin


def check_avalability_rn(rn):
    for i in studentlist:
        if i.get_rn()==rn:
            raise InvalidInput("this pincode is available already")
    else:
        return rn

def add_pincode_check(pin):
    if len_pincode(pin)>6 or len_pincode(pin)<6:
        raise InvalidInput("Pincode should be 6 digits only")
    else:
        return pin

def check_pincode(pin):
    
    flag="This city is not available please select Another pincode "
    for i in Addresslist:
        if i.get_pincode()==pin:
            flag="Available"
    if flag=="This city is not available please select Another pincode ":
        raise InvalidInput(flag)
    else:
        return pin
        

def check_String(s):
    if s.isalpha()==False:
        raise InvalidInput("Input must be alphabets only")
    else:
        return s
        
        

def check_marks(mark):
    if mark > 100 or mark <= 0:
        raise InvalidInput("Marks must not be less than zero or greater than 100")
    else:
        return mark


Addresslist=[]
studentlist=[]
while True:
    while True:
        try:
            ch=int(input("----select operation----"\
                 "\n1.Address"\
                 "\n2.Student"\
                 "\n3.Exit"\
                 "\n\nEnter your choice for operation : "))
            break
        except ValueError as e:
            print(e)
    print()
    if ch==1:
        while True:
            while True:
                try:
                    ch1=int(input("\n1.Create Address"\
                              "\n2.Update Address"\
                              "\n3.Delete Address"\
                              "\n4.Show Address"\
                              "\n5.Exit"\
                              "\n\nEnter your choice: "))
                    break
                except ValueError as e:
                    print(e)
            print()
            if ch1==1:
                while True:
                    try:
                        no_of_address=int(input("Enter no of cities u want to add : "))
                        break
                    except ValueError as e:
                        print(e)
                print()
                for i in range(no_of_address):
                    a1=Address()
                    while True:
                        try:
                            pin=check_avalability(add_pincode_check(int(input(f"Enter pincode of city {i+1} : "))))
                            break
                        except (ValueError,InvalidInput) as e:
                            print(e)
                    while True:
                        try:
                            city=check_String(input(f"Enter city {i+1} : "))
                            break
                        except InvalidInput as e:
                            print(e)
                            
                    a1.set_city(city)
                    a1.set_pincode(pin)
                    Addresslist.append(a1)
                    print()

            elif ch1==2:
                if len(Addresslist)==0:
                    print("No addresses Available ")
                else:
                    while True:
                        try:
                            pin=check_pincode(int(input("Enter pincode u want to change: ")))
                            print(type(pin))
                            break
                        except (InvalidInput) as e:
                            print(e)
                    
                    for i in Addresslist:
                        print(i.get_pincode(),i.get_city())
                        if i.get_pincode()==pin:
                            while True:
                                try:
                                    new_city=check_String(input("Enter new city name: "))
                                    break
                                except (InvalidInput) as e:
                                    print(e) 
                            i.set_city(new_city)
                    print(Addresslist)
                    print()
            elif ch1==3:
                    while True:
                        try:
                            pin=check_pincode(int(input("Enter pincode u want to delete: ")))
                            print(pin)
                            break
                        except (InvalidInput) as e:
                            print(e)
                 
                    for i in Addresslist:
                        if i.get_rn()==pin:
                            Addresslist.remove(i)
                    print()

            elif ch1==4:
                for i in Addresslist:
                    print(i)
                print()

            elif ch1==5:
                break

            else:
                print("\n Wrong choice")
                print()
                          
                            
    elif ch==2:           
        while True:
            while True:
                try:
                    ch1=int(input("1.Create Student"\
                      "\n2.Update Student"\
                      "\n3.Delete Student"\
                      "\n4.Show Student"\
                    "\n5.Show student by descending marks "\
                      "\n6.Exit"\
                    "\nEnter your choice: "))
                    break
                except ValueError as e:
                    print(e)
            print()
            if ch1==1:
                if len(Addresslist)==0:
                    a1=Address()
                    print("No cities available please add city first")
                    print()
                    while True:
                        try:
                            pin=add_pincode_check(int(input("Enter pincode of city : ")))
                            break
                        except (ValueError,InvalidInput) as e:
                            print(e)
                          
                    while True:
                        try:
                            city=check_String(input(f"Enter city : "))
                            break
                        except InvalidInput as e:
                            print(e)
                    a1.set_city(city)
                    a1.set_pincode(pin)
                    Addresslist.append(a1)
                    print(f"\n{a1.get_pincode()} {a1.get_city()} added successfully")
                    print()
                while True:
                    try:
                        no_of_students=int(input("Enter no of student u want to add: "))
                        break
                    except ValueError as e:
                        print(e)
                for i in range(no_of_students):
                    s1=Student()
                    while True:
                        try:
                            rn=check_avalability_rn(int(input("Enter Roll no: ")))
                            break
                        except (ValueError,InvalidInput) as e:
                            print(e)
                    while True:
                        try:
                            name=check_String(input("Enter Name: "))
                            break
                        except InvalidInput as e:
                            print(e)
                    while True:
                        try:
                            mark=check_marks(int(input("Enter Marks: ")))
                            break
                        except (ValueError,InvalidInput) as e:
                            print(e)
                    while True:
                        try:
                            address=check_pincode(int(input("Enter pincode: ")))
                            break
                        except (InvalidInput)  as e:
                            print(e)
                            
                    s1.set_rn(rn)
                    s1.set_name(name)
                    s1.set_marks(mark)
                    for i in Addresslist:
                        if i.get_pincode()==address:
                            s1.set_address(i)
                    print(type(s1.address))
                    print()
                    studentlist.append(s1)
                    print()
            elif ch1==2:
                if len(studentlist)==0:
                    print("No students Available ")
                    print()
                else:
                    while True:
                        try:
                            rn=int(input("Enter roll no u want to update the data: "))
                            break
                        except ValueError as e:
                            print(e)
                            
                    
                    print()
                    for i in studentlist:
                        if i.get_rn()==rn:
                            print(f"\nCurrently Avaialble information of roll no {rn}","\n",i)
                            print()
                            
                    while True:
                        while True:
                            try:
                                ch2=int(input("----select operation for student info update----"\
                                     "\n1.change name"\
                                     "\n2.change marks"\
                                     "\n3.change address"\
                                     "\n4.Exit"\
                                     "\n\nEnter your choice for operation : "))
                                break
                            except ValueError as e:
                                print(e)
                            
                        print()
                        if ch2==1:
                            new_name=check_String(input("Enter New name: "))
                            for i in studentlist:
                                if i.get_rn()==rn:
                                    i.set_name(new_name)
                            print("Name Updated Successfully\n")   
                        elif ch2==2:
                            new_mark=int(input("Enter New marks: "))
                            for i in studentlist:
                                if i.get_rn()==rn:
                                    i.set_marks(new_mark)
                            print("Marks Updated Successfully\n")   
                        elif ch2==3:
                            
                            print("Currently available cities")
                            for i in Addresslist:
                                print(i)
                            while True:
                                try:
                                    new_address=check_pincode(int(input("\nSelect pincode form Currently available cities for changing address: ")))
                                    break
                                except (InvalidInput) as e:
                                    print(e)
                            
                            for i in studentlist:
                                for j in Addresslist:
                                    if i.get_rn()==rn and j.get_pincode()==new_address:
                                        i.set_address(j)
                            print("\nAddress of student Updated Successfully \n")
                        elif ch2==4:
                            break

                        else:
                            print("Wrong Choice")
                print()
                                    
            elif ch1==3:
                if len(studentlist)==0:
                    print("No students Available ")
                else:
                    while True:
                        try:
                            rn=int(input("Enter roll no u want to update the data: "))
                            break
                        except ValueError as e:
                            print(e)
                    print()
                    for i in studentlist:
                        if i.get_rn()==rn:
                            studentlist.remove(i)
                            print(f"Deleted Successfully roll no {rn}")
                        
            
                print()

            elif ch1==4:
                if len(studentlist)==0:
                    print("No students Available ")
                else:
                    for i in studentlist:
                        print(i)
                print()


            elif ch1==5:
                marks_list=set()
                for i in studentlist:
                    marks_list.add(i.get_marks())
                    
                new_list=sorted(list(marks_list))
                
                for i in reversed(new_list):
                    for j in studentlist:
                        if i==j.get_marks():
                            print(j)

                print()

            elif ch1==6:
                break

            else:
                print("\n Wrong choice")
                
                
       
                
       
