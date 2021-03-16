import pytest
from django.urls import reverse
from rest_framework import status

from students.models import Course


@pytest.mark.django_db
def test_course_get(api_client, course_factory):
    course = course_factory()
    url = reverse("courses-detail", args=(course.id,))

    resp = api_client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['id'] == course.id


@pytest.mark.django_db
def test_courses_create(api_client, course_factory):
    courses = course_factory(_quantity=5)
    url = reverse("courses-list")

    resp = api_client.get(url)
    assert resp.status_code == status.HTTP_200_OK
    assert [course['id'] for course in resp.json()] == [course.id for course in courses]
    assert len(resp.json()) == 5


@pytest.mark.django_db
def test_courses_id_filter(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse("courses-list")
    for course in courses:
        resp = api_client.get(url, {'id': course.id})
        assert resp.status_code == status.HTTP_200_OK
        assert resp.json()[0]['id'] == course.id
        assert len(resp.json()) == 1


@pytest.mark.django_db
def test_courses_name_filter(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse("courses-list")
    for course in courses:
        resp = api_client.get(url, {'name': course.name})
        assert resp.status_code == status.HTTP_200_OK
        assert resp.json()[0]['name'] == course.name
        assert len(resp.json()) == 1


@pytest.mark.django_db
def test_course_create(api_client):
    url = reverse("courses-list")
    resp = api_client.post(url, {'name': 'Django-15'})
    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.json()['name'] == 'Django-15'


@pytest.mark.django_db
def test_course_patch(api_client):
    course = Course.objects.create(name='Django-15')
    url = reverse("courses-detail", args=(course.id,))
    resp = api_client.patch(url, {'name': 'Django-16'})
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()['name'] == 'Django-16'


@pytest.mark.django_db
def test_course_delete(api_client):
    course = Course.objects.create(name='Django-15')
    url = reverse("courses-detail", args=(course.id,))
    resp = api_client.delete(url)
    assert resp.status_code == status.HTTP_204_NO_CONTENT
