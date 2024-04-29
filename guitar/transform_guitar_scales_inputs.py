def apply_template(staff_music):
    return """\\version "2.22.2"

\\include "../common.ly"
    """

def transform_inputs():
    csv = "guitar-scales-inputs.csv"
    with open(csv, 'r') as file:
        for line in file:
            tokens = line.split(',')
            # for t in tokens:
            #     print(t)
            filename = f"{tokens[0]}.ly"
            key = tokens[1]
            staff_music = tokens[2].rstrip('\n')

            contents = apply_template(staff_music)

            with open(filename, 'w') as output_file:
                output_file.write(contents)



if __name__ == "__main__":
    transform_inputs()
