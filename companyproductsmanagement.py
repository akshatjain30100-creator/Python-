class CompanyProduct:
    def __init__(self):
        self.comp_name = ""
        self.prod_name = ""
        self.mfg_month = ""
        self.mfg_year = 0
        self.exp_month = ""
        self.exp_year = 0
        self.price = 0.0
        self.qty = 0.0
        self.tot_price = 0.0

    def input_data(self):
        self.comp_name = input("Enter the company name: ")
        print(f"Company name is {self.comp_name}")

        self.prod_name = input("Enter the product name: ")
        print(f"Product name is {self.prod_name}")

        print("Enter the manufacturing date (Month & Year)")
        self.mfg_month = input("Enter month: ")
        print(f"Manufacturing Month: {self.mfg_month}")
        self.mfg_year = int(input("Enter year: "))
        print(f"Manufacturing Year: {self.mfg_year}")

        print("Enter the expiry date (Month & Year)")
        self.exp_month = input("Enter month: ")
        print(f"Expiry Month: {self.exp_month}")
        self.exp_year = int(input("Enter year: "))
        print(f"Expiry Year: {self.exp_year}")

        self.price = float(input("Enter the price: "))
        print(f"Price is {self.price:.2f}")

        self.qty = float(input("Enter the quantity: "))
        print(f"Quantity is {self.qty:.2f}")

        self.tot_price = self.price * self.qty
        print(f"Total price: {self.tot_price:.2f}")


def main():
    products = []
    for i in range(3):
        print(f"\n--- Enter details for Product {i+1} ---")
        p = CompanyProduct()
        p.input_data()
        products.append(p)

    print("\n--- Summary of Products ---")
    for i, p in enumerate(products, start=1):
        print(f"\nProduct {i}:")
        print(f"Company Name     : {p.comp_name}")
        print(f"Product Name     : {p.prod_name}")
        print(f"Mfg Date         : {p.mfg_month} {p.mfg_year}")
        print(f"Exp Date         : {p.exp_month} {p.exp_year}")
        print(f"Price            : {p.price:.2f}")
        print(f"Quantity         : {p.qty:.2f}")
        print(f"Total Price      : {p.tot_price:.2f}")


if __name__ == "__main__":
    main()
