class ModuleCheck:
  def __init__(self):
    print(ModuleCheck.__module__)

def module_name_far():
  print(f"The name of the module is {__name__}")