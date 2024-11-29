def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for arg, annotation in zip(args, annotations.items()):
            expect = annotation[1]
            if not isinstance(arg, expect):
                raise TypeError(f"Argument '{annotation[0]}' must be {expect} type!")
        
        for kwarg_name, value in kwargs.items():
            if kwarg_name in annotations and not isinstance(value, annotations[kwarg_name]):
                raise TypeError(f"Argument '{kwarg_name}' must be {annotations[kwarg_name]} type!")

        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: bool, b: bool) -> int:
    return a + b
