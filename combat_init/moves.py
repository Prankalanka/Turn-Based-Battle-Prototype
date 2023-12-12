class MoveTemplate:
    def __init__(self, name, aug, elements, cooldown):
        self.name = name
        self.aug = aug
        self.elements = elements
        self.cooldown = cooldown

    def cd_init(self, origin):
        origin.cooldowns[self.name] = 0
        print(
            f"{self.cd_init.__name__}: For {origin.name}  {origin.e_index} cooldown of {self.name} is now {self.cooldown}"
        )


class MoveObj:
    def __init__(self, template, origin, target):
        self.origin = origin
        self.target = target
        self.template = template
        self.name = template.name
        self.aug = template.aug  # multipliers will be like this:
        self.elements = template.elements
        self.cooldown = template.cooldown  # * self.origin.multipliers["cooldown"]

    def cd_reset(self):
        self.origin.cooldowns[self.template.name] = self.cooldown
        print(
            f"{self.cd_reset.__name__}: Cooldown of {self.origin.name, self.origin.e_index}\'s {self.name} is now {self.cooldown}"
        )

    def do_move(self):
        if self.origin.cooldowns[self.name] == 0:
            self.origin.upd_status_target(self.target, *self.elements)
            self.origin.aug_target(self.target, self.aug)
            self.cd_reset()
