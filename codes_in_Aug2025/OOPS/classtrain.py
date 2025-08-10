class train:
    def __init__(self, trainno):
        self.trainno = trainno
    
    def book(self, fro, to):
        print(f"Booked ticket from {fro} to {to}")
    
    def getstatus(self):
        print(f"Train {self.trainno} is running on time")

    def cancel(self):
        print(f"Ticket for train {self.trainno} has been cancelled")

t = train(7693)
t.book("Delhi", "Mumbai")
t.getstatus()
t.cancel()    
