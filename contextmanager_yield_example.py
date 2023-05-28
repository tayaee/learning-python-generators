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
    print(f'obj.some_property = {obj.some_property} before with')
    with simple_context_manager(obj):
        print(f'obj.some_property = {obj.some_property} inside with')
        print(f'obj.some_property = {obj.some_property} inside with')
    print(f'obj.some_property = {obj.some_property} after with')

# obj.some_property = 5 before with
# Starting with 5
# obj.some_property = 6 inside with
# obj.some_property = 6 inside with
# Reverted to 5
# obj.some_property = 5 after with
