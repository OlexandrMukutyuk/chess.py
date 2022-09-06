import pygame
from Setting import *

pygame.init()
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Chees')


class Pawn:
    def rend(self):
        if self.live:
            if self.actv and self.y - 1 == ytm and self.color == 'White' and self.x == xtm and h1.board[xtm, ytm] != 'White':
                self.y = ytm
                self.x = xtm
                cords[self.name] = (self.x, self.y)
                cordw[self.name] = (self.x, self.y)
            elif self.actv and self.y + 1 == ytm and self.color == 'Black' and self.x == xtm and h1.board[
                xtm, ytm] != 'Black':
                self.y = ytm
                self.x = xtm
                cords[self.name] = (self.x, self.y)
                cordb[self.name] = (self.x, self.y)
            if self.color == 'Black':
                img = pygame.image.load('image/blackpawn.jpg')
                set = img.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(img, set)

            elif self.color == 'White':
                img = pygame.image.load('image/whitepawn.jpg')
                set = img.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(img, set)

    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.actv = False
        self.name = name
        self.live = True

    def die(self, x, y):
        self.x = x
        self.y = y


class Horse:
    def rend(self):
        if self.live:
            detekt_poz()
            if self.actv and self.y - ytm == 2 and h1.board[
                xtm, ytm] != self.color or self.actv and ytm - self.y == 2 and \
                    h1.board[xtm, ytm] != self.color:
                if self.x - xtm == 1 or xtm - self.x == 1:
                    self.y = ytm
                    self.x = xtm
                    cords[self.name] = (self.x, self.y)
                    if self.color == 'White':
                        cordw[self.name] = (self.x, self.y)
                        for item in cordb:
                            if cordb[item] == (self.x, self.y):
                                deleteb(self.x, self.y)

                    elif self.color == 'Black':
                        cordb[self.name] = (self.x, self.y)
                        for item in cordw:
                            if cordw[item] == (self.x, self.y):
                                deletew(self.x, self.y)

            elif self.actv and self.x - xtm == 2 or self.actv and xtm - self.x == 2:
                if self.y - ytm == 1 or ytm - self.y == 1:
                    self.y = ytm
                    self.x = xtm
                    cords[self.name] = (self.x, self.y)
                    if self.color == 'White':
                        cordw[self.name] = (self.x, self.y)
                        for item in cordb:
                            if cordb[item] == (self.x, self.y):
                                deleteb(self.x, self.y)
                    elif self.color == 'Black':
                        cordb[self.name] = (self.x, self.y)
                        for item in cordw:
                            if cordw[item] == (self.x, self.y):
                                deletew(self.x, self.y)
            if self.color == 'Black':
                blachorse = pygame.image.load('image/bblackhorse.jpg')
                blachorse1 = blachorse.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(blachorse, blachorse1)
            elif self.color == 'White':
                whitehorse = pygame.image.load('image/whitehorse.jpg')
                whitehorse1 = whitehorse.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(whitehorse, whitehorse1)

    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.actv = False
        self.name = name
        self.live = True


