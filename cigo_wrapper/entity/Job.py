import json

from cigo_wrapper.entity.JobGeocoding import JobGeocoding
from cigo_wrapper.entity.JobProgress import JobProgress
from cigo_wrapper.entity.VehicleTracking import VehicleTracking


# All dates are in ISO-8601 format


class Job:
    # In the documentation the create request used 'type' as the key but in the response it uses 'job_type'
    type = None
    quick_desc = None
    confirmation_status = None
    email = None
    # [0.0, 0.0]
    coordinates = None
    apartment = None
    postal_code = None
    balance_owed = None
    comment = None
    # {"start": "0:00 AM", "end": "0:00 AM"}
    time_frame = None
    # ['124', ]
    invoices = None
    # order reference id
    reference_id = None
    customer_reference_id = None

    actions = None

    # Data from Cigo
    job_id = None
    status = None

    # post_staging attributes
    tracking = None
    progress = None
    scheduling = None
    geocoding = None
    digital_signature = None
    payment_collection = None
    review = None

    def __init__(self, date=None, customer_first_name="", customer_last_name="", phone_number="", address="",
                 skip_staging=True):
        # Job created will skip the staging area (Import Tool) if True
        self.skip_staging = skip_staging

        self.date = date
        self.first_name = customer_first_name
        self.last_name = customer_last_name

        self.phone_number = phone_number
        # Cigo use the mobile_number to send an sms with the tracking code
        self.mobile_number = phone_number

        self.address = address

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    @classmethod
    def from_geocoding(cls, job_response):
        response_dic = job_response
        job = cls()
        for key in response_dic.keys():
            if key == 'job_id' and response_dic[key] is not None:
                job.job_id = response_dic[key]
            elif key == 'status' and response_dic[key] is not None:
                job.status = response_dic[key]
            elif key == 'progress' and response_dic[key] is not None:
                job.progress = JobProgress.from_json(response_dic[key])
            elif key == 'coordinates' and response_dic[key] is not None:
                job.coordinates = response_dic[key]  # is the location of the Job (the target location)
            elif key == 'geocoding' and response_dic[key] is not None:
                job.geocoding = JobGeocoding.from_json(response_dic[key])
            elif key == 'vehicle_tracking' and response_dic[key] is not None:
                job.vehicle_tracking = VehicleTracking.from_json(response_dic[key])
        return job

    @classmethod
    def from_json(cls, job_response):
        response_dic = job_response
        job = cls(date=response_dic['date'], customer_first_name=response_dic['first_name'],
                  customer_last_name=response_dic['last_name'],
                  phone_number=response_dic['phone_number'],
                  address=response_dic['address'])

        for key, value in response_dic.items():
            if key == 'post_staging':
                for post_key, post_value in value.items():
                    if post_key == 'progress':
                        post_value = JobProgress.from_json(post_value)
                    elif post_key == 'geocoding':
                        post_value = JobGeocoding.from_json(post_value)
                    setattr(job, post_key, post_value)
            else:
                setattr(job, key, value)

        return job
