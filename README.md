# FastApi-Microservice-Python

Learning Python microservice

## SpringBoot vs Python

| Spring Boot            | FastAPI (Industry Standard) | Explanation       |
| ---------------------- | --------------------------- | ----------------- |
| @RestController        | app/api/                    | Controllers       |
| @Service               | app/services/               | Business Logic    |
| @Repository            | app/repositories/           | Data Access Layer |
| @Entity + @Table       | app/entity/                 | Database Models   |
| application.properties | app/core/config.py + .env   | Configuration     |
| Spring Security (JWT)  | app/core/security.py        | Auth & JWT        |
| JUnit + Mockito        | pytest + unittest           | Unit Testing      |

## How Does request Work?

- FastAPI automatically injects the Request object when a request comes in.
- This object contains all the request details (headers, body, query params, etc.).
- Since we attached db to request.state in the middleware, we can retrieve it inside any endpoint.

## How This Compares to Spring Boot

| FastAPI (request: Request)                   | Spring Boot (HttpServletRequest)                              |
| -------------------------------------------- | ------------------------------------------------------------- |
| Request is passed as a parameter             | HttpServletRequest is injected automatically                  |
| We can store the DB session in request.state | We can store values in HttpSession (e.g., request attributes) |
| Middleware manages DB lifecycle globally     | Filters/Interceptors manage global request-level logic        |
