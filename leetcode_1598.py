# Crawler Log Folder
class Solution:
    def minOperations(self, logs: [str]) -> int:
        # TC: O(N) and SC:O(1)
        stack = 0
        for command in logs:
            if command == "../":
                if stack == 0:
                    continue
                else:
                    stack -= 1
            elif command == "./":
                continue
            else:
                stack += 1

        return stack

# # Correct solution but memory consumption is high, TC: O(N) and SC:O(N)
#     def minOperations(self, logs: List[str]) -> int:
#         stack = []
#         for command in logs:
#             if command == "../":
#                 if len(stack) == 0:
#                     continue
#                 else:
#                     stack.pop()
#             elif command == "./":
#                 continue
#             else:
#                 stack.append(command)

#         return len(stack)

s = Solution()
print(s.minOperations(logs = ["d1/","d2/","../","d21/","./"]))
print(s.minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"]))
print(s.minOperations(logs = ["d1/","../","../","../"]))
