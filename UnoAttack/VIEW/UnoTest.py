from random import shuffle, choice, randint
from itertools import product, repeat, chain
from threading import Thread
from time import sleep

"""
NOTA: Actor y screen son objetos provenientes de Pygame Zero (pgzero)
"""

COLORS = ['red', 'yellow', 'green', 'blue']           """Colores de las cartas"""
ALL_COLORS = COLORS + ['black']                       """Colores de todas las cartas"""
NUMBERS = list(range(10)) + list(range(1, 10))        """Numeros de las cartas"""
SPECIAL_CARD_TYPES = ['skip', 'reverse', '+2']        """Tipos de cartas"""
COLOR_CARD_TYPES = NUMBERS + SPECIAL_CARD_TYPES * 2   """Tipos de cartas con sus colores"""
BLACK_CARD_TYPES = ['wildcard', '+4']                """Cartas de cambio de color"""
CARD_TYPES = NUMBERS + SPECIAL_CARD_TYPES + BLACK_CARD_TYPES     """Todos tipos de cartas (numeros, skip, reversa, +2, +4, wildcard)"""


class UnoCard:
    """
    Representa una sola carta de Uno, con su color y tipo.

    color: string
    card_type: string/int

    >>> card = UnoCard('red', 5)
    """
    def __init__(self, color, card_type):
        self._validate(color, card_type)
        self.color = color                   """color"""
        self.card_type = card_type            """tipo de carta"""
        self.temp_color = None                 """para seleccion de color (color temporal)"""
        self.sprite = Actor('{}_{}'.format(color, card_type))       """sprite y Actor para dibujar la carta con un formato de [color]_[tipo]"""

    def __repr__(self):
        return '<UnoCard object: {} {}>'.format(self.color, self.card_type)

    def __str__(self):
        return '{}{}'.format(self.color_short, self.card_type_short)

    def __format__(self, f):                       """Formato de sprite"""
        if f == 'full':
            return '{} {}'.format(self.color, self.card_type)
        else:
            return str(self)

    def __eq__(self, other):                                          
        return self.color == other.color and self.card_type == other.card_type

    def _validate(self, color, card_type):
        """
        Valida la carta, si no es valida, arroja una excepcion
        """
        if color not in ALL_COLORS:
            raise ValueError('Invalid color')
        if color == 'black' and card_type not in BLACK_CARD_TYPES:
            raise ValueError('Invalid card type')
        if color != 'black' and card_type not in COLOR_CARD_TYPES:
            raise ValueError('Invalid card type')

    @property
    def color_short(self):             """Retorna el color de la carta"""
        return self.color[0].upper()

    @property
    def card_type_short(self):                           """Retorna el tipo de carta"""
        if self.card_type in ('skip', 'reverse', 'wildcard'):
            return self.card_type[0].upper()
        else:
            return self.card_type

    @property
    def _color(self):
        return self.temp_color if self.temp_color else self.color

    @property
    def temp_color(self):
        return self._temp_color

    @temp_color.setter
    def temp_color(self, color):          """Valida color"""
        if color is not None:
            if color not in COLORS:
                raise ValueError('Invalid color')
        self._temp_color = color

    def playable(self, other):
        """
        Devuelve True si la otra carta es jugable encima de la carta actual en la mesa, 
        de lo contrario retorna False.
        """
        return (
            self._color == other.color or
            self.card_type == other.card_type or
            other.color == 'black'
        )


class UnoPlayer:
    """
    Representa un jugador en un juego de Uno. Un jugador es creado con una lista de 7 cartas.

    cards: lista de 7 UnoCards
    player_id: int/str (default: None)

    >>> cards = [UnoCard('red', n) for n in range(7)]           Cartas en la mano
    >>> player = UnoPlayer(cards)                               Mano del jugador
    """
    def __init__(self, cards, player_id=None):
        if len(cards) != 7:
            raise ValueError(
                'Invalid player: must be initalised with 7 UnoCards'
            )
        if not all(isinstance(card, UnoCard) for card in cards):
            raise ValueError(
                'Invalid player: cards must all be UnoCard objects'
            )
        self.hand = cards
        self.player_id = player_id

    def __repr__(self):
        if self.player_id is not None:
            return '<UnoPlayer object: player {}>'.format(self.player_id)
        else:
            return '<UnoPlayer object>'

    def __str__(self):                      """ID del jugador como string"""
        if self.player_id is not None:
            return str(self.player_id)
        else:
            return repr(self)

    def can_play(self, current_card):
        """
        Retorna True si el jugador tiene alguna carta jugable con respecto a la carta actual en la mesa, 
        de lo contrario, devuelve False.
        """
        return any(current_card.playable(card) for card in self.hand)


