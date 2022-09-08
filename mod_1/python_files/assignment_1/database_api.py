c_1 = {
    "formatted-number":"(420)-113-0999",
    "name":"bill",
    "desc":"billerson, see i told you my number is in here",
    "address":"1 bill st",
    "tags":["bill","billiard","bills phone number"],
    "type":"city"
}

c_2 = {
    "formatted-number":"(420)-000-6969",
    "name":"programmer",
    "desc":"he made this",
    "address":"ay im not telling you that - in his own words",
    "tags":["lemons","are","limes"],
    "type":"personal"
}

c_3 = {
    "formatted-number":"(420)-125-320",
    "name":"Bills Abesdos mill",
    "desc":"abesdos",
    "address":"2 bill st",
    "tags":["abesdos","lawyer","sick"],
    "type":"org"
}


c_4 = {
    "formatted-number":"911",
    "name":"helpline",
    "desc":"cops, ambulance, fire",
    "address":"the police, ambulance and fire station (8 grande ave)",
    "tags":["ambulance","sick","help","fire","police"],
    "type":"org"
}

c_5 = {
    "formatted-number":"(420)-888-8888",
    "name":"Lawyer",
    "desc":"we dont like the abesdos mill",
    "address":"#######",
    "tags":["abesdos","sick","corrpution"],
    "type":"terorist orginization"
}


entire_database = [c_1, c_2, c_3, c_4, c_5]

def search(query):
    
    return_entries = []

    #search though the database for the number obj via query
    for entry in entire_database:

        #check everything
        is_number = query ==  entry['formatted-number']
        is_name = query ==  entry['name']
        is_desc = query ==  entry['desc']
        is_address = query ==  entry['address']
        is_tag = query in entry['tags']

        #if even one of those is true, return the entry
        if is_number or is_name or is_desc or is_address or is_tag:
            return_entries.append(entry)

    return return_entries 
        