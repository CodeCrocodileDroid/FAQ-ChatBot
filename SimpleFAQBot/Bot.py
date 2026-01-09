import re
import random
from datetime import datetime


class FAQChatbot:
    def __init__(self):
        self.name = "PyBot"
        self.topic = "Python Programming"
        self.responses = {
            'greeting': [
                f"Hello! I'm {self.name}, your {self.topic} assistant. How can I help you?",
                f"Hi there! I'm here to answer your {self.topic} questions.",
                f"Welcome! Ask me anything about {self.topic}."
            ],
            'farewell': [
                "Goodbye! Happy coding!",
                "See you later! Feel free to come back with more Python questions.",
                "Bye! Keep learning Python!"
            ],
            'help': [
                f"I can answer questions about: variables, functions, loops, classes, modules, and more in {self.topic}.",
                "Try asking me about Python syntax, data structures, or programming concepts."
            ],
            'unknown': [
                "I'm not sure I understand. Could you rephrase your question?",
                "I don't have an answer for that yet. Try asking about Python basics.",
                "That's an interesting question, but I'm limited to Python FAQ topics."
            ]
        }

        # Define patterns and responses for FAQ
        self.patterns = [
            # Greetings
            (r'hello|hi|hey|greetings', 'greeting'),
            (r'what is your name\?*', 'name'),

            # Farewell
            (r'bye|goodbye|exit|quit', 'farewell'),

            # Help
            (r'help|what can you do|capabilities', 'help'),

            # Python basics
            (r'what is python\?*|define python', 'python_definition'),
            (r'(how to|how do I) install python\?*', 'install_python'),
            (r'python version|which version', 'python_version'),

            # Variables and types
            (r'what is a variable\?*|define variable', 'variable'),
            (r'data types in python|python data types', 'data_types'),
            (r'string|int|float|list|tuple|dict|set', 'specific_type'),

            # Functions
            (r'what is a function\?*|define function', 'function'),
            (r'how to define a function|function syntax', 'function_syntax'),
            (r'lambda|anonymous function', 'lambda'),

            # Control flow
            (r'if statement|conditional', 'if_statement'),
            (r'for loop|while loop|loops in python', 'loops'),

            # Classes and OOP
            (r'what is a class\?*|define class', 'class'),
            (r'object oriented|OOP', 'oop'),

            # Modules and packages
            (r'import module|how to import', 'import_module'),
            (r'pip install|install package', 'install_package'),

            # Error handling
            (r'try except|error handling|exception', 'exception'),

            # Common questions
            (r'best IDE|editor for python', 'ide'),
            (r'resources to learn|learn python', 'resources'),
            (r'python vs |difference between python', 'comparison'),
        ]

        # FAQ answers
        self.faq_responses = {
            'name': f"My name is {self.name}. I'm a chatbot specialized in {self.topic}.",
            'python_definition': "Python is a high-level, interpreted programming language known for its readability and versatility. It's used for web development, data science, AI, and more.",
            'install_python': "You can install Python from python.org. Download the installer for your OS and follow the instructions. Consider using version 3.7 or higher.",
            'python_version': f"As of {datetime.now().year}, Python 3.x is recommended. The latest stable version is usually the best choice.",
            'variable': "A variable is a named location in memory that stores a value. In Python: `x = 5` creates variable x with value 5.",
            'data_types': "Python has several built-in data types: int, float, str, list, tuple, dict, set, bool, and NoneType.",
            'specific_type': "Which specific data type would you like to know about? I can explain strings, integers, lists, dictionaries, etc.",
            'function': "A function is a reusable block of code that performs a specific task. Use `def` keyword to define one.",
            'function_syntax': "Define a function with: `def function_name(parameters):` followed by indented code block. End with `return` (optional).",
            'lambda': "Lambda functions are anonymous, one-line functions: `lambda x: x*2` creates a function that doubles its input.",
            'if_statement': "Use if/elif/else for conditionals: `if x > 0: print('positive') elif x < 0: print('negative') else: print('zero')`",
            'loops': "Python has `for` loops (for iterating over sequences) and `while` loops (while condition is true).",
            'class': "A class is a blueprint for creating objects. Define with `class ClassName:` and use `__init__` method for initialization.",
            'oop': "Object-Oriented Programming in Python uses classes, objects, inheritance, polymorphism, and encapsulation.",
            'import_module': "Use `import module_name` or `from module import function`. Standard library modules don't need installation.",
            'install_package': "Use `pip install package_name` in terminal. For specific version: `pip install package_name==version`",
            'exception': "Use try/except blocks: `try: risky_code() except ExceptionType: handle_error()`",
            'ide': "Popular Python IDEs: VS Code, PyCharm, Jupyter Notebook, Spyder. Choose based on your needs.",
            'resources': "Great resources: Python.org documentation, Real Python, Corey Schafer YouTube, Automate the Boring Stuff book.",
            'comparison': "Python is generally easier to learn than languages like C++ or Java, with simpler syntax but sometimes slower execution.",
        }

    def match_pattern(self, user_input):
        """Match user input against patterns and return response type"""
        user_input = user_input.lower().strip()

        for pattern, response_type in self.patterns:
            if re.search(pattern, user_input):
                return response_type

        return None

    def get_response(self, user_input):
        """Generate response based on user input"""
        response_type = self.match_pattern(user_input)

        if response_type in self.responses:
            return random.choice(self.responses[response_type])
        elif response_type in self.faq_responses:
            return self.faq_responses[response_type]
        else:
            # Check for specific data type queries
            if 'string' in user_input.lower():
                return "Strings are sequences of characters. Use quotes: `s = 'hello'`. They're immutable and have many methods like .upper(), .split()."
            elif 'list' in user_input.lower():
                return "Lists are ordered, mutable collections: `my_list = [1, 2, 3]`. Access with indices: `my_list[0]` gives 1."
            elif 'dictionary' in user_input.lower() or 'dict' in user_input.lower():
                return "Dictionaries store key-value pairs: `d = {'key': 'value'}`. Access with keys: `d['key']` gives 'value'."
            elif 'integer' in user_input.lower() or 'int' in user_input.lower():
                return "Integers are whole numbers: `x = 42`. No size limit (except memory)."

            return random.choice(self.responses['unknown'])

    def chat(self):
        """Start the interactive chat session"""
        print(f"=== {self.name} - {self.topic} FAQ Chatbot ===")
        print("Type 'quit', 'exit', or 'bye' to end the chat.\n")

        print(random.choice(self.responses['greeting']))

        while True:
            try:
                user_input = input("\nYou: ").strip()

                if not user_input:
                    continue

                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print(f"\n{self.name}: {random.choice(self.responses['farewell'])}")
                    break

                response = self.get_response(user_input)
                print(f"{self.name}: {response}")

            except KeyboardInterrupt:
                print(f"\n\n{self.name}: {random.choice(self.responses['farewell'])}")
                break
            except Exception as e:
                print(f"{self.name}: Sorry, I encountered an error. Please try again.")


