
/*
*	Shopping Cart Con't Project - This project will allow users to create a 
*	personalized shopping cart with their Name / Date / Items. Built into said
*	shopping cart will be the functionality to create objects that hold values
*	of name, price, quantity, and a description of their characteristics. They will
*	also be able to remove items from their cart and modify the quantity of existing
*	objects.
*
*	Initial difficulties : 
*
*	Misunderstanding of how setters and getters work. Instead of
*	using the setter as intended we initially had a scanner call within the setter.
*
*	We were unsure how to have the user create new objects when they needed to create
*	them through the console.
*
*	Accessing a private arraylist within a different program also proved difficult.
*
*	Some difficulty calling certain methods from different classes.
*
*		@author Troy Rodgers
*		@author Brandon Rupp
*		@since 11/21/2019
*		@version 2.1
*	
*/

import java.util.*;

class Main {
	public static void main(String[] args) {

		// Creates a scanner and a boolean variable

		Scanner scnr = new Scanner(System.in);
		ShoppingCart shopper1 = new ShoppingCart();
		boolean contProgram = true;
		ItemToPurchase newItem;

		// Stores customer data and current date.

		System.out.println("Enter Customer's Name:");
		String customerName = scnr.nextLine();
		System.out.println("Enter Today's Date:");
		String todaysDate = scnr.nextLine();
		clearScreen();
		shopper1.nameDate(customerName, todaysDate);
		System.out.println("Customer Name: " + shopper1.getCustomerName());
		System.out.println("Today's Date: " + shopper1.getDate() + "\n");

		/*
		 * Logic behind the menu. Carries most of the workload of the code. Runs as a
		 * switch statement while boolean "contProgram" is not false. 'q' exits the
		 * program 'a' adds a new item/object 'd' removes an object 'c' changes item
		 * quantity 'i' outputs item descriptions 'o' outputs cost of individual items
		 * and total cost
		 */

		while (contProgram) {
			printMenu();
			switch (scnr.next().charAt(0)) {
			case 'q':
				contProgram = false;
				clearScreen();
				System.out.println("Thank you for using our shopping cart program. :)");
				break;
			case 'a':
				clearScreen();
				newItem = new ItemToPurchase();
				System.out.println("ADD ITEM TO CART");
				System.out.println("Enter the item name:");
				scnr.nextLine();
				String nameItem = scnr.nextLine();
				newItem.setName(nameItem);
				System.out.println("Enter the item description:");
				String describeItem = scnr.nextLine();
				newItem.setDescription(describeItem);
				System.out.println("Enter the item price:");
				int priceOfItem = scnr.nextInt();
				scnr.nextLine();
				newItem.setPrice(priceOfItem);
				System.out.println("Enter the item quantity:");
				int quantityOfItem = scnr.nextInt();
				scnr.nextLine();
				newItem.setQuantity(quantityOfItem);
				shopper1.addItem(newItem);
				break;
			case 'd':
				clearScreen();
				System.out.println("REMOVE ITEM FROM CART");
				System.out.println("Enter name of item to remove:");
				scnr.nextLine();
				shopper1.removeItem(scnr.nextLine());
				break;
			case 'c':
				clearScreen();
				ItemToPurchase item2 = new ItemToPurchase();
				System.out.println("CHANGE ITEM QUANTITY");
				System.out.println("Enter the item name:");
				scnr.nextLine();
				item2.setName(scnr.nextLine());
				System.out.println("Enter the new quantity:");
				item2.setQuantity(scnr.nextInt());
				scnr.nextLine();
				shopper1.modifyItem(item2);
				break;
			case 'i':
				clearScreen();
				System.out.println("OUTPUT ITEMS' DESCRIPTIONS");
				shopper1.printDescriptions();
				break;
			case 'o':
				clearScreen();
				System.out.println("OUTPUT SHOPPING CART");
				shopper1.printTotal();
				System.out.println();
				break;
			}
		}

		scnr.close();
	}

	// Clears the console window.

	public static void clearScreen() {
		System.out.println("\033[H\033[2J");
		System.out.flush();
	}

	// Print method for menu.

	public static void printMenu() {

		System.out.println("MENU");
		System.out.println("a - Add item to cart");
		System.out.println("d - Remove item from cart");
		System.out.println("c - Change item quantity");
		System.out.println("i - Output items' descriptions");
		System.out.println("o - Output shopping cart");
		System.out.println("q - Quit");
		System.out.println("\nChoose an option:");

	}

}