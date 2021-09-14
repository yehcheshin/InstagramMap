from InstagramMap.models import StoreCoord
from  InstagramMap import db
from shapely.geometry import Point

store_info = {
    "name":None ,
    "longitude": None,
    "latitude":None,
}

class TSP():
    def __init__(self,storeInfo=store_info,radius=0.5):
        self.storeInfo = storeInfo 
        self.radius = radius
    def SetRadius(self,radius):
        self.radius = radius
    def AccessInRange(self):
        
        
        loc_geo = "ST_GeomFromText('POINT({} {})', 4326) ".format(self.storeInfo["longitude"],self.storeInfo["latitude"])
        
        # sql = "SELECT * FROM store_coord ,ST_Distance( ST_Transform(geom, 900913), ST_Transform((SELECT geom FROM store_coord WHERE name='{}'), 900913) ) AS diff  WHERE diff < {} and name<>'{}' ORDER BY diff ASC;".format(
        #     self.storeInfo['name'], 
        #     self.radious*1000,
        #     self.storeInfo['name'])
        sql = "SELECT * FROM store_coord ,ST_Distance( ST_Transform(geom, 900913), ST_Transform({}, 900913) ) AS diff  WHERE diff < {} and name<>'{}' ORDER BY diff ASC;".format(
            loc_geo,
            self.radius*1000,
            self.storeInfo['name'])
        

        temp = db.session.execute(sql)
        res = []
        for store in temp:
            res.append((store.name,store.diff))
        return res
    
    


