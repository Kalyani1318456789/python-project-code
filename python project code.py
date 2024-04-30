print("Welcome to the UNIT CONVERTER!")
Input = input("Please enter what you want to convert.\nTemperature (type 't') \nVolume (type 'v') \n ")


class Temperature:
    
    def _init_(self, initial, final, amount):
            self.initial = initial
            self.final = final
            self.amount = amount
    
    def unit(self):
        
        def celsius(self):
            
            if self.final == "f":
                num = self.amount * 1.8 + 32
                print(self.amount,"°C is",num,"°F.")  
            
            elif self.final == "k":
                num = self.amount + 273.15
                print(self.amount,"°C is", num,"°K.")
        
        def fahrenheit(self):
            
            if self.final == 'c':
                num = (self.amount - 32) / 1.8
                print(self.amount,"°F is ",num,"°C.")
            
            elif self.final == 'k':
                num = (self.amount + 459.67) * (5/9)
                print(self.amount,"°F is ",num,"°K.")
                
            

        def kelvin(self):
            
            if self.final == 'c':
                num = self.amount - 273.15
                print(f"{self.amount}°K is {num}°C.")
            
            elif self.final == 'f':
                num = 1.8 * (self.amount - 273) + 32
                print(f"{self.amount}°K is {num}°F.")
            
        
        if self.initial == "c":
            celsius(self)
        
        elif self.initial == "f":
            fahrenheit(self)
            
        elif self.initial == "k":
            kelvin(self)