from team import Team

class Teams:

    #initialize teams list
    def __init__(self):
        self.teams = []
        
    # append new objects to teams list
    def create_new_team(self,name, teamtype, fee_paid, fee):
       
       self.teams.append(Team(name, teamtype, fee_paid,fee))    
    
    # retrieved team records fromtxt file will be loaded as team objects to teams list
    def retrieve_team(self,name, type, fee_paid,fee,cancel_date,id,date,):
       
       self.teams.append(Team(name, type, fee_paid,fee,cancel_date,id,date))  
    
    # retuen team object matches the filter
    def search_team(self, filter):

      return [ team for team in self.teams if team.match(filter)]
    
    # return team object matches the filter
    def search_team_by_type(self, filter):

      return [ team for team in self.teams if team.get_type()==filter]
    
    # return team object matches the filter
    def search_team_by_id(self, filter):

      return [ team for team in self.teams if team.get_id()==int(filter)]
    
    # delete team object from teams list
    def delete_team_by_id(self,delteam):
      self.teams.remove(delteam)

    # returns fee paid team count
    def check_fee_paid_team_count(self,filter):
      total=0
      for team in self.teams:
         if team.get_fee_paid()==filter:
              total +=1      
      return total

    # return the team object which needed  to be  update with team name
    def upate_team_by_name(self,filter,updatename):
      name=""
      for team in self.teams:
       if team.get_id()==int(filter):
           name= team.set_name(updatename)
           print("Name sucessfully updated to : " + team.get_name())
      return name

    # return the team object which needed  to be  update with team type
    def upate_team_by_type(self,filter,updatetype):
      type=""
      for team in self.teams:
       if team.get_id()==int(filter):
           type= team.set_type(updatetype)
           print("Team type sucessfully updated to : " + team.get_type())
      return type

     # # return the team object which needed  to be  update with fee paid status
    def upate_team_by_fee_paid(self,filter,updatefeepaid):
      feepaid=""
      for team in self.teams:
       if team.get_id()==int(filter):
           feepaid= team.set_fee_paid(updatefeepaid)
           print("Fee paid status sucessfully updated to : " + team.get_fee_paid())
      return feepaid

    # return the team object which needed  to be  update with fee
    def upate_team_by_fee(self,filter,updatefee):
      fee=""
      for team in self.teams:
       if team.get_id()==int(filter):
           fee= team.set_fee(updatefee)
           print("Fee sucessfully updated to : " + team.get_fee())
      return fee
    
    # return the team object which needed  to be  update with cancellation date
    def upate_team_by_cancel_date(self,filter,updatecanceldate):
      canceldate=""
      for team in self.teams:
       if team.get_id()==int(filter):
           canceldate= team.set_cancel_date(updatecanceldate)
           print("Cancellation date sucessfully updated to : " + team.get_cancel_date())
      return canceldate
    
    # returns team object list when backup_team_info function is called
    def backup_team_info(self):
      for team in self.teams:
        return team