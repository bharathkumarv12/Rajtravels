// Sample data representing products (can be fetched from a server or static)
const products = [
  { id: 1, name: "Product 1", image: "../static/images/f1.png", cost: 25.99 },
  { id: 2, name: "Product 2", image: "../static/images/f2.png", cost: 39.99 },
];

// Function to populate cart items
function populateCartItems() {
  const cartItemsDiv = document.querySelector('.cart_items');
  let totalCost = 0;

  // Clear existing content
  cartItemsDiv.innerHTML = '';

  // Iterate through each product and create HTML for it
  products.forEach(product => {
      // Create a card-like structure for each product
      const card = document.createElement('div');
      card.classList.add('card');
      card.innerHTML = `
          <img src="${product.image}" alt="${product.name}" class="product_image">
          <div class="product_details">
              <h4>${product.name}</h4>
              <p>Cost: $${product.cost.toFixed(2)}</p>
              <button class="remove_button" data-id="${product.id}">Remove</button>
          </div>
      `;
      // Append each card to the cart items container
      cartItemsDiv.appendChild(card);

      // Calculate total cost
      totalCost += product.cost;
  });

  // Update total cost in the HTML
  const totalCostSpan = document.querySelector('.total_cost');
  totalCostSpan.textContent = `$${totalCost.toFixed(2)}`;

  // Add event listener for remove buttons
  const removeButtons = document.querySelectorAll('.remove_button');
  removeButtons.forEach(button => {
      button.addEventListener('click', function() {
          const productId = parseInt(button.getAttribute('data-id'));
          removeProduct(productId);
      });
  });
}

// Function to remove a product from the cart
function removeProduct(productId) {
  // Find index of the product in the array based on productId
  const index = products.findIndex(product => product.id === productId);
  if (index !== -1) {
      // Remove the product from the products array
      products.splice(index, 1);
      // Repopulate the cart items
      populateCartItems();
  }
}

// Call the function to populate cart items when the page loads
document.addEventListener('DOMContentLoaded', () => {
  populateCartItems();
});
