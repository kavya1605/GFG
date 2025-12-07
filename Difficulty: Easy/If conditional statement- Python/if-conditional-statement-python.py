def friends_in_trouble(j_angry, s_angry):
    # You are in trouble if both are angry or both are not angry
    if (j_angry and s_angry) or (not j_angry and not s_angry):
        return True
    else:
        return False
