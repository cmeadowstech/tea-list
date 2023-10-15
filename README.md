# [Teahookup.com](https://teahookup.com/)

Website built with Django, Bootstrap, and HTMX. Hosted on Fly.io with a PostGres database.

Quick and dirty documentation provided by ChatpGPT. Will try to flesh this out more at a later date. 

```markdown
# Django Settings Configuration

This document provides an overview of the key settings in the Django `settings.py` file for the `config` project. The configuration is generated by `django-admin startproject` and uses Django 4.1.6.

## Table of Contents
- [Project Path Configuration](#project-path-configuration)
- [Security](#security)
- [Application Configuration](#application-configuration)
- [Database Configuration](#database-configuration)
- [Static File Delivery](#static-file-delivery)
- [Media Storage Backend](#media-storage-backend)
- [Allauth Settings](#allauth-settings)
- [Miscellaneous Settings](#miscellaneous-settings)
- [Logging](#logging)
- [django_comments_xtd Settings](#django_comments_xtd-settings)
```

## Project Path Configuration

Django's project paths are configured as follows:

```python
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")
```

- `BASE_DIR`: The root directory of the project.
- `.env` file: Configuration settings are read from this file.

## Security

Key security settings include:

```python
SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = env("DJANGO_DEBUG") != "False"
ALLOWED_HOSTS = ["*"]
```

- `SECRET_KEY`: Secret key used for cryptographic operations.
- `DEBUG`: Enable or disable debug mode.
- `ALLOWED_HOSTS`: List of allowed hostnames or IP addresses.

## Application Configuration

The `INSTALLED_APPS` list defines the installed Django applications:

```python
INSTALLED_APPS = [
    # List of installed apps
]
```

- This list includes standard Django apps like `django.contrib.admin` and custom apps like `tealist`.

## Database Configuration

Database settings are defined as follows:

```python
DJANGO_DB = env.db()
DATABASES = {"default": env.db()}
```

- `DJANGO_DB` and `DATABASES`: Configuration for the project's default database.

## Static File Delivery

Static file settings for serving CSS, JavaScript, and images:

```python
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

- `STATIC_ROOT`: Directory for collected static files.
- `STATIC_URL`: URL prefix for static files.
- `STATICFILES_STORAGE`: Storage backend for static files.

## Media Storage Backend

Settings for handling media files (e.g., uploaded user files):

```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

- `MEDIA_ROOT`: Directory where uploaded media is saved.
- `MEDIA_URL`: Public URL for media files.

## Allauth Settings

Settings related to the "allauth" authentication framework:

```python
SITE_ID = 4
LOGIN_REDIRECT_URL = "/"
```

- `SITE_ID`: Site ID for the allauth framework.
- `LOGIN_REDIRECT_URL`: URL to redirect to after login.

## Miscellaneous Settings

```python
REQUEST_BASE_URL = "https://tealist.fly.dev/"
```

- Miscellaneous settings like the base URL for requests.

## Logging

Logging configuration settings:

```python
LOGGING = {
    # Logging configuration
}
```

- Configures log handlers and formatters.

## django_comments_xtd Settings

```python
COMMENTS_APP = "django_comments_xtd"
```

- Configures the `django_comments_xtd` app for extended commenting functionality.
