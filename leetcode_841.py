# Keys and Rooms
class Solution:

# Backtracking Solution
    def canVisitAllRooms(self, rooms: [[int]]) -> bool:
        self.all_rooms = False
        self.no_of_rooms = len(rooms)
        self.s = {x for x in range(self.no_of_rooms)}

        def backtrack(room_no, keys_in_hand, visited):
            if keys_in_hand == self.s:
                self.all_rooms = True
                return
            else:
                room_list = rooms[room_no]
                for room in room_list:
                    if room not in visited:
                        keys_in_hand.add(room)
                        visited.add(room)
                        backtrack(room, keys_in_hand, visited)

        keys_in_hand = {0}
        visited = {0}
        backtrack(0, keys_in_hand, visited)
        return self.all_rooms


s = Solution()
print(s.canVisitAllRooms(rooms=[[1], [2], [3], []]))
print(s.canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]))
