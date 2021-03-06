import pyautogui
import time
import keyboard
import sys
# Global variables:
side = 0
gamestart = 0
gamecheck = 0
marker = False
markerst = False
game = 0
# timesLost = 0
# betlvl = 0
bet = 0
# games = int
bankstreak = 0
playerstreak = 0
chopstreak = 0
lastside = 0
win = False
betsafe = False
checksafe = False

# functions:
def exit():
    if keyboard.is_pressed('x'):
        sys.exit()

def player():
    pyautogui.click(829, 679)

def banker():
    pyautogui.click(1162, 679)

def chopper():
    global bet
    if side == 1:
        player()
        bet = 1
    elif side == 2:
        banker()
        bet = 2

def betting():
    global bet
    exit()

    if playerstreak == 3:
        banker()
        bet = 1
    elif playerstreak == 4:
        bet = 1
        for i in range(2):
            banker()
            time.sleep(0.3)
    elif playerstreak == 5:
        bet = 1
        for i in range(4):
            banker()
            time.sleep(0.3)
    elif playerstreak == 6:
        bet = 1
        for i in range(8):
            banker()
            time.sleep(0.3)

    if bankstreak == 3:
        player()
        bet = 2
    elif bankstreak == 4:
        bet = 2
        for i in range(2):
            player()
            time.sleep(0.3)
    elif bankstreak == 5:
        bet = 2
        for i in range(4):
            player()
            time.sleep(0.3)
    elif bankstreak == 6:
        bet = 2
        for i in range(8):
            player()
            time.sleep(0.3)

    if chopstreak == 2:
        chopper()
    elif chopstreak == 3:
        for i in range(2):
            chopper()
            time.sleep(0.3)
    elif chopstreak == 4:
        for i in range(4):
            chopper()
            time.sleep(0.3)
    elif chopstreak == 5:
        for i in range(8):
            chopper()
            time.sleep(0.3)


# Continius checks
def game():
    global side
    global gamestart
    global marker
    global markerst
    global gamecheck
    global game
    global playerstreak
    global bankstreak
    global chopstreak
    global lastside
    global bet
    global win
    global betsafe
    global checksafe
    while True:
        exit()
        if pyautogui.locateOnScreen('jugador.png', region=(590, 50, 800, 600), confidence=0.75):
            side = 1
            gamecheck += 1
            gamestart = 0
            print('Player')
        elif pyautogui.locateOnScreen('banca.png', region=(590, 50, 800, 600), confidence=0.75):
            side = 2
            gamecheck += 1
            gamestart = 0
            print('Banker')
        elif pyautogui.locateOnScreen('empate.png', region=(590, 50, 800, 600), confidence=0.75):
            side = 3
            gamecheck += 1
            gamestart = 0
            print('Empate')
        elif pyautogui.locateOnScreen('n20.png', region=(590, 50, 800, 600), confidence=0.90):
            gamestart += 1
            gamecheck = 0
            print('20')
        elif pyautogui.locateOnScreen('n19.png', region=(590, 50, 800, 600), confidence=0.87):
            gamestart += 1
            gamecheck = 0
            print('19')
        elif pyautogui.locateOnScreen('n18.png', region=(590, 50, 800, 600), confidence=0.85):
            gamestart += 1
            gamecheck = 0
            print('18')
        elif pyautogui.locateOnScreen('n17.png', region=(590, 50, 800, 600), confidence=0.80):
            gamestart += 1
            gamecheck = 0
            print('17')
        elif pyautogui.locateOnScreen('n16.png', region=(590, 50, 800, 600), confidence=0.75):
            gamestart += 1
            gamecheck = 0
            print('16')
        elif pyautogui.locateOnScreen('n15.png', region=(590, 50, 800, 600), confidence=0.70):
            gamestart += 1
            gamecheck = 0
            print('15')
        elif pyautogui.locateOnScreen('n14.png', region=(590, 50, 800, 600), confidence=0.67):
            gamestart += 1
            gamecheck = 0
            print('14')
        elif pyautogui.locateOnScreen('n13.png', region=(590, 50, 800, 600), confidence=0.65):
            gamestart += 1
            gamecheck = 0
            print('13')
        elif pyautogui.locateOnScreen('n12.png', region=(590, 50, 800, 600), confidence=0.60):
            gamestart += 1
            gamecheck = 0
            print('12')
        elif pyautogui.locateOnScreen('n11.png', region=(590, 50, 800, 600), confidence=0.57):
            gamestart += 1
            gamecheck = 0
            print('11')
        elif pyautogui.locateOnScreen('n10.png', region=(590, 50, 800, 600), confidence=0.55):
            gamestart += 1
            gamecheck = 0
            print('10')
        elif pyautogui.locateOnScreen('n9.png', region=(590, 50, 800, 600), confidence=0.55):
            gamestart += 1
            gamecheck = 0
            print('09')
        elif pyautogui.locateOnScreen('n8.png', region=(590, 50, 800, 600), confidence=0.55):
            gamestart += 1
            gamecheck = 0
            print('08')
        elif pyautogui.locateOnScreen('n7.png', region=(590, 50, 800, 600), confidence=0.70):
            gamestart += 1
            gamecheck = 0
            print('07')
        elif pyautogui.locateOnScreen('n6.png', region=(590, 50, 800, 600), confidence=0.70):
            gamestart += 1
            gamecheck = 0
            print('06')
        elif pyautogui.locateOnScreen('nuevo_mazo.png', region=(590, 50, 800, 600), confidence=0.87):
            bankstreak = 0
            playerstreak = 0
            chopstreak = 0
            lastside = 0
            side = 0
            print('chop streak= ' + str(chopstreak))
            print('player streak = ' + str(playerstreak))
            print('bank streak= ' + str(bankstreak))
            print('last side = ' + str(lastside))
            print('side = ' + str(side))
            print('mazo')
        exit()
        if side == 1:
            game = '1'
        elif side == 2:
            game = '2'
        elif side == 3:
            game = '3'
        exit()
        if gamestart <= 1:
            betsafe = True
        elif gamestart == 2:
            markerst = True
        exit()
        if gamecheck <= 2:
            checksafe = True
        elif gamecheck == 3:
            marker = True
        exit()
        # Everything inside this loop is run once:
        if marker:
            """chek = open('games.txt', 'a+')
            chek.write(game + "\n")
            chek.close()"""
            if side == 1:
                if bankstreak >= 1:
                    chopstreak += 1
                    lastside = 2
                playerstreak += 1
                bankstreak = 0
                if playerstreak >= 2:
                    chopstreak = 0
                    lastside = 1
            elif side == 2:
                if playerstreak >= 1:
                    chopstreak += 1
                    lastside = 1
                playerstreak = 0
                bankstreak += 1
                if bankstreak >= 2:
                    chopstreak = 0
                    lastside = 2
            elif side == 3:
                playerstreak = 0
                bankstreak = 0
                chopstreak = 0
                lastside = 0
            print('chop streak= ' + str(chopstreak))
            print('player streak = ' + str(playerstreak))
            print('bank streak= ' + str(bankstreak))
            print('last side = ' + str(lastside))
            print('side = ' + str(side))
            exit()
            # check if win code
            if bet == side:
                win = True
            elif bet != side:
                win = False
            print(win)
            checksafe = False
            marker = False

        if markerst and betsafe:
            # betting code
            betting()

            betsafe = False
            markerst = False


if __name__ == "__main__":
    game()
