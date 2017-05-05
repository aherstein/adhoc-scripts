import mysql.connector

user = 'root'
password = 'root'
database = 'adam_compligo'

the_form_id = 3024118
the_page_id = 5843


def get_connection():
    return mysql.connector.connect(user=user, password=password,
                                   host='127.0.0.1', port='8889', database=database)


def get_form_object_id(record_id):
    query = "SELECT right_object_id \
             FROM object_relationships \
             WHERE id IN \
                   (SELECT object_relationship_id \
                    FROM record_relationships \
                    WHERE left_record_id = {0}) \
                   AND right_relation_name LIKE '%Process%' \
                   AND right_object_id IS NOT NULL".format(record_id)

    cnx = get_connection()
    results = cnx.cursor()
    results.execute(query)
    results_list = results.fetchall()
    return results_list[0][0]


def get_form_record_id(record_id):
    query = "SELECT right_record_id \
             FROM record_relationships \
             WHERE left_record_id = {0} \
                   AND object_relationship_id = \
                       (SELECT id \
                        FROM object_relationships \
                        WHERE id IN \
                              (SELECT object_relationship_id \
                               FROM record_relationships \
                               WHERE left_record_id = {0}) \
                              AND right_relation_name LIKE '%Process%' \
                              AND right_object_id IS NOT NULL)".format(record_id)

    cnx = get_connection()
    results = cnx.cursor()
    results.execute(query)
    results_list = results.fetchall()
    return results_list[0][0]


def get_properties(record_id):
    query = "SELECT object_properties.name, property_values.value, property_values.property_id FROM ( \
                 SELECT * FROM record_object0{1}_property_value_integers WHERE record_id = {0} \
                 UNION ALL \
                 SELECT * FROM record_object0{1}_property_value_strings WHERE record_id = {0} \
                 UNION ALL \
                 SELECT * FROM record_object0{1}_property_value_texts WHERE record_id = {0} \
                 UNION ALL \
                 SELECT * FROM record_object0{1}_property_value_datetimes WHERE record_id = {0} \
          ) property_values \
          JOIN object_properties ON property_values.property_id = object_properties.id" \
        .format(get_form_record_id(record_id), get_form_object_id(record_id))

    cnx = get_connection()
    results = cnx.cursor()
    results.execute(query)
    results_list = results.fetchall()
    return results_list


def get_page(record_id):
    query = "SELECT type, field_path, element, set_settings \
             FROM nav_page_cell_fragments WHERE cell_id = ( \
                 SELECT id FROM nav_page_cells WHERE page_id = {0} \
             ) ORDER BY in_order" \
        .format(record_id)
    cnx = get_connection()
    results = cnx.cursor()
    results.execute(query)
    results_list = results.fetchall()
    return results_list


def get_page_with_data(form_id, page_id):
    properties = get_properties(form_id)
    page = get_page(page_id)

    page_with_data = {}

    for (type, field_path, element, set_settings) in page:
        if field_path is not None:
            page_property_id = int(field_path.split(':')[1])

            for (name, value, form_property_id) in properties:
                if form_property_id == page_property_id:
                    page_with_data[form_property_id] = {
                        'page_type': str(type),
                        'page_element': str(element),
                        'page_set_settings': str(set_settings),
                        'form_name': str(name),
                        'form_value': str(value)
                    }
                    break

    return page_with_data

# Get form
# print(get_properties(the_form_id))
# print(get_page(the_page_id))
print(get_page_with_data(the_form_id, the_page_id))