import pygame

GRAVITY = 1.622 # m/s^2
AIR_RESISTANCE = 0.07


class World(object):
    def __init__(self):
        # TODO: Break out level code into a level module
        self.ground = ((0,400),(200,250),(320,350),(400,300),(640,400))
        self.level_bounds = (0, 640) # Left and right limits for the level
        self.players = list()
        self.entities = list()

    def update(self):
        ent_list = self.entities + self.players
        for p in self.players:
            self._constrain_in_level(p)

        for entity in ent_list:
            self.collide(entity)
            entity.update()

    def draw(self, surf):
        for tri in self._triangulate():
            pygame.draw.polygon(surf, pygame.Color(100,100,100), tri)
            pygame.draw.lines(surf, pygame.Color(255,255,0), True, tri)

        pygame.draw.aalines(surf, pygame.Color(255,255,255), False, self.ground)

        ent_list = self.entities + self.players
        for entity in ent_list:
            entity.draw(surf)

    def add_player(self, player):
        self.players.append(player)

    def add_entity(self, entity):
        self.entities.append(entity)

    def collide(self, entity):
        tris = self._triangulate()
        entity.on_ground = False
        for tri in tris:
            for i in range(2):
                point = self._get_rect_corners(entity.position, entity.bb)[i]
                while self._point_in_triangle(point, tri[0], tri[1], tri[2]):
                    entity.position[1] = entity.position[1] + (-1 * GRAVITY)
                    point = self._get_rect_corners(entity.position, entity.bb)[i]
                    entity.on_ground = True

    def _constrain_in_level(self, player):
        """Constrain the passed player within the level."""
        if player.position[0] < self.level_bounds[0]:
            player.position[0] = self.level_bounds[0]
        elif player.position[0] > self.level_bounds[1]:
            player.position[0] = self.level_bounds[1] - player.bb[0]

    def _get_rect_corners(self, point, bb):
        """Returns two points for each bottom corner of a bounding box
        based on a fixed point."""
        points = list()
        points.append([point[0], point[1] + bb[1]]) # Bottom left
        points.append([point[0] + bb[0], point[1] + bb[1]]) # Bottom right
        return points

    def _get_segments(self):
        """Returns currently visible line segments."""
        ret = list()
        num = len(self.ground) - 1
        for i in range(num):
            ret.append((self.ground[i], self.ground[i+1]))
        return ret

    def _get_slope(self, segment):
        """Gets the slope of a line segment."""
        a = segment[0]; b = segment[1]
        return (b[1] - a[1]) / (b[0] - a[0] * 1.0)

    def _triangulate(self):
        """Adds a third vertex to each segment to divide the area under
        the ground plane into triangles. Returns a list of triangle
        segments."""

        tris = []
        segments = self._get_segments()
        size = len(segments)
        last_p = (0,480)

        for i in range(size):
            seg = segments[i]
            x = seg[0][0] + ((seg[1][0] - seg[0][0]) / 2)
            y = 480
            point = (x,y)
            tri = (seg[0], seg[1], point)

            # Create intermediary tri, unless it is in the corner
            if seg[0][1] != y:
                tris.append((last_p, seg[0], point))
            last_p = (x,y) # Move to the next point

            tris.append(tri)

            # Create last tri, unless it is in the corner
            if i == size - 1 and seg[1][1] != y:
                tris.append((seg[1], (640,y), (x,y)))

        return tris

    def _point_in_triangle(self, p, p0, p1, p2):
        A = 1.0/2.0 * (-p1[1] * p2[0] + p0[1] * (-p1[0] + p2[0]) + p0[0] * (p1[1] - p2[1]) + p1[0] * p2[1])
        sign = -1 if A < 0 else 1
        s = (p0[1] * p2[0] - p0[0] * p2[1] + (p2[1] - p0[1]) * p[0] + (p0[0] - p2[0]) * p[1]) * sign
        t = (p0[0] * p1[1] - p0[1] * p1[0] + (p0[1] - p1[1]) * p[0] + (p1[0] - p0[0]) * p[1]) * sign

        return s > 0 and t > 0 and (s + t) < 2 * A * sign;
