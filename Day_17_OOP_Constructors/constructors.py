class TrainingSession:
    def __init__(self, model_name, epochs=10):
        self.model_name = model_name
        self.epochs = epochs
        self.is_trained = False  # Default state

    def start_training(self):
        print(f"Training {self.model_name} for {self.epochs} epochs...")
        self.is_trained = True


# Testing default vs custom parameters
session1 = TrainingSession("VisionPro")
session2 = TrainingSession("ChatBot", epochs=50)

session1.start_training()
print(f"{session1.model_name} trained: {session1.is_trained}")
