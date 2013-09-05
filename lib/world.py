import pygame

class World:
    def __init__(self):
        self.ground = ((0,400),(200,250),(320,350),(400,300),(640,400))
        self.checked = False

    def draw(self, surf):
        for tri in self._triangulate():
            tri = list(tri)
            tri.append(tri[0]) # Add final side for drawing purposes
            pygame.draw.aalines(surf, pygame.Color(255,255,0), False, tri)

        pygame.draw.aalines(surf, pygame.Color(255,255,255), False, self.ground)

    def collide(self, player):
        if self.checked:
            return

        for segment in self._get_segments():
            if self._is_left(segment, player.position):
                print("Left")
                if self._get_slope(segment) < 0:
                    print("Penetrating")
            else:
                print("Right")
                if self._get_slope(segment) > 0:
                    print("Penetrating")
            #else:
               # print("We're good")
            print("Slope: %s" % self._get_slope(segment))
        self.checked = True
        print("------------")
        # If slope is negative, slopes up
        # If slope is positive, slopes down

    def _is_left(self, line, point):
        a = line[0]; b = line[1]
        if a[1] < b[1]: # If y1 < y2..
            a, b = b, a # Swap so our idea of 'right' and 'left' is consistent
        #print("a: %s, b: %s, player: %s" % (a, b, point))
        return ((b[0] - a[0]) * (point[1] - a[1])
               -(b[1] - a[1]) * (point[0] - a[0])) > 0

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
        for i in range(size):
            seg = segments[i]
            x = seg[0][0] + ((seg[1][0] - seg[0][0]) / 2)
            y = 480
            tri = (seg[0], seg[1], (x,y))

            # Create first tri, unless it is in the corner
            if i == 0 and seg[0][1] != y:
                tris.append(((0,y), seg[0], (x,y)))

            tris.append(tri)

            # Create last tri, unless it is in the corner
            if i == size - 1 and seg[1][1] != y:
                tris.append((seg[1], (640,y), (x,y)))

        return tris
