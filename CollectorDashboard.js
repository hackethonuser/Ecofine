import React, { useState, useEffect } from 'react';
import { fetchItems, placeOrder } from '../api'; // Import API helper functions
import ProductCard from '../components/ProductCard';

function CollectorDashboard() {
  const [items, setItems] = useState([]);

  // Fetch available items for collectors when the component mounts
  useEffect(() => {
    async function getItems() {
      try {
        const fetchedItems = await fetchItems();  // Fetch items from the backend
        setItems(fetchedItems);
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    }

    getItems();
  }, []); // Empty dependency array to run once after the initial render

  // Handle placing an order
  const handlePlaceOrder = async (itemId) => {
    try {
      const response = await placeOrder(itemId, 1, 1); // Example with collector_id = 1 and quantity = 1
      alert('Order placed successfully!');
    } catch (error) {
      console.error('Error placing order:', error);
      alert('Failed to place the order.');
    }
  };

  return (
    <div className="container">
      <h2>Collector Dashboard</h2>
      <h3>Browse Available Items</h3>
      <div className="product-list">
        {items.length === 0 ? (
          <p>No items available to order.</p>
        ) : (
          items.map((item) => (
            <ProductCard
              key={item.id}
              product={item}
              placeOrder={handlePlaceOrder}  // Pass the placeOrder function to ProductCard
            />
          ))
        )}
      </div>
    </div>
  );
}

export default CollectorDashboard;
