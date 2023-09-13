import json
import xml.etree.ElementTree as ET

json_data = {
    "fullname":"George",
    "characteristics":{
    "sex":"male",
    "age":27
    },
    "skills":["smart","strong"],
    "experience":[
        {
        "position":"developer",
        "workplace":"netflix",
        "salary":"7000"
        },
        {
        "position":"engineer",
        "workplace":"facebook",
        "id_card":56117,
        "Country":"Scotland"
        }
    ]
    }


# Function to convert JSON to XML
def json_to_xml(json_data):
    root = ET.Element("root")
    json_to_xml_recursive(json_data, root)
    return ET.tostring(root, encoding="utf-8", method="xml")

def json_to_xml_recursive(json_data, element):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            sub_element = ET.SubElement(element, key)
            json_to_xml_recursive(value, sub_element)
    elif isinstance(json_data, list):
        for item in json_data:
            json_to_xml_recursive(item, element)
    else:
        element.text = str(json_data)

xml_data = json_to_xml(json_data)

print(xml_data)