class Defender:
    def rend(self):
        if self.live:
            if self.actv and (ytm - self.y == xtm - self.x) and h1.board[xtm, ytm] != self.color or (
                    self.actv and (ytm - self.y == self.x - xtm) and h1.board[xtm, ytm] != self.color):
                tmp = True
                if xtm > self.x and ytm > self.y:
                    for i in range(xtm - self.x):
                        if h1.board[self.x + i + 1, self.y + i + 1] == self.color:
                            tmp = False
                elif self.x > xtm and self.y > ytm:
                    for i in range(self.x - xtm):
                        if h1.board[self.x - i - 1, self.y - i - 1] == self.color:
                            tmp = False
                elif self.x > xtm and self.y < ytm:
                    for i in range(self.x - xtm):
                        if h1.board[self.x - i - 1, self.y + i + 1] == self.color:
                            tmp = False
                elif self.x < xtm and self.y > ytm:
                    for i in range(self.y - ytm):
                        if h1.board[self.x + i + 1, self.y - i - 1] == self.color:
                            tmp = False
                if tmp:
                    self.y = ytm
                    self.x = xtm
                    cords[self.name] = (self.x, self.y)
                    if self.color == 'White':
                        cordw[self.name] = (self.x, self.y)
                        for item in cordb:
                            if cordb[item] == (self.x, self.y):
                                deleteb(self.x, self.y)
                    elif self.color == 'Black':
                        cordb[self.name] = (self.x, self.y)
                        for item in cordw:
                            if cordw[item] == (self.x, self.y):
                                deletew(self.x, self.y)
                if self.color == 'White':
                    cordw[self.name] = (self.x, self.y)
                elif self.color == 'Black':
                    cordb[self.name] = (self.x, self.y)
            if self.color == 'Black':
                defender = pygame.image.load('image/blackdefender.jpg')
                defender1 = defender.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(defender, defender1)
            elif self.color == 'White':
                whitedefender = pygame.image.load('image/whitedefender.jpg')
                whitedefender1 = whitedefender.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(whitedefender, whitedefender1)

    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.actv = False
        self.name = name
        self.live = True


class Quine:
    def rend(self):
        if self.live:
            if (self.actv and self.y == ytm and self.x != xtm and h1.board[xtm, ytm] != self.color):
                tmp = True
                if xtm > self.x:
                    for i in range(xtm - self.x):
                        if h1.board[self.x + i + 1, ytm] == self.color:
                            tmp = False
                elif self.x > xtm:
                    for i in range(self.x - xtm):
                        if h1.board[self.x - i - 1, ytm] == self.color:
                            tmp = False
                if tmp:
                    self.y = ytm
                    self.x = xtm
                    cords[self.name] = (self.x, self.y)
                    if self.color == 'White':
                        cordw[self.name] = (self.x, self.y)
                        for item in cordb:
                            if cordb[item] == (self.x, self.y):
                                deleteb(self.x, self.y)
                    elif self.color == 'Black':
                        cordb[self.name] = (self.x, self.y)
                        for item in cordw:
                            if cordw[item] == (self.x, self.y):
                                deletew(self.x, self.y)
            elif (self.actv and self.y != ytm and self.x == xtm and h1.board[xtm, ytm] != self.color):
                tmp = True
                if ytm > self.y:
                    for i in range(ytm - self.y):
                        if h1.board[xtm, self.y + i + 1] == self.color:
                            tmp = False
                elif self.y > ytm:
                    for i in range(self.y - ytm):
                        if h1.board[xtm, self.y - i - 1] == self.color:
                            tmp = False
                if tmp:
                    self.y = ytm
                    self.x = xtm
                    cords[self.name] = (self.x, self.y)
                    if self.color == 'White':
                        cordw[self.name] = (self.x, self.y)
                        for item in cordb:
                            if cordb[item] == (self.x, self.y):
                                deleteb(self.x, self.y)
                    elif self.color == 'Black':
                        cordb[self.name] = (self.x, self.y)
                        for item in cordw:
                            if cordw[item] == (self.x, self.y):
                                deletew(self.x, self.y)
            if self.actv and (ytm - self.y == xtm - self.x and h1.board[xtm, ytm] != self.color) or (
                    self.actv and (ytm - self.y == self.x - xtm) and h1.board[xtm, ytm] != self.color):
                tmp = True
                if xtm > self.x and ytm > self.y:
                    for i in range(xtm - self.x):
                        if h1.board[self.x + i + 1, self.y + i + 1] == self.color:
                            tmp = False
                elif self.x > xtm and self.y > ytm:
                    for i in range(self.x - xtm):
                        if h1.board[self.x - i - 1, self.y - i - 1] == self.color:
                            tmp = False
                elif self.x > xtm and self.y < ytm:
                    for i in range(self.x - xtm):
                        if h1.board[self.x - i - 1, self.y + i + 1] == self.color:
                            tmp = False
                elif self.x < xtm and self.y > ytm:
                    for i in range(self.y - ytm):
                        if h1.board[self.x + i + 1, self.y - i - 1] == self.color:
                            tmp = False
                if tmp:
                    self.y = ytm
                    self.x = xtm
                    cords[self.name] = (self.x, self.y)
                    if self.color == 'White':
                        cordw[self.name] = (self.x, self.y)
                        for item in cordb:
                            if cordb[item] == (self.x, self.y):
                                deleteb(self.x, self.y)
                    elif self.color == 'Black':
                        cordb[self.name] = (self.x, self.y)
                        for item in cordw:
                            if cordw[item] == (self.x, self.y):
                                deletew(self.x, self.y)
                if self.color == 'White':
                    cordw[self.name] = (self.x, self.y)
                elif self.color == 'Black':
                    cordb[self.name] = (self.x, self.y)
            if self.color == 'Black':
                quine = pygame.image.load('image/blackquine.jpg')
                quine1 = quine.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(quine, quine1)
            elif self.color == 'White':
                whitequine = pygame.image.load('image/whiteqine.jpg')
                whitequine1 = whitequine.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(whitequine, whitequine1)

    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.actv = False
        self.name = name
        self.live = True


