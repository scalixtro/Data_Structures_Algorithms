class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
      
    def __hash(self, key):
        """
        Hash function to map keys into the address space.
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  
    
    def set_item(self, key, value) -> None:
        """
        Add a key: value pair to the hash table.
        """
        # Create the address via hash function
        index = self.__hash(key)
        # If address is None, initialize it
        if self.data_map[index] is None:
            self.data_map[index] = []
        # Add the (key, value) pair in the address
        self.data_map[index].append([key, value])
        return None
    
    def get_item(self, key):
        """
        Gets the value of a given key. If key is not in the hash table,
        returns None.
        """
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                return self.data_map[index][i][1]
            

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)