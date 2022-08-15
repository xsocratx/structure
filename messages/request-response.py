import Request_pb2 as Request
import Response_pb2 as Response


def serialize_to_string(Request):
    import time

    my_request = Request.Request()

    step1 = Request.Request.Step()
    step1.id = 1
    step1.parent_id = 0
    step1.duration = time.time()
    step1.name = "Step_1"

    step2 = Request.Request.Step()
    step2.id = 2
    step2.parent_id = 1
    step2.duration = time.time()
    step2.name = "Step_2"

    step3 = Request.Request.Step()
    step3.id = 3
    step3.parent_id = 2
    step3.duration = time.time()
    step3.name = "Step_3"


    my_request.step_id = 1
    my_request.steps.extend([step1])
    my_request.steps.extend([step2])
    my_request.steps.extend([step3])

    print("Hello, World")
    print("From function")

    with open("./serializedFile", "wb") as fd:
        fd.write(my_request.SerializeToString())

#--------------------------------------------

def parse_from_string(Request, Response):
    import time

    my_request = Request.Request()

    with open("./serializedFile", "rb") as fd:
        my_request.ParseFromString(fd.read())

    print(my_request)

    my_response = Response.Response()

    hierarchical_step1 = Response.Response.HierarchicalStep()
    hierarchical_step1.name = "Hierarchical_Step_1"
    hierarchical_step1.duration = time.time()

    hierarchical_step2 = Response.Response.HierarchicalStep()
    hierarchical_step2.duration = time.time()
    hierarchical_step2.name = "Hierarchical_Step_2"

    my_response.hierarchical_step.extend([hierarchical_step1])
    my_response.hierarchical_step.extend([hierarchical_step2])

    max_duration_name = ''
    max_duration_step = 0
    for step in my_request.steps:
        if(step.duration > max_duration_step):
            max_duration_step = step.duration
            max_duration_name = step.name


    print(max_duration_step)
    
    my_response.max_duration_step_name = max_duration_name
    my_response.max_duration_step_duration = max_duration_step

    with open("./serialized_file_2", "wb") as fd:
        fd.write(my_response.SerializeToString())

    with open("./serialized_file_2", "rb") as fd:
        my_response.ParseFromString(fd.read())

    print(my_response)

#--------------------------------------------

serialize_to_string(Request)
parse_from_string(Request, Response)




















