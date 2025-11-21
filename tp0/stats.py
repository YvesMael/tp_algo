def update_stats_data(acc:dict[str,int],value:int) ->None:
    acc["min"] = min(int(acc["min"]), value)
    acc["max"] = max(int(acc["max"]), value)
    acc["moy"] = int(acc["moy"])