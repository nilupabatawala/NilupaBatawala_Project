from team import Team

class Teams:
    def __init__(self):
        self.teams = []
        

    def new_team(self,name, teamtype, fee_paid, fee):
       
       self.teams.append(Team(name, teamtype, fee_paid,fee))    
    
    def search_team(self, filter):

      return [ team for team in self.teams if team.match(filter)]
    
    def search_team_by_type(self, filter):

      return [ team for team in self.teams if team.get_type()==filter]
    
    def search_team_by_id(self, filter):

      return [ team for team in self.teams if team.get_id()==int(filter)]
    
    def search_team_by_cancellatio_date(self,filter):
     
      return [ team for team in self.teams if team.get_cancel_date()!=filter]
    
    def delete_team_by_id(self,delteam):

      self.teams.remove(delteam)

    def check_fee_paid_team_count(self,filter):
      total=0
      for team in self.teams:
        if team.get_fee_paid()==filter:
            total+=1      
      return total

    def upate_team_by_name(self,filter,updatename):
      name=""
      for team in self.teams:
       if team.get_id()==int(filter):
           print(team.get_id())
           name= team.set_name(updatename)
           print(team.get_name())
      return name

    def upate_team_by_type(self,filter,updatetype):
      type=""
      for team in self.teams:
       if team.get_id()==int(filter):
           print(team.get_type())
           type= team.set_type(updatetype)
           print(team.get_type())
      return type

    def upate_team_by_fee_paid(self,filter,updatefeepaid):
      feepaid=""
      for team in self.teams:
       if team.get_id()==int(filter):
           print(team.get_fee_paid())
           feepaid= team.set_fee_paid(updatefeepaid)
           print(team.get_fee_paid())
      return feepaid

    def upate_team_by_fee(self,filter,updatefee):
      fee=""
      for team in self.teams:
       if team.get_id()==int(filter):
           print(team.get_fee())
           fee= team.set_fee(updatefee)
           print(team.get_fee())
      return fee
    
    def upate_team_by_cancel_date(self,filter,updatecanceldate):
      canceldate=""
      for team in self.teams:
       if team.get_id()==int(filter):
           print(team.get_cancel_date())
           canceldate= team.set_cancel_date(updatecanceldate)
           print(team.get_cancel_date())
      return canceldate
    
    def backup_team_info(self):
      for team in self.teams:
        return team