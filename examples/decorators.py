import os

def example(title="Untitled", border_design="="):
    def example_decorator(function):
        def print_banner():
            border = border_design * len(title)
            print(border)
            print(title.upper())
            print(border, os.linesep)

        def example_wrapper(*args, **kwargs):
            print_banner()
            return_value = function(*args, **kwargs)
            print(os.linesep)
            return return_value

        return example_wrapper

    return example_decorator
