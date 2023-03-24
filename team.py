import datetime

class Team:
    
    
    # init menthod accepts four mandatory parameters  name,type,fee_paid,fee and two optional parameters id and date
    def __init__(self, name, type, fee_paid, fee, cancel_date="0000-00-00",id=0,date="0000-00-00"):
        
        # if id is not passed auto generator will populate the id
        if id ==0:
            self.__id = self.id_generator()
        else:
            #this will be used only when reading team records from txt file and load it to the memory 
            self.__id=id

        # if the date is not passed date will be set by datetime class
        if date=="0000-00-00":
            self.__date = datetime.date.today()
        else:
            #this will be used only when reading team records from txt file and load it to the memory 
            self.__date=date
        self.__name = name
        self.__type = type
        self.__fee_paid= fee_paid
        self.__fee= fee
        self.__cancel_date=cancel_date
    
    # getter method to get cancel date
    def get_cancel_date(self):
        return self.__cancel_date

    # setter method toset cancel date
    def set_cancel_date(self,cancel_date):
        self.__cancel_date=cancel_date
    
    # getter method to get type
    def get_type(self):
        return self.__type
    
    # this function generate unique idand store it in "id.txt" file
    def id_generator(self):
        with open("id.txt", "r") as f:
            f.seek(0)
            fc = f.readline()
            if not fc:
                with open("id.txt", "w") as f1:
                    f1.write("1")
                self.id = 1
            else:
                f.seek(0)
                fc = f.readline()
                nv = int(fc) + 1
                with open("id.txt", "w") as f2:
                    f2.write(str(nv))
                self.id = nv
        
        return self.id

    # getter method to get id
    def match(self, filter):
        return filter in self.id 
    

    # setter method to set the name
    def set_name(self,name):
        self.__name=name
    

     # getter method to get type
    def get_name(self):
        return self.__name

    # setter method to get type 
    def set_type(self,type):
        self.__type=type

    # getter method to get type
    def get_type(self):
        return self.__type
    
    # setter method to get fee  
    def set_fee(self,fee):
        self.__fee=fee

    # getter method to get fee
    def get_fee(self):
        return self.__fee
    
    # setter method to get fee_paid
    def set_fee_paid(self,fee_paid):
        self.__fee_paid=fee_paid

    # getter method to get fee_paid
    def get_fee_paid(self):
        return self.__fee_paid
    
     # getter method to get id
    def get_id(self):
        return int(self.__id)
    
    # getter method to get date
    def get_date(self):
        return self.__date
    

    # this method return string representation of the  team object 
    def __str__(self):
        return '-----------Team Information----------\n'+  'ID: ' + str(self.get_id()) + '\n'  + 'Date:' +str(self.get_date()) + '\n' +'Name: ' + str(self.get_name()) + '\n'  + 'Team Type: ' + str(self.get_type())+ '\n' + 'Fee Amount: ' + str(self.get_fee()) + '\n' + 'Fee Amount Paid: ' + str(self.get_fee_paid()) + '\n' + 'Cancellation Date:' + str(self.get_cancel_date())



  
   









    