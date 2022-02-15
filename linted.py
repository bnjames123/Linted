'''
Lint/Linter - Errors/Spellchecker for your code
Logical Lint
   Code syntax errors
   Code with potentially unintended results
   Overly complex code (cyclomatic)
   Dangerous or unsecure code patterns
Stylistic Lint
   Code not conforming to defined conventions
Lint Rules Include:
   Rule Checker Class, an AST (Abstract Syntax Tree) visitor
   Identification code
   Explanation of Violation to user
'''

import os
import ast
from typing import NamedTuple
# Library foundation - allows operating system portability, using ASTs, and NamedTuple class

class Auditor(ast.NodeVisitor):
   # Which/Where - Parses AST nodes and collects those in violation of rules
   
   def __init__(self, violation_code):
      self.violation_code = violation_code
      self.violation_set = set()

class WhyViolation(NamedTuple):
   # Where/Why - Contains locations of violations with explanations to user
   
   node: ast.AST
   explanation: str
   
class LinterRules:
   # What - Collates all rules against which code is linted
   
   def __init__(self):
      self.auditor_set = set()
      
   def print_violations(auditor, file_name):
      for node, explanation in auditor.violation_set:
         print(
            f"{file_name}:{node.lineno}:{node.col_offset}: "
            f"{Auditor.violation_code}: {explanation}"
         )
         
   def run(self, source_path):
      # Runs all linter rules against code
      file_name = os.path.basename(source_path)
      
      with open(source_path) as source_file:
         source_code = source_file.read()
         
      tree = ast.parse(source_code)
      for auditor in self.auditor_set:
         auditor.visit(tree)
         self.print_violations(auditor, file_name)