import tcod as libtcod


def _draw_entity(con, entity, fov_map):
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
        libtcod.console_set_default_foreground(con, entity.color)
        libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)


def render_all(
    con, entities, game_map, fov_map, fov_recompute, screen_width, screen_height, colors,
):
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight

                if visible:
                    if wall:
                        libtcod.console_set_char_background(
                            con, x, y, colors.get("light_wall"), libtcod.BKGND_SET,
                        )
                    else:
                        libtcod.console_set_char_background(
                            con, x, y, colors.get("light_ground"), libtcod.BKGND_SET,
                        )
                    game_map.tiles[x][y].explored = True

                elif game_map.tiles[x][y].explored:
                    if wall:
                        libtcod.console_set_char_background(
                            con, x, y, colors.get("dark_wall"), libtcod.BKGND_SET,
                        )
                    else:
                        libtcod.console_set_char_background(
                            con, x, y, colors.get("dark_ground"), libtcod.BKGND_SET,
                        )

    for entity in entities:
        _draw_entity(con, entity, fov_map)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def _clear_entity(con, entity):
    libtcod.console_put_char(con, entity.x, entity.y, " ", libtcod.BKGND_NONE)


def clear_all(con, entities):
    for entity in entities:
        _clear_entity(con, entity)
