from abc import ABC,abstractmethod
class Ride_sharing:
    def __init__(self,company_name,Location,logo) -> None:
        self.company_name = company_name
        self.employees = []
        self.Location = Location
        self.logo = logo
        self.riders = []
        self.drivers = []
    def add_riders(self,rider):
        self.riders.append(rider)
    def add_drivers(self,driver):
        self.drivers.append(driver)
    def __repr__(self) -> str:
        return f'{self.company_name} has {len(self.riders)} ans {len(self.drivers)} look lke{self.logo}'
class User(ABC):
    def __init__(self,name,email,nid,address) -> None:
        self.name=name
        self.email=email
        self.nid=nid
        self.address=address
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
class Driver(User):
    def __init__(self, name, email, nid, address,current_location) -> None:
        super().__init__(name, email, nid, address)
        self.current_location=current_location
    def display_profile(self):
        print(f'Driver name:{self.name} and email{self.email} or {self.current_location} nationality {self.nid}')

class Rider(User):
    def __init__(self, name, email, nid, address,current_location) -> None:
        self.current_ride = None
        super().__init__(name, email, nid, address)
        self.current_location = current_location
    def display_profile(self):
        print(f'Ride name is:{self.name} and {self.nid} or {self.address} ans mail {self.email}')

    def Ride_request(self,Uber,destination):
        print("--LOOKING FOR DESTINATION--")
        if not self.current_ride:
            ob = Ride_Matching(Uber.Driver)
            res = ob.has_driver(self,destination)
            print("Your result is,",res)

            self.current_ride = res
            return True
        else:
            return False
#------RIDE KORVE AKN--------
class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.Rider = None
    
    def start_rider(self):
        pass
    def end_rider(self):
        pass
    def __repr__(self) -> str:
        return f'start from:{self.start_location} destination {self.end_location}'
    
class Ride_Matching:
    def __init__(self,drivers) -> None:
        self.drivers = drivers

    def has_driver(self,rider,destination):
        if len(self.drivers) > 0:
            ride = Ride(rider.current_location,destination)
            return ride
        else:
            return "Sorry , Driver Not Found!"
        

uber = Ride_sharing("UBER","USA","GPG")
john = Driver("john_paki","jh92@yahoo.com","American","las_vegas","Bangladesh")
sakile = Rider("sakile khan","sk100@gmail.com","Barishal","Dhaka","Bangladesh")

uber.add_drivers(john)
uber.add_riders(sakile)

if sakile.Ride_request(uber,"Dhaka"):
    print("__TRAVELLING__")
else:
    print("---NO ride Found To Travel---")


