def dict_merge(dct: dict, merge_dct: dict) -> dict:
    for k, v in merge_dct.items():
        if k in dct and isinstance(dct[k], dict) and isinstance(v, dict):  # noqa
            dict_merge(dct[k], v)
        else:
            dct[k] = v
    return dct
