class Brand:
    """
    Represents a brand entity.

    Attributes:
        brand_name (str): The name of the brand.
    """

    def __init__(self, brand_name: str):
        """
        Initializes a new Brand object.

        Args:
            brand_name (str): The name of the brand.
        """
        self.brand_name = brand_name

    @property
    def brand(self):
        """
        Gets the brand name.

        Returns:
            str: The brand name.
        """
        return self.brand_name

    @brand.setter
    def brand(self, new_name: str):
        """
        Sets the brand name.

        Args:
            new_name (str): The new brand name.
        """
        self.brand_name = new_name
