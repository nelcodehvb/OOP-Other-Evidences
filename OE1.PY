class ml_hero():
    def __init__(self, name, role, dmg_type):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
    
    def __str__(self):
        return f"{self.name} is a/an {self.role} with a {self.dmg_type} power."
    
    def describe(self):
        return self
    
mm = ml_hero("Wanwan", "Marksman", "Physical")
mage = ml_hero("Kagura", "Mage", "Magic")
jungler = ml_hero("Guinevere", "Jungler", "Magic")
tank = ml_hero("Atlas", "Tank", "Physical")
supp = ml_hero("Floryn", "Support", "Magic")

print(f'''
MY TEAM:
{mm.name}
{mm.role}
{mm.dmg_type}
{mm.describe()}

{mage.name}
{mage.role}
{mage.dmg_type}
{mage.describe()}

{jungler.name}
{jungler.role}
{jungler.dmg_type}
{jungler.describe()}

{tank.name}
{tank.role}
{tank.dmg_type}
{tank.describe()}

{supp.name}
{supp.role}
{supp.dmg_type}
{supp.describe()}
""")