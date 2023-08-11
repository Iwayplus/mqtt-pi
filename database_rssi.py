from firebase import firebase 


firebase = firebase.FirebaseApplication("https://uwb-loc-log-default-rtdb.firebaseio.com/", None)

data = {
    "MAC" : "8A:23:34:33:23:A2",
    "RSSI" : "-77"    
}

for i in range(10):
    print(i)
    result = firebase.post("/uwb-loc-log-default-rtdb/Beacon", data)
    print(result)
    

result_new = firebase.get('/uwb-loc-log-default-rtdb/Beacon', '')
print(result_new)


firebase.put('/uwb-loc-log-default-rtdb/Beacon/-NVOXVZ6qDeKFcXg4B--', 'RSSI', '-99')
print("record updated!")