class Ladia:
    def rend(self):
        if self.live:
            if self.actv and self.y == ytm and self.x != xtm and h1.board[xtm, ytm] != self.color:
                print(1)
                tmp = True
                if xtm > self.x:
                    for i in range(xtm - self.x):
                        if h1.board[self.x + i + 1, ytm] == self.color:
                            tmp = False
                elif self.x > xtm:
                    for i in range(self.x - xtm):
                        if h1.board[self.x - i - 1, ytm] == self.color:
                            tmp = False
                if tmp:
                    self.y = ytm
                    self.x = xtm
                    cords[self.name] = (self.x, self.y)
                    if self.color == 'White':
                        cordw[self.name] = (self.x, self.y)
                        for item in cordb:
                            if cordb[item] == (self.x, self.y):
                                deleteb(self.x, self.y)
                    elif self.color == 'Black':
                        cordb[self.name] = (self.x, self.y)
                        for item in cordw:
                            if cordw[item] == (self.x, self.y):
                                deletew(self.x, self.y)
            elif (self.actv and self.y != ytm and self.x == xtm and h1.board[xtm, ytm] != self.color):
                tmp = True
                if ytm > self.y:
                    for i in range(ytm - self.y):
                        if h1.board[xtm, self.y + i + 1] == self.color:
                            tmp = False
                elif self.y > ytm:
                    for i in range(self.y - ytm):
                        if h1.board[xtm, self.y - i - 1] == self.color:
                            tmp = False
                if tmp:
                    self.y = ytm
                    self.x = xtm
                    cords[self.name] = (self.x, self.y)
                    if self.color == 'White':
                        cordw[self.name] = (self.x, self.y)
                        for item in cordb:
                            if cordb[item] == (self.x, self.y):
                                deleteb(self.x, self.y)
                    elif self.color == 'Black':
                        cordb[self.name] = (self.x, self.y)
                        for item in cordw:
                            if cordw[item] == (self.x, self.y):
                                deletew(self.x, self.y)
            if self.color == 'Black':
                blacladia = pygame.image.load('image/blackladia.jpg')
                blacladia1 = blacladia.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(blacladia, blacladia1)
            elif self.color == 'White':
                whiteladia = pygame.image.load('image/whiteladia.jpg')
                whiteladia1 = whiteladia.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(whiteladia, whiteladia1)

    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.actv = False
        self.name = name
        self.live = True


