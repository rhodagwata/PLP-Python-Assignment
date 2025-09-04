# OOP Assignment 1: Designing a Smartphone Store System
class Smartphone:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage
        self.is_on = False
        self.battery = 100
    
    def power_on(self):
        self.is_on = True
        return f"{self.brand} {self.model} is now ON"
    
    def power_off(self):
        self.is_on = False
        return f"{self.brand} {self.model} is now OFF"
    
    def make_call(self, number):
        if self.is_on and self.battery > 0:
            self.battery -= 5
            return f"Calling {number}..."
        return "Phone is off or battery dead!"
    
    def get_info(self):
        status = "ON" if self.is_on else "OFF"
        return f"{self.brand} {self.model} - ${self.price} | {self.storage}GB | Battery: {self.battery}% | Status: {status}"

# Inheritance (Gaming Smartphone)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, storage, cooling_system):
        super().__init__(brand, model, price, storage)
        self.cooling_system = cooling_system
        self.gaming_mode = False
    
    def activate_gaming_mode(self):
        if self.is_on:
            self.gaming_mode = True
            return f"🎮 Gaming mode activated! {self.cooling_system} cooling engaged."
        return "Turn on phone first!"
    
    def play_game(self, game_name):
        if self.gaming_mode:
            self.battery -= 15
            return f"Playing {game_name} with enhanced performance!"
        return "Activate gaming mode first!"

# Budget Smartphone
class BudgetSmartphone(Smartphone):
    def __init__(self, brand, model, price, storage):
        super().__init__(brand, model, price, storage)
        self.power_save_mode = True
    
    def make_call(self, number):  # Override - uses less battery
        if self.is_on and self.battery > 0:
            self.battery -= 2  # Uses less battery than regular phone
            return f"Calling {number} (Power save mode)"
        return "Phone is off or battery dead!"
