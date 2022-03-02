import services

class client():

    def __init__(self, email, isocode,accountid,password):
        self.email = email
        self.isocode = isocode
        self.accountid = accountid
        self.password = password


    def create(self):
      try:
          a = services.frRead(self.accountid,self.isocode) 
          
          if a:
              services.frDel(a.json()['userName'],self.isocode)
           
          
          return services.registro(self.accountid, self.isocode, self.email, self.password)


      except Exception as e:
          return e 


