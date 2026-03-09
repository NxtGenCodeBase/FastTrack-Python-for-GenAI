class SecureModel:
    def __init__(self, api_key):
        self.__api_key = api_key  # Private attribute (Encapsulation)

    def run_inference(self):
        # Abstraction: User doesn't see the complex logic inside
        self.__connect_to_server()
        print("Result: Success")

    def __connect_to_server(self):
        print(f"Connecting with key: {self.__api_key[:4]}****")


model = SecureModel("sk-123456789")
model.run_inference()
# print(model.__api_key) # This would raise an AttributeError
