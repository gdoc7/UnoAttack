from tkinter import *
from random import randint, choice, shuffle
from PIL import ImageTk

# Borde
col = "lightgoldenrodyellow"

# Configuración Ventana
root = Tk()
root.geometry("1500x750")
root.resizable(False, False)
root.wm_attributes('-transparentcolor', "orange")
root.configure(bg=col)
root.title(f"Uno Attack [P{player.num}]")

# Donde están las imagenes
folder = "Revamped Uno_Assets"   # Si no funciona, usar la ruta absoluta.

# Imagenes
images = {
    "Red": ImageTk.PhotoImage(Image.open(f"{folder}/Red.png").convert("RGBA").rotate(45)),
    "Green": ImageTk.PhotoImage(Image.open(f"{folder}/Green.png").convert("RGBA").rotate(45)),
    "Yellow": ImageTk.PhotoImage(Image.open(f"{folder}/Yellow.png").convert("RGBA").rotate(45)),
    "Blue": ImageTk.PhotoImage(Image.open(f"{folder}/Blue.png").convert("RGBA").rotate(45)),
    "Deck": ImageTk.PhotoImage(file=f"{folder}/Deck.png"), # Imagen del mazo (o launcher)
    "UNO": ImageTk.PhotoImage(file=f"{folder}/Logo.png"), # Logo UNO
    "UNO_Button": ImageTk.PhotoImage(file=f"{folder}/UnoButton.png"),
    "Start": ImageTk.PhotoImage(file=f"{folder}/startButton.png")
    }

# Colores de fondo
bgCols = {
    "Red": "#802019",
    "Purple": "#48406A",
    "Green": "#23863F",
    "Blue": "#40686A"
    }


mainBg = bgCols["Purple"]
# #1-#9: 2, Specials: 2, Wilds: 4, #0: 1
cards = ["Wild", "Wild_Draw", "Skip", "Draw", "Reverse", "Discard"] + [str(n) for n in range(10)]

canvas = Canvas(root, width=1126, height=700, bg=mainBg)
canvas.place(relx=0.225,rely=0.5, anchor="w")
            
colourPicker = {"Red": canvas.create_image(int(canvas["width"])/2+250, int(canvas["height"])/2-100,image=images["Red"], state="hidden"),
                "Yellow": canvas.create_image(int(canvas["width"])/2+180, int(canvas["height"])/2-30,image=images["Yellow"], state="hidden"), # 181, -30
                "Blue": canvas.create_image(int(canvas["width"])/2+320, int(canvas["height"])/2-30,image=images["Blue"], state="hidden"), # 322, -31
                "Green": canvas.create_image(int(canvas["width"])/2+250, int(canvas["height"])/2+40,image=images["Green"], state="hidden") # 251, 39
                }

