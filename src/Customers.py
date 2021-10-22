from src.ReadCSVFile import ReadCSVFile

class Customers:

    def load_customers(self):
        read_csv_file = ReadCSVFile()
        customer_data = read_csv_file.get_file_data("customer.csv")
        return customer_data

    def format_customers(self):
        display = ""
        customer_data = self.load_customers()
        for counter in range(1,len(customer_data)):
            display += customer_data[counter][0] + "  \n"
        return display