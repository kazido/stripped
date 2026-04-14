class StatusEffect:

    ON_FIRE: StatusEffect
    ETERNAL_FIRE: StatusEffect
    SILENCED: StatusEffect

    def __init__(self, statusType: str) -> None:
        self.statusType = statusType
        self.is_permanent = False
        self.is_unstackable = False
        self.turns_left = 1

    def set_unstackable(self):
        self.is_unstackable = True
        return self

    def set_permanent(self):
        self.is_permanent = True
        return self
    
    def set_duration(self, amount: int):
        self.turns_left = amount
        return self
    
    @property
    def is_expired(self) -> bool:
        return self.turns_left <= 0

    def __repr__(self) -> str:
        return f"DamageSource({self.statusType})"
    

StatusEffect.ON_FIRE = StatusEffect("on_fire").set_duration(3)
StatusEffect.ETERNAL_FIRE = StatusEffect("eternal_fire").set_permanent()
StatusEffect.SILENCED = StatusEffect("silenced").set_unstackable()