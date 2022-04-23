# Design Browser History
class ListNode:
    """Represents webpage"""
    def __init__(self, page, prev=None, next=None):
        self.page = page
        self.prev = prev
        self.next = next

class BrowserHistory:
    """Implementing a double linked list"""
    def __init__(self, homepage: str):
        self.current = ListNode(page=homepage)

    def visit(self, url: str) -> None:
        new = ListNode(page=url, prev=self.current)
        self.current.next = new
        self.current = new

    def back(self, steps: int) -> str:
        while steps and self.current.prev:
            steps -= 1
            self.current = self.current.prev
        return self.current.page

    def forward(self, steps: int) -> str:
        while steps and self.current.next:
            steps -= 1
            self.current = self.current.next
        return self.current.page

# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory('leetcode.com')
obj.visit('google.com')
obj.visit('facebook.com')
obj.visit('youtube.com')
print(obj.back(1))
print(obj.back(1))
print(obj.forward(1))
obj.visit('linkedin.com')
print(obj.forward(2))
print(obj.back(2))
print(obj.back(7))

