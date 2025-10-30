import easyocr 

reader = easyocr.Reader(['en'])

def extract_text(image):
    results = reader.readtext(image)
    results = sorted(results, key = lambda x: x[0][0][1])
    
    tolerance = 5
    y_val = None 
    
    
    items = []
    currentLine = []
    
    for (bbox, text, _) in results:
        
        y_top = bbox[0][1]
        if not y_val or abs(y_top - y_val) < tolerance:
            currentLine.append(text)
            y_val = y_top 
        else:
            curr = " ".join(currentLine)
            items.append(curr)
            currentLine = [text]
            y_val = y_top 
        #items.append(text)
    return items 



image = 'receipt1.jpg'
ret = extract_text(image)
for line in ret:
    if "$" in line:
        print(line)