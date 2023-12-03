class DriverAbsolutelyDemolishedBySingleMotherInSubaru(Exception):
    def __init__(self):
        self.message = (
            "The delivery driver has been absolutely demolished by a "
            "single mother driving a Subaru (they'll probably be fine)"
        )
        super().__init__(self.message)


class DriverAccidentallyHitAPotholeAndLaunchedThemselvesIntoOuterSpace(Exception):
    def __init__(self):
        self.message = (
            "The delivery driver accidentally hit a pothole and "
            "launched themselves into outer space (eventually they stopped thinking)"
        )
        super().__init__(self.message)


class JamaisVuDerealization(Exception):
    def __init__(self):
        self.message = (
            "The delivery driver has come to realize the futility of life"
            " and delivering tokens, and has decided to give up (on delivering"
            " this package, not on life)"
        )
        super().__init__(self.message)


class ForcedFailureError(Exception):
    def __init__(self):
        self.message = "Failure in delivery service!"
        super().__init__(self.message)
