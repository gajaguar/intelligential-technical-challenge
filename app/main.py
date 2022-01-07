def snail(array: list) -> list:
    """
    Convert a 2D array of integers into a 1D array in snail order.
    The array will be 2D rows x columns with minimum size 2 x 2.
    """
    assert len(array) >= 2, "Array must have at least 2 rows"
    for element in array:
        assert len(element) >= 2, "Array must have at least 2 columns"
        assert len(element) == len(array[0]), "All rows must be the same length"
        assert all(isinstance(item, int) for item in element), "Array must contain only integers"

    result = []
    rows = len(array)
    columns = len(array[0])
    total = rows * columns
    lap = 0

    while len(result) < total:
        # to right
        for i in range(lap, columns - lap):
            result.append(array[lap][i])
        # to down
        for i in range(lap + 1, rows - lap):
            result.append(array[i][columns - lap - 1])
        # to left
        for i in range(columns - lap - 2, lap - 1, -1):
            result.append(array[rows - lap - 1][i])
        # to up
        for i in range(rows - lap - 2, lap, -1):
            result.append(array[i][lap])
        lap += 1
    return result

if __name__ == "__main__": 
    from os import system
    import json


    def ui(message: str):
        system("clear")
        print("Welcome to the Snail Game (NOT Squid XD)\n")
        print(f"{message}")
         
    instruction = "Insert a 2D array of integers, eg. [[1, 2], [3, 4]]"
    ui(f"{instruction}\n")
    array_as_string = input()
    array = json.loads(array_as_string)
    reordered_array = snail(array)
    ui(f"The result is: {reordered_array}")
