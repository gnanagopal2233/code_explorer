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
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def main():
    calc = Calculator()
    result = calc.add(10, 5)
    print(f"Addition: {result}")
    result = calc.subtract(10, 5)
    print(f"Subtraction: {result}")
    result = calc.multiply(10, 5)
    print(f"Multiplication: {result}")
    result = calc.divide(10, 5)
    print(f"Division: {result}")

if __name__ == "__main__":
    main()
"""




# Get explanation
explanation = explainer.explain_code(sample_code)
print("Explanation:", explanation)

# Generate documentation
documentation = explainer.generate_docs(sample_code)
print("\nDocumentation:", documentation)
