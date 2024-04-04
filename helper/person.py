from helper import peopleLock, peopleDictionary, peopleWaitingForElevator, peopleInElevators

class Person():

  def __init__(self, identifier, startFloor, endFloor, timeTick):
    """Initialize the Person instance with their starting floor, which floor they want to end up on, as well as starting their waiting clock."""
    self.id = identifier
    self.startFloor = startFloor
    self.endFloor = endFloor
    self.startTime = timeTick
    self.endTime = None
    self.assignedBay = None

  def __str__(self):
    """Returns the formatted string for the personID, startFloor and endFloor."""
    return f"{self.id}|{self.startFloor}|{self.endFloor}"

  def setEndTime(self, timeTick):
    self.endTime = timeTick

  def getEndTime(self):
    return self.endTime

  def setAssignedBay(self, bay):
    self.assignedBay = bay

  def getAssignedBay(self):
    return self.assignedBay

  def getEndFloor(self):
    return self.endFloor

  def checkMatch(self, floor, bay):
    """Check if the person is on the current floor and waiting on the current bay."""
    return floor == self.startFloor and bay == self.assignedBay

  def completeJourney(self, currentTime):
    """This function is called when a person has reached their destination."""
    global peopleWaitingForElevator, peopleInElevators, peopleLock
    
    with peopleLock:
      #Remove the person from all other lists.
      try:
        peopleWaitingForElevator.remove(self.id)
      except ValueError:
        pass
      try:
        peopleInElevators.remove(self.id)
      except ValueError:
        pass

    #Move the person to the completed state and set their completed timestep.
    self.setEndTime(currentTime)
    peopleInCompletedState.append(self.id)
