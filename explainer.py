from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
import ast
from langchain.schema.runnable import RunnableLambda

class CodeExplainer:
    def __init__(self, huggingface_token: str):
        # Initialize LLM with explicit parameters
        self.llm = HuggingFaceEndpoint(
            model="meta-llama/Llama-2-7b-chat-hf",
            huggingfacehub_api_token=huggingface_token,
            task="text-generation",  # Specify task explicitly
            temperature=0.5,  # Explicitly specify temperature
            model_kwargs={
                "max_length": 512  # Include max_length inside model_kwargs
            }
        )

        # Initialize text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        # Setup prompts
        self.explanation_prompt = PromptTemplate(
            input_variables=["code_snippet"],
            template="""
            Analyze this Python code and provide a detailed explanation:

            ```python
            {code_snippet}
            ```
            """
        )

    def explain_code(self, code: str) -> str:
        """Generate explanation for the provided code."""
        try:
            # Parse code
            ast.parse(code)

            # Split long code into chunks
            code_chunks = self.text_splitter.split_text(code)

            # Create explanation chain
            chain = self.explanation_prompt | self.llm

            # Generate explanations
            explanations = [chain.invoke({"code_snippet": chunk}) for chunk in code_chunks]

            return "\n\n".join(explanations)

        except SyntaxError as e:
            return f"Invalid Python code: {str(e)}"

    def generate_docs(self, code: str) -> str:
        """Generate documentation for the provided code."""
        try:
            ast.parse(code)

            # Generate documentation using LLM
            docs_prompt = PromptTemplate(
                input_variables=["code"],
                template="Generate markdown documentation for:\n```python\n{code}\n```"
            )
            chain = docs_prompt | self.llm
            documentation = chain.invoke({"code": code})

            return documentation

        except SyntaxError as e:
            return f"Invalid Python code: {str(e)}"
