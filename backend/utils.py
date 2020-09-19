
def default_serialize(x):
    if hasattr(x, "__dict__"):
        result = dict(x.__dict__)
        result["class"] = x.__class__.__name__
        return result
    else:
        return repr(x)
