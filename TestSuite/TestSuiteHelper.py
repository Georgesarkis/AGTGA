def ElementFinder(driver, x, y):
    source = driver.page_source

    if "Button" in source:
        ButtonList = driver.find_elements_by_class_name('android.widget.Button')
        for el in ButtonList:
            if x == el.location["x"] and y == el.location["y"]:
                return el

    if "ImageView" in source:
        ImageViewList = driver.find_elements_by_class_name('android.widget.ImageView')
        for el in ImageViewList:
            if x == el.location["x"] and y == el.location["y"]:
                return el

    if "TextView" in source:
        TextViewList = driver.find_elements_by_class_name('android.widget.TextView')
        for el in TextViewList:
            if x == el.location["x"] and y == el.location["y"]:
                return el

    if "EditText" in source:
        EditTextList = driver.find_elements_by_class_name('android.widget.EditText')
        for el in EditTextList:
            if x == el.location["x"] and y == el.location["y"]:
                return el

    if "ImageButton" in source:
        ImageButtonList = driver.find_elements_by_class_name('android.widget.ImageButton')
        for el in ImageButtonList:
            if x == el.location["x"] and y == el.location["y"]:
                return el

    if "CheckedTextView" in source:
        CheckedTextViewList = driver.find_elements_by_class_name('android.widget.CheckedTextView')
        for el in CheckedTextViewList:
            if x == el.location["x"] and y == el.location["y"]:
                return el

    return None
