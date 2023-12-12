import pygame, threading
from settings import*

class CustomRect(
    pygame.Rect
):  # probably all parts of the gui can be custom rects (just inheriting the rect class)
    _registry = []
    _last_rect_held = None

    def __init__(self, origin):
        super().__init__(0, 0, 0, 0)
        self.origin = origin
        self.colour = (255, 255, 255)
        self.hovered = False
        self.held = False
        self.affected = False
        self.thread_name = "".join( [self.origin.name, str(self.origin.e_index)] )
        self.aff_thread = threading.Thread(name = self.thread_name )
        self.curr_threads = []
        # self.tags = [] # we can tag them with different properties like being part of the battle gui, or map gui
        self.lmb, self.mmb, self.rmb = pygame.mouse.get_pressed()
        self.points = []
        self.drawing = False
        CustomRect._registry.append(self)

    

    def upd_held(self, event):
            if event.type == pygame.MOUSEBUTTONUP:
                self.held = False
            if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_inpos:
                self.held = True
            #print(f"{self.origin.name, self.origin.e_index}: self.held is now {self.held}")


    def upd_hovered(self, event):
        self.pos = pygame.mouse.get_pos()
        self.mouse_inpos = True if self.collidepoint(self.pos[0], self.pos[1]) else False
        if self.mouse_inpos:
            self.hovered = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.hovered = False
        if self.mouse_inpos == False:
            self.hovered = False
        #print(f"{self.origin.name, self.origin.e_index}: hovered is now {self.hovered}")

    def upd_mbuttons(self):
        self.lmb, self.mmb, self.rmb = pygame.mouse.get_pressed()

    def upd_affected(self, event):
        self.affected = True if event.type == pygame.MOUSEBUTTONUP and self.hovered else False
        #print(f"{self.origin.name, self.origin.e_index}: self.affected is now {self.affected}")

    def if_affected(self, event):
        if self.affected and self.mouse_inpos:
            #if self.mouse_inpos:
                #print("inposssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        
            if event.type == pygame.MOUSEBUTTONUP: # if released this frame
                #print("done1")
                self.upd_mbuttons()
                self.origin.if_rect_affected(CustomRect._last_rect_held.origin)
                
                return True
            else:
                #print("done2")
                return False
        else:
            #print("done3")
            return False

    def check_thread(self, event):
            self.curr_threads = []
            for thread in threading.enumerate():
                if thread.name == self.thread_name and thread.is_alive():
                    self.curr_threads.append(True)

            if any(self.curr_threads) == False: #any returns True if any in the list are true
                if self.hovered and self.aff_thread.is_alive() == False:
                    self.aff_thread = threading.Thread(target=self.if_affected, name=self.thread_name, args=(event, ))               
                    self.aff_thread.start()
            
    def if_held(self):
        if self.held:
            CustomRect._last_rect_held = self
    # with more types of customrects we could have a dict of selected functions like:
    # self.check_selected_lst["battle gui"] that would have the value for a def like this one:~
    # then you call it with normal self.check_selected() since it will be redefined
    def upd_rect(event):
        for ele in CustomRect._registry:
            ele.upd_hovered(event)
        for ele in CustomRect._registry:
            ele.upd_affected(event)
        for ele in CustomRect._registry:
            ele.check_thread(event)
        for ele in CustomRect._registry:
            ele.upd_held(event)
            ele.if_held()     
        for ele in CustomRect._registry:
            ele.if_selected()

    
            
    
    def if_selected(self):
        if self.hovered:
            self.colour = (119, 221, 119)
        elif self.held:
            self.colour = (0, 221, 0)
        else:
            self.colour = (255, 255, 255)
        if self.hovered and self.held:
            self.colour = (255, 0, 0)
        
        pygame.draw.rect(pygame.display.get_surface(), self.colour, self, RBS // 2)

    def draw_mouse_lines(self):
        if len(self.points):
            pygame.draw.line(
                SCREEN, (255, 255, 255), self.points[-1], pygame.mouse.get_pos(), 4
            )

    def check_mouse_status(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.held:
            self.points.append(event.pos)
            self.drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.drawing = False
            self.points.clear()
        