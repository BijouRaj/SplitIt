import easyocr 
import bisect 

reader = easyocr.Reader(['en'])

def extract_text(image):
    # use easyocr to read text in image
    results = reader.readtext(image)
    # sort by y value to get lines (sharing same y value)
    results = sorted(results, key = lambda x: x[0][0][1])
    
    # tolerance value for y value mismatch
    tolerance = 5
    y_val = None 
    
    # store each line
    items = []
    
    # initial line
    currentLine = []
    
    # loop through each bounding box found in ocr
    for (bbox, text, _) in results:
        # set current y value equal to top of current bounding box
        y_top = bbox[0][1]
        # if within same line, add text to current line
        if not y_val or abs(y_top - y_val) < tolerance:
            currentLine.append(text)
            y_val = y_top 
        # otherwise, add last line to items, then create new line
        else:
            curr = " ".join(currentLine)
            items.append(curr)
            currentLine = [text]
            y_val = y_top 
    return items 

def extract_items(input):
    items = {}
    for line in input:
        if "$" in line:
            i = line.index("$")
            name = line[:i]
            price = line[i + 1:]
            items[name] = price 
    return items


image = 'receipt1.jpg'
ret = extract_text(image)
check = extract_items(ret)
print(check)
    