from contextlib import contextmanager


# yield와 @contextmanager가 동시에 필요하다.
@contextmanager
def simple_context_manager(obj):
    try:
        print(f"Starting with {obj.some_property}")
        obj.some_property += 1
        yield
    finally:
        obj.some_property -= 1
        print(f"Reverted to {obj.some_property}")


class Some_obj(object):
    def __init__(self, arg):
        self.some_property = arg


if __name__ == '__main__':
    obj = Some_obj(5)
    with simple_context_manager(obj):
        print(obj.some_property)
        print(obj.some_property)
