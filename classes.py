class Musician(object):
     def __init__(self, sounds):
          self.sounds = sounds
     
     def solo(self, length):
          for i in range(length):
               print(self.sounds[i % len(self.sounds)], end=" ")
          print()
          
class Bassist(Musician): # The Musician class is a parent of the Bassist class
     def __init__(self):
          # Call the __init__ method of the parent class
          super().__init__(["Twang", "Thrumb", "Bling"])
          
class Guitarist(Musician):
     def __init__(self):
          # Call the __init__ method of the parent class
          super().__init__(["Boink", "Bow", "Boom"])
          
     def tune(self):
          print("Be with you in a moment.")
          print("Twoning, sproing, splang")
          
          
"""Extend the example code to add a Drummer class. Drummers should be able to
solo, count to four, and spontaneously combust."""
          
class Drummer(Musician):
     def __init__(self):
          # Call the __init__ method of the parent class
          super(Drummer, self).__init__(["Tap", "Clap", "Crash"])
          
     def count(self):
          print("One, two, three, four!")
          
     def combust(self):
          print("Boom! I spontaneously combusted!")
          
          
"""Then add a Band class. Bands should be able to hire and fire musicians, and 
have the musicians play their solos after the drummer has counted time."""
          
class Band(object):
     def __init__(self):
          self.members = {}
          
     def fire_musician(self, role):
          if role in self.members:
               del self.members[role]
     
     def hire_musician(self, role, musician):
          self.members[role] = musician
     
     def sequence(self, length):
          self.members["drummer"].count()
          for role, musician in self.members.iteritems():
               musician.solo(length)
          
if __name__ == "__main__":
     Alex = Drummer()
     James = Guitarist()
     Paul = Bassist()
     Monkeys = Band()
     Monkeys.hire_musician = ("guitarist", James)
     Monkeys.hire_musician = ("bassist", Paul)
     Monkeys.hire_musician = ("drummer", Alex)
     Monkeys.sequence(3)