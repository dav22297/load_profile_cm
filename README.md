
### Application Structure


```
app/
├── requirements.txt
├── modules_registration.json
├── __init__.py
├── api_v1/
│    ├── __init__.py
│    ├── endpoints/
│        ├── __init__.py
│        └── ...
├── register/
│    └──__init__.py
├── commons/
│    └── __init__.py
├── tests/
│    └── ...
├── models/
│    └── ...
├── extensions/
│    └── __init__.py
└── modules/
     ├── requirements.txt
     ├── __init__.py
     └── ...

```
* `app/requirements.txt` - The list of Python (PyPi) requirements.
* `app/modules_registration.json` - This regroup all parameters of the calculation modules that the main API will need to work properly.
* `app/__init__.py` - Launche the entire application.
* `app/register/__init__.py` - The entrypoint of the registration of the CM to the main webservice. This is the first action that the application is doing 
* `app/api_v1/__init__.py` - The entrypoint to this RESTful API Server (Flask application is created here).
* `app/api_v1/endpoints/__init__.py` - 
* `app/extensions/__init__.py` - All extensions (ex. SQLAlchemy) are initialized here and can be used in the application by importing as, for example, 
    `from app.extensions import db`.
* `app/commons/` - This regroup the features that can be used by the API and modules.
* `app/models/` - 
* `app/modules/` - This regroup all business modules (features, treatments, algorithmes) that can be called by API endpoint.


### modules_registration.json




```json


```