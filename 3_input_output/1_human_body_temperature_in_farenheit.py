# human_normal_body_temperature_in_fahrenheit
normal_body_temperature = float(input("enter the normal body temperature: "))
temperature_in_degree = (normal_body_temperature - 32) * 5 / 9
print(
    """the temperature in celsius is :{normal_body_temperature}""".format(
        normal_body_temperature=temperature_in_degree
    )
)
