class Package:
    def __init__(self, code: str, weight: float, cost_per_gram: float, description: str):
        self._code = code
        self._weight = weight
        self._cost_per_gram = cost_per_gram
        self._description = description
    
    @property
    def code(self) -> str:
        return self._code
    
    @property
    def weight(self) -> float:
        return self._weight
    
    @property
    def cost_per_gram(self) -> float:
        return self._cost_per_gram
    
    @property
    def description(self) -> str:
        return self._description
    
    def calculate(self) -> float:
        return self.weight * self.cost_per_gram


class StandardPackage(Package):
    def __init__(self, code: str, weight: float, cost_per_gram: float, description: str, flat_fee: float):
        super().__init__(code, weight, cost_per_gram, description)
        self._flat_fee = flat_fee
    
    @property
    def flat_fee(self) -> float:
        return self._flat_fee
    
    def calculate(self) -> float:
        return super().calculate() + self.flat_fee


class OverweightPackage(Package):
    def __init__(self, code: str, weight: float, cost_per_gram: float, description: str, overweight_cost: float):
        super().__init__(code, weight, cost_per_gram, description)
        self._overweight_cost = overweight_cost
    
    @property
    def overweight_cost(self) -> float:
        return self._overweight_cost
    
    def calculate(self) -> float:
        if self.weight > 1:
            return super().calculate() + (self.weight - 1) * self.overweight_cost
        else:
            return super().calculate()

class Person:
    def __init__(self, name: str, address: str, number: str):
        self._name = name
        self._address = address
        self._number = number
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def address(self) -> str:
        return self._address
    
    @property
    def number(self) -> str:
        return self._number


class Contact(Person):
    def __init__(self, name: str, address: str, number: str, email: str):
        super().__init__(name, address, number)
        self._email = email
        
    @property
    def email(self) -> str:
        return self._email


class Delivery:
    def __init__(self, package: Package, sender: Contact, recipient: Contact, delivery_address: str, delivery_date: str):
        self._package = package
        self._sender = sender
        self._recipient = recipient
        self._delivery_address = delivery_address
        self._delivery_date = delivery_date
        
    @property
    def package(self) -> Package:
        return self._package
    
    @property
    def sender(self) -> Contact:
        return self._sender
    
    @property
    def recipient(self) -> Contact:
        return self._recipient
    
    @property
    def delivery_address(self) -> str:
        return self._delivery_address
    
    @property
    def delivery_date(self) -> str:
        return self._delivery_date
    
    def calculate_total_cost(self) -> float:
        return self.package.calculate()