class King:
    def rend(self):
        if self.live:
            if ((self.actv and self.y - 1 == ytm and h1.board[xtm, ytm] != self.color) or (
                    self.actv and self.y + 1 == ytm and h1.board[xtm, ytm] != self.color) or (
                    self.actv and self.y == ytm and h1.board[xtm, ytm] != self.color)):
                if (self.x - 1 == xtm) or (self.x + 1 == xtm) or self.x == xtm:
                    self.y = ytm
                    self.x = xtm
                    cords[self.name] = (self.x, self.y)
                    if self.color == 'White':
                        cordw[self.name] = (self.x, self.y)
                        for item in cordb:
                            if cordb[item] == (self.x, self.y):
                                deleteb(self.x, self.y)
                    elif self.color == 'Black':
                        cordb[self.name] = (self.x, self.y)
                        for item in cordw:
                            if cordw[item] == (self.x, self.y):
                                deletew(self.x, self.y)
            if self.color == 'Black':
                king = pygame.image.load('image/blackking.jpg')
                king1 = king.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(king, king1)
            elif self.color == 'White':
                whiteking = pygame.image.load('image/whiteking.jpg')
                whiteking1 = whiteking.get_rect(bottomright=(self.x * 50, self.y * 50))
                window.blit(whiteking, whiteking1)

    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.actv = False
        self.name = name
        self.live = True


class Board:

    def __init__(self, board):
        self.row = 8
        self.column = 8
        self.board = board


def chessboard():
    x = 0
    y = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    pygame.draw.rect(window, White, (x, y, 50, 50))
                    x += 50
                else:
                    pygame.draw.rect(window, Black, (x, y, 50, 50))
                    x += 50
            else:
                if j % 2 == 0:
                    pygame.draw.rect(window, Black, (x, y, 50, 50))
                    x += 50
                else:
                    pygame.draw.rect(window, White, (x, y, 50, 50))
                    x += 50
        y += 50
        x = 0


def detekt_poz():
    for r in range(8):
        for c in range(8):
            boar[c + 1, r + 1] = 'empty'
            for whi in cordw:
                if (c + 1, r + 1) == cordw[whi]:
                    boar[c + 1, r + 1] = 'White'
            for bl in cordb:
                if (c + 1, r + 1) == cordb[bl]:
                    boar[c + 1, r + 1] = 'Black'
    h1.board = boar


def bord():
    chessboard()
    detekt_poz()
    pygame.display.update()


def render():
    window.fill(Gray)
    chessboard()
    kingb.rend()
    kingw.rend()
    quineb.rend()
    quinew.rend()
    ladia1w.rend()
    ladia2w.rend()
    ladia1b.rend()
    ladia2b.rend()
    defender1w.rend()
    defender2w.rend()
    defender1b.rend()
    defender2b.rend()
    horse1w.rend()
    horse2w.rend()
    horse1b.rend()
    horse2b.rend()
    pawn1b.rend()
    pawn2b.rend()
    pawn3b.rend()
    pawn4b.rend()
    pawn5b.rend()
    pawn6b.rend()
    pawn7b.rend()
    pawn8b.rend()
    pawn1w.rend()
    pawn2w.rend()
    pawn3w.rend()
    pawn4w.rend()
    pawn5w.rend()
    pawn6w.rend()
    pawn7w.rend()
    pawn8w.rend()

    kingb.actv = False
    kingw.actv = False
    quineb.actv = False
    quinew.actv = False
    ladia1w.actv = False
    ladia2w.actv = False
    ladia1b.actv = False
    ladia2b.actv = False
    defender1w.actv = False
    defender2w.actv = False
    defender1b.actv = False
    defender2b.actv = False
    horse1w.actv = False
    horse2w.actv = False
    horse1b.actv = False
    horse2b.actv = False
    pawn1b.actv = False
    pawn2b.actv = False
    pawn3b.actv = False
    pawn4b.actv = False
    pawn5b.actv = False
    pawn6b.actv = False
    pawn7b.actv = False
    pawn8b.actv = False
    pawn1w.actv = False
    pawn2w.actv = False
    pawn3w.actv = False
    pawn4w.actv = False
    pawn5w.actv = False
    pawn6w.actv = False
    pawn7w.actv = False
    pawn8w.actv = False


