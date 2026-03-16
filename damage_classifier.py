def classify(title):

    t = title.lower()

    if "画面割れ" in t or "液晶" in t:
        return "screen"

    if "バッテリー" in t or "電池" in t:
        return "battery"

    if "カメラガラス" in t:
        return "camera_glass"

    if "カメラ" in t:
        return "camera"

    return None