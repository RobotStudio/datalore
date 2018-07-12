

def bay_sync(controller, on_change):

    def decorator(cls, on_change):
        class Wrapper:
            def __init__(self, *args, **kwargs):
                self.wrapped = cls(*args, **kwargs)
                self.down = self.wrapped.data

            def upward_action(self, *args, **kwargs):
                return on_change(*args, **kwargs)

            def __setitem__(self, key, item):
                if getattr(self, "wrapped", None) is not None:
                    if key not in self.up or self.up[key] != value:
                        controller.update_model(key, value)
                    if key not in self.down or self.down[key] != value:
                        controller.update_domain(key, value)
                    return setattr(self.wrapped, key, value)
                self.__dict__[key] = item

            def __getitem__(self, key):
                return self.__dict__[key]

            def __repr__(self):
                return repr(self.__dict__)

            def __len__(self):
                return len(self.__dict__)

            def __delitem__(self, key):
                del self.__dict__[key]

            def clear(self):
                return self.__dict__.clear()

            def copy(self):
                return self.__dict__.copy()

            def has_key(self, k):
                return k in self.__dict__

            def update(self, *args, **kwargs):
                return self.__dict__.update(*args, **kwargs)

            def keys(self):
                return self.__dict__.keys()

            def values(self):
                return self.__dict__.values()

            def items(self):
                return self.__dict__.items()

            def pop(self, *args):
                return self.__dict__.pop(*args)

            def __cmp__(self, dict_):
                return self.__cmp__(self.__dict__, dict_)

            def __contains__(self, item):
                return item in self.__dict__

            def __iter__(self):
                return iter(self.__dict__)

            def __unicode__(self):
                return unicode(repr(self.__dict__))

        return Wrapper

    return decorator


class KVCtrl:
    data: dict = {}

    def __init__(self, on_change):
        self.on_change = on_change

    def update_domain(self, attr, val):
        print(f"Updated attribute {attr}: {val}")

    def update_model(self, attr, val):
        self.on_change(attr, val)
        print(f"Updates to attribute {attr}: {val}")


if __name__ == "__main__":
    def changed(attr, val):
        print(f"Backend reports: {attr} = {val}")

    @bay_sync(KVCtrl, changed)
    class Dict(dict):
        pass


    v = Dict()
    v['asht'] = 'thsa'
    print(f"v: {v}")
    #print(f"""Set?: {v["asht"] = "thsa"}""")
    #print(f"""Set?: {v["asht"] = "1234"}""")
