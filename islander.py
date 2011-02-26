class Islander:
    """Represents an individual on an island"""

    isle = None

    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

    def __repr__(self):
        return self.name