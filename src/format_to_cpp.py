def to_cpp_array(name, arr):
    values= ", ".join([str(v) for v in arr])
    if name == "Intercept":
        return f"float {name}= {values};"

    else:
        return f"float {name}[]= {{{values}}};"


def export_arduino_params(name, value, operation):

    with open("../exports/arduino_model_params.h", operation) as f:

        f.write(to_cpp_array(name, value))
        f.write("\n")