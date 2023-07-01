import csv


with open("airports.csv", "r") as input_file:
    reader = csv.reader(input_file)
    input_data = list(reader)


# modify the data (here, were adding a prefix to each value)
output_data = [["Modified " + value for value in row] for row in input_data]

# open the output csv file for writing
with open("output.csv", "w", newline="") as output_file:
    writer = csv.writer(output_file)
    writer.writerows(output_data)


# open the second input csv file for reading
with open("output.csv", "r") as second_input_file:
    second_reader = csv.reader(second_input_file)
    second_input_data = list(second_reader)


# modify the second data (here, we're converting values to uppercase)
final_output_data = [[value.upper() for value in row] for row in second_input_data]


# open the final output.csc file writing
with open("final_output.csv", "w", newline="") as final_output_file:
    final_writer = csv.writer(final_output_file)
    final_writer.writerows(final_output_data)

