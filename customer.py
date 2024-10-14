class Customer:
    """A customer who rents movies."""

    def __init__(self, name):
        """Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        """Add a rental to this customer."""
        self.rentals.append(rental)

    def total_amount(self):
        """Calculate total charges and frequent renter points."""
        total_charge = 0
        frequent_renter_points = 0
        for rental in self.rentals:
            total_charge += rental.get_charge()
            frequent_renter_points += rental.get_rental_points()
        return total_charge, frequent_renter_points

    def statement(self):
        """Generate a statement for the customer."""
        total_charge, frequent_renter_points = self.total_amount()
        result = f"Rental Record for {self.name}\n"
        for rental in self.rentals:
            result += f"\t{rental.get_movie().get_title()}: {rental.get_charge():.2f}\n"
        result += f"Total charges: {total_charge:.2f}\n"
        result += f"Frequent renter points earned: {frequent_renter_points}\n"
        return result
