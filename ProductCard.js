import React from 'react';
import './ProductCard.css';  // Importing the specific CSS file for ProductCard

function ProductCard({ product, placeOrder }) {
  return (
    <div className="product-card">
      <h4>{product.name}</h4>
      <p>{product.description}</p>
      <p>Quantity Available: {product.quantity}</p>
      <button onClick={() => placeOrder(product.id)}>Place Order</button>
    </div>
  );
}

export default ProductCard;
