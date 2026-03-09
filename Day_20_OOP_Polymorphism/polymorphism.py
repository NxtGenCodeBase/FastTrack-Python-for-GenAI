class TextModel:
    def process(self, data):
        return data.lower()


class ImageModel:
    def process(self, data):
        return f"Processing image of size {len(data)}"

# Polymorphism in action


def deploy_model(model, payload):
    print(model.process(payload))


deploy_model(TextModel(), "HELLO WORLD")
deploy_model(ImageModel(), [255, 128, 0])
