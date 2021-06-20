#!/usr/bin/env python3
import tcod
from actions import EscapeAction, MovementAction
from input_handler import EventHandler
from entity import Entity

def main() -> None:
    screen_width = 80 #screen size
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD #font
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width//2), int(screen_height//2), "@", (255, 255, 0))
    npc = Entity(int(screen_width//2 + 5), int(screen_height//2 + 5), "@", (255, 0, 0))
    entities = {player, npc}

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Roguelike Tutorial",
        vsync=True,

    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F") #order=F flips y,x to x,y when accessing numpy library
        while True: #game loop
            root_console.print(x=player.x,y=player.y,string=player.char, fg=player.color)

            context.present(root_console) #updates screen

            root_console.clear() #clears outdated info

            for event in tcod.event.wait():

                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction): #checks if action is a Movement action, then moves if so
                    player.move(dx=action.dx, dy=action.dy)

                elif isinstance(action, EscapeAction): #checks if action is a Escape action, the raises system exit method
                    raise SystemExit()


if __name__ == "__main__":
    main()