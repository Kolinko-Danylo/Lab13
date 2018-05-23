# Implementation of the main simulation class.
from arrays import Array
from Queue.linkedqueue import LinkedQueue
from ticketcounter.passenger import TicketAgent, Passenger
import random


class TicketCounterSimulation:
    # Create a simulation object.
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        # Simulation components.
        self._passengerQ = LinkedQueue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i + 1)
        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.
    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    def _handleArrival(self, curTime):
        const_prob = random.random()
        if const_prob < self._arriveProb:
            passenger = Passenger(self._numPassengers + 1, curTime)
            self._passengerQ.add(passenger)
            self._numPassengers += 1
            print(f"Time {curTime}: Passenger {self._numPassengers} arrived.")

    def _handleBeginService(self, curTime):
        for agent in self._theAgents:
            if agent.isFree() and not self._passengerQ.isEmpty():
                passenger = self._passengerQ.pop()
                agent.startService(passenger, self._serviceTime + curTime)
                print(f"Time {curTime}: Agent {agent.idNum()} started serving Passenger {passenger.idNum()}.")

    def _handleEndService(self, curTime):
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                passenger = agent.stopService()
                self._totalWaitTime += curTime - passenger.timeArrived()
                print(f"Time {curTime}: Agent {agent.idNum()} stopped serving Passenger {passenger.idNum()}.")

    # Print the simulation results.
    def printResults(self):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("\n\n")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" % len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)

# The remaining methods that have yet to be implemented.
# def _handleArrive( curTime ): # Handles simulation rule #1.
# def _handleBeginService( curTime ): # Handles simulation rule #2.
# def _handleEndService( curTime ): # Handles simulation rule #3.



def main():
    c = TicketCounterSimulation(numAgents=20,numMinutes=100000, betweenTime=12,serviceTime=30)
    c.run()
    c.printResults()

if __name__ == "__main__":
    main()