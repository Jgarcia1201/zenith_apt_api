def process_complexes(complex_arr, client):
    for apt_complex in complex_arr:
        apt_complex["score"] = score_complex(apt_complex, client)
    return get_top_five(complex_arr)


def build_query(client):
    to_return = "SELECT name, address, luxScore, livScore, hood, img, phone FROM apartments WHERE "
    hoods = client['hoods']
    for i in range(len(hoods)):
        if i == len(hoods) - 1:
            to_return += "hood = " + hoods[i]
        else:
            to_return += "hood = " + hoods[i] + " OR "
    to_return += " AND {0}brMin >= {1} AND {2}brMax <= {3}".format(str(client['desiredBr']), str(client['rent_min']),
                                                                   str(client['desiredBr']), str(client['rent_max']))
    return to_return


def get_top_five(complex_arr):
    try:
        sorted_by_score = sorted(complex_arr, key=lambda d: d["score"], reverse=True)
        return sorted_by_score[0:5]
    except KeyError:
        missing_scores_removed = [apt for apt in complex_arr if ("score" in apt)]
        sorted_by_score = sorted(missing_scores_removed, key=lambda d: d["score"], reverse=True)
        return sorted_by_score[0:5]


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
