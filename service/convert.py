def convert(req):
        amount = float(req.get("amount"))
        unit_from = req.get("unit_from")
        unit_to = req.get("unit_to")
        
        if unit_from == unit_to:
            return req
        
        # check if it's a mass unit
        if unit_from in ["lb", "oz"]:
            match unit_from:
                case "oz":
                    return amount / 16
                case "lb":
                    return amount * 16
        # check if it's volume
        if unit_from in ["tsp", "tbsp", "c", "pt", "qt", "gal", "fl oz"]:
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

            # now convert from gallons to what we need
            
            match unit_to:
                case "gal":
                    return amount
                case "qt":
                    return amount * 4
                case "pt":
                    return amount * 8
                case "c":
                    return amount * 15.7725
                case "fl oz":
                    return amount * 128
                case "tbsp":
                    return amount * 256
                case "tsp":
                    return amount * 768
        
        return -1