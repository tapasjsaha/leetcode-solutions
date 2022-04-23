# Destroying Asteroids
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: [int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
            else:
                return False
        return True


s = Solution()
print(s.asteroidsDestroyed(mass=10, asteroids=[3, 9, 19, 5, 21]))
print(s.asteroidsDestroyed(mass=5, asteroids=[4, 9, 23, 4]))
print(s.asteroidsDestroyed(mass=5, asteroids=[6]))
