import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class Customer:
    def __init__(self, name, email, phone, passport, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.passport = passport
        self.address = address

    def __str__(self):
        return f"Customer(name={self.name}, email={self.email}, phone={self.phone}, passport={self.passport}, address={self.address})"

class Trip:
    def __init__(self, destination, option, hotel, duration, price):
        self.destination = destination
        self.option = option
        self.hotel = hotel
        self.duration = duration
        self.price = price

    def __str__(self):
        return f"Trip(destination={self.destination}, option={self.option}, hotel={self.hotel}, duration={self.duration} days, price=${self.price})"

class Booking:
    def __init__(self, customer, trip):
        self.customer = customer
        self.trip = trip

    def __str__(self):
        return f"Booking(Customer={self.customer.name}, Trip={self.trip.destination})"

class TravelAgencyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SU5 Travel Agency")

        self.customers = []
        self.trips = []
        self.bookings = []
        self.create_main_page()

    def create_main_page(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=1, fill='both')
        self.load_image(self.main_frame)
        enter_button = ttk.Button(self.main_frame, text="Enter", command=self.create_widgets)
        enter_button.pack(pady=20)

    def load_image(self, frame):
        # Path to the image file
        image_path = "C:/Users/leish/OneDrive/Desktop/SUM_Python/SU5 Cover Page.jpg"  # Correct path

        # Load the image using PIL
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        # Create a label widget to display the image
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack(padx=10, pady=10)
        
    def create_widgets(self):
        self.main_frame.destroy()  # Remove the main frame

        tab_control = ttk.Notebook(self.root)

        self.customer_tab = ttk.Frame(tab_control)
        self.trip_tab = ttk.Frame(tab_control)
        self.booking_tab = ttk.Frame(tab_control)

        tab_control.add(self.customer_tab, text='Customers')
        tab_control.add(self.trip_tab, text='Trips')
        tab_control.add(self.booking_tab, text='Bookings')

        tab_control.pack(expand=1, fill='both')

        self.create_customer_tab()
        self.create_trip_tab()
        self.create_booking_tab()

    def create_customer_tab(self):
        ttk.Label(self.customer_tab, text="Name:").grid(column=0, row=0, padx=10, pady=10)
        self.customer_name = ttk.Entry(self.customer_tab)
        self.customer_name.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.customer_tab, text="Email:").grid(column=0, row=1, padx=10, pady=10)
        self.customer_email = ttk.Entry(self.customer_tab)
        self.customer_email.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.customer_tab, text="Phone:").grid(column=0, row=2, padx=10, pady=10)
        self.customer_phone = ttk.Entry(self.customer_tab)
        self.customer_phone.grid(column=1, row=2, padx=10, pady=10)
        
        ttk.Label(self.customer_tab, text="Passport:").grid(column=0, row=3, padx=10, pady=10)
        self.customer_passport = ttk.Entry(self.customer_tab)
        self.customer_passport.grid(column=1, row=3, padx=10, pady=10)
        
        ttk.Label(self.customer_tab, text="Address:").grid(column=0, row=4, padx=10, pady=10)
        self.customer_address = ttk.Entry(self.customer_tab)
        self.customer_address.grid(column=1, row=4, padx=10, pady=10)

        ttk.Button(self.customer_tab, text="Add Customer", command=self.add_customer).grid(column=1, row=5, padx=10, pady=10)

        self.customer_list = tk.Listbox(self.customer_tab)
        self.customer_list.grid(column=0, row=6, columnspan=2, padx=10, pady=10, sticky='nsew')

    def create_trip_tab(self):
        ttk.Label(self.trip_tab, text="Destination:").grid(column=0, row=0, padx=10, pady=10)
        self.trip_destination = ttk.Entry(self.trip_tab)
        self.trip_destination.grid(column=1, row=0, padx=10, pady=10)
        
        ttk.Label(self.trip_tab, text="Option").grid(column=0, row=1, padx=10, pady=10)
        self.option_var = tk.StringVar()
        options = ["Transportation", "Package Tours", "Cruises", "Flight Ticket", "Trekking"]
        self.trip_option = ttk.OptionMenu(self.trip_tab, self.option_var, *options)
        self.trip_option.grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.trip_tab, text="Hotel:").grid(column=0, row=2, padx=10, pady=10)
        self.trip_hotel = ttk.Entry(self.trip_tab)
        self.trip_hotel.grid(column=1, row=2, padx=10, pady=10)
        
        ttk.Label(self.trip_tab, text="Duration (days):").grid(column=0, row=3, padx=10, pady=10)
        self.trip_duration = ttk.Entry(self.trip_tab)
        self.trip_duration.grid(column=1, row=3, padx=10, pady=10)

        ttk.Label(self.trip_tab, text="Price:").grid(column=0, row=4, padx=10, pady=10)
        self.trip_price = ttk.Entry(self.trip_tab)
        self.trip_price.grid(column=1, row=4, padx=10, pady=10)

        ttk.Button(self.trip_tab, text="Add Trip", command=self.add_trip).grid(column=1, row=5, padx=10, pady=10)

        self.trip_list = tk.Listbox(self.trip_tab)
        self.trip_list.grid(column=0, row=6, columnspan=2, padx=10, pady=10, sticky='nsew')

    def create_booking_tab(self):
        ttk.Label(self.booking_tab, text="Customer:").grid(column=0, row=0, padx=10, pady=10)
        self.booking_customer = ttk.Combobox(self.booking_tab)
        self.booking_customer.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.booking_tab, text="Trip:").grid(column=0, row=1, padx=10, pady=10)
        self.booking_trip = ttk.Combobox(self.booking_tab)
        self.booking_trip.grid(column=1, row=1, padx=10, pady=10)

        ttk.Button(self.booking_tab, text="Create Booking", command=self.create_booking).grid(column=1, row=2, padx=10, pady=10)
        
        self.booking_list = tk.Listbox(self.booking_tab)
        self.booking_list.grid(column=0, row=3, columnspan=2, padx=10, pady=10, sticky='nsew')

        ttk.Button(self.booking_tab, text="Confirm Booking", command=self.confirm_booking).grid(column=1,row=4,padx=10,pady=10)
        
    def add_customer(self):
        name = self.customer_name.get()
        email = self.customer_email.get()
        phone = self.customer_phone.get()
        passport = self.customer_passport.get()
        address = self.customer_address.get()

        if name and email and phone and passport and address:
            customer = Customer(name, email, phone, passport, address)
            self.customers.append(customer)
            self.customer_list.insert(tk.END, str(customer))
            self.booking_customer['values'] = [customer.name for customer in self.customers]
            self.customer_name.delete(0, tk.END)
            self.customer_email.delete(0, tk.END)
            self.customer_phone.delete(0, tk.END)
            self.customer_passport.delete(0, tk.END)
            self.customer_address.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def add_trip(self):
        destination = self.trip_destination.get()
        option = self.option_var.get()
        hotel = self.trip_hotel.get()
        duration = self.trip_duration.get()
        price = self.trip_price.get()

        if destination and hotel and duration and price and option != "Please select your Purpose of travel":
            trip = Trip(destination, option, hotel, int(duration), float(price))
            self.trips.append(trip)
            self.trip_list.insert(tk.END, str(trip))
            self.booking_trip['values'] = [trip.destination for trip in self.trips]
            self.trip_destination.delete(0, tk.END)
            self.trip_hotel.delete(0, tk.END)
            self.trip_duration.delete(0, tk.END)
            self.trip_price.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def create_booking(self):
        customer_name = self.booking_customer.get()
        trip_destination = self.booking_trip.get()

        customer = next((c for c in self.customers if c.name == customer_name), None)
        trip = next((t for t in self.trips if t.destination == trip_destination), None)

        if customer and trip:
            booking = Booking(customer, trip)
            self.bookings.append(booking)
            self.booking_list.insert(tk.END, str(booking))
            #self.show_booking_confirmation(booking)  #use this script if you want to pop up details after creat booking and delete the (confirm booking function)
        else:
            messagebox.showwarning("Input Error", "Please select valid customer and trip")
            
    def confirm_booking(self):
        try:
            selected_index = self.booking_list.curselection()[0]
            selected_booking = self.bookings[selected_index]
            self.show_booking_confirmation(selected_booking)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a booking to confirm")
            
    def show_booking_confirmation(self, booking):
        customer_info = f"Customer: {booking.customer.name}, Email: {booking.customer.email}, Phone: {booking.customer.phone}, Passport: {booking.customer.passport}, Address: {booking.customer.address}"
        trip_info = f"Trip: {booking.trip.destination}, Option: {booking.trip.option} , Duration: {booking.trip.duration} days, Price: ${booking.trip.price}"

        confirmation_message = f"Booking Confirmed!\n\n{customer_info}\n{trip_info}"
        messagebox.showinfo("Booking Confirmation", confirmation_message)

def main():
    root = tk.Tk()
    app = TravelAgencyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