def move(cords):
    xt = cords[0] // 50 + 1
    yt = cords[1] // 50 + 1
    if xt == pawn1w.x and yt == pawn1w.y:
        pawn1w.actv = True
    elif xt == pawn2w.x and yt == pawn2w.y:
        pawn2w.actv = True
    elif xt == pawn3w.x and yt == pawn3w.y:
        pawn3w.actv = True
    elif xt == pawn4w.x and yt == pawn4w.y:
        pawn4w.actv = True
    elif xt == pawn5w.x and yt == pawn5w.y:
        pawn5w.actv = True
    elif xt == pawn6w.x and yt == pawn6w.y:
        pawn6w.actv = True
    elif xt == pawn7w.x and yt == pawn7w.y:
        pawn7w.actv = True
    elif xt == pawn8w.x and yt == pawn8w.y:
        pawn8w.actv = True

    if xt == pawn1b.x and yt == pawn1b.y:
        pawn1b.actv = True
    elif xt == pawn2b.x and yt == pawn2b.y:
        pawn2b.actv = True
    elif xt == pawn3b.x and yt == pawn3b.y:
        pawn3b.actv = True
    elif xt == pawn4b.x and yt == pawn4b.y:
        pawn4b.actv = True
    elif xt == pawn5b.x and yt == pawn5b.y:
        pawn5b.actv = True
    elif xt == pawn6b.x and yt == pawn6b.y:
        pawn6b.actv = True
    elif xt == pawn7b.x and yt == pawn7b.y:
        pawn7b.actv = True
    elif xt == pawn8b.x and yt == pawn8b.y:
        pawn8b.actv = True

    if xt == ladia1w.x and yt == ladia1w.y:
        ladia1w.actv = True
    elif xt == ladia2w.x and yt == ladia2w.y:
        ladia2w.actv = True
    elif xt == ladia1b.x and yt == ladia1b.y:
        ladia1b.actv = True
    elif xt == ladia2b.x and yt == ladia2b.y:
        ladia2b.actv = True

    if xt == horse1w.x and yt == horse1w.y:
        horse1w.actv = True
    elif xt == horse2w.x and yt == horse2w.y:
        horse2w.actv = True
    elif xt == horse1b.x and yt == horse1b.y:
        horse1b.actv = True
    elif xt == horse2b.x and yt == horse2b.y:
        horse2b.actv = True

    if xt == defender1w.x and yt == defender1w.y:
        defender1w.actv = True
    elif xt == defender2w.x and yt == defender2w.y:
        defender2w.actv = True
    elif xt == defender1b.x and yt == defender1b.y:
        defender1b.actv = True
    elif xt == defender2b.x and yt == defender2b.y:
        defender2b.actv = True

    if xt == kingb.x and yt == kingb.y:
        kingb.actv = True
    elif xt == kingw.x and yt == kingw.y:
        kingw.actv = True
    elif xt == quineb.x and yt == quineb.y:
        quineb.actv = True
    elif xt == quinew.x and yt == quinew.y:
        quinew.actv = True


def click(cords):
    global xtm, ytm
    xtm = cords[0] // 50 + 1
    ytm = cords[1] // 50 + 1
    tm = h1.board


