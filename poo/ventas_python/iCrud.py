from abc import ABC, abstractmethod

class ICrud(ABC):
 
    @abstractmethod    
    def create():
        pass
    @abstractmethod   
    def update():
        pass
    @abstractmethod 
    def delete():
        pass
    @abstractmethod 
    def consult():
        pass