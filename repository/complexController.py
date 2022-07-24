def process_complexes(complex_arr, client):
    return None


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
