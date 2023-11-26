class personne :
    #constructor
    def __init__(self , number , name ) :
        self.__number = number
        self.__name  = name

    #get and set
    def getnumber(self ):
        return self.__number
    

class stagiaire (personne):
    def __init__(self ,number,name ,note1 ,note2) :
       super() .__init__(number , name )
       self.__note1 = note1
       self.__note2 = note2

    def info(self)  :
        personne.info(self)
        print("my name:",self.__name)  
        print("my number :",self.__number)
        print("note 1 :",self.__note1)
        print("note 2 :",self.__note2)
  
    #objects
s1 =stagiaire( "sara",13 , 14 ,15,)
s1.info()
