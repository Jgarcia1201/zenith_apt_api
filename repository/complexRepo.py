from service.complexService import ComplexService

'''
get_complexes is the main function being called in the Controller layer.
Everything else should be set to private eventually. It's public now to make testing a little easier.
Should stay that way, we only want one contact point with other layers of the API and this one.
'''


def get_complexes(client):
    query = build_query(client)
    data = ComplexService().execute_query(query=query)
    apts = package_data(data)
    top_five = process_complexes(apts, client)
    return top_five


def process_complexes(complex_arr, client):
    for apt_complex in complex_arr:
        apt_complex["score"] = score_complex(apt_complex, client)
    return get_top_five(complex_arr)


def score_complex(apt_complex, client):
    try:
        score = 0
        # Luxury Score
        if client["lux_score"] == apt_complex["lux_score"]:
            score += 15
        elif client["lux_score"] == apt_complex["lux_score"] + 1 or client["lux_score"] == apt_complex["lux_score"] - 1:
            score += 10
        elif client["lux_score"] == apt_complex["lux_score"] + 2 or client["lux_score"] == apt_complex["lux_score"] - 2:
            score += 5

        # Liveliness Score
        if client["liv_score"] == apt_complex["liv_score"]:
            score += 15
        elif client["liv_score"] == apt_complex["liv_score"] + 1 or client["liv_score"] == apt_complex["liv_score"] - 1:
            score += 10
        elif client["liv_score"] == apt_complex["liv_score"] + 2 or client["liv_score"] == apt_complex["liv_score"] - 2:
            score += 5
        return score
    except KeyError:
        return 0


def get_top_five(complex_arr):
    try:
        sorted_by_score = sorted(complex_arr, key=lambda d: d["score"], reverse=True)
        return sorted_by_score[0:5]
    except KeyError:
        missing_scores_removed = [apt for apt in complex_arr if ("score" in apt)]
        sorted_by_score = sorted(missing_scores_removed, key=lambda d: d["score"], reverse=True)
        return sorted_by_score[0:5]


def package_data(data):
    to_return = []
    for apt in data:
        temp = {
            "name": apt[0],
            "address": apt[1],
            "lux_score": apt[2],
            "liv_score": apt[3],
            "hood": apt[4],
            "img": apt[5],
            "phone": apt[6]
        }
        to_return.append(temp)
    return to_return


def build_query(client):
    to_return = "SELECT name, address, luxScore, livScore, hood, img, phone FROM apartments WHERE "
    hoods = client['hoods']
    for i in range(len(hoods)):
        if i == len(hoods) - 1:
            to_return += "hood = " + "'" + hoods[i] + "'"
        else:
            to_return += "hood = " + "'" + hoods[i] + "'" + " OR "
    to_return += " AND {0}brMinRent >= {1} AND {2}brMaxRent <= {3}".format(str(client['desiredBr']),

                                                                     str(client['rent_min']),
                                                                           str(client['desiredBr']),
                                                                           str(client['rent_max']))
    return to_return
