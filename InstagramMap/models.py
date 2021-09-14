
from InstagramMap import db
from geoalchemy2 import Geometry
class StoreCoord(db.Model):
    __tablename__ = "store_coord"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    geom = db.Column(Geometry(geometry_type='POINT', srid='4326'))
    def __repr__(self):
        return f"StoreInfo(id, name={self.name} ,latitude={self.latitude}, longitude={self.longitude},geometry={self.geom})"


