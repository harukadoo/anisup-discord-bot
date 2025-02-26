#------------Метакласи для розширення функціоналу------------

# class MetaCommandRegistry(type):
#     def __new__(cls, name, bases, dct):
#         new_cls = super().__new__(cls, name, bases, dct)

#         if hasattr(new_cls, "command_name"):
#             registered_commands[new_cls.command_name] = new_cls
#         return new_cls