# Alternative: Using a simpler approach for specific use cases
class SimpleFAQBot:
    """A simpler version for specific FAQ handling"""

    def __init__(self):
        self.faqs = {
            r'hello|hi|hey': "Hello! How can I help you with Python today?",
            r'what is python': "Python is a popular programming language for web dev, data science, and automation.",
            r'how (to|do I) install': "Download from python.org and run the installer.",
            r'variable in python': "Use `name = value` to create variables. No declaration needed!",
            r'function in python': "Define with `def my_function():` and call with `my_function()`",
            r'list vs tuple': "Lists are mutable [1,2,3], tuples are immutable (1,2,3).",
            r'quit|exit|bye': "Goodbye! Happy coding!"
        }

    def respond(self, query):
        query = query.lower()
        for pattern, response in self.faqs.items():
            if re.search(pattern, query):
                return response
        return "I'm not sure about that. Try asking about Python installation, variables, or functions."


# Example usage
if __name__ == "__main__":
    # Create and run the chatbot
    bot = FAQChatbot()

    # Run interactive chat
    bot.chat()

    # Alternatively, test with sample questions
    print("\n" + "=" * 50)
    print("Sample Q&A Examples:")
    print("=" * 50)

    test_questions = [
        "Hello",
        "What is Python?",
        "How do I install Python?",
        "What are data types in Python?",
        "Tell me about functions",
        "What IDE should I use?",
        "How to handle errors?",
        "Explain lists in Python",
        "Goodbye"
    ]

    for question in test_questions:
        response = bot.get_response(question)
        print(f"Q: {question}")
        print(f"A: {response}\n")