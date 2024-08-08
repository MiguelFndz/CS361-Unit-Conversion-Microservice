def convert(req):
        amount = float(req.get("amount"))
        unit_from = req.get("unit_from")
        unit_to = req.get("unit_to")
        
        if unit_from == unit_to:
            return req
        
        # check if it's a mass unit
        if unit_from in ["lb", "oz", "g", "kg"]:
            # convert averything to lb
            match unit_from:
                case "oz":
                    amount =  amount / 16
                case "kg":
                    amount = amount * 2.20462
                case "g":
                    amount = amount * 0.00220462
            
            # now convert to whatever we need
            match unit_to:
                case "lb": 
                    return round(amount, 2)
                case "oz":
                    return round(amount * 16, 2)
                case "kg":
                    return round(amount * 0.453592, 2)
                case "g":
                    return round(amount * 453.592, 2)
                
        # check if it's volume
        if unit_from in ["tsp", "tbsp", "c", "pt", "qt", "gal", "fl oz", "mL", "L"]:
            # convert everything to a gallon first
            match unit_from:
                case "tsp":
                    amount = amount / 768
                case "tbsp":
                    amount = amount / 256
                case "fl oz":
                    amount = amount / 128
                case "c":
                    amount = amount / 15.7725
                case "pt":
                    amount = amount / 8
                case "qt":
                    amount = amount / 4
                case "mL":
                    amount = amount / 3785.41
                case "L":
                    amount = amount / 3.78541

            # now convert from gallons to what we need
            
            match unit_to:
                case "gal":
                    return round(amount, 2)
                case "qt":
                    return round(amount * 4, 2)
                case "pt":
                    return round(amount * 8, 2)
                case "c":
                    return round(amount * 15.7725, 2)
                case "fl oz":
                    return round(amount * 128, 2)
                case "tbsp":
                    return round(amount * 256, 2)
                case "tsp":
                    return round(amount * 768, 2)
                case "mL":
                    return round(amount * 3785.41, 2)
                case "L":
                    return round(amount * 3.78541, 2)
        
        return -1