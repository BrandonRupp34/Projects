import java.util.*;

class ItemToPurchase {

	// Initialized default values

	private String itemName = "none";
	private String itemDescription = "none";
	private int itemPrice = 0;
	private int itemQuantity = 0;

	// The majority of the setters and getters of the program

	public void setName(String itemName) {
		this.itemName = itemName;
	}

	public String getName() {
		return itemName;
	}

	public int getPrice() {
		return itemPrice;
	}

	public void setPrice(int itemPrice) {
		this.itemPrice = itemPrice;
	}

	public int getQuantity() {
		return itemQuantity;
	}

	public void setQuantity(int itemQuantity) {
		this.itemQuantity = itemQuantity;
	}

	public void setDescription(String itemDescription) {
		this.itemDescription = itemDescription;
	}

	public String getDescription() {
		return itemDescription;
	}

	public int priceOfQuantity() {
		return itemPrice * itemQuantity;
	}

	public void setAttributes(String name, String description, int price, int quantity) {
		this.itemName = name;
		this.itemDescription = description;
		this.itemPrice = price;
		this.itemQuantity = quantity;
	}

	// Methods that print the item name, cost, quantity and description.

	public void printItemCost() {
		System.out.println(itemName + " " + itemQuantity + " @ $" + itemPrice + " = $" + (itemPrice * itemQuantity));
	}

	public void printItemDescription() {
		System.out.println(itemName + ": " + itemDescription);
	}

}