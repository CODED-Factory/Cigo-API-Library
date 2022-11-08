import json


# All dates are in ISO-8601 format
class JobAction:
    action_id = None
    id = None
    status = None
    status_counters = None
    type = None
    description = None
    value = None
    unit_weight = None
    total_weight = None
    unit_volume = None
    total_volume = None
    piece_count = None
    piece_count_unit = None
    quantity = None
    quantity_unit = None
    handle_time = None
    stop_location_id = None
    invoice_number = None
    external_reference_id = None
    shipping_barcode = None
    create_datetime = None

    def __init__(self, ref_id, action_type, description):
        self.id = ref_id
        self.type = action_type
        self.description = description

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    @classmethod
    def from_json(cls, action_response):
        response_dic = action_response
        action = cls(
            ref_id=response_dic['id'],
            description=response_dic['description'],
            action_type=response_dic['type'],
        )

        for key, value in response_dic.items():
            setattr(action, key, value)

        return action