class UnoGame:
    """
    Representa un juego de Uno.

    players: int
    random: bool (default: True)

    >>> game = UnoGame(5)
    """
    def __init__(self, players, random=True):
        if not isinstance(players, int):
            raise ValueError('Invalid game: players must be integer')
        if not 2 <= players <= 15:
            raise ValueError('Invalid game: must be between 2 and 15 players')
        self.deck = self._create_deck(random=random)          """Crea el mazo"""
        self.players = [
            UnoPlayer(self._deal_hand(), n) for n in range(players)     """Crea las manos de los jugadores"""
        ]
        self._player_cycle = ReversibleCycle(self.players)               """Asigna el ciclo de turnos"""
        self._current_player = next(self._player_cycle)                  """Jugador actual"""
        self._winner = None                                              """Ganador"""
        self._check_first_card()                                         """Primera carta en la mesa"""

    def __next__(self):
        """
        La iteracion coloca el jugador actual al proximo jugador en el ciclo.
        Es decir, le da el turno al proximo jugador
        """
        self._current_player = next(self._player_cycle)

    def _create_deck(self, random):
        """
        Devuelve una lista de las cartas de Uno. Si random es True, el mazo sera barajeado, 
        si no, se procede como esta.
        """
        color_cards = product(COLORS, COLOR_CARD_TYPES)          """Colores de las cartas con sus tipos"""
        black_cards = product(repeat('black', 4), BLACK_CARD_TYPES)     """Cartas negras o de cambio de color"""
        all_cards = chain(color_cards, black_cards)                   """Todas las cartas"""
        deck = [UnoCard(color, card_type) for color, card_type in all_cards]         """Crea el mazo"""
        if random:
            shuffle(deck)
            return deck
        else:
            return list(reversed(deck))              """Retorna la lista del mazo invertido"""

    def _deal_hand(self):
        """
        Devuelve una lista de 7 cartas del mazo y los quita del mazo.
        """
        return [self.deck.pop() for i in range(7)]

    @property
    def current_card(self):               """Carta actual"""
        return self.deck[-1]              """Retorna mazo -1""""

    @property
    def is_active(self):              """Partida activa? Retorna todos los jugadores"""
        return all(len(player.hand) > 0 for player in self.players)

    @property
    def current_player(self):           """Jugador actual"""
        return self._current_player

    @property
    def winner(self):                  """Ganador"""
        return self._winner

    def play(self, player, card=None, new_color=None):
        """
        Procesa la jugada del jugador.

        player: int representando el numero de index del jugador
        card: int representa el numero de index de las cartas en la mano del jugador

        Debe ser el turno del jugador, y si una carta es seleccionada, esta debe ser jugable.
        Si una carta no es seleccionada (None), el jugador toma una carta del mazo.

        Si el juego termina, arroja una excepcion.
        """
        """VALIDACIONES"""
        if not isinstance(player, int):
            raise ValueError('Invalid player: should be the index number')
        if not 0 <= player < len(self.players):
            raise ValueError('Invalid player: index out of range')
        _player = self.players[player]
        if self.current_player != _player:
            raise ValueError('Invalid player: not their turn')
        """Si no hay carta seleccionada"""
        if card is None:
            self._pick_up(_player, 1)  """Toma del mazo"""
            next(self)                 """Proximo turno"""
            return
        _card = _player.hand[card]     """Mano del jugador"""
        """Si no es jugable la carta"""
        if not self.current_card.playable(_card):
            raise ValueError(
                'Invalid card: {} not playable on {}'.format(
                    _card, self.current_card
                )
            )
        """Si es de cambio de color"""
        if _card.color == 'black':
            """VALIDACION DE COLOR"""
            if new_color not in COLORS:
                raise ValueError(
                    'Invalid new_color: must be red, yellow, green or blue'
                )
        """VALIDACION DE PARTIDA"""
        if not self.is_active:
            raise ValueError('Game is over')

        """Hace pop a la carta jugada"""
        played_card = _player.hand.pop(card)
        """Añade la carta jugada al mazo"""
        self.deck.append(played_card)

        """Asigna el color de la carta jugada"""
        card_color = played_card.color
        """Asigna el tipo de la carta jugada"""
        card_type = played_card.card_type
        """Si la carta es de cambio de color"""
        if card_color == 'black':
            self.current_card.temp_color = new_color   """Asigna el color temporal a new_color"""
            """Si el tipo de carta es +4"""
            if card_type == '+4':
                next(self)                  """El proximo jugador debe tomar +4 cartas del mazo"""
                self._pick_up(self.current_player, 4)
        """Si el tipo de carta es reversa"""
        elif card_type == 'reverse':
            self._player_cycle.reverse()   """El ciclo de turnos es invertido"""
        """Si el tipo de carta es skip"""
        elif card_type == 'skip':              """Se salta el turno del proximo jugador"""
            next(self)
        """Si el tipo de carta es +2"""
        elif card_type == '+2':                  """El proximo jugador debe tomar +2 cartas del mazo"""
            next(self)
            self._pick_up(self.current_player, 2)

        """Si la partida esta activa (no hay ganadores)"""
        if self.is_active:
            next(self)   """Proximo turno"""
        """Si ya ha ganado alguien"""
        else:
            self._winner = _player
            self._print_winner()

    def _print_winner(self):
        """
        Imprime el nombre del ganador si esta disponible, 
        de lo contrario indica el numero del index del jugador.
        """
        if self.winner.player_id:
            winner_name = self.winner.player_id
        else:
            winner_name = self.players.index(self.winner)
        print("Player {} wins!".format(winner_name))

    def _pick_up(self, player, n):
        """
        Toma n cartas del mazo y lo añade a la mano del jugador

        player: UnoPlayer
        n: int
        """
        penalty_cards = [self.deck.pop(0) for i in range(n)]    """Aplica a las cartas +2 y +4, itera el mazo"""
        player.hand.extend(penalty_cards)                       """Añade de penalty_cards a la mano del jugador"""

    """Chequea la primera carta (NOTA: ESTO ES PARA EL IA QUE JUEGA CONTRA EL JUGADOR)"""
    def _check_first_card(self):
        """Si la carta es de cambio de color"""
        if self.current_card.color == 'black':
            color = choice(COLORS)
            self.current_card.temp_color = color                """Selecciona un color al azar"""
            print("Selected random color for black card: {}".format(color))


