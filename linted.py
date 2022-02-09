#All manner of Library Testing
#All manner of Unit Testing
#All manner of Other Testing (Abstract Syntax Tree -ast)

'''
Logical Lint
   Code syntax errors
   Code with potentially unintended results
   Overly complex code (cyclomatic)
   Dangerous or unsecure code patterns
Stylistic Lint
   Code not conforming to defined conventions
Lint Rules Include:
   Identification code
   Explanation of Violation to user
   Rule Checker Class, an AST visitor
'''

name = input("Name: ")

print("Hello, ", name)