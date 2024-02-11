from typing import List

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output:        [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image
        
        self.fill(image,  sr, sc, color, image[sr][sc])
        
        return image
        
    def fill(self, image, sr, sc, chosenColour, startingColour):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]): return
        
        if image[sr][sc] != startingColour: return
        
        image[sr][sc] = chosenColour
        
        self.fill(image, sr - 1, sc, chosenColour, startingColour)
        self.fill(image, sr + 1, sc, chosenColour, startingColour)
        self.fill(image, sr, sc - 1, chosenColour, startingColour)
        self.fill(image, sr, sc + 1, chosenColour, startingColour)
        
        
        
        