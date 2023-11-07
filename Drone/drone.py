from dronekit import connect

def connectMyCopter():
    vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=57600)
    print("version: %s" % vehicle.version)
    print("Attitude: %s" % vehicle.attitude)
    print(f"현재 고도: {vehicle.location.global_relative_frame.alt} 미터")
    print('현재 위도: {}'.format(vehicle.location.global_frame.lat))
    print('현재 경도: {}'.format(vehicle.location.global_frame.lon))
    store_lat = vehicle.location.global_frame.lat
    store_lng = vehicle.location.global_frame.lon

    return vehicle, store_lng, store_lat