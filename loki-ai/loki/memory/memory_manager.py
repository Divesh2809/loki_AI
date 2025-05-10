class MemoryManager:
    def __init__(self):
        self.memory = {}

    def store_information(self, key, value):
        self.memory[key] = value

    def retrieve_information(self, key):
        return self.memory.get(key, None)

    def clear_memory(self):
        self.memory.clear()

    def get_all_memory(self):
        return self.memory.copy()