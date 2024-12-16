# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED 1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the current directory contents into the container
COPY . /app/

# Step 5: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Expose the port that Django will run on (default is 8000)
EXPOSE 8000

# Step 7: Set the default command to run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
