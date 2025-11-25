from django.test import TestCase

# Create your tests here.
import pytest
from django.urls import reverse
from .models import Todo

@pytest.mark.django_db
def test_create_todo():
    todo = Todo.objects.create(title="Test Task", is_completed=False)
    assert todo.title == "Test Task"
    assert todo.is_completed is False

@pytest.mark.django_db
def test_home_view(client):
    # Create a test TODO
    Todo.objects.create(title="View Test", is_completed=False)

    # Call the home page
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    assert b"View Test" in response.content
