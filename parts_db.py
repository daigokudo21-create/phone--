parts = {

"iphone15":{
"screen":6500,
"battery":2200,
"camera":4800,
"camera_glass":1200
},

"iphone14":{
"screen":6000,
"battery":2000,
"camera":4200,
"camera_glass":1000
},

"iphone13":{
"screen":4200,
"battery":1800,
"camera":3500,
"camera_glass":800
},

"iphone12":{
"screen":3800,
"battery":1600,
"camera":3000,
"camera_glass":700
},

"iphone11":{
"screen":3200,
"battery":1500,
"camera":2800,
"camera_glass":600
}

}

def get_part(model, part):

    if model not in parts:
        return None

    return parts[model].get(part)