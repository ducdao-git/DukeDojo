from collections import deque


class Solution2:  # runtime O(4^(n*m)), space O(n*m)
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int, check_color=None
    ) -> list[list[int]]:
        if check_color is None:
            check_color = image[sr][sc]

        if check_color == color:
            return image

        ROWCT, COLCT = len(image), len(image[0])
        if (
            min(sr, sc) < 0
            or sr == ROWCT
            or sc == COLCT
            or image[sr][sc] != check_color
        ):
            # cannot use 'any([ ])' here as all elems inside the list will be eval when
            #  buiding the list, result in 'image[sr][sc]' get index out of bound
            return

        image[sr][sc] = color
        self.floodFill(image, sr, sc - 1, color, check_color)
        self.floodFill(image, sr, sc + 1, color, check_color)
        self.floodFill(image, sr - 1, sc, color, check_color)
        self.floodFill(image, sr + 1, sc, color, check_color)

        return image


class Solution:  # runtime O(n*m), space O(n*m)
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        ROWCT, COLCT = len(image), len(image[0])

        tbp = deque()
        tbp.append((sr, sc))

        check_color = image[sr][sc]
        if check_color == color:
            return image

        while tbp:
            r, c = tbp.popleft()

            if image[r][c] != check_color:
                continue

            image[r][c] = color

            if c - 1 >= 0:
                tbp.append((r, c - 1))
            if c + 1 < COLCT:
                tbp.append((r, c + 1))
            if r - 1 >= 0:
                tbp.append((r - 1, c))
            if r + 1 < ROWCT:
                tbp.append((r + 1, c))

        return image


# Question URL: https://neetcode.io/problems/flood-fill/question
# Solution: Matrix BFS -- runtime O(n*m), space O(n*m)
#
sol_test = Solution()
print(sol_test.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
