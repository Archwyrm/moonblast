import pygame

class World:
    def __init__(self):
        self.ground = ((0,400),(200,250),(320,350),(400,300),(640,400))
        self.checked = False
        self.gravity = 1.622 # m/s^2

    def update(self, player):
        player.position[1] = player.position[1] + self.gravity

    def draw(self, surf):
        for tri in self._triangulate():
            pygame.draw.polygon(surf, pygame.Color(100,100,100), tri)
            pygame.draw.lines(surf, pygame.Color(255,255,0), True, tri)

        pygame.draw.aalines(surf, pygame.Color(255,255,255), False, self.ground)

    def collide(self, player):
        tris = self._triangulate()
        for tri in tris:
            point = (player.position[0] + player.bb[0], player.position[1] + player.bb[1])
            while self._point_in_triangle(point, tri[0], tri[1], tri[2]):
                player.position[1] = player.position[1] + (-1 * self.gravity)
                point = (player.position[0] + player.bb[0], player.position[1] + player.bb[1])

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
