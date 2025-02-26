#--------------Допоміжні функції та дескриптори-------------

# class NonEmptyString:
#     def __init__(self, name):
#         self.name = name

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name)

#     def __set__(self, instance, value):
#         if not value or not isinstance(value, str):
#             raise ValueError(f"{self.name} не может быть пустой строкой!")
#         instance.__dict__[self.name] = value


# def log_command(func):
#     async def wrapper(ctx, *args, **kwargs):
#         print(f"Команда {func.__name__} вызвана пользователем {ctx.author}")
#         return await func(ctx, *args, **kwargs)
#     return wrapper
