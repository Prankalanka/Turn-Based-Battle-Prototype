from combat_init import moves, cust_rects, stats

class EntityTemplate:
    _registry = []

    def __init__(self, name, stats, moves):
        self._registry.append(self)
        self.entity = []
        self.entity_amt = 0
        self.name = name
        self.b_stats = stats
        self.b_moves = moves # make normal attack, elemental skill, and elemental burst

    
    def create(self, side):
        # we gotta create instances of this member template
        # im thinking we do smthn like: Ajax.entity[0].rect
        prev_entity = Entity(self, side, None)
        prev_entity.full_init()
        self.entity_amt += 1

        side.members.append(prev_entity)
        side.member_amt += 1
        print(prev_entity)


class Entity:
    _registry = []
    def __init__(self, template, side, artifact):
        self.template = template
        self.name = template.name
        self.b_stats = template.b_stats
        self.b_moves = template.b_moves 
        self.side = side
        self.arti = artifact
        self.moves = {}  # holds template moves
        self.cooldowns = {}  # holds template moves
        self.aff_move = None
        self.template.entity.append(self)
        self.e_index =  self.template.entity.index(self)
        Entity._registry.append(self)
        self.rect = cust_rects.CustomRect(self)
        self.stat_obj = stats.StatObj(self)

    def typeof(self):
        print(self.template.name)

    def upd_status_target(self, target, *args):
        target.stat_obj.upd_status(self, *args)

    def aug_target(self, target, aug):
        target.stat_obj.update_curr_stats(aug, self)

    def do_move(self, t_move, target):
        move = moves.MoveObj(t_move, self, target)
        move.do_move()
        del move

    def add_move(self, *args):
        int_to_move = {0 : "Normal Attack", 1 : "Elemental Skill", 2 : "Elemental Burst"}
        for count, value  in enumerate(args):
            print(f"{self.name} : {value}")
            self.moves[int_to_move[count]] = value
            value.cd_init(self)
        print(f"{__name__}: Moves of {self.name} {self.e_index} is now {self.moves}")

    def full_init(self):
        self.stat_obj.update_max_stats()
        self.stat_obj.init_curr_stats()
        self.stat_obj.behave()
        self.add_move(self.b_moves)

    def cd_tick(self):
        for key, value in self.cooldowns.items():
            if self.cooldowns[key] > 0:
                self.cooldowns[key] -= 1
            if self.cooldowns[key] < 0:
                self.cooldowns[key] = 0
        # print(f"{self.cd_tick.__name__}: Cooldowns of {self.name} is now {self.cooldowns}")]

    def if_rect_affected(self, affector):
        if self.rect.affected:
            self.aff_move = affector.moves["Normal Attack"]
            if self.rect.lmb:
                self.aff_move = affector.moves["Normal Attack"]
            if self.rect.mmb:
                self.aff_move = affector.moves["Elemental Burst"]
            if self.rect.rmb:
                self.aff_move = affector.moves["Elemental Skill"]   
            affector.do_move(self.aff_move, self)
                
