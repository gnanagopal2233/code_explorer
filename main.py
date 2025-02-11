from explainer import CodeExplainer
import os

# Get token from environment variable
token = os.getenv('HUGGINGFACE_TOKEN')

# Initialize explainer
if token is None:
    raise ValueError("HUGGINGFACE_TOKEN environment variable is not set")
explainer = CodeExplainer(token)

# Example code to analyze
sample_code = """
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Top item: {stack.peek()}")
    print(f"Stack size: {stack.size()}")
    print(f"Popped item: {stack.pop()}")
    print(f"Stack size after pop: {stack.size()}")

if __name__ == "__main__":
    main()
"""




# Get explanation
explanation = explainer.explain_code(sample_code)
print("Explanation:", explanation)

# Generate documentation
documentation = explainer.generate_docs(sample_code)
print("\nDocumentation:", documentation)
