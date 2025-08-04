class ListManager:
    def __init__(self):
        """Initialize empty 1D and 2D lists."""
        self.list_1d = []
        self.list_2d = []

    def create_1d_list(self, elements):
        """Create a 1D list from a comma-separated string of numbers."""
        try:
            self.list_1d = [int(x) for x in elements.split(",")]
            print("1D list created:", self.list_1d)
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

    def add_element(self, element):
        """Add an element to the 1D list."""
        try:
            self.list_1d.append(int(element))
            print("Element added. Current 1D list:", self.list_1d)
        except ValueError:
            print("Invalid input. Please enter a number.")

    def remove_element(self, element):
        """Remove the first occurrence of an element from the 1D list."""
        try:
            element = int(element)
            if element in self.list_1d:
                self.list_1d.remove(element)
                print("Element removed. Current 1D list:", self.list_1d)
            else:
                print(f"Element {element} not found in the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def sort_list(self, order):
        """Sort the 1D list in ascending or descending order."""
        if not self.list_1d:
            print("1D list is empty. Create a list first.")
            return
        if order.lower() in ["asc", "ascending"]:
            self.list_1d.sort()
            print("1D list sorted in ascending order:", self.list_1d)
        elif order.lower() in ["desc", "descending"]:
            self.list_1d.sort(reverse=True)
            print("1D list sorted in descending order:", self.list_1d)
        else:
            print("Invalid order. Use 'asc' or 'desc'.")

    def search_element(self, element):
        """Search for an element in the 1D list and return its index."""
        try:
            element = int(element)
            if element in self.list_1d:
                index = self.list_1d.index(element)
                print(f"Element {element} found at index {index}.")
            else:
                print(f"Element {element} not found in the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def create_2d_list(self, rows, cols):
        """Create a 2D list with user-input values."""
        try:
            rows, cols = int(rows), int(cols)
            if rows < 1 or cols < 1:
                print("Rows and columns must be positive.")
                return
            print(f"Enter {rows * cols} numbers for a {rows}x{cols} matrix (row-wise, comma-separated):")
            values = input().split(",")
            if len(values) != rows * cols:
                print(f"Expected {rows * cols} numbers, got {len(values)}.")
                return
            self.list_2d = [[int(values[i * cols + j]) for j in range(cols)] for i in range(rows)]
            print("2D list created:")
            self.print_2d_list()
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    def transpose_2d_list(self):
        """Transpose the 2D list (swap rows and columns)."""
        if not self.list_2d:
            print("2D list is empty. Create a 2D list first.")
            return
        self.list_2d = [list(row) for row in zip(*self.list_2d)]
        print("2D list transposed:")
        self.print_2d_list()

    def print_1d_list(self):
        """Print the current 1D list."""
        if not self.list_1d:
            print("1D list is empty.")
        else:
            print("Current 1D list:", self.list_1d)

    def print_2d_list(self):
        """Print the current 2D list in a readable format."""
        if not self.list_2d:
            print("2D list is empty.")
        else:
            for row in self.list_2d:
                print(" ".join(map(str, row)))

    def display_menu(self):
        """Display the interactive menu."""
        print("\nList Manager Menu:")
        print("1. Create 1D List")
        print("2. Add Element to 1D List")
        print("3. Remove Element from 1D List")
        print("4. Sort 1D List")
        print("5. Search Element in 1D List")
        print("6. Create 2D List")
        print("7. Transpose 2D List")
        print("8. Print 1D List")
        print("9. Print 2D List")
        print("0. Exit")

    def run(self):
        """Run the interactive menu."""
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (0-9): "))
                if choice == 0:
                    print("Exiting...")
                    break
                if choice not in range(1, 10):
                    print("Invalid choice. Please select 0-9.")
                    continue
                if choice == 1:
                    elements = input("Enter numbers (comma-separated, e.g., 1,2,3): ")
                    self.create_1d_list(elements)
                elif choice == 2:
                    element = input("Enter element to add: ")
                    self.add_element(element)
                elif choice == 3:
                    element = input("Enter element to remove: ")
                    self.remove_element(element)
                elif choice == 4:
                    order = input("Enter order (asc/desc): ")
                    self.sort_list(order)
                elif choice == 5:
                    element = input("Enter element to search: ")
                    self.search_element(element)
                elif choice == 6:
                    rows = input("Enter number of rows: ")
                    cols = input("Enter number of columns: ")
                    self.create_2d_list(rows, cols)
                elif choice == 7:
                    self.transpose_2d_list()
                elif choice == 8:
                    self.print_1d_list()
                elif choice == 9:
                    self.print_2d_list()
            except ValueError:
                print("Invalid input. Please enter a valid number for choice.")

if __name__ == "__main__":
    manager = ListManager()
    manager.run()