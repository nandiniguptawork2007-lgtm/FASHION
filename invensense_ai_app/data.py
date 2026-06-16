import pandas as pd

CATEGORIES = [
    "Dresses", "Tops", "Bottoms", "Outerwear", "Accessories",
    "Footwear", "Activewear", "Denim", "Ethnic Wear", "Loungewear"
]

RAW_INVENTORY = [
    {"sku":"SKU001","product_name":"Satin Slip Dress","category":"Dresses","stock_qty":120,"unit_cost":850,"selling_price":1899,"weekly_sales":8,"trend_score":72,"season":"Summer","age_days":45},
    {"sku":"SKU002","product_name":"Floral Midi Dress","category":"Dresses","stock_qty":95,"unit_cost":920,"selling_price":2199,"weekly_sales":5,"trend_score":64,"season":"Spring","age_days":70},
    {"sku":"SKU003","product_name":"Bodycon Party Dress","category":"Dresses","stock_qty":140,"unit_cost":780,"selling_price":1999,"weekly_sales":12,"trend_score":86,"season":"Party","age_days":32},
    {"sku":"SKU004","product_name":"Cotton Shirt Dress","category":"Dresses","stock_qty":60,"unit_cost":650,"selling_price":1499,"weekly_sales":9,"trend_score":78,"season":"Summer","age_days":28},
    {"sku":"SKU005","product_name":"Ruffle Maxi Dress","category":"Dresses","stock_qty":180,"unit_cost":1100,"selling_price":2599,"weekly_sales":4,"trend_score":48,"season":"Spring","age_days":115},
    {"sku":"SKU006","product_name":"Crop Ribbed Top","category":"Tops","stock_qty":220,"unit_cost":280,"selling_price":799,"weekly_sales":30,"trend_score":91,"season":"Summer","age_days":20},
    {"sku":"SKU007","product_name":"Oversized Graphic Tee","category":"Tops","stock_qty":260,"unit_cost":320,"selling_price":899,"weekly_sales":24,"trend_score":84,"season":"All Season","age_days":38},
    {"sku":"SKU008","product_name":"Silk Blouse","category":"Tops","stock_qty":110,"unit_cost":700,"selling_price":1699,"weekly_sales":6,"trend_score":61,"season":"Office","age_days":82},
    {"sku":"SKU009","product_name":"Off-Shoulder Top","category":"Tops","stock_qty":155,"unit_cost":390,"selling_price":999,"weekly_sales":10,"trend_score":69,"season":"Summer","age_days":63},
    {"sku":"SKU010","product_name":"Peplum Formal Top","category":"Tops","stock_qty":90,"unit_cost":520,"selling_price":1299,"weekly_sales":3,"trend_score":42,"season":"Office","age_days":130},
    {"sku":"SKU011","product_name":"Wide-Leg Trousers","category":"Bottoms","stock_qty":130,"unit_cost":620,"selling_price":1599,"weekly_sales":13,"trend_score":80,"season":"All Season","age_days":44},
    {"sku":"SKU012","product_name":"Pleated Mini Skirt","category":"Bottoms","stock_qty":170,"unit_cost":450,"selling_price":1199,"weekly_sales":15,"trend_score":88,"season":"Summer","age_days":35},
    {"sku":"SKU013","product_name":"Cargo Pants","category":"Bottoms","stock_qty":210,"unit_cost":720,"selling_price":1899,"weekly_sales":17,"trend_score":83,"season":"Streetwear","age_days":56},
    {"sku":"SKU014","product_name":"High-Waist Shorts","category":"Bottoms","stock_qty":190,"unit_cost":360,"selling_price":999,"weekly_sales":11,"trend_score":67,"season":"Summer","age_days":77},
    {"sku":"SKU015","product_name":"Faux Leather Skirt","category":"Bottoms","stock_qty":145,"unit_cost":680,"selling_price":1799,"weekly_sales":4,"trend_score":45,"season":"Party","age_days":118},
    {"sku":"SKU016","product_name":"Denim Jacket","category":"Outerwear","stock_qty":150,"unit_cost":1200,"selling_price":2899,"weekly_sales":7,"trend_score":63,"season":"Winter","age_days":90},
    {"sku":"SKU017","product_name":"Cropped Bomber Jacket","category":"Outerwear","stock_qty":125,"unit_cost":1350,"selling_price":3299,"weekly_sales":6,"trend_score":58,"season":"Winter","age_days":104},
    {"sku":"SKU018","product_name":"Faux Fur Coat","category":"Outerwear","stock_qty":85,"unit_cost":2100,"selling_price":4999,"weekly_sales":2,"trend_score":35,"season":"Winter","age_days":155},
    {"sku":"SKU019","product_name":"Lightweight Trench","category":"Outerwear","stock_qty":70,"unit_cost":1650,"selling_price":3899,"weekly_sales":5,"trend_score":52,"season":"Monsoon","age_days":96},
    {"sku":"SKU020","product_name":"Puffer Vest","category":"Outerwear","stock_qty":115,"unit_cost":980,"selling_price":2499,"weekly_sales":3,"trend_score":40,"season":"Winter","age_days":142},
    {"sku":"SKU021","product_name":"Mini Shoulder Bag","category":"Accessories","stock_qty":240,"unit_cost":500,"selling_price":1399,"weekly_sales":22,"trend_score":87,"season":"All Season","age_days":24},
    {"sku":"SKU022","product_name":"Statement Belt","category":"Accessories","stock_qty":190,"unit_cost":180,"selling_price":599,"weekly_sales":18,"trend_score":76,"season":"All Season","age_days":50},
    {"sku":"SKU023","product_name":"Chunky Hoop Earrings","category":"Accessories","stock_qty":300,"unit_cost":120,"selling_price":499,"weekly_sales":36,"trend_score":92,"season":"Party","age_days":18},
    {"sku":"SKU024","product_name":"Printed Scarf","category":"Accessories","stock_qty":160,"unit_cost":220,"selling_price":699,"weekly_sales":5,"trend_score":49,"season":"Winter","age_days":121},
    {"sku":"SKU025","product_name":"Hair Claw Set","category":"Accessories","stock_qty":280,"unit_cost":90,"selling_price":399,"weekly_sales":28,"trend_score":81,"season":"All Season","age_days":41},
    {"sku":"SKU026","product_name":"Platform Sneakers","category":"Footwear","stock_qty":100,"unit_cost":1450,"selling_price":3499,"weekly_sales":10,"trend_score":82,"season":"All Season","age_days":47},
    {"sku":"SKU027","product_name":"Strappy Heels","category":"Footwear","stock_qty":140,"unit_cost":1100,"selling_price":2799,"weekly_sales":8,"trend_score":68,"season":"Party","age_days":86},
    {"sku":"SKU028","product_name":"Chelsea Boots","category":"Footwear","stock_qty":95,"unit_cost":1700,"selling_price":3999,"weekly_sales":3,"trend_score":41,"season":"Winter","age_days":149},
    {"sku":"SKU029","product_name":"Slide Sandals","category":"Footwear","stock_qty":210,"unit_cost":520,"selling_price":1299,"weekly_sales":16,"trend_score":74,"season":"Summer","age_days":54},
    {"sku":"SKU030","product_name":"Ballet Flats","category":"Footwear","stock_qty":130,"unit_cost":760,"selling_price":1799,"weekly_sales":6,"trend_score":57,"season":"Office","age_days":101},
    {"sku":"SKU031","product_name":"Yoga Leggings","category":"Activewear","stock_qty":175,"unit_cost":620,"selling_price":1599,"weekly_sales":21,"trend_score":89,"season":"All Season","age_days":30},
    {"sku":"SKU032","product_name":"Sports Bra","category":"Activewear","stock_qty":160,"unit_cost":430,"selling_price":1199,"weekly_sales":19,"trend_score":85,"season":"All Season","age_days":34},
    {"sku":"SKU033","product_name":"Training Shorts","category":"Activewear","stock_qty":145,"unit_cost":360,"selling_price":999,"weekly_sales":14,"trend_score":71,"season":"Summer","age_days":59},
    {"sku":"SKU034","product_name":"Zip Hoodie","category":"Activewear","stock_qty":120,"unit_cost":900,"selling_price":2199,"weekly_sales":7,"trend_score":60,"season":"Winter","age_days":92},
    {"sku":"SKU035","product_name":"Mesh Tank Top","category":"Activewear","stock_qty":135,"unit_cost":310,"selling_price":899,"weekly_sales":12,"trend_score":70,"season":"Summer","age_days":67},
    {"sku":"SKU036","product_name":"Mom Jeans","category":"Denim","stock_qty":125,"unit_cost":980,"selling_price":2499,"weekly_sales":11,"trend_score":79,"season":"All Season","age_days":48},
    {"sku":"SKU037","product_name":"Straight Fit Jeans","category":"Denim","stock_qty":180,"unit_cost":1050,"selling_price":2699,"weekly_sales":13,"trend_score":81,"season":"All Season","age_days":46},
    {"sku":"SKU038","product_name":"Denim Mini Skirt","category":"Denim","stock_qty":150,"unit_cost":620,"selling_price":1599,"weekly_sales":10,"trend_score":66,"season":"Summer","age_days":73},
    {"sku":"SKU039","product_name":"Distressed Shorts","category":"Denim","stock_qty":175,"unit_cost":550,"selling_price":1399,"weekly_sales":7,"trend_score":51,"season":"Summer","age_days":110},
    {"sku":"SKU040","product_name":"Wide-Leg Denim","category":"Denim","stock_qty":100,"unit_cost":1150,"selling_price":2899,"weekly_sales":9,"trend_score":77,"season":"All Season","age_days":61},
    {"sku":"SKU041","product_name":"Embroidered Kurta","category":"Ethnic Wear","stock_qty":160,"unit_cost":700,"selling_price":1799,"weekly_sales":18,"trend_score":86,"season":"Festive","age_days":37},
    {"sku":"SKU042","product_name":"Printed Palazzo Set","category":"Ethnic Wear","stock_qty":120,"unit_cost":900,"selling_price":2399,"weekly_sales":11,"trend_score":73,"season":"Festive","age_days":65},
    {"sku":"SKU043","product_name":"Chikankari Top","category":"Ethnic Wear","stock_qty":135,"unit_cost":800,"selling_price":1999,"weekly_sales":15,"trend_score":84,"season":"Summer","age_days":42},
    {"sku":"SKU044","product_name":"Festive Dupatta","category":"Ethnic Wear","stock_qty":210,"unit_cost":350,"selling_price":999,"weekly_sales":8,"trend_score":55,"season":"Festive","age_days":112},
    {"sku":"SKU045","product_name":"Indo-Western Jacket","category":"Ethnic Wear","stock_qty":90,"unit_cost":1300,"selling_price":3199,"weekly_sales":3,"trend_score":39,"season":"Festive","age_days":151},
    {"sku":"SKU046","product_name":"Soft Knit Co-ord","category":"Loungewear","stock_qty":155,"unit_cost":820,"selling_price":1999,"weekly_sales":9,"trend_score":69,"season":"Winter","age_days":74},
    {"sku":"SKU047","product_name":"Cotton Lounge Set","category":"Loungewear","stock_qty":170,"unit_cost":620,"selling_price":1599,"weekly_sales":16,"trend_score":78,"season":"Summer","age_days":53},
    {"sku":"SKU048","product_name":"Oversized Sleep Tee","category":"Loungewear","stock_qty":230,"unit_cost":300,"selling_price":899,"weekly_sales":26,"trend_score":88,"season":"All Season","age_days":26},
    {"sku":"SKU049","product_name":"Satin Pajama Set","category":"Loungewear","stock_qty":115,"unit_cost":760,"selling_price":1899,"weekly_sales":7,"trend_score":62,"season":"All Season","age_days":88},
    {"sku":"SKU050","product_name":"Fleece Joggers","category":"Loungewear","stock_qty":140,"unit_cost":650,"selling_price":1699,"weekly_sales":4,"trend_score":44,"season":"Winter","age_days":136},
]

def load_inventory() -> pd.DataFrame:
    df = pd.DataFrame(RAW_INVENTORY)
    df["total_value"] = df["stock_qty"] * df["unit_cost"]
    df["weeks_of_supply"] = (df["stock_qty"] / df["weekly_sales"].replace(0, 1)).round(1)
    df["risk_score"] = (
        (df["weeks_of_supply"].clip(0, 30) / 30 * 45)
        + ((100 - df["trend_score"]) / 100 * 35)
        + (df["age_days"].clip(0, 180) / 180 * 20)
    ).round(0).astype(int)
    df["status"] = pd.cut(df["risk_score"], bins=[-1, 39, 69, 100], labels=["Healthy", "Watch", "At Risk"])
    df["suggested_discount"] = pd.cut(df["risk_score"], bins=[-1, 39, 54, 69, 100], labels=[5, 15, 25, 35]).astype(int)
    df["estimated_recovery"] = (df["stock_qty"] * df["selling_price"] * (1 - df["suggested_discount"] / 100) * 0.35).round(0).astype(int)
    df["margin_preserved"] = (df["estimated_recovery"] - (df["stock_qty"] * df["unit_cost"] * 0.20)).clip(lower=0).round(0).astype(int)
    return df
