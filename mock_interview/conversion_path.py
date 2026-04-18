# We have a directed graph representing currency conversion routes:

# rates = {
#     "USD": {"EUR": 0.9,  "GBP": 0.75},
#     "EUR": {"JPY": 130},
#     "GBP": {"INR": 100}
# }
# Implement
# def find_conversion_path(src: str, dst: str) -> list[str] | None:
#     """
#     Return one valid path of currency codes from `src` to `dst`
#     (e.g., ["USD", "EUR", "JPY"]).
#     If no path exists, return None.
#     """
# Bonus – also return the total conversion rate along that path.

class Conversion:
    def __init__(self):
        pass

    def find_conversion_path(self, rates: dict, source: str, target: str, rate_amount = 1, path=None, visited=None) -> list | None:
        if path is None: path = []
        if visited is None: visited = set()
        path.append(source)
        visited.add(source)
        if source == target: return (path, rate_amount)
        
        if source not in rates:
            return
        
        for (currency, value) in rates[source].items():
            if currency not in visited:
                curr_path = self.find_conversion_path(rates, currency, target, rate_amount*value, path[:], visited)
                if curr_path:
                    return curr_path

rates = {
    "USD": {"EUR": 0.9,  "GBP": 0.75},
    "EUR": {"JPY": 130},
    "GBP": {"INR": 100}
}

convert = Conversion()
print(convert.find_conversion_path(rates, "USD", "INR")) # 0.75*100 = 75
print(convert.find_conversion_path(rates, "INR", "INR")) # 1
print(convert.find_conversion_path(rates, "INR", "JPY")) # None
print(convert.find_conversion_path(rates, "JPY", "GBP")) # None
print(convert.find_conversion_path(rates, "GBP", "INR")) # 100
print(convert.find_conversion_path(rates, "USD", "JPY")) # 0.9 * 130 = 117
print(convert.find_conversion_path(rates, "BRL", "USD")) # None
print(convert.find_conversion_path(rates, "", "")) # ""





        