class Card():
    def __init__(self, name, displayName, colour, cardType, worth):      
        self.name = name
        self.colour = colour
        self.cardType = cardType
        self.worth = worth    #puntos
        self.animating = True
        self.up = False
        self.displayName = displayName
        self.time = 100
        #print(name, colour, cardType)
        self.rawImage = Image.open(f"{folder}/{name}.png").convert("RGBA")   #imagen de frente
        self.backRaw = Image.open(f"{folder}/Back.png").convert("RGBA")      #imagen de atras
        self.storedImage = ImageTk.PhotoImage(self.rawImage)                 #imagen raw
        # 
        #self.main = Label(canvas, image=self.storedImage, bg=mainBg)

        #crea el canvas, en donde la imagen se dibuja
        self.main = canvas.create_image(int(canvas["width"])/2+self.storedImage.width(), int(canvas["height"])/2, image=self.storedImage, state="hidden")

    def disable(self):
        canvas.tag_unbind(self.main, "<1>")
        
    def RightToCentre(self): # Ubicado en la derecha del canvas (jugador de la derecha), girado 90° y puesto al centro
        #self.main["image"] = images["R_Back"]
        #self.main.unbind("<1>")
        self.backImage = ImageTk.PhotoImage(self.backRaw.rotate(90, expand=True))
        canvas.itemconfig(self.main, image=self.backImage)
        self.disable()

    def LeftToCentre(self): # Ubicado en la izquierda del canvas (jugador de la izquierda), girado -90° y puesto al centro
        self.backImage = ImageTk.PhotoImage(self.backRaw.rotate(-90, expand=True))
        canvas.itemconfig(self.main, image=self.backImage)
        self.disable()

    def Reverse(self): # Ubicado arriba en el canvas (jugador de arriba). Girado 180° y puesto al centro
        self.backImage = ImageTk.PhotoImage(self.backRaw.rotate(180))
        canvas.itemconfig(self.main, image=self.backImage)
        self.disable()

    def Normal(self): # Ubicado abajo en el canvas (jugador de abajo). Imagen de carta normal
        canvas.itemconfig(self.main, image=self.storedImage)
        canvas.tag_bind(self.main, "<1>", self.attemptCardUsage)

    def animateUp(self):     #animación arriba
        if self.animating: return
        self.animating = True
        base = canvas.coords(self.main)
        animateWidgetMovement(self.main, base[0], base[1]-self.storedImage.height()/2, self.time)
        root.after(self.time, self.toggleUp, True)

    def animateDown(self):   #animación abajo
        if self.animating: return
        self.animating = True
        base = canvas.coords(self.main)
        animateWidgetMovement(self.main, base[0], base[1]+self.storedImage.height()/2, self.time)
        root.after(self.time, self.toggleUp, False)

    def toggleUp(self, val):      #toggle de animación
        self.up = val
        self.animating = False
        
        
    def isUsable(self):       # Se puede usar la carta?
        if not game.started:
            game.log.output("El juego todavía no ha comenzado!")
            return False
        elif self.name.find("Wild") > -1 or self.colour == game.deck.lastCardUsed.colour or self.cardType == game.deck.lastCardUsed.cardType:
            return True
        
    def attemptCardUsage(self, event):       # Intento de uso de carta
        if self.isUsable() and game.turnNumber == 0 and not game.pickingColour:
            self.use(game.user)

    def use(self, player):                # Uso de carta
        game.log.output(f"{player.name} jugó {self.displayName}")
        # Quita la carta de la mano del jugador
        for i, cardObj in enumerate(player.hand):
            if cardObj == self:
                player.hand.pop(i)
                player.visualiseHand(len(player.hand))
                break
        game.deck.updateLastUsed(self)      # Añade la carta usada a la pila de cartas usadas
        if len(player.hand) == 1 :
            if game.uno: # Canta UNO
                game.log.output(f"{player.name}: UNO!")
            else: # No dijo uno, el jugador toma +2 manotazos
                game.log.output(f"{player.name} no cantó UNO! Tomando 2 manotazos como penalty.")
                for n in range(2):
                    q = getRandom()
                    player.draw(q)
        incrementTurn = True
        if self.cardType == "Reverse":
            if game.playerCount == 2: # Funciona como skip si hay solo dos jugadores
                game.skipNext = True
            else: # Else invierte el orden de los turnos
                game.increment *= -1
        elif self.cardType == "Skip":
            game.skipNext = True
        elif self.cardType == "Discard":   # Descarta todas las cartas del mismo color
            game.skipNext = True
            for i, cardObj in enumerate(player.hand):
                if cardObj.colour == self.colour:
                    player.hand.pop(i)
                    player.visualiseHand(len(player.hand))
                    game.deck.updateLastUsed(cardObj)
        elif self.cardType == "Draw":
            game.skipNext = True # Salta el proximo turno
            # +2 manotazos al proximo jugador
            for n in range(2):
                a = getRandom()
                game.turnList[game.simplifyTurnNumber(False, game.increment)].draw(a)
        elif self.cardType == "Wild":
            if self.name == "Wild_Draw": # Wild draw 4, chequea legalidad
                legal = True
                for cardObj in player.hand:
                    if cardObj.colour == game.deck.usedPile[-1].colour and cardObj.cardType != "Wild": # Ilegal!!
                        legal = False
                        break
                if legal:
                    game.skipNext = True # salta al proximo
                    # +4 manotazos al proximo jugador
                    for n in range(4):                  
                        p = getRandom()
                        game.turnList[game.simplifyTurnNumber(False, game.increment)].draw(p)
                else: # Jugada ilegal, castigo
                    game.log.output("Jugada prohibida (manotazo cuadruple). El jugador dará 4 manotazos como castigo.")
                    for n in range(4):
                        o = getRandom()
                        player.draw(o)
            if player == game.user and len(player.hand) > 0:
                game.pickingColour = True
                toggleColourPicker("normal")
            incrementTurn = False

        if len(player.hand) == 0: # game over
            # Cuenta los puntos y muestra el ganador
            totalScore = 0
            for plr in game.players:
                for cardObj in plr.hand:
                    totalScore += cardObj.worth
                    # Devuelve las cartas de todos los jugadores al mazo
                    game.deck.cards.append(cardObj)
                plr.hand = []
            game.log.output(f"{player.name} won, scoring {totalScore} points!")
            if player == game.user:
                game.log.output("Congratulations!")
            else:
                game.log.output("Better luck next time!")
                
            # Devuelve la pila de cartas usadas al mazo
            game.deck.cards += game.deck.usedPile
            game.deck.usedPile = []
            game.deck.cards.append(game.deck.lastCardUsed)
            game.deck.lastCardUsed = None
            # Esconde todas las cartas del mazo
            for cardObj in game.deck.cards:
                canvas.itemconfig(cardObj.main, state="hidden")
                canvas.coords(cardObj.main,int(canvas["width"])/2+self.storedImage.width(), int(canvas["height"])/2) 

            # Esconde el mazo
            game.deck.main.place_forget()
            
            # Esconde el botón de UNO
            canvas.itemconfig(game.unoButton, state="hidden")
            
            # Muestra la pantalla de inicio
            game.displayTitleScreen(True)
            
        elif incrementTurn: # Próximo turno
            game.incTurn()


