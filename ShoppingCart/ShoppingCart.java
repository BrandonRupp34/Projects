import java.util.*;
import java.util.ArrayList;

class ShoppingCart {

	// Default values of the item attributes

	private String customerName = "none";
	private String currentDate = "January 1, 2016";
	private ArrayList<ItemToPurchase> cartItems = new ArrayList<ItemToPurchase>();

	// Default constructor

	ShoppingCart() {
	}

	Scanner scan = new Scanner(System.in);
	int i = 0;

	// Setters and getters

	public void nameDate(String name, String date) {
		this.customerName = name;
		this.currentDate = date;
	}

	public String getCustomerName() {
		return customerName;
	}

	public String getDate() {
		return currentDate;
	}

	// Add item method / Creates an object to hold defined characteristics

	public void addItem(ItemToPurchase itemToAdd) {
		cartItems.add(itemToAdd);
	}

	// Uses boolean to check if the cart is empty. If the cart is empty, the method
	// outputs that nothing was modified. If the cart is not empty, the method
	// allows you to remove an item from the cart.

	public void removeItem(String itemToRemove) {
		boolean bool = false;
		if (!cartItems.isEmpty()) {
			for (i = 0; i < cartItems.size(); i++) {
				if (cartItems.get(i).getName().equals(itemToRemove)) {
					bool = true;
					cartItems.remove(i);
					break;
				} else {
					bool = false;
				}
			}
		}

		if (!bool) {
			System.out.println("Item not found in cart. Nothing modified.");
		}
	}

	// Modifies the quantity of an item in the cart while also checking to see if
	// the item's attributes are still at their default quantity. If the values are
	// still at default, the method prints that the item was not found.

	public void modifyItem(ItemToPurchase newItemAttributes) {
		boolean bool = false;
		//Iterates through the array and when item is found it immediately breaks out
		//of the array so that it holds the i or index.
		for (i = 0; i < cartItems.size(); i++) {

			if (cartItems.get(i).getName().compareTo(newItemAttributes.getName()) == 0) {
				bool = true;
				break;
			} else {
				bool = false;
			}
		}

		if (bool == true) {
			if (!newItemAttributes.getDescription().equals("none")) {
				cartItems.get(i).setDescription(newItemAttributes.getDescription());
			}
			if (newItemAttributes.getPrice() != 0) {
				cartItems.get(i).setPrice(newItemAttributes.getPrice());
			}
			if (newItemAttributes.getQuantity() != 0) {
				cartItems.get(i).setQuantity(newItemAttributes.getQuantity());
			}
		}

		else {
			System.out.println("Item not found in cart. Nothing modified");
		}
	}

	// Retrives amount of items in cart
	public int getNumItemsInCart() {
		int totalQuantity = 0;
		// Iterates through cart and adds all quantities together.
		for (i = 0; i < cartItems.size(); i++) {
			totalQuantity += cartItems.get(i).getQuantity();
		}
		return totalQuantity;
	}

	// Retrieves cost of cart
	public int getCostOfCart() {
		int totalCost = 0;
		// Iterates through cart and adds all prices together.
		for (i = 0; i < cartItems.size(); i++) {
			totalCost += (cartItems.get(i).getPrice() * cartItems.get(i).getQuantity());
		}
		return totalCost;
	}

	// Combines printItemCost and getCostOfCart methods to display total cost.
	public void printTotal() {
		System.out.println(customerName + "'s Shopping Cart - " + currentDate);
		System.out.println("Number of Items: " + getNumItemsInCart() + "\n");
		for (i = 0; i < cartItems.size(); i++) {
			cartItems.get(i).printItemCost();
		}
		System.out.println("\nTotal: $" + getCostOfCart());
	}

	// Utilizes getName and getDescription methods to display both.
	public void printDescriptions() {

		System.out.println(customerName + "'s Shopping Cart - " + currentDate + "\n");
		System.out.println("Item Descriptions");
		for (i = 0; i < cartItems.size(); i++) {
			System.out.print(cartItems.get(i).getName() + ": ");
			System.out.println(cartItems.get(i).getDescription());
		}
		System.out.println();
	}

}
