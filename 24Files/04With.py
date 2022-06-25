'''with statements. This creates a temporary variable (often called f), which is only accessible
in the indented block of the with statement.'''
with open("filename.txt") as f:
   print(f.read())
'''The file is automatically closed at the end of the with statement, even if exceptions
occur within it.'''
