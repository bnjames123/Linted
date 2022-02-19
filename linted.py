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
   Rule Auditor Class, an AST (Abstract Syntax Tree) visitor
   Identification code
   Explanation of Violation to user
'''

import os
import sys
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
   
class LinterProcess:
   # What/How - Collects lint from file and provides feedback
   
   def __init__(self):
      self.auditor_set = set()
      
   def print_violations(auditor, file_name):
      for node, explanation in auditor.violation_set:
         print(
            f"{file_name}:L{node.lineno}:C{node.col_offset}: "
            f"{auditor.violation_code}: {explanation}"
         )
         
   def run(self, linted_file):
      # Advances through all rules, against which code is linted
      file_name = os.path.basename(linted_file)
      
      with open(linted_file) as source_file:
         source_code = source_file.read()
         
      tree = ast.parse(source_code)
      for auditor in self.auditor_set:
         auditor.visit(tree)
         self.print_violations(auditor, file_name)
         
class Naming:
   # What's in a name? -Optional[Shakespeare]. My name..is Neo!=Mr Anderson.
   def __init__(self, name, given_name, convention):
      self.name = name
      given_name: str
      self.convention = convention
      self.misnomer_set = []
   pass

class NamingConvention(Auditor):
   # Verifies code elements conform to PEP8 naming conventions by type
   #
   # Identify elements by type
   # Separate type from typestring, audit string by comparison
   # Store to self.violation_set if misnomer
   # Identify and store violation code
   def naming_script(naming):
      self.given_name = ast.parse(source.name)
      if self.given_name 
      pass
   def naming_class(naming):
      self.given_name = ast.ClassDef.name # take name from definition (name = class GrabThis)
      
      pass
   def naming_method(naming):
      self.given_name = ast.FunctionDef.name
      pass
   def naming_function(naming):
      self.given_name = ast.FunctionDef.name
      pass
   def naming_variable(naming):
      self.given_name = 
      pass
   def naming_constant(naming):
      self.given_name = 
      pass
   
   pass
   
class DeadVariable(Auditor):
   # Ensures variables are used
   
   pass
   
class LineLength(Auditor):
   # Keep code lines no longer than 79 characters
   
   pass
   
class Other(Auditor):
   # Describe
   
   pass
   
def main():
   linted_file_set = sys.argv[1:]
   # argv[0] always holds script name, this array holds all files to lint as arguments afterward
   
   linted = LinterProcess()
   # Collates all rules under process
   linted.auditor_set.add("AuditorClassName"("violation_code"))
   linted.auditor_set.add("AuditorClassName"("violation_code"))
   linted.auditor_set.add("AuditorClassName"("violation_code"))
   
   for linted_file in linted_file_set:
      linted.run(linted_file)
      
if __name__ == "__main__":
   main()