class ReversibleCycle:
    """
    Representa una interfaz para un iterable que puede ser ciclado como itertools.cycle
    y que puede ser invertido.

    Empieza en el primer item (index 0), a menos que sea invertido antes de la primera
    iteracion, que en dado caso empieza en el ultimo item.

    iterable: algun finito iterable

    >>> rc = ReversibleCycle(range(3))
    >>> next(rc)
    0
    >>> next(rc)
    1
    >>> rc.reverse()
    >>> next(rc)
    0
    >>> next(rc)
    2
    """
    def __init__(self, iterable):
        self._items = list(iterable)      """Lista de items (jugadores)"""
        self._pos = None                  """Posicion del item"""
        self._reverse = False             """Invertido?"""

    def __next__(self):                   """Proximo"""
        if self.pos is None:
            self.pos = -1 if self._reverse else 0
        else:
            self.pos = self.pos + self._delta
        return self._items[self.pos]

    @property
    def _delta(self):
        return -1 if self._reverse else 1

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value % len(self._items)

    def reverse(self):
        """
        Invierte el orden del iterable.
        """
        self._reverse = not self._reverse


class GameData:
    def __init__(self):
        self.selected_card = None   """Carta seleccionada"""
        self.selected_color = None  """Color seleccionado"""
        self.color_selection_required = False      """Si necesita seleccionar un color nuevo"""
        self.log = ''               """Para mensajes del terminal"""

    @property
    def selected_card(self):
        selected_card = self._selected_card
        self.selected_card = None
        return selected_card

    @selected_card.setter
    def selected_card(self, value):
        self._selected_card = value

    @property
    def selected_color(self):
        selected_color = self._selected_color
        self.selected_color = None
        return selected_color

    @selected_color.setter
    def selected_color(self, value):
        self._selected_color = value


game_data = GameData()

"""Juego para los IA (NPC)"""
class AIUnoGame:
    def __init__(self, players):
        self.game = UnoGame(players)
        self.player = choice(self.game.players)
        self.player_index = self.game.players.index(self.player)
        print('The game begins. You are Player {}.'.format(self.player_index))

    """Proximo turno"""
    def __next__(self):
        game = self.game                  """Asigna game"""
        player = game.current_player      """Asigna el jugador actual"""
        player_id = player.player_id      """ID del jugador""""
        current_card = game.current_card  """Carta en la mesa"""
        """Si es el turno del jugador"""
        if player == self.player:
            played = False
            """Si no ha jugado"""
            while not played:
                card_index = None
                """Mientras que no haya seleccionado una carta"""
                while card_index is None:
                    card_index = game_data.selected_card
                new_color = None
                """Si existe la carta seleccionada"""
                if card_index is not False:
                    card = player.hand[card_index]   """Asigna la carta seleccionada del index"""
                    """Si no se puede jugar la carta"""
                    if not game.current_card.playable(card):
                        game_data.log = 'You cannot play that card'
                        continue
                    """De lo contrario, se juega la carta"""
                    else:
                        game_data.log = 'You played card {:full}'.format(card)
                        """Si la carta es negra, es decir, es de cambio de color y la mano del jugador es mayor que 1"""
                        if card.color == 'black' and len(player.hand) > 1:
                            game_data.color_selection_required = True   """Le asigna color_selection_required para que pase a seleccionar un color"""
                            """Mientras que el nuevo color no haya sido seleccionado"""
                            while new_color is None:
                                new_color = game_data.selected_color       """Le asigna el color seleccionado"""
                            game_data.log = 'You selected {}'.format(new_color)
                """De lo contrario, si no existe la carta seleccionada, se procede a tomar del mazo"""
                else:
                    card_index = None
                    game_data.log = 'You picked up'
                game.play(player_id, card_index, new_color)
                played = True
            """Si el jugador puede jugar una carta"""
        elif player.can_play(game.current_card):
            """Para cada carta en la mano del jugador, itera"""
            for i, card in enumerate(player.hand):
                """Si la carta actual se puede jugar"""
                if game.current_card.playable(card):
                    """Si la carta es de cambio de color"""
                    if card.color == 'black':
                        new_color = choice(COLORS)   """Escoge el color nuevo"""
                    """Si no es de cambio de color"""
                    else:
                        new_color = None
                    game_data.log = "Player {} played {:full}".format(player, card)
                    game.play(player=player_id, card=i, new_color=new_color)
                    break
        """De lo contrario, toma del mazo"""
        else:
            game_data.log = "Player {} picked up".format(player)
            game.play(player=player_id, card=None)


    def print_hand(self):
        print('Your hand: {}'.format(
            ' '.join(str(card) for card in self.player.hand)
        ))

