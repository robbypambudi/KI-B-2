# Author : Robby Ulung Pambudi


import DES

class Server:
  def __init__(self):
    self.key = '12345678'
    self.des = DES(self.key)