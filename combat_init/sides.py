from settings import *
import pygame

class Side(pygame.Rect):
    def __init__(self, xpos, ypos):
        super().__init__(self)
        self.length = (HEIGHT - DBS) * 1 / 3
        self.member_amt = 0
        self.members = []
        self.left = xpos
        self.top = ypos
        self.width = self.length
        self.height = self.length
        self.mem_search_count = 0
        self.screen = pygame.display.get_surface()

    def draw_side(self):  # works for up to eight members on each side
        # REDO THIS, like bruh this the dumbest solution ever
        # just seperate the side into smaller rects and then convert that into a 2d array
        # then portion it out depending it out depending on the circumstances
        # taking the amt of members
        # pygame.draw.rect(self.screen, (255, 255, 255), self, RBS)
        if self.member_amt == 0:
            pygame.draw.rect(self.screen, (255, 255, 255), self, RBS)
        if self.member_amt  == 1:
            if self.mem_search_count == 0:
                for ele in self.members:
                    if ele != 0 and self.mem_search_count == 0:
                        ele.rect.topleft = self.topleft

                        ele.rect.width = self.width
                        ele.rect.height = self.height
                        self.mem_search_count += 1

        if self.member_amt == 2:
            self.mem_search_count = 0
            for ele in self.members:
                if ele != 0:
                    if self.mem_search_count == 0:
                        ele.rect.topleft = self.topleft

                        ele.rect.width = self.width
                        ele.rect.height = self.height / 2
                        self.mem_search_count += 1

                    elif self.mem_search_count == 1:
                        ele.rect.topleft = self.midleft

                        ele.rect.width = self.width
                        ele.rect.height = self.height / 2
                        self.mem_search_count += 1

        if self.member_amt == 3:
            self.mem_search_count = 0
            for ele in self.members:
                if ele != 0:
                    if self.mem_search_count == 0:
                        ele.rect.topleft = self.topleft

                        ele.rect.width = self.width
                        ele.rect.height = self.height / 2
                        self.mem_search_count += 1

                    elif self.mem_search_count == 1:

                        ele.rect.topleft = self.center

                        ele.rect.width = self.width / 2
                        ele.rect.height = self.height / 2
                        self.mem_search_count += 1

                    elif self.mem_search_count == 2:
                        ele.rect.topleft = self.midleft

                        ele.rect.width = self.width / 2
                        ele.rect.height = self.height / 2
                        self.mem_search_count += 1

        if self.member_amt == 4:
            self.mem_search_count = 0
            for ele in self.members:
                if ele != 0:
                    if self.mem_search_count == 0:
                        ele.rect.topleft = self.topleft

                        ele.rect.width = self.width / 2
                        ele.rect.height = self.height / 2
                        self.mem_search_count += 1

                    elif self.mem_search_count == 1:
                        ele.rect.topleft = self.midtop

                        ele.rect.width = self.width / 2
                        ele.rect.height = self.height / 2
                        self.mem_search_count += 1
                    elif self.mem_search_count == 2:
                        ele.rect.topleft = self.midleft
                        ele.rect.width = self.width / 2
                        ele.rect.height = self.height / 2
                        self.mem_search_count += 1
                    elif self.mem_search_count == 3:
                        ele.rect.topleft = self.center
                        ele.rect.width = self.width / 2
                        ele.rect.height = self.height / 2
                        self.mem_search_count += 1

        if self.member_amt == 5:
            self.mem_search_count = 0
            for ele in self.members:
                if ele != 0:
                    if self.mem_search_count == 0:
                        ele.rect.topleft = self.topleft

                        ele.rect.width = self.width / 2
                        ele.rect.height = self.height / 3
                        self.mem_search_count += 1
                        self.topl_rect = ele

                    elif ele != 0 and self.mem_search_count == 1:
                        ele.rect.topleft = self.midtop

                        ele.rect.width = self.width / 2
                        ele.rect.height = self.height / 3
                        self.mem_search_count += 1
                        self.topr_rect = ele

                    elif ele != 0 and self.mem_search_count == 2:
                        ele.rect.topleft = self.topr_rect.rect.bottomleft

                        ele.rect.width = self.width / 2
                        ele.rect.height = self.height / 3
                        self.mem_search_count += 1
                        self.midr_rect = ele

                    elif ele != 0 and self.mem_search_count == 3:
                        ele.rect.topleft = self.topl_rect.rect.bottomleft

                        ele.rect.width = self.width / 2
                        ele.rect.height = self.height / 3
                        self.midl_rect = ele
                        self.mem_search_count += 1

                    elif ele != 0 and self.mem_search_count == 4:
                        ele.rect.topleft = self.midl_rect.rect.bottomleft

                        ele.rect.width = self.width
                        ele.rect.height = self.height / 3
                        self.bot_rect = ele
                        self.mem_search_count += 1

        if self.member_amt == 6:
            self.mem_search_count = 0
            for ele in self.members:
                if self.mem_search_count < 6:
                    if ele != 0 and self.mem_search_count == 0:
                        ele.rect.topleft = self.topleft

                        ele.rect.width = self.width / 3
                        ele.rect.height = self.height / 3
                        self.mem_search_count += 1
                        self.topl_rect = ele

                    elif ele != 0 and self.mem_search_count == 1:
                        ele.rect.topleft = self.topl_rect.rect.topright

                        ele.rect.width = self.width * (2 / 3)
                        ele.rect.height = self.height * (2 / 3)
                        self.mem_search_count += 1
                        self.topm_rect = ele

                    elif ele != 0 and self.mem_search_count == 2:
                        ele.rect.topleft = self.topl_rect.rect.bottomleft

                        ele.rect.width = self.width / 3
                        ele.rect.height = self.height / 3
                        self.mem_search_count += 1
                        self.midl_rect = ele

                    elif ele != 0 and self.mem_search_count == 3:
                        ele.rect.topleft = self.midl_rect.rect.bottomleft

                        ele.rect.width = self.width / 3
                        ele.rect.height = self.height / 3
                        self.mem_search_count += 1
                        self.botl_rect = ele

                    elif ele != 0 and self.mem_search_count == 4:
                        ele.rect.topleft = self.botl_rect.rect.topright

                        ele.rect.width = self.width / 3
                        ele.rect.height = self.height / 3
                        self.mem_search_count += 1
                        self.botm_rect = ele

                    elif ele != 0 and self.mem_search_count == 5:
                        ele.rect.topleft = self.botm_rect.rect.topright

                        ele.rect.width = self.width / 3
                        ele.rect.height = self.height / 3
                        self.mem_search_count += 1
                        self.botr_rect = ele

        if self.member_amt == 7:
            self.mem_search_count = 0
            for ele in self.members:
                if ele != 0 and self.mem_search_count == 0:
                    ele.rect.topleft = self.topleft

                    ele.rect.width = self.width / 4
                    ele.rect.height = self.height / 4
                    self.mem_search_count += 1
                    topltl_rect = ele

                elif ele != 0 and self.mem_search_count == 1:
                    ele.rect.topleft = topltl_rect.rect.topright

                    ele.rect.width = self.width / 4
                    ele.rect.height = self.height / 4
                    self.mem_search_count += 1
                    topltr_rect = ele

                elif ele != 0 and self.mem_search_count == 2:
                    ele.rect.topleft = topltl_rect.rect.bottomleft

                    ele.rect.width = self.width / 4
                    ele.rect.height = self.height / 4
                    self.mem_search_count += 1
                    toplbl_rect = ele

                elif ele != 0 and self.mem_search_count == 3:
                    ele.rect.topleft = toplbl_rect.rect.topright

                    ele.rect.width = self.width / 4
                    ele.rect.height = self.height / 4
                    midl_rect = ele
                    self.mem_search_count += 1

                elif ele != 0 and self.mem_search_count == 4:
                    ele.rect.topleft = topltr_rect.rect.topright

                    ele.rect.width = self.width / 2
                    ele.rect.height = self.height / 2
                    topr_rect = ele
                    self.mem_search_count += 1

                elif ele != 0 and self.mem_search_count == 5:
                    ele.rect.topleft = toplbl_rect.rect.bottomleft

                    ele.rect.width = self.width / 2
                    ele.rect.height = self.height / 2
                    botl_rect = ele
                    self.mem_search_count += 1

                elif ele != 0 and self.mem_search_count == 6:
                    ele.rect.topleft = botl_rect.rect.topright

                    ele.rect.width = self.width / 2
                    ele.rect.height = self.height / 2
                    botr_rect = ele
                    self.mem_search_count += 1

        if self.member_amt == 8:
            self.mem_search_count = 0
            for ele in self.members:
                if ele != 0 and self.mem_search_count == 0:
                    ele.rect.topleft = self.topleft

                    ele.rect.width = self.width / 4
                    ele.rect.height = self.height / 4
                    self.topl_rect = ele.rect
                    self.mem_search_count += 1

                elif ele != 0 and self.mem_search_count == 1:
                    ele.rect.topleft = self.topl_rect.bottomleft

                    ele.rect.width = self.width / 4
                    ele.rect.height = self.height / 4
                    self.mid1_rect = ele.rect
                    self.mem_search_count += 1

                elif ele != 0 and self.mem_search_count == 2:
                    ele.rect.topleft = self.mid1_rect.bottomleft

                    ele.rect.width = self.width / 4
                    ele.rect.height = self.height / 4
                    self.mid2_rect = ele.rect
                    self.mem_search_count += 1

                elif ele != 0 and self.mem_search_count == 3:
                    ele.rect.topleft = self.mid2_rect.bottomleft

                    ele.rect.width = self.width / 4
                    ele.rect.height = self.height / 4
                    self.botl_rect = ele.rect
                    self.mem_search_count += 1

                elif ele != 0 and self.mem_search_count == 4:
                    ele.rect.topleft = self.botl_rect.topright

                    ele.rect.width = self.width / 4
                    ele.rect.height = self.height / 4
                    self.botm1_rect = ele.rect
                    self.mem_search_count += 1

                elif ele != 0 and self.mem_search_count == 5:
                    ele.rect.topleft = self.botm1_rect.topright

                    ele.rect.width = self.width / 4
                    ele.rect.height = self.height / 4
                    self.botm2_rect = ele.rect
                    self.mem_search_count += 1

                elif ele != 0 and self.mem_search_count == 6:
                    ele.rect.topleft = self.botm2_rect.topright

                    ele.rect.width = self.width / 4
                    ele.rect.height = self.height / 4
                    self.botr_rect = ele.rect
                    self.mem_search_count += 1

                elif ele != 0 and self.mem_search_count == 7:
                    ele.rect.topleft = self.topl_rect.topright

                    ele.rect.width = self.width * 3 / 4
                    ele.rect.height = self.height * 3 / 4
                    self.big_rect = ele.rect
                    self.mem_search_count += 1

        for ele in self.members:
            pygame.draw.rect(
                pygame.display.get_surface(), ele.rect.colour, ele.rect, RBS // 2
            )