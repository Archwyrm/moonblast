import pygame

class World:
    def __init__(self):
        self.ground = ((0,400),(200,250),(320,350),(400,300),(640,400))
        self.checked = False
        #print_slope(self.ground)

    def draw(self, surf):
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

    # http://geomalgorithms.com/a02-_lines.html#Distance-to-Ray-or-Segment
    def dist_Point_to_Segment(point, segment):
        pass
        v = (segment[1][0] - segment[0][0],
             segment[1][1] - segment[0][1])
        w = (point[1][0] - segment[0][0],
             point[1][1] - segment[0][1])

        c1 = self._dot_product(w, v)
        if c1 <= 0:
            return d(P, S.P0);

        c2 = self._dot_product(v, v)
        if c2 <= c1:
            return d(P, S.P1)

        b = c1 / c2
        Pb = S.P0 + b * v
        return d(P, Pb)

    def _dot_product(self, a, b):
        return a[0] * b[0] + a[1] * b[1]
