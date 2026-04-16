class Status:

    ON_FIRE: Status
    ETERNAL_FIRE: Status
    SILENCED: Status

    def __init__(self, statusType: str) -> None:
        self.statusType = statusType
        self.is_permanent = False
        self.is_unstackable = False
        self.duration = 1

    def set_unstackable(self):
        self.is_unstackable = True
        return self

    def set_permanent(self):
        self.is_permanent = True
        return self
    
    def set_duration(self, amount: int):
        self.duration = amount
        return self

    def __repr__(self) -> str:
        return f"Status({self.statusType})"
    

Status.ON_FIRE = Status("on_fire").set_duration(3)
Status.ETERNAL_FIRE = Status("eternal_fire").set_permanent()
Status.SILENCED = Status("silenced").set_unstackable()


class StatusEffect:

    def __init__(self, status: Status) -> None:
        self.status = status
        self._turns_remaining = status.duration

    def tick(self) -> None:
        """Decreases turns remaining by 1, unless the effect is permanent."""
        if not self.status.is_permanent:
            self._turns_remaining -= 1

    @property
    def turns_remaining(self) -> int:
        return self._turns_remaining

    @property
    def is_expired(self) -> bool:
        return self._turns_remaining <= 0
    
    def __repr__(self) -> str:
        return f"{self.status.statusType}: {self.turns_remaining}"