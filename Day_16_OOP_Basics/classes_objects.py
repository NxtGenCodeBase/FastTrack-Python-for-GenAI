# The blueprint for an AI Model
class AIModel:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def get_info(self):
        return f"Model: {self.name} | v{self.version}"


# Creating an instance (Object)
my_model = AIModel("LLM-Core", 1.0)
print(my_model.get_info())
