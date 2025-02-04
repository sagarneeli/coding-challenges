"""
The application we're building allows users to upload a CSV containing data that we need to parse into a data structure
that we can then use to (for example) putthat data into our database.

A sample CSV file might look like:

product_id,product_name,stock_remaining\n
1,"pixel,5",55\n
2,pixelbook,31\n
3,nesthub,2\n
product_list =
{
    1: (pixel5, 55)
    2:
}
                        0     1
product_list["1"] => Product(pixel5, 55)
product_list["2"][1] => {pixel5: 55}
[{
    product_id: 1
    product_name: pixel5
    .../
},

]

N ->





Write a function
parseCSV(inputString)


 that can parse this CSV and return the parsed data in an appropriate data structure. It is up to you what data structure you choose to return the data in.
"""

from typing import List


def parseCSV(input_str: str) -> List[dict]:
    lines = input_str.split("\n")
    column_names = lines[0].split(",")
    result = []
    for line in lines[1:]:
        col_values = line.split(",")
        dictionary = {}
        for col_name, col_val in zip(column_names, col_values):
            dictionary[col_name] = col_val
        result.append(dictionary)

    return result


# string = "1,'pixel,5',55"
# print(string.split(",")) =>
# ['1', "'pixel5'", '55']

# def splitWords(line):
#     for ch in line:
csv_data = "product_id,product_name,stock_remaining\n1,pixel5,55\n2,pixelbook,31\n3,nesthub,2\n"
print(parseCSV(csv_data))
