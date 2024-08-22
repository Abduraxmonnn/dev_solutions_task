# Project
from brand import Brand


class Model(Brand):
    """
    Represents a model entity associated with a brand.

    Attributes:
        brand_name (str): The name of the brand.
        model_name (str): The name of the model.
    """

    def __init__(self, brand_name: str, model_name: str):
        """
        Initializes a new Model object.

        Args:
            brand_name (str): The name of the brand.
            model_name (str): The name of the model.
        """
        super().__init__(brand_name=brand_name)
        self.model_name = model_name

    @property
    def model(self):
        """
        Gets the model name.

        Returns:
            str: The model name.
        """
        return self.model_name

    @model.setter
    def model(self, new_name: str):
        """
        Sets the model name.

        Args:
            new_name (str): The new model name.
        """
        self.model_name = new_name
