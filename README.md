# Restapi-status

This django rest api project allow you to perform a CRUD operation on status post


## Table of Contents

- [Example](#example)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Features](#features)
- [Deployment](#deployment)

## Example
```python
# Detail View class for each status
class StatusAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # authentication_classes  = []
    serializer_class        = StatusSerializer
    queryset                = Status.objects.all()
    lookup_field            = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

```

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


## Prerequisites

What things you need to install the software and how to install them

- python3 env
- some pip packages



## Installation

To get a development env running:

>clone this repo to your local machine
```
git clone https://github.com/JohnJohnsonOkah/restapi-status.gitt
```

>install requirements
```
pip install -r requirements.txt
```

>setup database
```
python manage.py makemigrations
python manage.py migrate
```

>create superuser
```
python manage.py createsuperuser
```

>run development server
```
python manage.py runserver
```
... 👯 Now development server is up and running...



## Features

- CRUD on status api
- 



## Deployment

Additional notes about how to deploy this on a live system