class Command:
    """Command to be executed"""
    def __init__(self, name: str):
        """
        :param name: name of the command (is used to get method from Strategy)
        """
        self.name = name

    def configure(self, **kwargs: str):
        """
        Configure commands params and dependencies
        :param kwargs:
        """
        pass
