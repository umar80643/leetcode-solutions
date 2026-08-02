class RideSharingSystem:

    def __init__(self):
        self.riders = []
        self.drivers = []

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId);

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId);

    def matchDriverWithRider(self) -> List[int]:
        if self.riders and self.drivers:
            rider = self.riders.pop(0);
            driver = self.drivers.pop(0);
            return [rider, driver]
        return []




    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riders:
            self.riders.remove(riderId);


rideSharingSystem = RideSharingSystem();
rideSharingSystem.addRider(8);

rideSharingSystem.addDriver(8);

rideSharingSystem.addDriver(6);
rideSharingSystem.matchDriverWithRider();
rideSharingSystem.addRider(2);
rideSharingSystem.cancelRider(2);
rideSharingSystem.matchDriverWithRider();

