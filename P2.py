class ElectricityBill:
    def __init__(self, previous_reading, new_reading, cost_per_kwh, fixed_charges):
        self.previous_reading = previous_reading
        self.new_reading = new_reading
        self.cost_per_kwh = cost_per_kwh
        self.fixed_charges = fixed_charges

    def calculate_usage(self):
        return self.new_reading - self.previous_reading

    def calculate_variable_cost(self, usage):
        return usage * self.cost_per_kwh

    def calculate_total_cost(self, variable_cost):
        return variable_cost + self.fixed_charges

    def generate_bill(self):
        usage = self.calculate_usage()
        variable_cost = self.calculate_variable_cost(usage)
        total_cost = self.calculate_total_cost(variable_cost)

        bill_details = {
            "Previous Meter Reading": self.previous_reading,
            "New Meter Reading": self.new_reading,
            "Energy Consumption (kWh)": usage,
            "Cost per kWh": self.cost_per_kwh,
            "Variable Cost": variable_cost,
            "Fixed Charges": self.fixed_charges,
            "Total Amount Due": total_cost
        }
        return bill_details


# Input data
previous_reading = 1200  # Example previous reading
new_reading = 1500       # Example new reading
cost_per_kwh = 0.12      # Cost per kWh
fixed_charges = 10        # Fixed charges

# Create an instance of the ElectricityBill class
bill = ElectricityBill(previous_reading, new_reading, cost_per_kwh, fixed_charges)

# Generate the bill
bill_details = bill.generate_bill()

# Display the bill
for key, value in bill_details.items():
    print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")