num_players = 3               """Numero de jugadores"""

game = AIUnoGame(num_players)   """Inicializa el juego con num_players(numero de jugadores)"""

WIDTH = 1200      """Tamaño de la ventana"""
HEIGHT = 800

deck_img = Actor('back')   """Imagen del mazo"""
color_imgs = {color: Actor(color) for color in COLORS}   """Imagenes de los colores para la seleccion de colores (red, yellow, green, blue)"""

def game_loop():           """Ciclo del juego"""
    while game.game.is_active:
        sleep(1)
        next(game)

game_loop_thread = Thread(target=game_loop)
game_loop_thread.start()

"""Dibuja el mazo"""
def draw_deck():
    deck_img.pos = (130, 70)
    deck_img.draw()
    current_card = game.game.current_card
    current_card.sprite.pos = (210, 70)
    current_card.sprite.draw()
    """Si requiere seleccionar un color"""
    if game_data.color_selection_required:
        """Para cada color, dibuja una carta para la seleccion de colores"""
        for i, card in enumerate(color_imgs.values()):
            card.pos = (290+i*80, 70)
            card.draw()
    """De lo contrario, dibuja el color seleccionado"""
    elif current_card.color == 'black' and current_card.temp_color is not None:
        color_img = color_imgs[current_card.temp_color]
        color_img.pos = (290, 70)
        color_img.draw()

"""Dibuja las cartas de los jugadores"""
def draw_players_hands():
    """Para cada jugador, itera"""
    for p, player in enumerate(game.game.players):
        """Si es el turno del jugador, cambia el color del texto del jugador(nombre) a rojo"""
        color = 'red' if player == game.game.current_player else 'black'
        """Si un jugador gana, imprime el mensaje"""
        text = 'P{} {}'.format(p, 'wins' if game.game.winner == player else '')
        screen.draw.text(text, (0, 300+p*130), fontsize=100, color=color)
        """Para cada carta en la mano del jugador, itera"""
        for c, card in enumerate(player.hand):
            """Si es el jugador actual, dibuja las cartas del jugador"""
            if player == game.player:
                sprite = card.sprite
            """De lo contrario, dibuja las cartas negras, indicando que se estan viendo por detras"""
            else:
                sprite = Actor('back')     """Actor indica que imagen a utilizar, al asignarlo a sprite y realizar .draw(), este lo dibuja en pantalla"""
            sprite.pos = (130+c*80, 330+p*130)
            sprite.draw()

def show_log():
    screen.draw.text(game_data.log, midbottom=(WIDTH/2, HEIGHT-50), color='black')

def update():
    screen.clear()
    screen.fill((255, 255, 255))
    draw_deck()
    draw_players_hands()
    show_log()

"""En click"""
def on_mouse_down(pos):
    """Si es el turno del jugador"""
    if game.player == game.game.current_player:
        """Para cada carta en la mano del jugador, itera"""
        for card in game.player.hand:
            """Si se le da click a una carta"""
            if card.sprite.collidepoint(pos):
                game_data.selected_card = game.player.hand.index(card)
                print('Selected card {} index {}'.format(card, game.player.hand.index(card)))
        """Si se le da click al mazo"""
        if deck_img.collidepoint(pos):
            game_data.selected_card = False
            print('Selected pick up')
        """Para las cartas de cambio de color"""
        for color, card in color_imgs.items():
            if card.collidepoint(pos):
                game_data.selected_color = color
                game_data.color_selection_required = False
