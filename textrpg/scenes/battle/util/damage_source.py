class DamageSource:

    GENERIC: DamageSource
    FIRE: DamageSource
    DIVINE: DamageSource

    def __init__(self, damageType: str) -> None:
        self.damageType = damageType
        self.is_unblockable = False
        self.is_fire_damage = False

    def set_fire_damage(self):
        self.is_fire_damage = True
        return self
    
    def set_unblockable(self):
        self.is_unblockable = True
        return self
    
    def __repr__(self) -> str:
        return f"DamageSource({self.damageType})"
    

DamageSource.GENERIC = DamageSource("generic")
DamageSource.FIRE = DamageSource("fire").set_fire_damage()
DamageSource.DIVINE = DamageSource("divine").set_unblockable()