# Cigo API Library

## Cigo API Doc

Cigo is a last mile delivery software solution [link to Cigo website](https://cigotracker.com/)

You can visit the API Doc to get a general idea [API Doc](https://cigotracker.com/api/)

## Factory Cigo Library

This library will help you connect with the api by calling the methods in [`CigoConnect.py`](https://github.com/CODED-Factory/Cigo-API-Library/blob/main/cigo_wrapper/network/CigoConnect.py).

We have 4 entities a `Job`, `JobSearch`, `JobAction` and `Itinerary`.

1. [`Job`](https://github.com/CODED-Factory/Cigo-API-Library/blob/main/cigo_wrapper/entity/Job.py) is used to create and retrieve Jobs
2. [`JobSearch`](https://github.com/CODED-Factory/Cigo-API-Library/blob/main/cigo_wrapper/entity/JobSearch.py) is used to search for a job
3. [`JobAction`](https://github.com/CODED-Factory/Cigo-API-Library/blob/main/cigo_wrapper/entity/JobAction.py) is used to create and retrieve JobActions
4. [`JobGeocoding`](https://github.com/CODED-Factory/Cigo-API-Library/blob/main/cigo_wrapper/entity/JobGeocoding.py) is used retrieve job geocoding
5. [`JobProgress`](https://github.com/CODED-Factory/Cigo-API-Library/blob/main/cigo_wrapper/entity/JobProgress.py) is used retrieve job progress
6. [`Itinerary`](https://github.com/CODED-Factory/Cigo-API-Library/blob/main/cigo_wrapper/entity/Itinerary.py) is used to retrieve itineraries
7. [`VehicleTracking`](https://github.com/CODED-Factory/Cigo-API-Library/blob/main/cigo_wrapper/entity/VehicleTracking.py) is used to retrieve itineraries

### Get Started with `CigoConnect`

Start by calling `CigoConnect()` with `debug`, `account_id` and `auth_key`. `debug` is used to switch between demo and production endpoints.

> cc = CigoConnect(debug, account_id, auth_key)

Now you can use `cc` to call the endpoint functions, each function has a docstring that shows the return.

- `Retrieve` functions return:
  - Object / List of objects.
  - Raise an exception if the response has an error.
- `Search` functions return:
  - List of ids.
  - Raise an exception if the response has an error.
- `Create` / `Delete` / `Update` functions always return the response from the endpoint.

You can find a sample on how to use `CigoConnect.py` in [`example.py`](https://github.com/CODED-Factory/Cigo-API-Library/blob/main/example.py)
