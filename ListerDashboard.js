import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ProductCard from '../components/ProductCard';

function ListerDashboard() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    async function fetchProducts() {
      const response = await axios.get('http://localhost:5000/api/view_items/1'); // 1 is the Lister ID
      setProducts(response.data.items);
    }
    fetchProducts();
  }, []);

  return (
    <div className="container">
      <h2>Lister Dashboard</h2>
      <button>Add New Item</button>
      <div>
        <h3>Your Products</h3>
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

export default ListerDashboard;
