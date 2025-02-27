#--------------Допоміжні функції та дескриптори-------------

import discord

class NonEmptyString: #des
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not value or not isinstance(value, str):
            raise ValueError(f"{self.name} не может быть пустой строкой!")
        instance.__dict__[self.name] = value


def log_command(func):
    async def wrapper(interaction: discord.Interaction, *args, **kwargs):
        print(f"Command {func.__name__} called by user {interaction.user}")
        return await func(interaction, *args, **kwargs)
    return wrapper

registered_commands = {}

def register_command(name):
    def decorator(func):
        print(f"Registering command: {name}") 
        registered_commands[name] = func
        return func
    return decorator
