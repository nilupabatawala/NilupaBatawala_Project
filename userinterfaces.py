import sys
from teams import Teams
import pickle


class UserInterface:

    flag=0
    def __init__(self):
      
      # instantiate new object of Teams Class
      self.teams = Teams()

      #define menu options
      self.options= {
          "1": self.create_team,
          "2": self.search_by_id,
          "3": self.search_by_type,
          "4": self.show_all_teams,
          "5": self.update_teams,
          "6": self.delete_team,
          "7": self.team_summary,
          "8": self.update_cancellation,
          "9": self.backup_team_info,
          "10": self.retrieve_team_info,
          "11": self.exit
      }

        
    #function to print main menu
    def main_menu(self):

         print("""================================"\n
           "MENU"\n
               "================================"\n
               "1 - Register New Team"\n
               "2 - View Team by ID"\n
               "3 - View Teams by Type"\n
               "4 - View All Teams"\n
               "5 - Modify Team"\n
               "6 - Delete Team"\n
               "7 - Team Summary Report"\n
               "8 - Update Cancellation Date"\n
               "9 - Backup All Teams Info"\n
               "10 - Retrieve Team Info"\n
               "11 - Exit"\n
               "================================"\n
           """) 

    # run function which invoke main menu
    def run(self):
        print("Welcome to Youth Hockey Cup Team Management System")
       # self.retrieve_team_info()
        
        while (True):

            start=input("Do you want to continue to the Main Menu?   [Y/N]  ")
            if(start =='Y'):
                self.main_menu()
                option = input("select an option: ")
                action = self.options.get(option)
                if action:
                    action()
                else:
                    print("{0} is not a valid option".format(option))
            elif (start =='N'):
                print("Thank you for using Youth Hockey Cup Team Management System")
                exit()
            else:
                print("Invalid entry")
            
    
    def create_team(self):
       
        name = input("Enter team name:  " )
        teamtype = input("Enter team type:  [boys/girls]  ")
               
        while teamtype != 'boys' and teamtype !='girls': 
            print('Enter boys or girls')
            teamtype = input('Enter team type:  [boys/girls]  ')
        
        fee_paid= input("Have the team paid the fee:    [Y/N]   ")

        while fee_paid != 'Y' and fee_paid != 'N' : 
            fee_paid = input('Have the team paid the fee:    [Y/N] ')
        
        while True:
            fee= input("Enter the fee :  ")
            try:
                fee = float(fee)       
                break;
            except ValueError:
                try:
                    float(fee)
                    break;
                except ValueError:
                    print("This is not a number. Please enter a valid number")
        
        self.teams.create_new_team(name, teamtype, fee_paid, fee)

        print("Team sucessfully created in the system")

    def delete_team(self):
        filter = input("Enter ID to Delete:  ")
        delteam = self.teams.search_team_by_id(filter)
        
        for team in delteam:
            confirm=input("Are you sure you want to delete Team   [Y/N]   ?")
            if (confirm == 'Y'):

                print(team.get_name()," will be deleted") 
                self.teams.delete_team_by_id(team)
                print("Team Sucessfully deleted")

    def search_by_id(self):
        filter = input("Enter ID:  ")
        teams = self.teams.search_team_by_id(filter)
        print(teams)
        for team in teams:
            if team == None:
                print("No ID found")
            else:
                print(team) 
    
    def search_by_type(self):
        filter = input("Enter Type:  ")
        teams = self.teams.search_team_by_type(filter)
        for team in teams:
            if team == None:
                print("No ID found")
            else:
                print(team) 

    def show_all_teams(self, teams=None):
   

        if not teams:
            teams = self.teams.teams
            for team in teams:
                print(team) 
        else:
            print("There is no teams registered in the system")

   
    def team_summary(self, teams=None):
        filter="Y"
        if not teams:
            teams = self.teams.teams
            totalteams=len(teams)
            print("Total Teams registered in  the system: " + str(totalteams))
            teamstotalcount = self.teams.check_fee_paid_team_count(filter)
            try:
                percenatge=(teamstotalcount/totalteams)*100
           
                print("Percentage of teams paid fees: " + str(percenatge)+' %')
            except:
                print("No sufficent data available in the system to generate the report")
       
    def update_teams(self):
        filter = input("Enter ID to  update:  ")
        teams = self.teams.search_team_by_id(filter)
        for team in teams:
            confirm=input("Are you sure you want to update Team   [Y/N]   ?  ")
            if (confirm == 'Y'):
                    print("Here is the current details of the system")
                    print(team)
                    newname=input("Do you want to update the name  [Y/N]  ?  ")
                    if (newname =='Y'):
                        updatename= input("Enter Name to update ?   ")
                        self.teams.upate_team_by_name(filter,updatename)
                        print("Team name updated sucessfully")

                    newtype=input("Do you want to change the type [Y/N]?  ")
                    if (newtype == 'Y'):
                        updatetype= input("Enter new type [boys/girls] ?  ")
                        self.teams.upate_team_by_type(filter,updatetype)
                        print("Team type updated sucessfully")
                
                    newfee=input("Do you want to change the fee  [Y/N] ?  ")
                    if (newfee == 'Y'):
                        updatefee= input("Enter new fee amount ?  ")
                        self.teams.upate_team_by_fee(filter,updatefee)
                        print("Team fee  updated sucessfully")

                    newfee_paid=input("Do you want to change Fee Paid Status [Y/N]  ?  ")
                    if (newfee_paid == 'Y'):
                        updatefee_paid= input("Enter new Fee paid status [Y/N]  ?  ")
                        self.teams.upate_team_by_fee_paid(filter,updatefee_paid)
                        print("Team fee paid status updated sucessfully")
    
    def update_cancellation(self):
        filter = input("Enter ID to  update cancellation date:  ")
        teams = self.teams.search_team_by_id(filter)
        print(teams)
        for team in teams:
            confirm=input("Are you sure you want to update Team   [Y/N]   ?  ")
            if (confirm == 'Y'):
                    print("Here is the current details of the system")
                    print(team)
                    cdate=input("Do you want to update cancellation date [Y/N]  ?  ")
                    if (cdate =='Y'):
                        updatecdate= input("Enter cancellation date ? [YYYY-MM-DD]   ")
                        self.teams.upate_team_by_cancel_date(filter,updatecdate)

                    
            print("Team Sucessfully update with cancellationdate")

    def backup_team_info(self, teams=None):
        file_name = 'backup_team1.txt'
        if not teams:
            teams = self.teams.teams
            with open(file_name, 'wb') as file:
           # bkp= self.teams.backup_team_info
                
                for team in teams:
                    id=team.get_id()
                    date= team.get_date()
                    name= team.get_name()
                    type= team.get_type()
                    fee= team.get_fee()
                    fee_paid= team.get_fee_paid()
                    cancel_date= team.get_cancel_date()
                    #pickle.dump(teams, file)
                    team_str= str(id) + "," + str(date) + "," + str(name) + ","+ str(type) + "," + str(fee_paid) + "," + str(fee)+ "," + str(cancel_date)
                    if team_str !="":
                        newline="\n"
                        file.write(team_str.encode())
                        file.write(newline.encode())
                print(f'Object successfully saved to "{file_name}"')

            file.close()
    
    #def retrieve_team_info(self,  teams=None):
        # open a file, where you stored the pickled data
    #    file = open('backup_team.txt', 'rb')
    #    if not teams:
    #        teams=pickle.load(file)
    #        for team in teams:
    #            print(team)
    #            self.teams.teams.append(team)
    #    file.close()
               
    def retrieve_team_info(self,  teams=None):
        if self.flag == 0:
            with open("backup_team1.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    if not currentline:
                    ##total = str(int(currentline[0]) + int(currentline[1]) + int(currentline [2])) + "\n"
                        print("no records to load")
                    else:
                        try:
                            id= str(currentline[0])
                            date=str(currentline[1])
                            name=str(currentline[2])
                            type=str(currentline[3])
                            fee_paid=str(currentline[4])
                            fee=str(currentline[5])
                            cancel_date=str(currentline[6])
                            self.teams.retrieve_team(name, type, fee_paid,fee,cancel_date,id,date)
                        except:
                            continue
            filestream.close()
            print("Team information successfully loaded into the system")
            self.flag=1
        else:
            print("Team information already loaded to  the system")

        

    def exit(self):
      print("Thank you for using Youth Hockey Cup Team Management System")
      sys.exit(0)