# PYON

This module helps you load and save data in a simple text format called PYON.

## load(file, target=None)
- **What it does:** Reads a PYON file and turns its content into a Python dictionary.
- **Parameters:**
  - `file`: The file to read from.
  - `target` (optional): A group name to load only data from that group.
- **How it works:**
  - Skips empty lines and lines starting with "--".
  - Splits each line by ":" to get the group, key, and value.
  - Converts the value into the correct Python type.
- **Example:**
  ```
  user:
      name:John Doe
      age:30
  ```
  becomes:
  ```python
  {'user': {'name': 'John Doe', 'age': 30}}
  ```

## save(file, data, category, overwrite=False, indent=4)
- **What it does:** Writes data into a PYON file.
- **Parameters:**
  - `file`: The file to write to.
  - `data`: A dictionary with the data to save.
  - `category`: The group name under which the data will be stored.
  - `overwrite`: If `True`, it replaces the old data. If `False`, it merges new data with the old data.
  - `indent`: Number of spaces to use for indentation (default is 4).
- **How it works:**
  - Reads the existing file.
  - Keeps data from other groups intact.
  - Updates the data for the given category.
  - Writes all the data back to the file.
- **Example:**
  ```python
  data = {
      "user": {
          "name": "Alice",
          "age": 25,
          "active": True
      }
  }

  with open("data.pyon", "r+") as file:
      save(file, data, "user")
  ```
  This will save the `user` data into the file in PYON format.