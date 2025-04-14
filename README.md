## Setup Instructions for FastAPI Backend
1. Clone the repo:
   
   ```code
   git clone https://github.com/fxdnz/fast-api.git
   ```
2. Navigate to the project folder:

   ```code
   cd fast-api
   ```
3. Create a virtual environment and activate it:
   
   - Windows:
     ```code
     python -m venv venv && venv\Scripts\activate
     ```
   - macOS/Linux:
     ```code
     python3 -m venv venv && source venv/bin/activate
     ```
4. Install dependencies:

   ```code
   pip install -r requirements.txt
   ```
5. Start the development server:

   ```code
   uvicorn main:app --reload
   ```
## API Endpoints from FastAPI Backend
### GET `https://fast-api-ffw9.onrender.com/tasks` 
- **Description**: Returns a list of all tasks.
- **Method**: GET
- **Response**:
   ```json
    [
     {
       "title": "fast api testing edit",
       "is_completed": false,
       "id": 9
     },
     {
       "title": "edit man diay ni",
       "is_completed": true,
       "id": 8
     }
   ]
   ```
### POST `https://fast-api-ffw9.onrender.com/tasks` 
- **Description**: Creates a new task.
- **Method**: POST
- **Request Body**:
  ```json
  {
     "title": "testing filter",
     "is_completed": false,
  },
  ```
- **Response**:
   ```json
   [
     {
       "title": "fast api testing edit",
       "is_completed": false,
       "id": 9
     },
     
     {
       "title": "testing filter",
       "is_completed": false,
       "id": 26
      },
     {
       "title": "edit man diay ni",
       "is_completed": true,
       "id": 8
     }
   ]
   ```
### PUT `https://fast-api-ffw9.onrender.com/tasks/{task_id}` 
- **Description**: Updates an existing task by its ID.
- **Method**: PUT
- **Request Body**:
  ```json
  {
     "title": "testing filter edit",
     "is_completed": false
   }
  ```
- **Response**:
   ```json
    {
     "title": "testing filter edit",
     "is_completed": false,
     "id": 26
    }
   ```
### DELETE `https://fast-api-ffw9.onrender.com/tasks/{task_id}` 
- **Description**: Deletes a task by its ID.
- **Method**: DELETE
- **Response**:
   ```json
   {
     "message": "Task deleted successfully"
   }
   ```
## Routes for task filtering based on completion status
### GET `https://fast-api-ffw9.onrender.com/tasks/filter` 
- **Description**: Returns tasks filtered by their completion status.
- **Method**: GET
- **Query Parameter**: `is_completed` (`true` or `false`)
- **Response**:
   ```json
   [
     {
       "title": "fast api testing edit",
       "is_completed": false,
       "id": 9
     },
     {
       "title": "testing filter",
       "is_completed": true,
       "id": 26
     },
     {
       "title": "edit man diay ni",
       "is_completed": true,
       "id": 8
     }
   ]
   ```
- **Response if True**: `https://fast-api-ffw9.onrender.com/tasks/filter?is_completed=true`
  ```json
  [
     {
        "title":"edit man diay ni",
        "is_completed":true,
        "id":8
     }
  ]
  ```
- **Response if False**: `https://fast-api-ffw9.onrender.com/tasks/filter?is_completed=false`
  ```json
  [
     {
        "title":"fast api testing edit",
        "is_completed":false,"id":9
     },
     {
        "title":"testing filter edit",
        "is_completed":false,"id":26
     }
  ]
  ```

## Live Deployed Links
**Frontend**: 
```code
https://fastapi-front.netlify.app/
```

**Backend**: 
```code
https://fast-api-ffw9.onrender.com/
```
