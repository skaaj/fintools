from dataclasses import fields, asdict

class DataClassIO:
    cache = {}

    @classmethod
    def update_cache(cls, targetClass):
        cls.cache[targetClass] = {f.name for f in fields(targetClass) if f.init}

    @classmethod
    def read(cls, targetClass, sourceDict):
        if targetClass not in cls.cache:
            cls.update_cache(targetClass)
        requiredFields = cls.cache[targetClass]
        providedFields = {k : v for k, v in sourceDict.items() if k in requiredFields}
        return targetClass(**providedFields)

    @staticmethod
    def write(obj):
        return asdict(obj)