def deleteb(x, y):
    if x == pawn1b.x and y == pawn1b.y:
        cords['pawn1b'] = (100, 100)
        cordb['pawn1b'] = (100, 100)
        pawn1b.rend()
        pawn1b.live = False
    elif x == pawn2b.x and y == pawn2b.y:
        if x == pawn2b.x and y == pawn2b.y:
            cords['pawn2b'] = (100, 100)
            cordb['pawn2b'] = (100, 100)
            pawn2b.rend()
            pawn2b.live = False
    elif x == pawn3b.x and y == pawn3b.y:
        if x == pawn3b.x and y == pawn3b.y:
            cords['pawn3b'] = (100, 100)
            cordb['pawn3b'] = (100, 100)
            pawn3b.rend()
            pawn3b.live = False
    elif x == pawn4b.x and y == pawn4b.y:
        if x == pawn4b.x and y == pawn4b.y:
            cords['pawn4b'] = (100, 100)
            cordb['pawn4b'] = (100, 100)
            pawn4b.rend()
            pawn4b.live = False
    elif x == pawn5b.x and y == pawn5b.y:
        if x == pawn5b.x and y == pawn5b.y:
            cords['pawn5b'] = (100, 100)
            cordb['pawn5b'] = (100, 100)
            pawn5b.rend()
            pawn5b.live = False
    elif x == pawn6b.x and y == pawn6b.y:
        if x == pawn6b.x and y == pawn6b.y:
            cords['pawn6b'] = (100, 100)
            cordb['pawn6b'] = (100, 100)
            pawn6b.rend()
            pawn6b.live = False
    elif x == pawn7b.x and y == pawn7b.y:
        if x == pawn7b.x and y == pawn7b.y:
            cords['pawn7b'] = (100, 100)
            cordb['pawn7b'] = (100, 100)
            pawn7b.rend()
            pawn7b.live = False
    elif x == pawn8b.x and y == pawn8b.y:
        if x == pawn8b.x and y == pawn8b.y:
            cords['pawn8b'] = (100, 100)
            cordb['pawn8b'] = (100, 100)
            pawn8b.rend()
            pawn8b.live = False

    elif x == ladia1b.x and y == ladia1b.y:
        if x == ladia1b.x and y == ladia1b.y:
            cords['ladia1b'] = (100, 100)
            cordb['ladia1b'] = (100, 100)
            ladia1b.rend()
            ladia1b.live = False
    elif x == ladia2b.x and y == ladia2b.y:
        if x == ladia2b.x and y == ladia2b.y:
            cords['ladia2b'] = (100, 100)
            cordb['ladia2b'] = (100, 100)
            ladia2b.rend()
            ladia2b.live = False

    elif x == horse1b.x and y == horse1b.y:
        if x == horse1b.x and y == horse1b.y:
            cords['horse1b'] = (100, 100)
            cordb['horse1b'] = (100, 100)
            horse1b.rend()
            horse1b.live = False
    elif x == horse2b.x and y == horse2b.y:
        if x == horse2b.x and y == horse2b.y:
            cords['horse2b'] = (100, 100)
            cordb['horse2b'] = (100, 100)
            horse2b.rend()
            horse2b.live = False

    elif x == defender1b.x and y == defender1b.y:
        if x == defender1b.x and y == defender1b.y:
            cords['defender1b'] = (100, 100)
            cordb['defender1b'] = (100, 100)
            defender1b.rend()
            defender1b.live = False
    elif x == defender2b.x and y == defender2b.y:
        if x == defender2b.x and y == defender2b.y:
            cords['defender2b'] = (100, 100)
            cordb['defender2b'] = (100, 100)
            defender2b.rend()
            defender2b.live = False

    if x == kingb.x and y == kingb.y:
        if x == kingb.x and y == kingb.y:
            cords['kingb'] = (100, 100)
            cordb['kingb'] = (100, 100)
            kingb.rend()
            kingb.live = False
    elif x == quineb.x and y == quineb.y:
        if x == quineb.x and y == quineb.y:
            cords['quineb'] = (100, 100)
            cordb['quineb'] = (100, 100)
            quineb.rend()
            quineb.live = False


