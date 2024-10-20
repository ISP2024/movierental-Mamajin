from rental import Rental


class Customer:
    """A customer who rents movies."""

    def __init__(self, name: str):
        """Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        """Add a rental for this customer."""
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self):
        """Get the customer's name."""
        return self.name

    def total_amount(self):
        """Calculates the total amount and frequent renter points for all rentals."""
        total = 0
        frequent_renter_points = 0
        statement = ""  # Initialize the statement

        for rental in self.rentals:
            frequent_renter_points += rental.get_rental_points()

            # Add a detail line to the statement
            statement += "{:40s}  {:6d} {:6.2f}\n".format(
                rental.get_movie().get_title(),
                rental.get_days_rented(),
                rental.get_price()
            )

            total += rental.get_price()

        return total, frequent_renter_points, statement

    def statement(self):
        """Create a statement of rentals for the current period."""
        statement = f"Rental Report for {self.name}\n\n"
        header_fmt = "{:40s}  {:6s} {:6s}\n"
        statement += header_fmt.format("Movie Title", "  Days", " Price")

        total, frequent_renter_points, rental_details = self.total_amount()
        statement += rental_details  # Add rental details to the statement

        # Footer: Summary of charges and frequent renter points
        statement += "\n"
        statement += "{:40s}  {:6s} {:6.2f}\n".format("Total Charges", "", total)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement

