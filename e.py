from Mongo import Mongodb
import pymongo
mongo = Mongodb('mongodb+srv://UserHome:smarthomemongodb@cluster0.optcn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority','SmartHome','devices')
select = {'tipo': 'Foco'}
params = {'tipo':1,'pin':1}
for i in mongo.findWithParams(select,params):
    print(i)   