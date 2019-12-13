# Django Todo app RESTful API

Methods available:

- Get all todos:

  ```
  GET /api/todos
  ```

- Create todo:

  ```
  POST /api/todos
  ```

  ```json
  {
    "title": "Create README",
    "tags": ["Very important", "Open Source", "Python"]
  }
  ```

- Get one todo:

  ```
  GET /api/todos/:id
  ```

- Update todo:

  ```
  PUT /api/todos/:id
  ```

  ```json
  {
    "title": "Create README for Todo app",
    "tags": ["Very important", "Previous tags will be deleted"]
  }
  ```

- Delete todo:

  ```
  DELETE /api/todos/:id
  ```
