# Product Service

This is the Product Service for managing product information.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Product Service is a microservice responsible for handling product-related operations such as creating, updating, and retrieving product details.

## Features
- Create new products
- Update existing products
- Retrieve product information
- Delete products

## Installation
To install and run the Product Service, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/product-service.git
    ```
2. Navigate to the project directory:
    ```sh
    cd product-service
    ```
3. Build the Docker image:
    ```sh
    docker build -t product-service .
    ```
4. Run the Docker container:
    ```sh
    docker run -p 5000:5000 product-service
    ```

## Usage
Once the service is running, you can interact with it using the following endpoints:

- `GET /products` - Retrieve a list of products
- `POST /product` - Create a new product
- `GET /product/{id}` - Retrieve a specific product by ID
- `PUT /product/{id}` - Update a specific product by ID
- `DELETE /product/{id}` - Delete a specific product by ID

## Testing
You can test the endpoints using `curl` commands as follows:

- Retrieve a list of products:
    ```sh
    curl -X GET http://localhost:5000/products
    ```
- Create a new product:
    ```sh
    curl --header "Content-Type: application/json" --request POST --data "{\"name\": \"Product 3\"}" -v http://localhost:5000/product
    ```
- Update a specific product:
    ```sh
    curl --header "Content-Type: application/json" --request PUT --data "{\"name\": \"Updated Product 2\"}" -v http://localhost:5000/product/2
    ```
- Delete a specific product by ID:
    ```sh
    curl --request DELETE -v http://localhost:5000/product/2
    ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.