from concurrent.futures import ThreadPoolExecutor

class CustomList:
    def __init__(self):
        self.size = 0  # Ukuran kubus
        self.arr = []
    
    def add(self,element):
        self.arr.append(element)
        self.size += 1

    def reset(self):
        self.arr = []
        self.size = 0


    def isIn(self,element):
        if self.size <= 5:
            return self.__checkElement(element)
        else:
            return self.__checkElementConcurrent(element)

    def __checkElement(self,element):
        for el in self.arr:
            if element == el:
                return True
            
    
    def __checkElementConcurrent(self,element):
        # Ensure we always divide into 4 chunks
        chunk_size = max(1, len(self.arr) // 4)
        chunks = [self.arr[i:i + chunk_size] for i in range(0, len(self.arr), chunk_size)]

        with ThreadPoolExecutor() as executor:
            # Submit tasks for each chunk
            futures = [executor.submit(self.__check_in_chunk, chunk, element) for chunk in chunks]
            
            # Wait for any future to complete successfully
            for future in futures:
                if future.result():  # If any future returns True
                    return True
        return False

    def __check_in_chunk(self, chunk, element):
        return element in chunk

