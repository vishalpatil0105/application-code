FROM python:3.12

WORKDIR /app
# Copy the requirements file 
COPY ./requirements.txt /app/

# Install the Python dependencies
RUN pip install -r /app/requirements.txt

# Copy the rest of the application
COPY ./board /app/board/

# Expose the port the app runs on
EXPOSE 8000

ENTRYPOINT ["python", "-m", "flask", "--app", "board", "run", "--port", "8000"]
 