class Deck():
    def __init__(self):
        self.cards = []
        self.usedPile = []
        self.lastCardUsed = None
        # Añade cartas de cada color
        for colour in ["Yellow", "Red", "Green", "Blue"]:
            # Añade cartas de cada tipo
            for cardType in cards:
                name = f"{colour}_{cardType}"
                displayName = f"{colour} {cardType}"
                times = 1
                if len(cardType) == 1: # Carta de números
                    worth = int(cardType)
                    if cardType != "0": #1-9 Cartas de números. Crear dos sets.
                        times = 2
                elif cardType.find("Wild") > -1: # Cambio de color. Crear una vez (total 4 cartas).
                    worth = 50
                    name = cardType
                    cardType = "Wild"
                    if name == "Wild_Draw":
                        displayName = "Wild Draw 4"
                    else:
                        displayName = "Wild Card"
                elif cardType.find("Discard") > -1:  # Cartas de descarte de color. Crear una vez (total 4 cartas).
                    worth = 50
                    name = f"{colour}_{cardType}"
                    cardType = "Discard"
                    displayName = f"{colour} {cardType}"
                else: # Cartas especiales (Skip, Reversa, +2 Manotazos). Crear dos veces.
                    worth = 20
                    times = 2
                self.cards.append(Card(name, displayName, colour, cardType, worth))
                if times == 2:
                    self.cards.append(Card(name, displayName, colour, cardType, worth))

        self.cardHeight = self.cards[0].storedImage.height() + 2
        self.cardWidth = self.cards[0].storedImage.width() + 2
        self.main = Label(canvas, image=images["Deck"], bg=mainBg)
        self.main.bind("<1>", self.drawAttempted)

    def shuffle(self):
        try:
            shuffle(self.cards)
            game.log.output(f"El mazo ha sido barajeado! Quedan {len(self.cards)} cartas!")
        except Exception as e:
            game.log.output(f"El mazo no pudo ser barajeado:\n\n {e}", error=True)

    def drawAttempted(self, event):    # Intento de dar manotazo
        if game.turnNumber == 0 and game.started: # Sólo deja que le de al launcher al que esté jugando 
            r = getRandom()
            game.user.draw(r)
            if not game.user.hand[-1].isUsable(): # No puede usar la carta, el turno termina
                game.incTurn()

    def createUsedPile(self):      # Crea la pila de cartas usadas
        #self.usedPileLabel.place(relx=0.5, rely=0.5,anchor="e")
        self.lastCardUsed = game.deck.cards[0]
        # animación de descarte de cartas
        finalX = int(canvas["width"])/2 - self.cardWidth//1.5
        time = 200
        animateWidgetMovement(self.lastCardUsed.main, finalX, int(canvas["height"])/2, time)
        root.after(int(time), self.checkUsedPile, time)

    def checkUsedPile(self, time):    #Chequea la pila de cartas usadas
        if self.lastCardUsed.name == "Wild_Draw":
            # Wild Draw 4 = Reshuffle + new discard
            game.log.output("Wild Draw 4 fue la primera carta en la pila. Volviendo a barajear...")
            finalX = int(canvas["width"])/2 + self.cardWidth
            animateWidgetMovement(self.lastCardUsed.main, finalX, int(canvas["height"])/2, time/3*2)
            self.shuffle()
            root.after(int(time/3*2), self.createUsedPile)
        else:
            del self.cards[0]
            if self.lastCardUsed.name == "Wild":    # Si la última carta en ser usada es de cambio de color
                game.pickingColour = True
                toggleColourPicker("normal")        # Muestra los botones de cambio de color
            else:
                game.started = True
                for cardObj in game.user.hand:
                    cardObj.animating = False
                    
            if self.lastCardUsed.name == "Skip": # Skip player 1's turn
                game.turnNumber = 1
                game.log.output(f"{game.user.name} tuvo su turno saltado.")
            elif self.lastCardUsed.name == "Draw": # Player 1 draws 2 and loses turn
                for n in range(2):
                    t = getRandom()
                    game.user.draw(t)
                game.log.output(f"{game.user.name} tuvo su turno saltado.")
                game.turnNumber = 1
            elif self.lastCardUsed.name == "Reverse": # Reverse order and skip player's turn
                game.log.output("Orden de turnos invertido!")
                game.turnNumber = game.playerCount-1
                game.increment = -1
                

    def updateLastUsed(self, card):      # Actualiza la última carta jugada
        self.usedPile.append(self.lastCardUsed)
        # Hide prior last card
        root.after(250, canvas.coords, self.lastCardUsed.main, -1*self.cardWidth, -1*self.cardHeight)
        # Update and show new last card
        self.lastCardUsed = card
        card.animating = True
        animateWidgetMovement(card.main, int(canvas["width"])/2 - self.cardWidth//1.5, int(canvas["height"])/2, 250)
        canvas.itemconfig(card.main, image=card.storedImage)

    def remakeDeck(self): # Barajea la pila de cartas usadas al mazo
        self.cards = self.usedPile
        self.usedPile = []
        self.shuffle()
        # Pone las cartas debajo del mazo
        for cardObj in self.cards:
            canvas.coords(cardObj.main, int(canvas["width"])/2+self.cardWidth, int(canvas["height"])/2)
        
class Player(): # Jugadores & Computadoras (BOTS)
    def __init__(self, name, playerNumber, colour):    
        self.name = name
        self.hand = []
        self.num = playerNumber
        self.colour = colour
        self.turn = self.num == 1 # True si es jugador, false si es computador
        game.log.main.tag_configure(f"PlayerNum{self.num}", foreground=self.colour)
        # Prepara las posiciones de anclaje para las cartas en la mano
        height = game.deck.cardHeight
        width = game.deck.cardWidth
        if self.num == 1: # Jugador de abajo
            self.xVal = int(canvas["width"])/2 + width/2 # relx = 0.5
            self.yVal = int(canvas["height"]) - height/2 - 10
        elif self.num == 2: # Jugador de arriba
            self.xVal = int(canvas["width"])/2 + width/2 # relx = 0.5
            self.yVal = 10 + height/2
        elif self.num == 4: # Jugador de la izquierda
            self.xVal = 10 + height/2
            self.yVal = int(canvas["height"])/2 + width/2 # rely = 0.5
        else: # Jugador de la derecha
            # resta la altura (height) porque las cartas estan giradas
            self.xVal = int(canvas["width"])- height/2 - 10 
            self.yVal = int(canvas["height"])/2 + width/2 # rely = 0.5
        self.draw(7, bulk=True)    # Prepara las 7 cartas iniciales de cada jugador
        
    def visualiseHand(self, handSize, time=200): # Visualización de la mano del jugador
        if self.num <= 2: # Arriba o abajo. Usa el eje x para la posición de las cartas
            xVal = self.xVal - (handSize * game.deck.cardWidth / 2)
            xInc = game.deck.cardWidth
            yVal = self.yVal
            yInc = 0
        else: # Izquierda o derecha. Usa el eje y para la posición de las cartas
            xVal = self.xVal
            xInc = 0
            yVal = self.yVal - (handSize * game.deck.cardWidth /2)
            yInc = game.deck.cardWidth
        for i in range(handSize):
            self.hand[i].animating = True # Previene que la animación sea interrumpida
            animateWidgetMovement(self.hand[i].main, xVal+(i*xInc), yVal+(i*yInc), time)
            root.after(time, self.hand[i].toggleUp, False) # Deshabilita la animación

    def draw(self, amount=1, bulk=False):    # Tomar cartas del mazo
        time = 100
        try:
            for i in range(amount):
                if len(game.deck.cards) == 0:
                    game.log.output("El mazo se quedó sin cartas. Barajeando la pila de cartas usadas!")
                    game.deck.remakeDeck()
                self.hand.append(game.deck.cards.pop(0))
                canvas.itemconfig(self.hand[-1].main, state="normal")  # hand[-1] cuenta de derecha a izquierda
                if self.num == 1: # Jugador de abajo
                    self.hand[-1].Normal() 
                elif self.num == 2: # Jugador de arriba
                    self.hand[-1].Reverse()
                elif self.num == 4: # Jugador de la izquierda
                    self.hand[-1].LeftToCentre()
                else: # Jugador de la derecha
                    self.hand[-1].RightToCentre()
                if not bulk:
                    delay = 300*i
                else:
                    delay = time*(i+(self.num-1)*amount)
                root.after(delay, self.visualiseHand, len(self.hand), time)
            if amount == 1:
                game.log.output(f"{self.name} tomó 1 carta")
            elif amount == 0:
                game.log.output(f"{self.name} no tomó ninguna carta")
            elif amount > 0:
                game.log.output(f"{self.name} tomó {amount} cartas")
            if bulk and self.num == game.playerCount:
                root.after(delay+time, game.deck.createUsedPile)
        except Exception as e:
            game.log.output(f"{self.name} no pudo tomar {amount} cartas \n\n {e}", error=True)

    def botPlay(self):        # Jugada del BOT
        #game.log.output(f"{self.name} invoked botPlay")
        usableCards = []
        colours = []
        wild4Present = False
        wild4Allowed = True
        delay = 0
        for cardObj in self.hand:
            # Crea una lista de cartas usables de la mano del BOT
            if cardObj.isUsable():
                usableCards.append(cardObj)
                if cardObj.name == "Wild_Draw":
                    wild4Present = True
            # Crea una lista de los colores en la mano del BOT
            if cardObj.cardType != "Wild":
                colours.append(cardObj.colour)

        # Si no tiene cartas usables, le da un manotazo. Si la carta se puede usar, la usa.
        if len(usableCards) == 0:
            m = getRandom()
            self.draw(m)
            if self.hand[-1].isUsable():
                usableCards.append(self.hand[-1])
                delay = 300 # Deja que la animación de draw ocurra
        # Confirma si wild draw 4 es legal (auto-legal si es la única carta en la mano)
        elif wild4Present and game.deck.lastCardUsed.colour in colours:
            wild4Allowed = False

        # Selecciona una carta al azar de las cartas usables, si es que tiene cartas todavía
        if len(usableCards) > 0:
            card = choice(usableCards)
            while card.name == "Wild_Draw" and not wild4Allowed:
                card = choice(usableCards)
            root.after(delay, self.botUse, card, colours) # Deja que la animación del draw ocurra, si es necesario
        else: # No hay carta jugable, acaba su turno
            game.incTurn()
            
    def botUse(self, card, colours):     # Jugada BOT
        if len(self.hand) == 2 and not game.uno: # Tiene que cantar UNO
            game.toggleUno()
        card.use(self)
        if card.name.find("Wild") > -1 and len(self.hand) > 0:  # Si la carta es de cambio de color
            if len(colours) > 0:
                game.changeWildColour(None, colours)
            else:
                game.changeWildColour(None)
        
        
class CustomText(Text):       # Para el texto
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end", regexp=False):
        self.mark_set("matchStart", self.index(start))
        self.mark_set("matchEnd", self.index(start))
        self.mark_set("searchLimit", self.index(end))

        count = IntVar()
        while True:
            index = self.search(pattern, "matchEnd", "searchLimit", count=count, regexp=regexp)
            if index == "": break
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")
        
class Log():          # Para el historial de acciones
    def __init__(self):
        widthVal = 301
        heightVal = 612
        self.frame = Frame(root, width=widthVal, height=heightVal, bg=col)
        self.frame.place(x=10, rely=0.5, anchor="w")
        self.main = CustomText(self.frame, width=33, height=32, state="disabled", wrap=WORD, bg="grey", fg="white", font=("ArialBold", 13))
        self.main.place(x=0,y=0)
        self.main.tag_configure("error", background="yellow", foreground = "red")
        self.lastLineAppearedTwice = False

    def output(self, msg, error=False):
        self.main["state"] = "normal"
        # Si es el mismo mensaje, añade número "x" al final del mensaje. Si no, añade una línea nueva.
        if self.main.get("end-2l", "end-2l lineend").find(msg) > -1:
            if not self.lastLineAppearedTwice: # Sólo añade "x2"
                self.main.insert("end-2l lineend", " x2")
            else: # Quita y registra caracteres hasta alcanzar la "x"
                lastLine = self.main.get("end-2l", "end-2l lineend")
                # Invierte la línea, obtiene el número, invierte el número a normal
                number = lastLine[::-1][:lastLine[::-1].find("x")][::-1]
                self.main.delete(f"end-{len(number)+2}c", "end-2l lineend")
                self.main.insert("end-2l lineend", str(int(number)+1))
            self.lastLineAppearedTwice = True
        else:
            self.lastLineAppearedTwice = False
            self.main.insert(END, "- " + str(msg) + "\n")
            for plr in game.players: # Nombres de jugadores en colores
                self.main.highlight_pattern(plr.name, f"PlayerNum{plr.num}", start="end-2l")
            if error: # Highlight línea de error
                self.main.highlight_pattern(self.main.get("end-4l", "end-2l lineend"), "error", start="end-4l")
                self.main.insert("end-4l+2c", "ERROR: ")
        self.main["state"] = "disabled"
        self.main.see("end")

    def update(self):
        for plr in game.players:
            self.main.highlight_pattern(plr.name, f"PlayerNum{plr.num}")

class Game():    
    def __init__(self):
        self.players = []
        self.started = False
        self.skipNext = False
        self.uno = False
        self.pickingColour = False
        self.playerCount = 2
        self.turnList = []
        self.turnNumber = 0
        self.increment = 1
        self.botDelay = 1000
        self.firstGame = True

        # Widgets de la pantalla de inicio
        width = int(canvas["width"])
        height = int(canvas["height"])
        
        self.title = canvas.create_image(width/2, height/3, image=images["UNO"])
        self.playButton = canvas.create_image(width/2, height//1.4, image=images["Start"])
        canvas.tag_bind(self.playButton, "<1>", self.hideTitleScreen)

        # Widgets para escoger número de jugadores
        self.playerCountLabel = canvas.create_text(width/2 , height/5, text="Choose player count of ", font=("Arial", 50), fill="white", state="hidden")

        self.player2Background = canvas.create_image(width/3, height/2, image=images["Red"], state="hidden")
        self.player3Background = canvas.create_image(width/2, height/2, image=images["Green"], state="hidden")
        self.player4Background = canvas.create_image(width/3*2, height/2, image=images["Blue"], state="hidden")

        self.player2Label = canvas.create_text(width/3, height/2, text="2", state="hidden", font=("Arial", 50))
        self.player3Label = canvas.create_text(width/2, height/2, text="3", state="hidden", font=("Arial", 50))
        self.player4Label = canvas.create_text(width/3*2, height/2, text="4", state="hidden", font=("Arial", 50))

        self.playerCountWidgets = {
            "label": self.playerCountLabel,
            "2bg": self.player2Background, "3bg": self.player3Background, "4bg": self.player4Background,
            "2label": self.player2Label, "3label": self.player3Label, "4label": self.player4Label
            }
        
        for k, widget in self.playerCountWidgets.items():
            if k != "label":
                canvas.tag_bind(widget, "<1>", self.playerCountButtonClicked)  # Cuando se le da click al botón de selección de jugadores


    def playerCountButtonClicked(self, event):     # Si se le ha dado click al botón de selección de jugadores 
        for k, widget in self.playerCountWidgets.items():
            if widget == canvas.find_withtag(CURRENT)[0]:
                self.real_init(int(k[0]))
        
    def real_init(self, playerCount):
        # Esconde los widgets relacionados a la escogencia de jugadores
        for k, widget in self.playerCountWidgets.items():
            canvas.itemconfig(widget, state="hidden")
            
        # Pone y barajea el mazo
        self.deck.main.place(relx=0.5, rely=0.5, anchor="w")
        self.deck.shuffle()
        
        # Hace que todas las cartas sean visibles en avance
        for cardObj in self.deck.cards:
            canvas.itemconfig(cardObj.main, state="normal")
            # Remueve los objetos de carta en avance, por si acaso
            canvas.coords(cardObj.main,int(canvas["width"])/2+self.deck.cardWidth, int(canvas["height"])/2) 
            canvas.itemconfig(cardObj.main, image=cardObj.storedImage)
        # Clear log
        self.log.main.delete(1.0, "END")
        
        # Creación de los jugadores
        self.playerCount = playerCount
        playerHighlights = ["red3","CadetBlue3", "DarkGoldenRod2", "plum3"]
        self.user = Player("Player1", 1, playerHighlights[0])
        self.players.append(self.user)
        for i in range(1, self.playerCount):
            self.players.append(Player(f"Computer{i}", i+1, playerHighlights[i]))
        self.log.update()

        # Altera turnList para mantener un orden horario (el orden original es antihorario)
        if self.playerCount == 2:
            self.turnList = self.players
        else:
            self.turnList = [self.user, self.players[2], self.players[1]]
            self.players[2].name, self.players[1].name = self.players[1].name, self.players[2].name
            self.players[2].colour, self.players[1].colour = self.players[1].colour, self.players[2].colour
            if self.playerCount == 4:
                self.turnList.append(self.players[3])
                
        # Muestra el botón de UNO
        canvas.itemconfig(self.unoButton, state="normal")
        # Bind animación
        canvas.bind("<Motion>", motion)

    def toggleUno(self, event=None):    # Cantar UNO (evento de click sobre el botón de UNO)
        self.uno = not self.uno
        if self.uno:
            self.log.output(f"Uno status toggled on")
        else:
            self.log.output("Uno status toggled off")
        
    def incTurn(self):
        # Procede al turno del próximo jugador
        self.turnNumber += self.increment
        self.uno = False
        # Permite saltos de turno
        if self.skipNext:
            # Simplifica el número de turno
            self.simplifyTurnNumber()
            # Salto de turno
            self.log.output(f"{self.turnList[self.turnNumber].name} tuvo su turno saltado!")
            self.turnNumber += self.increment
            self.skipNext = False
        # Simplifica el número de turno
        self.simplifyTurnNumber()
        # Deja que el computador juegue el turno
        game.log.output(f"Es el turno de {self.turnList[self.turnNumber].name}!")
        if self.turnNumber != 0:
            root.after(self.botDelay, self.turnList[self.turnNumber].botPlay)

    def simplifyTurnNumber(self,  alter=True, offset=0):    # Simplifica el número de turno
        num = self.turnNumber + offset
        while num >= self.playerCount:
                num -= self.playerCount
        # Para incrementos negativos, asegurarse que al menos sea cero.
        while num < 0:
            num += self.playerCount
        if alter:
            self.turnNumber = num
        else:
            return num
            
    def changeWildColour(self, event, colours=["Red", "Green", "Blue", "Yellow"]):   # Cambio de color
        toggleColourPicker("hidden")
        colour = ""
        if event: # Se le ha dado click por un jugador, selecciona un color
            for key, obj in colourPicker.items():
                if canvas.find_withtag(CURRENT)[0] == obj:
                    colour = key
        else: # BOT eligiendo color
            colour = choice(colours)
        self.deck.lastCardUsed.colour = colour
        game.log.output(f"{self.turnList[self.turnNumber].name} ha escogido el color {colour}")
        game.pickingColour = False
        if event and not game.started: # Dispara cuando una carta de cambio de color empieza en la pila de cartas usadas
            game.started = True
            for cardObj in game.user.hand:
                cardObj.animating = False
        else:
            self.incTurn()

    def displayTitleScreen(self, restart=False):  # Muestra la pantalla principal
        if restart:
            # Resetea las variables
            game.started = False
            self.skipNext = False
            self.uno = False
            self.pickingColour = False
            self.turnList = []
            self.turnNumber = 0
            self.increment = 1
            self.firstGame = False
            # Unbind animación
            canvas.unbind("<Motion>")
            # Vacía la lista de jugadores
            for i in game.players:
                del game.players[0]
            game.players = []
        else:
            # Crea un log y un mazo por primera vez
            self.log = Log()
            self.deck = Deck()
            # Crea el botón de UNO
            self.unoButton = canvas.create_image(int(canvas["width"])/2+self.deck.cardWidth, int(canvas["height"])/2+1.25*(self.deck.cardHeight), image=images["UNO_Button"], state="hidden")
            canvas.tag_bind(self.unoButton, "<1>", self.toggleUno)

        # Muestra la pantalla de inicio
        canvas.itemconfig(self.playButton, state="normal")
        canvas.itemconfig(self.title, state="normal")

    def hideTitleScreen(self, event):
        # Esconde la pantalla de inicio
        canvas.itemconfig(self.playButton, state="hidden")
        canvas.itemconfig(self.title, state="hidden")

        # Muestra los widgets relacionados a escoger el número de jugadores
        for k, widget in self.playerCountWidgets.items():
            canvas.itemconfig(widget, state="normal")

        

def animateWidgetMovement(label, finalX, finalY, time):      # Animar el movimiento de los widgets
    baseX = canvas.coords(label)[0]
    baseY = canvas.coords(label)[1]
    deltaX = finalX-baseX
    deltaY = finalY-baseY
        
    duration = int(time)
    # Animar movimiento
    for i in range(1, duration + 1):
        root.after(int(i*(time/duration)), canvas.coords, label, baseX+i*(deltaX/duration), baseY+i*(deltaY/duration))

    root.after(duration, canvas.coords, label, finalX, finalY) # Asegura que alcance el lugar destino
    
def motion(event):       # Animación de cartas
    if not game.started: return
    # Anima el movimiento de las cartas cuando le pasa el cursor por encima
    item = canvas.find_withtag(CURRENT)
    for cardObj in game.user.hand:
        if len(item) > 0 and cardObj.main == item[0]:
            # Al separar los if, se previene que el elif ocurra cuando no sea necesario.
            if not cardObj.up:
                cardObj.animateUp()
        elif cardObj.up:
            cardObj.animateDown()

def toggleColourPicker(newState):       # Mostrar/Esconder escoger colores
    for k, obj in colourPicker.items():
        canvas.itemconfigure(obj, state=newState)

def getRandom():
    r = randint(0, 5)
    return r

game = Game()
game.displayTitleScreen()

for k, obj in colourPicker.items():
    canvas.tag_bind(obj,"<1>", game.changeWildColour)

input()
