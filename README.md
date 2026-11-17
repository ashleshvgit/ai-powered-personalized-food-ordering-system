# 🍽️ AI-Powered Personalized Food Ordering System

An intelligent food ordering application designed to provide personalized food recommendations based on users' dietary preferences, allergies, nutritional requirements, and wellness goals.

The project combines a Java Spring Boot-based food ordering backend with an AI-powered wellness recommendation model. The AI model is developed separately using Python, LangChain, and Google Gemini API, with integration into the Spring Boot backend using Spring AI planned as the next development phase.

## 🚀 Project Overview

Traditional food ordering applications allow users to browse and order food based primarily on restaurant menus and personal preferences.

This project aims to enhance that experience by introducing AI-powered personalized food recommendations.

Users will be able to provide their wellness profiles, including dietary preferences, food allergies, and fitness goals. The AI recommendation component will use this information to suggest suitable food options from the available restaurant food catalog.

## ✨ Key Features

### Food Ordering Backend (Implemented)

- Restaurant Management – Manage restaurant information and operations.
- Food Item Management – Perform CRUD operations on food items.
- Customer Management – Manage customer information.
- Cart Management – Add, update, and remove food items from carts.
- Order Management – Place orders and manage order status.
- DTO-based Architecture – Separate entity models from API request and response structures.
- Global Exception Handling – Handle application exceptions with structured error responses.
- Pagination and Sorting – Efficiently retrieve and organize food items and restaurant data.
- API Documentation – Document and test REST endpoints using Swagger UI and Postman.

### AI-Powered Personalization (In Progress)

- User Wellness Profiles – Capture dietary preferences, allergies, and fitness goals.
- AI Food Recommendations – Generate personalized food suggestions using Google Gemini.
- Nutritional Awareness – Consider nutritional information such as calories, protein, carbohydrates, and fats.
- Personalized Food Discovery – Recommend suitable items from the existing food catalog.
- AI Integration – Connect the recommendation model with the Spring Boot backend using Spring AI.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Java | Backend development |
| Spring Boot | REST API development |
| Spring Data JPA | Database operations |
| Hibernate | ORM and entity relationships |
| PostgreSQL | Relational database |
| Maven | Dependency management |
| Swagger/OpenAPI | API documentation |
| Postman | API testing |
| Python | AI model development |
| LangChain | LLM integration |
| Google Gemini API | AI-powered recommendations |
| Spring AI | Planned AI integration with Spring Boot |

## 🏗️ Backend Architecture

The backend follows a layered architecture:

```text
Client
  |
  v
Controller Layer
  |
  v
Service Layer
  |
  v
Service Implementation
  |
  v
Mapper Layer
  |
  v
Repository Layer
  |
  v
Hibernate / JPA
  |
  v
PostgreSQL Database
```

## 🤖 Planned AI Integration Architecture

The proposed AI workflow:

```text
             USER
               |
               v
       Spring Boot Backend
               |
               v
       User Wellness Profile
               |
               v
       AI Recommendation Service
               |
               v
            Spring AI
               |
               v
          Gemini API
               |
               v
       Personalized Recommendations
               |
               v
         Available Food Catalog
               |
               v
           Cart Management
               |
               v
          Order Placement
```

The AI component will recommend only food items retrieved from the application's available food catalog. Dietary restrictions and allergen information will be checked by the backend rather than relying solely on AI-generated responses.

## 📋 Development Roadmap

- [x] Food ordering REST API development.
- [x] Restaurant and food item management.
- [x] Customer, cart, and order management.
- [x] DTOs and global exception handling.
- [x] Pagination, sorting, and filtering.
- [x] Swagger API documentation.
- [x] Separate AI wellness recommendation model development.
- [ ] User wellness profile implementation in Spring Boot.
- [ ] Integration of the AI model using Spring AI.
- [ ] Personalized recommendations from the food catalog.
- [ ] Integration of recommendations with cart and order workflows.

## 🔮 Future Enhancements

- Personalized food discovery based on wellness goals.
- Nutrition-based food filtering.
- Recommendation history and tracking.
- Improved personalization based on user preferences.
- AI-powered conversational food assistant.

## 🔧 Getting Started

### Prerequisites

- Java 17 or later (as configured in the project).
- Maven.
- PostgreSQL.
- IntelliJ IDEA or another Java IDE.
- Postman or Swagger UI.

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/ashleshvgit/food-ordering-rest-api.git
```

**2. Navigate to the project**

```bash
cd food-ordering-rest-api
```

**3. Configure PostgreSQL**

Create a PostgreSQL database and configure the database URL, username, and password in your application configuration.

**4. Run the application**

```bash
mvn spring-boot:run
```

**5. Access API documentation**

Open Swagger UI using the configured Swagger endpoint.

## 👨‍💻 Developer

**Ashlesh V**

Java Backend Developer

GitHub: https://github.com/ashleshvgit
