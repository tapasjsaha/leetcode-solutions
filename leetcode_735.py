# Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: [int]) -> [int]:
        stack = []
        for asteroid in asteroids:
            while True:
                # run until new astroid is pushed in stack
                if not stack:
                    # stack is empty = no prior astroid present
                    stack.append(asteroid)
                    break
                elif asteroid > 0:
                    # this astroid going right so will not colide with watever is there in stack
                    stack.append(asteroid)
                    break
                elif stack[-1] > 0 and asteroid < 0:
                    # this astoid is going left and existing astroid is going right = colide
                    last = stack.pop()
                    if abs(last) == abs(asteroid):  # both same size
                        break
                    elif abs(last) > abs(asteroid):  # existing astroid is bigger
                        stack.append(last)
                        break
                    else:  # new astroid is bigger, will continue to check for it
                        continue
                else:
                    # this astroid is going left and existing astroid is also going left
                    stack.append(asteroid)
                    break
        return stack


s1 = Solution()
print(s1.asteroidCollision(asteroids=[5, 10, -5]))
print(s1.asteroidCollision(asteroids=[8, -8]))
print(s1.asteroidCollision(asteroids=[10, 2, -5]))
print(s1.asteroidCollision(asteroids=[-2, -1, 1, 2]))
