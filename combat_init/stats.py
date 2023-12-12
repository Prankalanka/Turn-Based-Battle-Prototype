class StatObj:
    def __init__(self, entity):
        self.entity = entity
        self.b_stats = entity.template.b_stats
        self.max_stats = {}
        self.curr_stats = {}
        self.elements = []
        self.augmenters = {}

    def update_max_stats(self):
        for key, value in self.b_stats.items():
            self.max_stats[key] = value * 1  # self.entity.arti.multipliers[key]
        print(
            f"{self.update_max_stats.__name__}: Max Stats of {self.entity.name}  {self.entity.e_index} is now {self.max_stats}"
        )

    def init_curr_stats(self):
        self.curr_stats = self.max_stats
        print(
            f"{self.init_curr_stats.__name__}: Current Stats of {self.entity.name}  {self.entity.e_index} is now {self.curr_stats}"
        )

    def update_curr_stats(
        self, aug, origin
    ):  # aug is a dict with stat name keys and integer values to change the named stat
        for key in self.curr_stats:
            if key in aug:
                self.curr_stats[key] = self.curr_stats[key] + aug[key]
        print(
            f"{self.update_curr_stats.__name__}: Current Stats of {self.entity.name}  {self.entity.e_index} is now {self.max_stats}"
        )

    def upd_status(self, origin, *args):
        self.elements.extend([*args])
        print(
            f"{self.upd_status.__name__}: Status of {self.entity.name}  {self.entity.e_index} is now {self.elements}"
        )

    def behave(self):
        for ele in self.elements:
            if ele == "Pyro":
                pass
