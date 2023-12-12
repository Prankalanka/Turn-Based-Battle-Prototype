# 1. create the team and enemy side that changes the amount depending on how many members there are (a square per person)
# 1a. each box is a side with a maximum of 8 members, they should be able to change proportions based on how many members there are. (probably set them up as fractions of the screen to be compatible with all resolutions)
import pygame, sys, time, threading
from settings import *
import combat_init.__init__ as combat_i
import combat_start.__init__ as combat_s


class Game:
    def __init__(self):
        self.screen = SCREEN
        self.clock = pygame.time.Clock()
        self.points = []

    def run(self):  # runs every frame
        while True:

            
            self.event_loop()

    
            #background layer
            self.screen.fill((0, 0, 0))

            #game layer
            self.ally_side.draw_side()
            self.enemy_side.draw_side()

            #user layer
            for ele in combat_i.cust_rects.CustomRect._registry: 
                if ele.drawing: ele.draw_mouse_lines()

            #screen update
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(FPS)

    

    #stats = ("health", "attack", "defense", "elemental mastery", "critical rate", "critical damage")
    # could make a tuple and unwrap it

    # Base Stats
    def init_stats(self):
        # might use a generator to only get the ones we need
        self.base_stats_ajax = {
            "health": 100,
            "attack": 25,
            "defense": 10,
            "elemental mastery": 5,
            "critical rate": 20,
            "critical damage": 20,
        }
        self.base_stats_xinyan = {
            "health": 100,
            "attack": 25,
            "defense": 10,
            "elemental mastery": 5,
            "critical rate": 20,
            "critical damage": 20,
        }
        self.base_stats_klee = {
            "health": 100,
            "attack": 25,
            "defense": 10,
            "elemental mastery": 5,
            "critical rate": 20,
            "critical damage": 20,
        }
        self.base_stats_fischl = {
            "health": 100,
            "attack": 25,
            "defense": 10,
            "elemental mastery": 5,
            "critical rate": 20,
            "critical damage": 20,
        }
        self.base_stats_keqing = {
            "health": 100,
            "attack": 25,
            "defense": 10,
            "elemental mastery": 5,
            "critical rate": 20,
            "critical damage": 20,
        }
        self.base_stats_slime = {
            "health": 100,
            "attack": 25,
            "defense": 10,
            "elemental mastery": 5,
            "critical rate": 20,
            "critical damage": 20,
        }
        self.base_stats_lumine = {
            "health": 100,
            "attack": 25,
            "defense": 10,
            "elemental mastery": 5,
            "critical rate": 20,
            "critical damage": 20,
        }
        self.base_stats_ganyu = {
            "health": 100,
            "attack": 25,
            "defense": 10,
            "elemental mastery": 5,
            "critical rate": 20,
            "critical damage": 20,
        }

    # Sides
    def init_sides(self):
        self.ally_side = combat_i.sides.Side(DBS, DBS)
        self.enemy_side = combat_i.sides.Side(WIDTH - DBS - self.ally_side.length, DBS)
        self.sides = [self.ally_side, self.enemy_side]

    # Moves
    def init_moves(self):
        self.water_punch = combat_i.moves.MoveTemplate(
            "Water Punch", {"health": -20, "attack": 2}, ["Hydro"], 10
        )
        self.fire_spit = combat_i.moves.MoveTemplate(
            "Fire Spit", {"health": -20, "defense": -5}, ["Pyro"], 12
        )

    # Entity Template Creation
    def init_templates(self):
        self.Ajax = combat_s.entities.EntityTemplate("Ajax", self.base_stats_ajax, self.water_punch)
        self.Pyro_Slime = combat_s.entities.EntityTemplate(
            "Pyro Slime", self.base_stats_slime, self.fire_spit
        )

    # Entity Creation
    def init_entities(self):
        self.Ajax.create(self.ally_side)
        self.Pyro_Slime.create(self.enemy_side)
        self.Ajax.create(self.ally_side)
        self.Pyro_Slime.create(self.enemy_side)
        self.Ajax.create(self.ally_side)
        self.Pyro_Slime.create(self.enemy_side)

    def tick_cd_global(self):
        self.start_time = time.time()
        while True:
            time.sleep(1)
            for item in combat_s.entities.EntityTemplate._registry:
                for ele in item.entity:
                    ele.cd_tick()

    
    def game_setup(self):
        self.init_sides()
        self.init_stats()
        self.init_moves()
        self.init_templates()
        self.init_entities()
        tick = threading.Thread(target=self.tick_cd_global)
        tick.start()



    def event_loop(self):
        for event in pygame.event.get():
                check_exit(event)
                combat_i.cust_rects.CustomRect.upd_rect(event)
                for ele in combat_i.cust_rects.CustomRect._registry: ele.check_mouse_status(event)
# checks that are run every frame

def check_exit(event):
    if event.type == pygame.QUIT:  # if there is a quit event
        pygame.quit()  # stop all pygame processes
        sys.exit()  # exit the window


if __name__ == "__main__":
    game = Game()
    game.game_setup()
    game.run()

# next steps: a ui for the users, and an ai for the enemy
# so like do a thing where the lmb is normal attacks, rmb is elemental skills, mmb is elemnental bursts