def deletew(x, y):
    if x == pawn1w.x and y == pawn1w.y:
        cords['pawn1w'] = (100, 100)
        cordw['pawn1w'] = (100, 100)
        pawn1w.rend()
        pawn1w.live = False
    elif x == pawn2w.x and y == pawn2w.y:
        if x == pawn2w.x and y == pawn2w.y:
            cords['pawn2w'] = (100, 100)
            cordw['pawn2w'] = (100, 100)
            pawn2w.rend()
            pawn2w.live = False
    elif x == pawn3w.x and y == pawn3w.y:
        if x == pawn3w.x and y == pawn3w.y:
            cords['pawn3w'] = (100, 100)
            cordw['pawn3w'] = (100, 100)
            pawn3w.rend()
            pawn3w.live = False
    elif x == pawn4w.x and y == pawn4w.y:
        if x == pawn4w.x and y == pawn4w.y:
            cords['pawn4w'] = (100, 100)
            cordw['pawn4w'] = (100, 100)
            pawn4w.rend()
            pawn4w.live = False
    elif x == pawn5w.x and y == pawn5w.y:
        if x == pawn5w.x and y == pawn5w.y:
            cords['pawn5w'] = (100, 100)
            cordw['pawn5w'] = (100, 100)
            pawn5w.rend()
            pawn5w.live = False
    elif x == pawn6w.x and y == pawn6w.y:
        if x == pawn6w.x and y == pawn6w.y:
            cords['pawn6w'] = (100, 100)
            cordw['pawn6w'] = (100, 100)
            pawn6w.rend()
            pawn6w.live = False
    elif x == pawn7w.x and y == pawn7w.y:
        if x == pawn7w.x and y == pawn7w.y:
            cords['pawn7w'] = (100, 100)
            cordw['pawn7w'] = (100, 100)
            pawn7w.rend()
            pawn7w.live = False
    elif x == pawn8w.x and y == pawn8w.y:
        if x == pawn8w.x and y == pawn8w.y:
            cords['pawn8w'] = (100, 100)
            cordw['pawn8w'] = (100, 100)
            pawn8w.rend()
            pawn8w.live = False

    elif x == ladia1w.x and y == ladia1w.y:
        if x == ladia1w.x and y == ladia1w.y:
            cords['ladia1w'] = (100, 100)
            cordw['ladia1w'] = (100, 100)
            ladia1w.rend()
            ladia1w.live = False
    elif x == ladia2w.x and y == ladia2w.y:
        if x == ladia2w.x and y == ladia2w.y:
            cords['ladia2w'] = (100, 100)
            cordw['ladia2w'] = (100, 100)
            ladia2w.rend()
            ladia2w.live = False

    elif x == horse1w.x and y == horse1w.y:
        if x == horse1w.x and y == horse1w.y:
            cords['horse1w'] = (100, 100)
            cordw['horse1w'] = (100, 100)
            horse1w.rend()
            horse1w.live = False
    elif x == horse2w.x and y == horse2w.y:
        if x == horse2w.x and y == horse2w.y:
            cords['horse2w'] = (100, 100)
            cordw['horse2w'] = (100, 100)
            horse2w.rend()
            horse2w.live = False

    elif x == defender1w.x and y == defender1w.y:
        if x == defender1w.x and y == defender1w.y:
            cords['defender1w'] = (100, 100)
            cordw['defender1w'] = (100, 100)
            defender1w.rend()
            defender1w.live = False
    elif x == defender2w.x and y == defender2w.y:
        if x == defender2w.x and y == defender2w.y:
            cords['defender2w'] = (100, 100)
            cordw['defender2w'] = (100, 100)
            defender2w.rend()
            defender2w.live = False

    if x == kingw.x and y == kingw.y:
        if x == kingw.x and y == kingw.y:
            cords['kingw'] = (100, 100)
            cordw['kingw'] = (100, 100)
            kingw.rend()
            kingw.live = False
    elif x == quinew.x and y == quinew.y:
        if x == quinew.x and y == quinew.y:
            cords['quinew'] = (100, 100)
            cordw['quinew'] = (100, 100)
            quinew.rend()
            quinew.live = False


boar = {}
h1 = Board(boar)


