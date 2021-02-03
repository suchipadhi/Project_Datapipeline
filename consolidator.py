# From the Input and output jsonl files and structure are provided, designing the consolidator algorithm below.

import json

Priority_list = ["Partner_A",
                 "Partner_B",
                 "Partner_C"
                 ]


# reads and extracts the partner records from the file
def partner_consolidator():
    with open(r'C:\Users\SuchismitaPadhi\Project_datapipeline\Input.json', 'r') as myfile:
        data = myfile.read()

    # parse file
    obj = json.loads(data)

    # read the priority list and sort the data
    highest_partner = sorted([x for (i, x) in enumerate(Priority_list)], reverse=False)

    # show values in json file
    partner_records = []
    priority_list = [i1 for i1 in obj if i1['partner_name'] in highest_partner]

    acct_id = {k: v for k, v in priority_list[0].items() if k == 'accommodation_id'}
    acct_data = priority_list[0]['accommodation_data']
    acct_data = {k: v for k, v in acct_data.items() if k == 'accommodation_name'}
    partner_records.append([acct_id, {'accommodation_data':acct_data}])
    return partner_records


output = partner_consolidator()

# Serializing json
json_object = json.dumps(output, indent=4)


# Writing to .json
with open("Output.json", "w") as outfile:
    outfile.write(json_object)

