```javascript
// script.js: Frontend logic for the application
class Laptop {
    constructor(id, name, description, price, image) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.price = price;
        this.image = image;
    }
}

class LaptopStore {
    constructor() {
        this.laptops = [];
    }

    async fetchLaptops() {
        try {
            const response = await fetch('https://example.com/api/laptops');
            const data = await response.json();
            this.laptops = data.map(laptop => new Laptop(laptop.id, laptop.name, laptop.description, laptop.price, laptop.image));
            this.renderLaptopList();
        } catch (error) {
            console.error('Error fetching laptops:', error);
        }
    }

    renderLaptopList() {
        const laptopList = document.getElementById('laptop-list');
        laptopList.innerHTML = '';
        this.laptops.forEach(laptop => {
            const laptopCard = document.createElement('div');
            laptopCard.classList.add('laptop-card');
            laptopCard.innerHTML = `
                <img src="${laptop.image}" alt="${laptop.name}">
                <h2>${laptop.name}</h2>
                <p>${laptop.description}</p>
                <p>Price: $${laptop.price}</p>
                <button>Add to Cart</button>
            `;
            laptopList.appendChild(laptopCard);
        });
    }
}

const store = new LaptopStore();
store.fetchLaptops();
```

###