def game():
    global h1
    Run = True
    bord()
    render()
    pygame.display.update()
    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(h1.board[(event.pos[0] // 50 + 1, event.pos[1] // 50 + 1)])
                    click(event.pos)
                    detekt_poz()
                    bord()
                    render()
                    move(event.pos)
                    detekt_poz()
                    pygame.display.update()


if __name__ == '__main__':
    chessboard()
    detekt_poz()
    kingbc = cords['kingb']
    kingb = King(kingbc[0], kingbc[1], 'Black', 'kingb')
    kingwc = cords['kingw']
    kingw = King(kingwc[0], kingwc[1], 'White', 'kingw')
    quinebc = cords['quineb']
    quineb = Quine(quinebc[0], quinebc[1], 'Black', 'quineb')
    quinewc = cords['quinew']
    quinew = Quine(quinewc[0], quinewc[1], 'White', 'quinew')
    ladia1wc = cords['ladia1w']
    ladia1w = Ladia(ladia1wc[0], ladia1wc[1], 'White', 'ladia1w')
    ladia2wc = cords['ladia2w']
    ladia2w = Ladia(ladia2wc[0], ladia2wc[1], 'White', 'ladia2w')
    ladia1bc = cords['ladia1b']
    ladia1b = Ladia(ladia1bc[0], ladia1bc[1], 'Black', 'ladia1b')
    ladia2bc = cords['ladia2b']
    ladia2b = Ladia(ladia2bc[0], ladia2bc[1], 'Black', 'ladia2b')
    defender1wc = cords['defender1w']
    defender1w = Defender(defender1wc[0], defender1wc[1], 'White', 'defender1w')
    defender2wc = cords['defender2w']
    defender2w = Defender(defender2wc[0], defender2wc[1], 'White', 'defender2w')
    defender1bc = cords['defender1b']
    defender1b = Defender(defender1bc[0], defender1bc[1], 'Black', 'defender1b')
    defender2bc = cords['defender2b']
    defender2b = Defender(defender2bc[0], defender2bc[1], 'Black', 'defender2b')
    horse1wc = cords['horse1w']
    horse1w = Horse(horse1wc[0], horse1wc[1], 'White', 'horse1w')
    horse2wc = cords['horse2w']
    horse2w = Horse(horse2wc[0], horse2wc[1], 'White', 'horse2w')
    horse1bc = cords['horse1b']
    horse1b = Horse(horse1bc[0], horse1bc[1], 'Black', 'horse1b')
    horse2bc = cords['horse2b']
    horse2b = Horse(horse2bc[0], horse2bc[1], 'Black', 'horse2b')
    pawn1b = cords['pawn1b']
    pawn1b = Pawn(pawn1b[0], pawn1b[1], 'Black', 'pawn1b')
    pawn2b = cords['pawn2b']
    pawn2b = Pawn(pawn2b[0], pawn2b[1], 'Black', 'pawn2b')
    pawn3b = cords['pawn3b']
    pawn3b = Pawn(pawn3b[0], pawn3b[1], 'Black', 'pawn3b')
    pawn4b = cords['pawn4b']
    pawn4b = Pawn(pawn4b[0], pawn4b[1], 'Black', 'pawn4b')
    pawn5b = cords['pawn5b']
    pawn5b = Pawn(pawn5b[0], pawn5b[1], 'Black', 'pawn5b')
    pawn6b = cords['pawn6b']
    pawn6b = Pawn(pawn6b[0], pawn6b[1], 'Black', 'pawn6b')
    pawn7b = cords['pawn7b']
    pawn7b = Pawn(pawn7b[0], pawn7b[1], 'Black', 'pawn7b')
    pawn8b = cords['pawn8b']
    pawn8b = Pawn(pawn8b[0], pawn8b[1], 'Black', 'pawn8b')
    pawn1w = cords['pawn1w']
    pawn1w = Pawn(pawn1w[0], pawn1w[1], 'White', 'pawn1w')
    pawn2w = cords['pawn2w']
    pawn2w = Pawn(pawn2w[0], pawn2w[1], 'White', 'pawn2w')
    pawn3w = cords['pawn3w']
    pawn3w = Pawn(pawn3w[0], pawn3w[1], 'White', 'pawn3w')
    pawn4w = cords['pawn4w']
    pawn4w = Pawn(pawn4w[0], pawn4w[1], 'White', 'pawn4w')
    pawn5w = cords['pawn5w']
    pawn5w = Pawn(pawn5w[0], pawn5w[1], 'White', 'pawn5w')
    pawn6w = cords['pawn6w']
    pawn6w = Pawn(pawn6w[0], pawn6w[1], 'White', 'pawn6w')
    pawn7w = cords['pawn7w']
    pawn7w = Pawn(pawn7w[0], pawn7w[1], 'White', 'pawn7w')
    pawn8w = cords['pawn8w']
    pawn8w = Pawn(pawn8w[0], pawn8w[1], 'White', 'pawn8w')
    game()
